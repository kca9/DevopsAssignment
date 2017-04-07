dict = {'first': 'apple', 'second': '100', 'third': 16, 4: 42, 'six': (5, 12, 8), 'ten': ['aaa', 'ball', 34, 01],
        'seven': '555', '100': {1: 10, 2: 20, 'pop': 5}, 'float': 10.5}
# this is for (5,12,8)calculation
tuple = dict['six']
a = tuple[0]
a1 = tuple[1]
a2 = tuple[2]
# this is for 'third' calc
tuple6 = int(dict['third'])
#this is for dict [4]
tuple7 = dict[4]
#this is for dict ['ten']
tuple1 = dict['ten']
b1 = tuple1[2]
b2 = tuple1[3]
#this is for dict ['second']
tuple2 = int(dict['second'])
#this is for dict ['seven']
tuple3 = int(dict['seven'])
#this is for dict [100]
tuple4 = dict['100']
c1 = tuple4[1]
c2 = tuple4[2]
c3 = int(tuple4['pop'])
#this is for dict ['float']
tuple5 = dict['float']
sum = a + a1 + a2 + tuple2 + tuple3 + c1 + c2 + c3 + tuple5 + b1 + b2 + tuple6 + tuple7
print sum
