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


if __name__ == '__main__':
  print("shit man %s"%__name__)
  gena = (x for x in range(0,20))
  for s in gena:
    print(s)
else:
  print("gogobich")