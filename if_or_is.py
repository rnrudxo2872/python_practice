def hello_test(a,b):
  # || 대신 or <=> && 대신 and   또한  is는 객체의 id가 같은지, ==은 value가 같은지 비교하는 것.
  if(type(b) == int or type(b) == float):
    return "true"
  else:
    return "ye"

print(hello_test(1,2))