#!/usr/bin/python

#coding: utf-8

import os


def main():
    meta = {}
    for meta_data_file  in os.listdir('/Users/fabio/Estudo/Prog/Python/'
                                      'python_casa_do_codigo/cap4/data/'
                                      'meta-data/'):
        table_name = meta_data_file.split('.')[0]
        print(table_name)

if __name__ == "__main__":
    main()
