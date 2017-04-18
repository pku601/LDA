

def write_file(fp, stop, content1, content2):
    for ii in range(1, stop):
        fp.write(content1 + str(ii) + content2 + '\n')


def combine_str(start_year, stop_year):
    return '?facet-language=%22En%22&facet-content-type=%22Article%22&sortOrder=newestFirst&facet-discipline=%22Computer+Science%22&date-facet-mode=between&facet-start-year=' + str(start_year) + '&facet-end-year=' + str(stop_year)


def combine_str_two(year):
    return '?facet-language=%22En%22&facet-content-type=%22Article%22&sortOrder=newestFirst&facet-discipline=%22Computer+Science%22&date-facet-mode=in&facet-start-year=' + str(year) + '&facet-end-year=' + str(year)

with open('lncs_urls.txt', 'wb') as f:
    str1 = 'http://link.springer.com/search/page/'
    write_file(f, 936, str1, combine_str(1961, 1987))
    write_file(f, 886, str1, combine_str(1988, 1994))
    write_file(f, 792, str1, combine_str(1995, 1998))
    write_file(f, 933, str1, combine_str(1999, 2002))
    write_file(f, 911, str1, combine_str(2003, 2005))
    write_file(f, 961, str1, combine_str(2006, 2007))
    write_file(f, 577, str1, combine_str_two(2008))
    write_file(f, 565, str1, combine_str_two(2009))
    write_file(f, 636, str1, combine_str_two(2010))
    write_file(f, 676, str1, combine_str_two(2011))
    write_file(f, 737, str1, combine_str_two(2012))
    write_file(f, 791, str1, combine_str_two(2013))
    write_file(f, 822, str1, combine_str_two(2014))
    write_file(f, 930, str1, combine_str_two(2015))
    write_file(f, 1001, str1, combine_str_two(2016))
    write_file(f, 94, str1, combine_str_two(2017))
f.close()
