import json


class RHS:

    def __init__(self, s=None, l=None, dot_pos = -1):
        self._l = l
        if s is not None:
            self._l = tuple(s.split(' '))
        
        self._dotpos = dot_pos


    @property
    def item_after_dot(self):
        if self._dotpos != -1 and self._dotpos != len(self._l):
            return self._l[self._dotpos]
        return None

    @property
    def has_dot(self):
        return self._dotpos != -1

    @property
    def is_dot_last(self):
        return self.has_dot and self.item_after_dot == None
    


    def increment_dot_pos(self):
        return RHS(l = self.items, dot_pos=self.dot + 1)
    
    

    
    @property
    def items(self):
        return self._l
    
    @property
    def dot(self):
        return self._dotpos
    
    @dot.setter
    def dot(self, value):
        self._dotpos = value

    def __str__(self):
        l = self._l
        if self.has_dot:
            l = list(l)
            l.insert(self.dot, '.')
            l = tuple(l)
        return str(l)

    def __repr__(self):
        return self.__str__()
    
    def __key(self):
        return (self._l, self._dotpos)
    
    def __hash__(self):
        return hash(self.__key())
    
    def __eq__(self, other):
        if isinstance(other, RHS):
            return self.__key() == other.__key()
        return False
    
    def __iter__(self):
        for it in self._l:
            yield it
    




