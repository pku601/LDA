import re
import codecs

fp = open('abstracts_clean.txt', 'wb')

with open('abstracts_small_test.txt', 'r') as f:
    line_num = 0
    for line in f:
        if line_num > 100000:
            pass
        line_num += 1
        if line_num % 2 == 0:
            if line.strip() == 'Section None':
                fp.write(line)
                continue
            line = line.strip()
            # print line
            line = line.replace('. ', ' ').replace('.', ' ')
            line = line.replace(', ', ' ').replace(',', ' ')
            line = line.replace(':', '').replace(';', '').replace('\\', '')
            line = re.sub(' {2,}', ' ', line)  # substitute multiple space to one space
            line = re.sub('\(.*?\)', '', line)
            line = line.replace(')', '').replace('=', ' ').replace('<', ' ').replace('>', ' ')
            # line = re.sub('|.*?|', ' ', line)
            line = re.sub(' {2,}', ' ', line)  # substitute multiple space to one space
            print line.strip()
            fp.write(line.strip())
            fp.write('\n')
            # print ''
        else:  # line content: xxx.html
            fp.write(line)
fp.close()
fin = codecs.open('abstracts_small_test.txt')
lines = fin.readlines()
for line in lines:
    if line.find('∈'):
        print 'find'
