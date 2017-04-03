# -*- coding: utf-8 -*-
import method

a = 'my name is %s, and my age is %d, and my life is @ %d %%' %('张明之', 77-49, 29/100*100);
# print(a);
member = ('sjb','zmz', 'joker');
tuples = 22;
if tuples > 10:
		for shit in member:
			print("my name is %s " %shit)
elif tuples > 20:
		print("no shit")
else:
		print(" hahaha")


listone = ['me','father','monther','wife','son']
# listtwo = []
# count = 0
# while len(listone) > len(listtwo):
# 	listtwo.append(input("input your %s's name: " %listone[count]))
# 	count = count + 1

# for indivudual in listtwo:
# 	print("there are %s and hello!" % indivudual);

# objects = {'name': "zhangmingzhi"}
# objects[member] = [1,2,3,4,5]
# print(objects)

methodresult = method.minmingguanjianzicanshufn("张明之",28, salary="11000", fucking="nice" )
print(methodresult)
print(method.reducer(100))