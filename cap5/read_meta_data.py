#!/usr/bin/python

#coding:utf-8


def read_meta_data(path):
    data = open(path, 'rt')
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0],
                          line_data[1],
                          line_data[2]))
        data.close()
        return meta_data

read_meta_data('/Users/fabio/Estudo/Prog/Python/python_casa_do_codigo/cap4/data/meta-data/Instituicao.txt')