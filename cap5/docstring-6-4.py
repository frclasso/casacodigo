#!/usr/bin/python

#coding: utf-8

#Usando docstrings


class DataTable:
    """ Representa uma Tabela de dados.

    Essa class representa uma tabela de dados do portal
    de transparência. Deve ser capaz d validar linhas
    inseridas de acordo com as colunas que possui.
    As linhas ficam registradas dentro dela.


    Attrbutes:
       name: Nome da Tabela
       columns: [Lista de colunas]
       data: [Lista de dados]

       """
    def __init__(self, name):
        """Constructor
             Args:
                 name: Nome da Tabela"""
        self._name = name
        self._columns = []
        self.data = []


class Column:
    """Representa uma coluna em um DataTable

        Essa classe contém as informações de uma coluna
        e deve validar um dado de acordo com o tipo de
        dado configurado no construtor.

        Attributes:
            name = Nome da coluna
            kind = Tipo de dado(varchar, bigint, numeric)
            description = Descrição da coluna.
            """
    def __init__(self, name, kind, description=""):
        """Constructor
            Args:
                name = Nome da coluna
                kind = Tipo de dado(varchar, bigint, numeric)
                description = Descrição da coluna.
            """

        self._name = name
        self._kind = kind
        self._description = description