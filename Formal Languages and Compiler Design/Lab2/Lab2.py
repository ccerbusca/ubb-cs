
class SymbolTable:

    def __init__(self, size = 100):
        self.__table = [None] * size
        self.__size = size
    
    # in: key - dictionary key
    # out: the function returns a hash code for the specified key argument
    def hash_code(self, key):
        return hash(key) % self.__size

    # in: key - dictionary key
    # out: function adds the key to the table and returns position of the key
    def add(self, key):
        position = self.hash_code(key)
        if self.__table[position] is None:
            self.__table[position] = []
            self.__table[position].append(key)
        else:
            for k in self.__table[position]:
                if k == key:
                    break
            else:
                self.__table[position].append(key)
        return position
    
    # in: key - dictionary key
    # out: value corresponding to the key and None if key not is not found
    def __getitem__(self, key):
        position = self.hash_code(key)
        if self.__table[position] is None:
            return None
        else:
            for k in self.__table[position]:
                if k == key:
                    return position
            return None
    
    # in: key - dictionary key
    # out: deletes the key from the table
    #      raises Exception if key does not exist
    def __delitem__(self, key):
        position = self.hash_code(key)
        if self.__table[position] is None:
            raise Exception()
        else:
            for i, k in enumerate(self.__table[position]):
                if k == key:
                    del self.__table[position][i]
                    break
            else:
                raise Exception()

    def __str__(self):
        return str(self.__table)


def main():
    table = SymbolTable(100)
    table.add("def")
    table.add("while")
    table.add("for")
    table.add("rof")
    print(table["for"], table["while"], table["def"], table["nope"], table["rof"])
    del table["for"]
    table.add("while")
    print(table["for"], table["while"], table["def"], table["nope"])

    print(table)


main()