class Grammar:

    def __init__(self, file_path):
        with open(file_path) as f:
            self._data = json.load(f)
            self._non_terminals = self._data["non_terminals"]
            self._terminals = self._data["terminals"]
            self._start_symbol = self._data["start_symbol"]
            self._productions = self._data["productions"]
            self._productions['S_'] = [self._start_symbol]
            self._non_terminals.append('S_')

            if self._start_symbol not in self._non_terminals:
                raise Exception("Start symbol not in non terminals")

            self._productions = {
                k : tuple(map(lambda x: RHS(s=x), v)) for k, v in self._productions.items()
            }

            for k, v in self._productions.items():
                if k not in self._non_terminals:
                    raise Exception("Production left hand side symbol not in non terminals")
                for it in v:
                    for s in it:
                        if s not in self._non_terminals and s not in self._terminals:
                            raise Exception("Production right hand side symbol not in non terminals")
        
        self.__menu = {
            "1": self.__non_terminals,
            "2": self.__terminals,
            "3": self.__start_symbol,
            "4": self.__productions,
            "5": self.__production_for_non_terminal,
            "6": self.__close
        }
        self._finished = False
    
    def __non_terminals(self):
        print(self._non_terminals)

    def __terminals(self):
        print(self._terminals)

    def __start_symbol(self):
        print(self._start_symbol)

    def __productions(self):
        print(self._productions)

    def __production_for_non_terminal(self):
        non_terminal = input("Non-Terminal = \n")
        print(self._productions[non_terminal])

    def __close(self):
        self._finished = True

    def __print_menu(self):
        s = ""
        s += "1. Print non_terminals\n"
        s += "2. Print terminals\n"
        s += "3. Print starting symbol\n"
        s += "4. Print productions\n"
        s += "5. Print productions for given non-terminal\n"
        s += "6. Close\n"
        print(s)
    
    def menu(self):
        while not self._finished:
            self.__print_menu()
            key = input()
            if key in self.__menu.keys():
                self.__menu[key]()
            else:
                print("Invalid key")

    def __stringify_prod(self, production):
        return "{}->{}".format(production[0], ' '.join(production[1]))

    def closure(self, productions):
        c = list(productions)

        i = 0
        while i < len(c):
            p = c[i][1]
            if p.has_dot:
                if p.item_after_dot in self._non_terminals:
                    for item in self._productions[p.item_after_dot]:
                        it = (p.item_after_dot, RHS(l=item.items, dot_pos=0))
                        if it not in c:
                            c.append(it)
            else:
                raise Exception("Closure production should contain dot")
            i += 1
        return c
    
    def goto(self, s, token):
        c = []
        for closure_item in s:
            if closure_item[1].has_dot:
                if closure_item[1].item_after_dot == token:
                    c.append((closure_item[0], closure_item[1].increment_dot_pos()))
            else:
                raise Exception("Must have dot")
        return self.closure(c) if len(c) > 0 else None
    
    def col_can(self):
        c = []
        s0 = self.closure([("S_", RHS(s="S", dot_pos=0))])
        c.append((-1, 0, 'S_'))

        id_ = 1
        states = {0: s0}

        i = 0
        while i < len(c):
            s = states[c[i][1]]
            ws = self._non_terminals + self._terminals
            for w in ws:
                g = self.goto(s, w)
                if g is not None:
                    if next(filter(lambda x: x[0] == c[i][1] and x[2] == w and states[x[1]] == g, c), None) == None:
                        if g not in states.values():
                            states[id_] = g
                            c.append((c[i][1], id_, w))
                            id_ += 1
                        else:
                            c.append(
                                (
                                    c[i][1],
                                    next(filter(lambda x: x[1] == g, states.items()))[0],
                                    w
                                )
                            )
            i += 1
        return c, states

    def __is_end_state(self, state):
        return len(state) == 1 and state[0][1].is_dot_last
    
    def __is_extended_production(self, state):
        return state[0][0] == "S_"

    def __numbered_productions(self):
        i = 0
        productions = {}
        for symbol, prods in self._productions.items():
            for prod in prods:
                productions[i] = (symbol, prod)
                i += 1
        return productions



    def table(self, col_can, states):
        productions = self.__numbered_productions()

        actions = [None for i in range(len(states))]
        goto = { symbol : [ None for i in range(len(states))] for symbol in self._terminals + self._non_terminals }


        for i, state in states.items():
            if self.__is_end_state(state):
                if not self.__is_extended_production(state):
                    for j, prod in productions.items():
                        if prod[0] == state[0][0] and prod[1].items == state[0][1].items:
                            actions[i] = "r{}".format(j)
                            break
                else:
                    actions[i] = 'acc'
            else:
                actions[i] = 'shift'
        
        for g in col_can:
            if g[0] != -1:
                goto[g[2]][g[0]] = g[1]
        


        return actions, goto, productions

    def parse(self, seq):
        col_can = self.col_can()
        actions, goto, productions = self.table(col_can[0], col_can[1])
        working_stack = [0]

        i = 0
        while True:
            if actions[working_stack[-1]] == 'shift':
                if i  >= len(seq):
                    return False
                working_stack.append(seq[i])
                working_stack.append(goto[seq[i]][working_stack[-2]])
                i += 1
            elif actions[working_stack[-1]].startswith('r'):
                red = int(actions[working_stack[-1]][1:])
                production = productions[red]
                for _ in range(2 * len(production[1].items)):
                    working_stack.pop()
                working_stack.append(production[0])
                working_stack.append(goto[production[0]][working_stack[-2]])
            elif actions[working_stack[-1]] == 'acc':
                return i == len(seq)
            else:
                return False
                

            





if __name__ == "__main__":
    grammar = Grammar("g1.txt")

    col_can = grammar.col_can()
    table = grammar.table(col_can[0], col_can[1])
    print(
        '\n'.join(map(str, col_can[0]))
        + '\n\n' +
        '\n'.join(map(str, col_can[1].items()))
    )

    print(table[0])
    print(table[1])

    keys = table[1].keys()
    print()

    print(table[2])
    print(" \taction\t{}".format('\t'.join(keys)))
    for i in range(len(table[0])):
        
        print("{}\t{}\t{}".format(i, table[0][i], '\t'.join(map(lambda k: str(table[1][k][i]) , keys))))

    if grammar.parse("aaaaaaaaaaaaaaaaab"):
        print("accepted")
    else:
        print("not accepted")


    


        
        
            
