#-*- coding: utf8 -*-

#new
def name(name="zmz"):
  print('hello: %s'%name)


print(__name__)

if(__name__ == "__main__"):
  name()
else:
  print("when shit hits the fan")