class General(object):
    def __init__(self):
        self.int_field = 0
        self.str_field = ''
        self.array_field = []

    def __init__(self, crObject):
        self.CopyFrom(crObject)

    def CopyFrom(self, crObject):
        if type(crObject) != General:
            return
        self.int_field = crObject.int_field
        self.str_field = crObject.str_field
        self.array_field = crObject.array_field

    def CopyTo(self, rObject):
        crObject.int_field = self.int_field
        crObject.str_field = self.str_field
        crObject.array_field = self.array_field

    def __eq__(self, crObject):
        return type(crObject) == General and crObject.int_field == self.int_field and \
               crObject.str_field == self.str_field and crObject.array_field == self.array_field

    def print(self):
        str.format('int_field: {1}; str_field: {2}; array_field: {3}', self.int_field, self.str_field, "".join(self.array_field))

    def serilize(self):
        rDict = {'int_field': self.int_field, 'str_field': self.str_field, 'array_field': ''.join(self.array_field)}
        return rDict

    def unserilize(self, crDict):
        self.int_field = crDict['int_field']
        self.str_field = crDict['str_field']
        self.array_field = list(map(int, crDict['array_field']))

    def type(self):
        return General


class Any(General):
    def DoSomething(self):
        pass