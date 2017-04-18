
fout_name = open('file_name.txt', 'wb')
fout_abstracts = open('abstracts.txt', 'wb')

with open('../abstracts_clean2.txt', 'r') as f:
    count = 0
    file_name_record = f.readline()
    abstract_record = f.readline()
    while file_name_record.strip() != '':
        count += 1
        print count
        if abstract_record.strip() != 'section none':
            fout_name.write(file_name_record)
            fout_abstracts.write(abstract_record)
        file_name_record = f.readline()
        abstract_record = f.readline()

    if abstract_record.strip() != 'section none':
        fout_name.write(file_name_record)
        fout_abstracts.write(abstract_record)

fout_name.close()
fout_abstracts.close()
