#_*_coding:utf-8_*_
import codecs
import numpy as np


def load_data(path):
    lines=codecs.open(path,'r','utf-8')
    item_dict={}
    stu_dict={}
    for line in lines:
        lists=line.replace('\r\n','').split(',')
        day_time=':'.join(lists[0].split(':')[:-1:])
        stu=int(lists[1])
        locate=lists[2]
        if item_dict.__contains__(day_time):
            item_dict[day_time].append((stu, locate))
        else:
            item_dict[day_time]=[(stu, locate)]
        if stu_dict.__contains__(stu):
            stu_dict[stu].append((day_time,locate))
        else:
            stu_dict[stu]=[(day_time,locate)]

    return item_dict,stu_dict


def get_range(eat_time):
    day_time=eat_time[0]
    loc=eat_time[1]
    min=int(day_time.split('_')[1].split(':')[1])
    hour=int(day_time.split('_')[1].split(':')[0])
    if min>=5 and min<=54:
        range_min=np.arange(min-5,min+6,1)
        range_hour=[hour for _ in range_min]
        range_min_60=range_min
    elif min<5:
        range_min=np.arange(min-5,min+6,1)
        range_hour=[hour-1 if min <0 else hour for min in range_min]
        range_min_60=[i%60 for i in range_min]
    elif min >=55:
        range_min = np.arange(min - 5, min + 6, 1)
        range_hour = [hour + 1 if min >= 60 else hour for min in range_min]
        range_min_60 = [i % 60 for i in range_min]
    else:
        print('error')
    list_all=[]
    for (h,m) in zip(range_hour,range_min_60):
        if h<10:
            h='0'+str(h)
        if m<10:
            m='0'+str(m)
        list_all.append(day_time.split('_')[0]+'_'+str(h)+':'+str(m))

    #l=[':'.join(day_time.split(':')[0],h,m) for (h,m) in zip(range_hour,range_min_60)]
    return list_all,loc
def sum_row(row_num):
    sum_list=[stu_matrix[row_num][col] for col in range(stu_matrix.shape[1])]
    return sum(sum_list)
def sum_col(col_num):
    col_list=[stu_matrix[row][col_num] for row in range(stu_matrix.shape[0])]
    return sum(col_list)
PATH='log.txt'
item_dict, stu_dict = load_data(PATH)
stu_matrix=np.zeros((max(stu_dict.keys())+1,max(stu_dict.keys())+2),dtype=int)
for stu in stu_dict.keys():
    eat_item_list=stu_dict[stu]
    stu_matrix[stu][-1]=len(eat_item_list)
    for eat_time in eat_item_list:
        eat_range,loc=get_range(eat_time)
        for eat in eat_range:
            if not item_dict.__contains__(eat):
                pass
            else:
                co_stu_eat_item=item_dict[eat]
                for (ostu,oloc) in co_stu_eat_item:
                    if oloc==loc and ostu!=stu:
                        stu_matrix[stu][ostu]+=1
                        #print(stu,'-------',ostu)
                    else:
                        pass
print('start write')
write_file=codecs.open('answer','w','utf-8')
for stu in range(stu_matrix.shape[0]):
    friend_list=[]
    write_str=str(stu)+'#'
    total_eat_time=stu_matrix[stu][-1]
    for if_friend in range(stu_matrix.shape[1]-1):
        if stu_matrix[stu][if_friend] >= total_eat_time/4:
            write_str+=str(if_friend)+','
        else:
            pass
    if write_str[-1]==',':
        write_str=write_str[:-1]
    write_file.write(write_str+'\n')
write_file.close()









