# -*- coding: utf8 -*-

#sorted
def fuckyou(dick):
  return dick[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = fuckyou, reverse = True)

print(L2)