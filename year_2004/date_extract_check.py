# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:26:26 2020

@author: DemiGod
"""
import re



inp=input('Enter file name: ')
if len(inp) < 1: inp = 'Index 2004.txt'

toglist=inp.split('.')
toglist=toglist[0].split()

tog=toglist[1] + '_Date_Output.txt'


fhand = open(inp, errors='ignore')
fout=open(tog, 'w+')

date_pattern=re.compile(r'\d\d-\d\d-\d\d\d\d')

total=0
count=0
for line in fhand:
    count =count + 1
    line=line.strip()
    if '\\' not in line: continue
    line=line.split('\\')
    date =line[0]
    date=date_pattern.search(date)
    if date is not None:
        date=date.group(0)
    else:
        print(count, ' ~ ', date)
        date = 0

    fout.write(str(count))
    fout.write(' ~ ')
    fout.write(date)
    fout.write('\n')



fout.close()
