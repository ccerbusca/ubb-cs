class repoIterator:
    def __init__(self):
        self.__data = []
        self.idx = 0
    
    def __iter__(self):
        self.idx = 0
        return self
    
    def __next__(self):
        if self.idx >= len(self.__data):
            self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return self.__data[self.idx - 1]

    def __setitem__(self, idx, value):
        self.__data[idx] = value
    
    def __delitem__(self, key):
        del self.__data[key]
    
    def __getitem__(self, key):
        return self.__data[key]
    
    def __len__(self):
        return len(self.__data)
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new):
        self.__data = new

def myFilter(ls, fun):
    return [i for i in ls if fun(i)]

def shellsort(ls, fun):
    n = len(ls) 
    gap = n // 2
    while gap > 0: 
        for i in range(gap, n): 
            aux = ls[i] 
            j = i 
            while  j >= gap and fun(ls[j - gap], aux): 
                ls[j] = ls[j - gap] 
                j -= gap 
            ls[j] = aux 
        gap //= 2
    return ls