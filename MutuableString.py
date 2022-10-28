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
        return "".join(self.__s)

# Check the correctness of the index (helper method)