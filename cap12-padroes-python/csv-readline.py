#!/usr/bin/python

import csv


class Reader():
    with open('data/data/ExecucaoFinanceira.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
