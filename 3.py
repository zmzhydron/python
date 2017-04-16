# -*- coding: utf-8 -*-
# day3

import sys
import PIL

lista = ['zmz']+[ 'index is '+ str(index)+'value is:'+str(value) for index, value in enumerate(range(0,100)) if index%2 == 0][20:]
# print(lista)
# print(sys.path)
print("paper bich")
def main():
  count = 0
  while(count < 20):
    count = count + 1
    yield count

def profiles(age,name='zmz',*l,**s):
		print('my name is %s, and my age is %s, my wish are: %s'%(name,age,l));
		for v in s.items():
			print('my skill %s is %s'%(v[0],v[1]))

if __name__ == '__main__':
  print("module name is: %s"%__name__)
  gena = (x for x in range(0,20))
  # for s in gena:
    # print(str(s)+" zmz")
  wish = ['fuckbigass', 'fuckbigtits', 'salay@16k']
  skills = {"js":"execlenent", "eng":"soso","python":"good","math":"knowsome"}
  profiles(29,'zmz',*wish,**skills)
else:
  print("import")