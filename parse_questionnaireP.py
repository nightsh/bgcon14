#/usr/bin/python

import sys, csv, re
from operator import itemgetter


def find_columns(file):
# answer possibilities are equal to regex [A-Z][0-9][0-9]?\.
    
    columns = []
    
    readfile = file.read()
    for i in re.findall(r'[A-Z][0-9][0-9]?\.', readfile):
        columns.append(i)

#    print columns
    
    return sorted(set(columns))

def output(list):

    lastQ = ''
    edgelist = []

    for row in list:
        print row
        question = row[0]
        UI = row[1]

        if lastQ == '':
            lastQ = question
            edgelist.append(UI)

        elif lastQ == question:
            edgelist.append(UI)

        elif lastQ != question:
            if len(edgelist) < 1:
                pass
            else:
                while len(edgelist) > 1:
                    edges.writerow(edgelist)
                    del edgelist[0]

            lastQ = question
            edgelist = []
            edgelist.append(UI)

    # print the last line
    while len(edgelist) > 1:
        edges.writerow(edgelist)
        del edgelist[0]

networks = open(sys.argv[2]).read()
networks = filter(None, networks.split('\n'))
print networks

for row in networks:

    print row
    l = row.split(' ')    

    nname = l[0]
    target = l[1:]
    print target

    # read inputfile as csv
    inputfile = open(sys.argv[1])
    reader = csv.reader(inputfile, delimiter = ',', quotechar = '"')

    # create attributes csv
    aname = 'attributes-'+nname+'.csv'
    attributes = csv.writer(open(aname,'w'), delimiter = ',', quotechar = '"')
    attributes.writerow(["ID", "name", "organisation", "age", "gender", "based in", "born in", "field","track"])

    id = 0
    IDs = []

    answers = []

    columns_list = find_columns(inputfile)

    inputfile.seek(0)
    for row in reader:

        if id == 0:
            header = row
            id +=1
        else:
        # create unique indentifiers
            ID = 'BG'+str(id).zfill(3)
            IDs.append(ID)
            id += 1

            name = row [1]
            organisation = row[2] 
            age = row[3]
            gender = row[4]
            based = row[5]
            born = row[6]
            field = row[7]
            track = row[9]        

    #   print ID,age,gender,track

            attributes.writerow([ID, name, organisation, age, gender, based, born, field, track])

    # create edges csv
        
            for i in columns_list:
                if i in ','.join(row):
                    answers.extend([[i,ID]])


    #print answers
    ename = 'edges-'+nname+'.csv'
    edges = csv.writer(open(ename,'w'), delimiter = ',')
    sorted = sorted(answers, key=itemgetter(0))

    output(sorted)
    print "%s added" % len(sorted)

#   # read most popular_answers.csv
#    popular = csv.reader(open('popular_answers.csv'), delimiter = ',', quotechar = '"')
#
#
#    filtered = [] # list created by a filter
#
#    filter = raw_input("Specify answers you want to filter out: \n questions (A-Z) or answers (B09) separated with space \n answers with occurence below or above a certain number (<50) [max %s] \n or enter if you want to use all the answers:" % len(IDs))
#
#
#    if filter == '':
#        output(sorted)
#
#        print "%s responses added to 'attributes.csv' and 'edges.csv'" % len(sorted)
#
#    elif '<' in filter or '>' in filter:
#        
#        filters = []
#        
#        for row in popular:
#     
#            numAns = int(row[0])
#            code = row[1]
#
#            if '<' in filter:
#                f = filter.lstrip('<')
#                if numAns <= int(f):
#                    filters.append(code)
#
#            elif '>' in filter:
#                f = filter.lstrip('>')
#                if numAns >= int(f):
#                    filters.append(code)
#
#        print filters
#        for a in sorted:
#            for f in filters:
#                if f in a[0]:
#                    filtered.append(a)
#                    
#        output(filtered)
#        print "%s responses added to 'attributes.csv' and 'edges.csv'" % len(filtered)
#
#            
#
#    else:
#        filters = filter.split(' ') # list created by user
#        for a in sorted:
#            for f in filters:
#                if f in a[0]:
#                    filtered.append(a)
#                    
#        output(filtered)
#        print "%s responses added to 'attributes.csv' and 'edges.csv'" % len(filtered)
