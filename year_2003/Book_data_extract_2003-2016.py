# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:14:17 2020

@author: DemiGod
"""

import re


inp = input('File name: ')


if len(inp)<1: inp = 'Index 2003.txt'


toglist=inp.split('.')
toglist=toglist[0].split()

tog=toglist[1] + '_Output.txt'


fhand = open(inp, errors='ignore')

fout=open(tog, 'w+')




#worked for files 2009,2008,2007

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

def by_name (names):
        namer = re.findall('By (.+) ' , names)
        return namer

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













count = 0
for line in fhand:
    line=line.rstrip()
    count = count + 1

#code to test only part of the file, for debugging purposes

#    if count == 3700:
#        break

#for non-book lines, skips over them
    if '\\' not in line: continue

#position of first '\', which should be the one following the date
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


# finding the author name, not perfect but pretty close
    dashpos1 = line.find('-',datepos)
    name= line[datepos+1:dashpos1]
    name= comma_name(name)
    bob = re.findall('([0-9]+)', name)
    for item in bob:
        if item == ' ':
            continue
        else:
            namer= by_name(line)
            if len(namer) < 1:
                name = line[datepos+1:dashpos1]
                name= comma_name(name)
                name=name.strip()
                temp=line[datepos+1:].split('-')
                if len(temp) >= 4:
                    name = temp[1]
                    name= comma_name(name)
                    name=name.strip()
            else:
                name = namer[0]
    if '-' not in line:
        name = line[datepos+1:]
        name = name.split('.')
        name= name[0]

#finding the title
    if re.search('\(.+\-.+\-.+\)', line) != None:
        line = re.sub('\(.+\-.+\-.+\)', '', line)
    else:
        line = line
    if re.search('\[[.+]*\]', line) != None:
        line= re.sub('\[[.+]*\]?', '', line)
    else:
        line = line
 #   if re.search('\(V[0-9]*', line) != None:
 #       line = re.sub('\(V[0-9]*', '', line)
 #   else:
 #       line = line
 #   if re.search('\(v[0-9]*', line) != None:
 #       line = re.sub('\(v[0-9]*', '', line)
 #   else:
 #       line = line
    temp=line[datepos+1:].split('-')
    tits = len(temp)
    tit = temp[tits-1]
    if len(tit)<16:
        tit=temp[tits-2]
    ti = tit.split('.')
    pretitle=ti[0]
    maintit=pretitle.strip()
    if pretitle.startswith(' ['):
        titlelst=pretitle.split(']')
        try:
            tittemp=titlelst[1]
            tittemp2=tittemp.strip()
            maintit=tittemp2
        except:
            tittemp=titlelst[0]
            tittemp2=tittemp.strip()
            maintit=tittemp2
    print(maintit)




#    print(count,'--' ,dates)
#    print(dates, ' - ', name, ' - ', maintit)

#    fout.write(str(count))
#    fout.write(': ')

#    fout.write('Missing Packs: ')
    fout.write(toglist[1])
    fout.write('@')
    if len(dates)==1:
        fout.write(dates[0])
    else:
        for x in dates:
            fout.write(x)
            fout.write(', ')
    fout.write('@')
    if len(date_qual)>=1:
        for y in date_qual:
            fout.write(y)
            fout.write('@')
    else:
        fout.write(' ')
#    fout.write('@')
    fout.write(name)
    fout.write('@')
    fout.write(maintit)
    fout.write('\n')
#    print(count)


fout.close()
print ("All Done!")
print('Count: ', count)

denom=[i for i in range(250,4, -1)]
for d in denom:
    if count%d==0:
        print('Divisable by: ', d)
        break
    else:
        continue