# Python is a loosely typed language
# we dont need to define the data
# different data types in python are :
# int, float, string, list, tuple, set, dictionary
num=293
decimal=569.44
word="This is string"
group=['raju','rajeev','ram']
group1=(2,4,5,56)
group2={245,6,2,562,2562}
group3={"i":"one","ii":"two","iii":"three"}

datatype={
    "number":type(num),
    "float":type(decimal),
    "string":type(word),
    "list":type(group),
    "tuple":type(group1),
    "set":type(group2),
    "dictionary":type(group3)
    }
valueOfvariable=[num,decimal,word,group,group1,group2,group3]
print(len(valueOfvariable))
for i in valueOfvariable:
    print(i)
for i in datatype.values():
    print(i)