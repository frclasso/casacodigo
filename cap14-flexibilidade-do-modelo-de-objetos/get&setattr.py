#!/usr/bin/python


class DataTable:
    def __init__(self, name, data):
        self._name = name
        self._data = data

        def __getattr__(self, attr_name):
            print("Attributo não defino '{}' acessado".format(attr_name))

            if attr_name == "data":
                return []
            raise AttributeError("Atrinuto '{}' não existe".format(attr_name))

        def __getattribute__(self, attr_name):
            print("Atributo {} acessado".format(attr_name))
            return object.__getattribute__(self, attr_name)

t = DataTable("ExecucaoFinanceira")
t._name
print("")
t.data
print("")
t.cols