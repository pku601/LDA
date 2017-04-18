import re

filename = 'dblp.txt'
output_file = 'dblp_titles.txt'
fp = open(output_file, 'wb')
with open(filename, 'r') as f:
    for line in f:
        title_line = re.search('<title>(.*?)</title>', line, re.S)
        if title_line and title_line.group(0) != '<title>Home Page</title>':
            title_line = title_line.group(0)[7:-8]
            print title_line
            fp.write(title_line)
            fp.write('\n')
fp.close()
