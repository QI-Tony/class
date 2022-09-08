# Author: Qi Zhang
# File: hw1.py

def is_diagonal(lists):
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if (i!=j) and(lists[i][j] !=0):
                return False
    return True


def is_upper_triangular(lists):
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if (i>j) and(lists[i][j] !=0):
                return False
    return True
def contains(lists, value):
    for i in lists:
        if value in i:
            return True
    return False
def biggest(lists):
    tem = lists[0][0]
    for i in lists:
        for j in i:
            if j > tem:
                tem = j
    return tem
def indices_biggest(lists):  
    tem = lists[0][0]
    ret = [0,0]
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if lists[i][j] > tem:
                tem = lists[i][j]
                ret[0] = i
                ret[1] = j
    return ret
def substr_in_values(dic, substring):
    ret_list = []
    for key, value in dic.items():
        for i in value:
            if substring.upper() in i.upper():
                ret_list.append(key)
                break
    return sorted(ret_list)

def indices_divisible_by_3(lists):
    ret = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if ((i+j)%3 == 0):
                ret.append(lists[i][j])
    return ret
def sort_int_string (string):
    string = string.strip("\n").strip("\t")
    lists_new = string.split()
    for i in range(len(lists_new)):
        lists_new[i] = int(lists_new[i])
    lists_new.sort()
    return " ".join(str(x) for x in lists_new)
