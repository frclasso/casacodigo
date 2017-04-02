#!/usr/bin/python

#coding: utf-8


class DataTable:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr_name):
        print("Atributo nao definido '{}' acessado".format(attr_name))

        if attr_name == "data":
            return []
        raise AttributeError("Atributo '{}' nao existe".format(attr_name))

    def __getattribute__(self, attr_name):
        print("Atributo {} acessado".format(attr_name))
        return object.__getattribute__(self, attr_name)


t = DataTable("ExecucaoFinanceira")
t._name
t.data
t.cols