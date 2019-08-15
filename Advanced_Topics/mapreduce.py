'''
CTCI Advanced - MapReduce
'''

def map(document):
    res = {}
    for item in document:
        key = str(item[1])+'_'+str(item[0])
        if key in res:
            res[key].append((item[2], 1))
        else:
            res[key] = [(item[2], 1)]
    return res


def reduce(map, year, cityName):
    key = str(cityName)+'_'+str(year)
    
    if key not in map:
        return -1
    
    temps = map[key]
    sum = 0
    total = 0
    for temp, num in temps:
        sum += int(temp)*num
        total += num
    return sum/total
        
# Driver to test
document = [
    ('2012', 'Philadelphia', '58.2'),
    ('2011', 'Seattle', '45.1'),
    ('2019', 'Seoul', '25'),
    ('2019', 'Seoul', '100'),
    ('2019', 'Seoul', '75'),
    ('2019', 'Seoul', '85'),
    ('2019', 'Seoul', '50')
]

res = map(document)
print(reduce(res, '2019', 'Seoul'))