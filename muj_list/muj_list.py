class MujList:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str(self.my_list)

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            result = [a + b for a, b in zip(self.my_list, other.my_list)]
            return MujList(result)
        else:
            raise ValueError("Lists must have the same length for addition")

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.my_list, other.my_list)]
        return MujList(result)


    def __mul__(self, other):
        result = [a * b for a, b in zip(self.my_list, other.my_list)]
        return MujList(result)

    def __truediv__(self, other):
        result = [a / b for a, b in zip(self.my_list, other.my_list)]
        return MujList(result)
