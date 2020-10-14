# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:26:26 2020

@author: DemiGod
"""
import re





inp=input('Enter file name: ')
if len(inp) < 1: inp = 'Index 2003.txt'

toglist=inp.split('.')
toglist=toglist[0].split()

tog=toglist[1] + '_Title_Output.txt'


fhand = open(inp, errors='ignore')
fout=open(tog, 'w+')


total=0
count=0
for line in fhand:
    count =count + 1
    line=line.strip()
    if '\\' not in line: continue
    line=line.split('\\')
    date =line[0]
    line=line[1]
    line=line.split('.rar')
    line=line[0]

    bline=line.split(' - ')
    title=bline[-1]
    if len(title)<4:
        title=bline[-2]
    fout.write(str(count))
    fout.write(' ~ ')
    fout.write(title)
    fout.write('\n')



fout.close()
