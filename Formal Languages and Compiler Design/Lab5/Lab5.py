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
        c.append(s0)
        i = 0
        while i < len(c):
            s = c[i]
            ws = self._non_terminals + self._terminals
            for w in ws:
                g = self.goto(s, w)
                if g is not None and g not in c:
                    c.append(g)
            i += 1
        return c




if __name__ == "__main__":
    grammar = Grammar("g1.txt")

    print(
        '\n'.join(map(str, grammar.col_can()))
    )


    


        
        
            
