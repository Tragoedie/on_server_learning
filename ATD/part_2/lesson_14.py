class Void:
    def __new__(cls, *args, **kwargs):
        return None


class Item:
    def __init__(self, value):
        self.__value = value

    def __add__(self, data):
        try:
            if type(data) is Item:
                val = self.__value + data.__value
            else:
                val = self.__value + data
        except TypeError:
            val = Void
        return val

    @classmethod
    def assignment_attempt(cls, target, source):
        if type(target) != cls or type(source) != cls:
            return Void()
        target = source
        return target


class Vector:
    def __init__(self, size = 0):
        self.__array_val = []
        for i in range(0, size):
            self.__array_val.append(Void)

    def __len__(self):
        return len(self.__array_val)

    def __getitem__(self, index):
        return self.__array_val[index]

    def __setitem__(self, index, value):
        self.__array_val[index] = value

    def __add__(self, data_array):
        if type(data_array) is Vector and len(self.__array_val) == len(data_array):
            result_array = Vector(len(self.__array_val))
            for i in range(0, len(self.__array_val)):
                result_array[i] = self.__array_val[i] + data_array[i]
            return result_array
        else:
            return Void

    def push_back(self, val):
        item = Item(val)
        self.__array_val.append(item)

    def print(self):
        print(self.__array_val)

    @classmethod
    def assignment_attempt(cls, target, source):
        if type(target) != cls or type(source) != cls:
            return Void()
        target.__array_val = source.__array_val
        return target


left = Item(1)
right = Item(2)
result = left + right

vec = Vector()
vec.push_back(1)
vec.push_back(2)
vec.push_back(3)

vec2 = Vector()
vec2.push_back(4)
vec2.push_back(5)
vec2.push_back(6)

vec_1 = Vector()
vec_1.push_back(vec)
vec_1.push_back(vec2)

vec3 = Vector()
vec3.push_back(1)
vec3.push_back(2)
vec3.push_back(3)

vec4 = Vector()
vec4.push_back(4)
vec4.push_back(5)
vec4.push_back(6)


vec_2 = Vector()
vec_2.push_back(vec3)
vec_2.push_back(vec4)

vec_3 = (vec_1 + vec_2)
vec_3[1].print()
# [5, 7, 9]
# if vec2.push_back(6) is commented:
#     AttributeError: type object 'Void' has no attribute 'print'