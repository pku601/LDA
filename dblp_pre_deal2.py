# -*- coding: utf-8 -*-
import codecs
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

fin = codecs.open('dblp_titles_without_titleelement.txt', 'r', 'utf-8')
fout = codecs.open('dblp_titles_clean.txt', 'w', "utf-8")

lines = fin.readlines()

line_num = 0
for line in lines:
    if len(line.strip()) == 0:
        continue
    line_num += 1

    line = line.strip()

    line = re.sub('\(.*?\)', '', line)

    line = re.sub('[^a-zA-Z]', ' ', line)
    line = re.sub(' {2,}', ' ', line)  # substitute multiple space to one space

    fout.write(line.strip())
    fout.write('\n')

fout.close()
