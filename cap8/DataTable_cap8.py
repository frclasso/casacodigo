#!/usr/bin/python

#coding: utf-8

#DataTable  executando testes unitários, jogando execeções
import unittest
from decimal import Decimal
from cap5.domain import Column


class Relationship:
    """Class que representa um relacionamento entre  DataTables

        Essa class tem todas as informações que identificam um relacionamento
        entre tableas. Em qual coluna ele existe, de onde vem e pra onde vai.
    """
    def __init__(self, name, _from, to, on):

        """Construtor

            Args:
                name: Nome
                from: Tabela de onde sai
                to: Tabela pra onde vai
                on: instancia de coliuna onde existe
        """
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


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
        self._references = []
        self._referenced = []
        self.data = []

    def _get_name(self):
        print('Getter executado!')
        return self._name

    def _set_name(self, _name):
        print('Setter executado!')
        self._name = _name

    def _del_name(self):
        print('Delleter executado!')
        raise AttributeError("Não pode deletar esse atributo")

    name = property(_get_name, _set_name, _del_name)

    def add_column(self, name, kind, description=""):
        self._validate_kind(kind)
        column  = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception('Tipo inválido')

    def add_references(self, name, to ,on):
        """Cria uma referencia dessa tabela para uma outra tabela

            Args:
                name: nome da relação
                to: instancia da tabela apontada
                on: instancia coluna em que existe a relação

        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referencia para outra tabela que aponta para essa.

            Args:
                name: nome da relação
                by: instancia da tabela que aponta para essa
                on: instancia coluna em que existe a relacao
        """
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)


class DataTableTest(unittest.TestCase):
    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))

        self.table.add_column('BId', 'bigint')
        self.assertEqual(1, len(self.table._columns))

        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns))

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))

    def test_add_column_invalid_type(self):
        a_table = DataTable('A')
        self.assertRaises(Exception, a_table.add_column, ('col', 'invalid'))


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
        self._is_pk = False

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)

    def _validate(cls, kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

    #validate = staticmethod(_validate)
    validate = classmethod(_validate)


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)

        return "{}  - {} ".format('PK', _str)