# # array functions
# arr  = [1,2,3]
# arr.insert(3, 4)
# print(arr)


# # defaultdict
# import collections
# from collections import defaultdict

# list_dict = defaultdict(list)
# s = [('red', 1), ('blue', 2), ('red', 3), ('green', 6), ('blue', 4)]
# for k, v in s:
#     list_dict[k].append(v)

# print(list_dict)
# print(list_dict.items())


##TIME and DATE###
## https://dojang.io/mod/page/view.php?id=2463
## https://python.bakyeono.net/chapter-11-3.html
import time
#secs. returns time since 1970.1.1, uses UTC
# print(time.time())
# print(time.localtime())
# print(time.strftime('%d-%m-%y', time.localtime()))
# print(time.strftime('%c', time.localtime()))

# #Time 계산, 현재시간 활용하기
from datetime import timedelta, datetime, date
import time
# d = date.today() #date only
# n = datetime.now()
# h = time.localtime() #structured time
# print(n.time().hour)
# print(n.minute)
# print(n.minute+60)

# now = datetime.now()
# then = datetime.

start_hour = 00
start_minute = 00
length = 180

start = datetime(100, 1, 1, start_hour, start_minute, 0)
end = start - timedelta(minutes=length)
# result = str(end.time())
result = end - start
# result = end.strftime('%H:%M')
diff = datetime(100,1,1,11) > datetime(100,1,1,12)
print(type(end))


###generate random number
print('------generate random number----')
from random import *
n = randint

## testing list in list
print('---------testing list in list---')
newSubset = [3]
subset = [2,3,4]
for value in subset:
    if value not in newSubset:
        newSubset.append(value) 
print(newSubset)

## getting first digit
print('---------getting first digit---')
n = 567 % 10

### file 조작 https://simplesolace.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%8C%8C%EC%9D%BC

## map
print('---------map---')
# two_times.py
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times2(x): 
        return x*2

print(list(map(two_times2, [1, 2, 3, 4])))

list(map(lambda a: a*2, [1, 2, 3, 4]))

##
print('-----easy way to define graph list')
graph = defaultdict(list)

###sorting!!!!!
# self.graph = sorted(self.graph,key=lambda item: item[2]) 

########orderedDict!!
#OrderedDict.move_to_end(key)!!!!!!!!!!!!! <- when iserting for cacheing