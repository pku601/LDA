# -*- coding: utf-8 -*-

from numpy import *
import time
import datetime
import pp

'''
模板以元组的形式保存，例如：('前缀1', '后缀1')
所有模板保存在列表中
'''

seeds = ('北京', '成都', '石家庄', '武汉', '长沙')  # 种子(保存在元组中)
file_path = 'querybig_1000000.txt'


def Caltime(date1, date2):  # 参考网址：http://blog.csdn.net/zhangdedezhu/article/details/7942344
    date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    date1 = datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    date2 = datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    return date2 - date1


def print_template(template_):  # 打印模板信息
    if len(template_) == 2:
        print template_[0], template_[1]
    else:
        print 'wrong template'


def find_templates():  # 查找种子的所有模板

    fp = open(file_path, 'r')
    line_num = 0
    count = 0
    temp_set_templates = set()

    lines = fp.readlines()
    for line in lines:
        line_num += 1

        for seed in seeds:
            position = line.find(seed)
            if position == -1:
                # print line, 'not find'
                count += 1
            elif position == 0:  # 只有后缀
                line_split = line.split(seed)
                if len(line_split) == 2 and line_split[1].strip() != '':
                    template = ('', line_split[1].strip())
                    temp_set_templates.add(template)
            else:  # 只有前缀 or 前缀和后缀
                line_split = line.split(seed)
                if len(line_split) == 2 and line_split[1] == '\n':  # 只有前缀
                    template = (line_split[0].strip(), '')
                    temp_set_templates.add(template)
                elif len(line_split) == 2:  # 前缀和后缀
                    template = (line_split[0].strip(), line_split[1].strip())
                    temp_set_templates.add(template)
    seeds_templates_inter = list(temp_set_templates)

    print 'seeds_templates_inter:', len(seeds_templates_inter)
    print '\nprint seeds_templates...'
    # for template in seeds_templates_inter:
    #     print_template(template)
    print '\nprint seeds_templates done...'
    print 'seeds_templates length:', len(seeds_templates_inter)
    fp.close()
    return temp_set_templates


def fun(each_template):  # 并发执行函数，找出每个模板的候选实例
    temp_set = set()
    fp = open('querybig.txt', 'r')

    for line in fp.readlines():

        line = line.strip()
        prefix = each_template[0]
        suffix = each_template[1]
        prefix_len = len(prefix)
        suffix_len = len(suffix)

        if prefix == '' and line.endswith(suffix):
            candidate = line[:-suffix_len]
            temp_set.add((candidate, each_template))

        elif suffix == '' and line.startswith(prefix):
            candidate = line[prefix_len:]
            temp_set.add((candidate, each_template))

        else:
            if line.startswith(prefix) and line.endswith(suffix):
                candidate = line[prefix_len:-suffix_len]
                temp_set.add((candidate, each_template))

    return temp_set


def add_to_candidates_vectors(candidate, template):   # 添加到候选实例向量
    # print '\nadd_to_candidates_vectors...'
    flag = False
    global candidates_vectors
    global candidates
    for every in candidates_vectors:
        if every[0] == candidate:
            dict_ = every[1]
            if (template[0], template[1]) in dict_:
                dict_[(template[0], template[1])] += 1
            else:
                dict_[(template[0], template[1])] = 1
            flag = True
            break
    if flag is False:
        candidates.append(candidate)
        temp_list = [candidate, {(template[0], template[1]): 1}]
        candidates_vectors.append(temp_list)


def construct_class_vectors(candidates_in_construct):  # 根据类模板为每个实例构建带权值的向量
    print '\nconstruct_class_vectors...'
    global class_vectors_only_seeds
    global class_vectors_no_seeds
    global candidates_no_seeds
    seeds_templates_length = len(seeds_templates)
    for candidate in candidates_in_construct:
        vector = [0 for x in range(0, seeds_templates_length)]
        for every_ in candidates_vectors:
            if every_[0] == candidate:
                for key, value in every_[1].items():
                    i = 0
                    for template in seeds_templates:
                        if key == template:
                            vector[i] = value
                            break
                        i += 1
                break
        # print vector
        if candidate in seeds:
            class_vectors_only_seeds.append(vector)
        else:
            class_vectors_no_seeds.append(vector)
            candidates_no_seeds.append(candidate)


def caculate_distance():
    print '\ncaculate_distance...'
    count = len(class_vectors_no_seeds)
    sum_ = 0
    index = 0
    adict = []
    for candidate_vector in class_vectors_no_seeds:
        for seed_vector in class_vectors_only_seeds:
            # cosine
            sum_ += dot(candidate_vector, seed_vector)/(linalg.norm(candidate_vector)*linalg.norm(seed_vector))
        distance = sum_ / count
        adict.append([distance, candidates_no_seeds[index]])
        sum_ = 0
        index += 1
    # 排序
    adict.sort(reverse=True)
    result = [[v[1], v[0]] for v in adict]
    # print result
    # 将结果写入文件
    fp = open('result.txt', 'wb')
    for each in result:
        fp.write(each[0])
        fp.write('\t')
        fp.write(str(each[1]))
        fp.write('\n')
    fp.close()


def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


start_time_1 = get_current_time()
seeds_templates = find_templates()
start_time_2 = get_current_time()
print 'time1:'
print Caltime(start_time_1, start_time_2)

ppservers = ()
job_server = pp.Server(ppservers=ppservers)
jobs = [job_server.submit(fun, (each,)) for each in seeds_templates]
candidates_vectors = []  # 候选实例向量 结构复杂：[['instance_name', {('prefix','suffix'): 1, (): 3, ... }], ... ]
candidates = []  # 候选实例集
for job in jobs:  # 合并结果
    middle_set = job()
    for each_middle_set in middle_set:
        add_to_candidates_vectors(each_middle_set[0], each_middle_set[1])

print 'candidates_vectors length:', len(candidates_vectors)
print 'candidates length:', len(candidates)
job_server.print_stats()

start_time_3 = get_current_time()
print 'time23:'
print Caltime(start_time_2, start_time_3)

class_vectors_only_seeds = []  # 只包含种子的所有候选实例对应的的（类）向量
class_vectors_no_seeds = []  # 不包含种子的所有候选实例对应的的（类）向量
candidates_no_seeds = []  # 不包括种子的候选实例集

construct_class_vectors(candidates)
start_time_4 = get_current_time()
print 'time34:'
print Caltime(start_time_3, start_time_4)

caculate_distance()
start_time_5 = get_current_time()
print 'time45:'
print Caltime(start_time_4, start_time_5)
