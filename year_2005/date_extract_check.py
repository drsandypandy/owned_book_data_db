# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:26:26 2020

@author: DemiGod
"""
import re

def month_conversion(name_of_month):
    if name_of_month == 'January' or name_of_month == 'Jan':
        return "01"
    elif name_of_month == 'February' or name_of_month == 'Feb':
        return '02'
    elif name_of_month == 'March':
        return '03'
    elif name_of_month == 'April':
        return '04'
    elif name_of_month == 'May':
        return '05'
    elif name_of_month == 'June' or name_of_month == 'Jun':
        return '06'
    elif name_of_month == 'July':
        return '07'
    elif name_of_month == 'August' or name_of_month == 'Aug':
        return '08'
    elif name_of_month == 'September' or name_of_month == 'Sept':
        return '09'
    elif name_of_month == 'October' or name_of_month == 'Oct':
        return '10'
    elif name_of_month == 'November' or name_of_month == 'Nov':
        return '11'
    elif name_of_month == 'December' or name_of_month == 'Dec':
        return '12'

def find_date(something):
    datepos = something.find('\\')
    begin=something[:datepos]
    begin=begin.split()
    lstnum=len(begin)
    year = begin[lstnum-1]
    if len(year)== 2:
        year='20'+year
    else:
        year=year
    month = begin[lstnum-2]
    month=month_conversion(month)

    begin.pop()
    begin.pop()
    date=[]
    for item in begin:
        if re.search('.*[0-9][0-9].*',item)==None:
            continue
        else:
            datenums= re.findall('.*([0-9][0-9]).*', item)
            for x in datenums:
                y= month +'-'+ x + '-'+ year
                date.append(y)
    #print(date)
    return date


inp=input('Enter file name: ')
if len(inp) < 1: inp = 'Index 2005.txt'

toglist=inp.split('.')
toglist=toglist[0].split()

tog=toglist[1] + '_Date_Output.txt'


fhand = open(inp, errors='ignore')
fout=open(tog, 'w+')

date_pattern=re.compile(r'\d\d-\d\d-\d\d\d\d')

total=0
count=0
for line in fhand:
    count=count+1
    if '\\' not in line: continue
    datepos = line.find('\\')

#only has the date info to contend with, even though unformatted.
    beginning=line[:datepos]





#extracting dates in format like 01-01-1999 or 10_11_1999
    if re.search('(.*[0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9])', line) != None:
        dates = re.findall('.*([0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9])', line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''
    elif 'EXTRA'in beginning:
        line= re.sub('EXTRA', '', line)


# searches the dates for dates that are written out long hand and formats them into correct format
    elif re.search('.*[0-9][0-9].+Jan.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Jan.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Jan.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Feb.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Feb.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Feb.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+March.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+March.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+March.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+April.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+April.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+April.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+May.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+May.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+May.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Jun.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Jun.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Jun.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+July.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+July.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+July.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Aug.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Aug.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Aug.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Sept.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Sept.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Sept.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Oct.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Oct.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Oct.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Nov.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Nov.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Nov.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

    elif re.search('.*[0-9][0-9].+Dec.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+&.+[0-9][0-9].+Dec.+[0-9].+\\\\', line) or re.search('.*[0-9][0-9].+[0-9][0-9].+[0-9][0-9].+Dec.+[0-9].+\\\\', line) is not None:
        dates=find_date(line)
        if re.search ('.*Part.*[0-9]\\\\',line) is not None:
            date_qual = re.findall('.*(Part.*[0-9])\\\\',line)
        else:
            date_qual=''

#if all else fails...we can see what input they included

    else:
        dates =[beginning]
    fout.write(str(count))
    fout.write(' ~ ')
    for date in dates:
        fout.write(date)
        fout.write(' ')
    if len(date_qual)>4:
        fout.write(' - ')
        fout.write(date_qual)
    fout.write('\n')



fout.close()
