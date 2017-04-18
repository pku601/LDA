# -*- coding: utf-8 -*-
import codecs
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

fin = codecs.open('abstract_temp.txt', 'r', 'utf-8')
fout = codecs.open('abstracts_clean.txt', 'w', "utf-8")

lines = fin.readlines()

line_num = 0
for line in lines:
    if len(line.strip()) == 0:
        continue
    line_num += 1
    if line_num % 2 == 0:

        if line.strip() == 'Section None':
            fout.write(line)
            continue

        line = line.strip()
        print line

        line = re.sub('\(.*?\)', '', line)

        line = re.sub('[^a-zA-Z]', ' ', line)
        line = re.sub(' {2,}', ' ', line)  # substitute multiple space to one space

        print line.strip()
        print ''

        fout.write(line.strip())
        fout.write('\n')

    else:  # line content: xxx.html
        fout.write(line)

fout.close()
