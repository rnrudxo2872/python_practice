test = ('ef','dumyy','dffqwq','a'
)

print(max(test))
print(min(test))

test2 = (4,2,3,4,6,1,4,5,10)

print(max(test2))
print(min(test2))

dic = {
  "name" :"경태",
  "age": 24,
  "type":None
}

print(dic);
print(dic["name"]);
print(type(dic["type"]));
print(type(dic["age"]))
dic["type"] = "null";
dic["ref"] = "Yes";

print(dic)

dic["addList"] = [];
dic["addList"].append("add name");

print(dic)
print(len(dic))

character = '10'
print(int(character))

def wellcome(name="unknown"):
  print("hellow", name+"!");

wellcome();
wellcome("경태")

def plus(a=1,b=5):
  return a-b;

print(plus(b=2))

def pluse(a,b):
  return (int(a) + int(b))

def minus(a,b):
  return int(a) - int(b);
a = 3;
if a==1:
  print(a);
elif(a==2):
  print(2);


def hello_test(a,b):
  # || 대신 or <=> && 대신 and   또한  is는 객체의 id가 같은지, ==은 value가 같은지 비교하는 것.
  if(type(b) == int or type(b) == float):
    return "true"
  else:
    return "ye"

print(hello_test(1,2))