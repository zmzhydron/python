# -*- coding: utf-8 -*-
# day3

lista = ['zmz']+[ 'index is '+ str(index)+'value is:'+str(value) for index, value in enumerate(range(0,100)) if index%2 == 0][20:]
print(lista)