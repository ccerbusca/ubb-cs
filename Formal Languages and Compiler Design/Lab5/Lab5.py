import json

class Grammar:

    def __init__(self, file_path):
        with open(file_path) as f:
            self._data = json.load(f)
            self._non_terminals = self._data["non_terminals"]
            self._terminals = self._data["terminals"]
            self._start_symbol = self._data["start_symbol"]
            self._productions = self._data["productions"]

            if self._start_symbol not in self._non_terminals:
                raise Exception("Start symbol not in non terminals")

            for k, v in self._productions.items():
                if k not in self._non_terminals:
                    raise Exception("Production left hand side symbol not in non terminals")
                for it in v:
                    for s in it.split(' '):
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




if __name__ == "__main__":
    grammar = Grammar("g1.txt")
    grammar.menu()
        
        
            
