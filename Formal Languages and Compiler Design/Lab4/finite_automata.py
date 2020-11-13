import json

class FiniteAutomaton:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.data = json.load(f)

        self._states = self.data["states"]
        self._alphabet = self.data["alphabet"]
        self._transitions = {}
        self._final_states = self.data["final_states"]

        for key, value in self.data["transitions"].items():
            newdict = {}
            for ikey, ivalue in value.items():
                for a in ikey:
                    if a in newdict.keys() and newdict[a] != ikey:
                        raise Exception("Automaton is not deterministic")
                    newdict[a] = ivalue
                self._transitions[key] = newdict
                    
        self.__finished = False
        self.__menu = {
            "1": self.__display_states,
            "2": self.__display_alphabet,
            "3": self.__display_transitions,
            "4": self.__display_final_states,
            "5": self.__check_sequence,
            "6": self.__close
        }
    
    def menu(self):
        while not self.__finished:
            self.__print_menu()
            c = input()
            fun = self.__menu[c]
            if c is not None:
                fun()
            else:
                print("Unrecognized input")

    def __display_states(self):
        print(self.data["states"])

    def __display_alphabet(self):
        print(self.data["alphabet"])

    def __display_transitions(self):
        print(self.data["transitions"])

    def __display_final_states(self):
        print(self.data["final_states"])

    def __close(self):
        self.__finished = True

    def __print_menu(self):
        s = "1. Display states\n"
        s += "2. Display alphabet\n"
        s += "3. Display transitions\n"
        s += "4. Display final states\n"
        s += "5. Check sequence\n"
        s += "6. Close\n"
        print(s)

    def __check_sequence(self):
        seq = input("Enter sequence...\n")
        self.__check(seq)


    def __check(self, sequence):
        state = "initial"
        for a in sequence:
            if a not in self._alphabet:
                print("character '{}' not in alphabet".format(a))
                return
            try:
                next_state = self._transitions[state][a]
            except KeyError:
                print("invalid state transition from state {} with '{}'".format(state, a))
                return
            state = next_state
        if state not in self._final_states:
            print("state {} is not a final state".format(state))
            return
        print("Valid sequence")

fa = FiniteAutomaton("finite_automata_integer_constant.json")
fa.menu()