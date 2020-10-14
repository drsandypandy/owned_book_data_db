# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:26:26 2020

@author: DemiGod
"""
import re

def comma_name(names):
    if ',' in names:
        try:
            pieces=names.split(', ')
            name= pieces[1] + pieces[0]
            return name
        except:
            return names
    else:
        return names




inp=input('Enter file name: ')
if len(inp) < 1: inp = 'Index 2003.txt'

toglist=inp.split('.')
toglist=toglist[0].split()

tog=toglist[1] + '_Output.txt'


fhand = open(inp, errors='ignore')
fout=open(tog, 'w+')



name_pattern=re.compile(r'[Bb]y (.+)')

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


    author=bline[0]
    author=comma_name(author)
    name=name_pattern.search(author)
    if name is not None:
        author=name.group(1)
    else:
        author = author


    fout.write(date)
    fout.write(' @ ')
    fout.write(author)
    fout.write(' @ ')
    fout.write(title)
    fout.write('\n')



fout.close()


#finding least common denominator for count to input for commit intervals
denom=[i for i in range(250,4, -1)]
for d in denom:
    if count%d==0:
        print('Divisable by: ', d)
        break
    else:
        continue