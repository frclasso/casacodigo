#!/usr/bin/python

#coding: utf-8

from collections import namedtuple

ExecucaoFinanceira = namedtuple('ExecucaoFinanceira',
                                ['IdExecucaoFinanceira',
                                 'IdEmpreendimento',
                                 'IdInstituicaoContradado',
                                 'IdPessoaFisicaContratado',
                                 'IdLicitacao',
                                 'ValContrato',
                                 'ValTotal',
                                 'DatAssinatura',
                                 'DatInicioVigencia',
                                 'DatFinalVigencia'])

execucao = ExecucaoFinanceira(
    '1',
    '2',
    '132',
    '-1',
    '76',
    '696648486.09',
    '0',
    '19/03/2010',
    '21/03/2010',
    '05/10/2013'
)

print(execucao.ValContrato)
print("Saída: {}".format(execucao))