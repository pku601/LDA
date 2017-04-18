import os
from bs4 import BeautifulSoup
import re

input_dir = 'LNCS_articles'
files = os.listdir(input_dir)

none_count = 0
valid_count = 0
total_count = len(files)

fp = open('abstracts.txt', 'wb')
count = 0
for _file in files:
    count += 1
    if count % 1000 == 0:
        print count
    with open(input_dir + "/" + _file, 'r') as f:
        # print _file
        fp.write(_file)
        fp.write('\n')
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'lxml')
        section = soup.find_all("section", class_="Abstract", limit=1)
        if section is None or len(section) == 0:
            # print 'Section None'
            fp.write('Section None')
            fp.write('\n')
            none_count += 1
        else:
            valid_count += 1
            _section = str(section[0])
            _soup = BeautifulSoup(_section, 'lxml')
            text = _soup.get_text()[8:]
            # print text
            text = text.encode("utf-8")
            text = re.sub('\n', ' ', text)
            fp.write(text)
            fp.write('\n')

print '\nnone_count: ' + str(none_count)
print 'valid_count: ' + str(valid_count)
print 'total_count: ' + str(total_count)

fp.close()
