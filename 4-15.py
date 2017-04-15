import moduleb
import PIL 
# moduleb.name();
# print(PIL)

#decorator

def log(value):
  def shit(fn):
    print("this is log function")
    def wrapper(*arg,**kw):
      print("fuckyou bitch : %s"%value)
      fn(*arg,**kw)
      print("cumming into your pussy : %s"%value)
    return wrapper
  return shit

@log("alice")
def myname(name='zhangmingzhi'):
  print("hello my name is %s"%name)

myname('sjb');

def argumentsTest(a,b,c='c',*l,**kw):
  print("a:%s, b:%s, c%s"%(a,b,c))
  for k,v in enumerate(l):
    print("k is %s value is: %s"%(k,v))
  
  for k,v in kw.items():
    print("k is %s value is: %s"%(k,v))

# L = ["z","m","z"]
# argumentsTest(1,2,3,*L,name="sjb",age=28)