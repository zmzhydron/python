# -*- coding: utf-8 -*-
# day3

import sys
import PIL

lista = ['zmz']+[ 'index is '+ str(index)+'value is:'+str(value) for index, value in enumerate(range(0,100)) if index%2 == 0][20:]
print(lista)
# print(sys.path)