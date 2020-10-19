# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:26:26 2020

@author: DemiGod
"""


inp=input('Enter file name: ')
if len(inp) < 1: inp = '2005_Output.txt'



tog='2005_Final_Check.txt'


fhand = open(inp, errors='ignore')
fout=open(tog, 'w+')





count=0
for line in fhand:
    count =count + 1
    line=line.split('@')
    if len(line)==3: continue
    else:
        fout.write(str(count))
        fout.write(' ~ ')
        num=str(len(line))
        fout.write(num)
        fout.write('\n')

#too many with out spaces, not worth fixing
#    elif  '_' in author:
#        fout.write(str(count))
#        fout.write(' ~ ')
#        fout.write(author)
#        fout.write('\n')
#still too many with out spaces, not worth fixing
#    elif ' ' not in author:
#        fout.write(str(count))
#        fout.write(' ~ ')
#        fout.write(author)
#        fout.write('\n')
#        total=total+1




fout.close()
