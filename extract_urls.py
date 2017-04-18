import re
import os

_dir = './LNCS'

files = os.listdir(_dir)

fp_write = open('lncs_article_urls.txt', 'wb')

for _file in files:
    with open(_dir + '/' + _file, 'r') as fp:
        content = fp.read()
        result_list = re.search('<ol id="results-list" (.*?)</ol>', content, re.S)
        if result_list is None:
            print _file + ' None'
        else:
            h2s = re.findall('<h2>(.*?)</h2>', result_list.group(1), re.S)
            if h2s is not None:
                for h2 in h2s:
                    href = re.search('href="(.*?)">', h2, re.S)
                    if href is not None:
                        cur_url = 'http://link.springer.com' + href.group(1) + '\n'
                        fp_write.write(cur_url)

fp_write.close()
