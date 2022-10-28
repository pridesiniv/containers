class MutableString:
    def __init__(self, s):
        self.__s = list(s)

    # Implement iterator functionality

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > len(self.__s) - 1:
            raise StopIteration
        else:
            a = self.__s[self.__i]
            self.__i = self.__i + 1
            return a

    def __len__(self):
        return len(self.__s)

    def __str__(self):
        return "".join(self.__s)

    # Check the correctness of the index (helper method)

    def __iscorrectindex(self, i):
        if type(i) == int or type(i) == slice:
            if type(i) == int and i > self.__len__() - 1:
                raise IndexError
        else:
            raise TypeError

    # Implementing functionality

    def __getitem__(self, i):
        self.__iscorrectindex(i)
        return self.__s[i]

    def __setitem__(self, i, v):
        self.__iscorrectindex(i)
        self.__s[i] = v

    def __delitem__(self, i):
        self.__iscorrectindex(i)
        del self.__s[i]

    def __contains__(self, v):
        return v in self.__s


s = MutableString('Python')
print(s[-1])
print(s)
s[0] = 'J'
print(s)
del s[2:4]
print(s)
print('J' in s)
for i in s:
    print(i, end='')
