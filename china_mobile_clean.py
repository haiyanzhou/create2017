"""
异常手机清洗流程
"""
import math
from collections import Counter
######
def clean_number(mobile):
    #function returns 'NULL' and error code if mobile invalid
    #returns correct mobile and code = 0 if valid
    #error code
    # 0-normal 正确手机号
    # 1-empty value 空值
    # 2-invalid mobile format 非法格式
    # 3-invalid mobile length 非法长度
    # 4-invalid mobile prefix 非法号段
    # 5-invalid entropy 非法信息熵
    tmp=list()
    flag = 0
    new = 'NULL'
    #head_list is the prefix of 3 length belongs to Chinese mobile operators.
    head_list_cmcc=['134','135','136','137','138','139','150','151','152','157','158','159','182','183','184','187','188','147','178']
    head_list_unicom=['130','131','132','155','156','185','186','145','176']
    head_list_tel=['133','153','180','181','189','177']
    head_list_virtual=['170','171']
    head_list = list()
    head_list.extend(head_list_cmcc)
    head_list.extend(head_list_unicom)
    head_list.extend(head_list_tel)
    head_list.extend(head_list_virtual)
    #Empty value
    if(not mobile):
        return ('NULL',1)
    #find the first '1'
    start = mobile.find('1')
    if(start==-1):
        return ('NULL',2)
    else:
        new = mobile[start:]
    if(len(new)<11):
        return ('NULL',3)
    #fulfill 11 digits
    for s in new:
        if(s.isdigit()):
            tmp.append(s)
            flag = flag + 1
    #check length
    if(flag==11):
        new = ''.join(tmp)
    else:
        return ('NULL',3)

    #check head
    head = new[0:3]
    if(head not in head_list):
        return ('NULL',4)

    #check entropy
    var = 2 #entropy threshold
    if(mobile_entropy(new)<=var):
        return('NULL',5)
    return(new,0)

def mobile_entropy(mobile):
    new = mobile + '#'
    bigrams = list()
    for i in range(0,len(mobile)-1):
        bigrams.append(new[i:i+2])
    c = Counter(bigrams)
    frequency = [1.0*element/len(mobile) for element in c.itervalues()]
    e = 0
    for element in frequency:
        e = e - element*math.log(element,2)
    return e
