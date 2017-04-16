# -*- coding: utf8 -*-

import functools
#返回函数，闭包

L = [1,2,3,4,5]
def one(L):
  def two():
    def core(a,b):
      return a+b;
    return functools.reduce(core,L)
  return two

r = one(L)
rr = r()
print(rr);
      