#!/usr/bin/python

"""Protocolos iteráveis e iteradores
    métodos __iter__() e __next__() 
"""


class DataTable:
    def __init__(self, name, filename):
        self._name = name
        self._c = 0
        with open(filename)as data:
            self._data = data.readlines()

    @property
    def name(self):
        return self._name

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            element = self._data[self._c]
        except IndexError as ie:
            self._c = 0
            raise StopIteration
        self._c += 1
        return element

    """Protocolo de Sequencia método __getitem__()"""

    def __getitem__(self, i):
        if isinstance(i, int) or isinstance(i, slice):
            return self._data[i]
        raise TypeError("Invalid index/slice object '{}'".format(str(i)))


table = DataTable("ExecucaoFinanceira", "data/data/ExecucaoFinanceira.csv")

"""for line in table:
    print(line)"""

#print(table[0])

#print(table[1:3])

print(table['1']) # raise TypeError: Invalid index/slice object '1'