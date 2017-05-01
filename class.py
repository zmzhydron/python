#-*- encoding: utf8 -*-

#4.15 python类型尝试

class Person(object):
  def __init__(self,name,power="fuck"):
    self.__name = name
    self.__power = power
  def sayname(self):
    # print("my name is %s my sex is %s, my age is %s"%(self.name,self.sex,self.age))
    print("my name is %s"%self.__name)
  def getName(self):
    return self.__name
  def setName(self,name):
    self.__name = name
  def showPower(self):
    print(" iam i hunmanbeing, and my power is %s"%self.__power)

me = Person('zhangmingzhi')
me.sayname()


class SUPERMAN(Person):
  def __init__(self,power,name="kenclark"):
    self.__power = power
    self.__name = name
    self.__speed = 200
  def showPower(self):
    print("my name is %s and i can :%s current speed is %s"%(self.__name,self.__power,self.__speed))
  @property
  def speed(self):
    return self.__speed
  # @speed.setter
  # def speed(self,value):
  #   self.__speed = value

kenclark = SUPERMAN("fly")
kenclark.showPower();
