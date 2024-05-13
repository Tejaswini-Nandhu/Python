# list is a mutable datatype in python enclosed in b/w [] square braces
"""
EX: my_list=[39,453,56]
* we can store heterogenous data in lists
* values inside list are known as elements 
* we can assess those elements through indexing where 
  indexing starts from 0
"""

my_list=[1,2,3,4,5,6]
print(type(my_list))
# iterating the list
for i in my_list:
    print(i)
    print(type(i))

# slicing 

print(my_list[0:])
print(my_list[:])
print(my_list[2:5])
print(my_list[-5]) #accesing the list backward

# concatenation
list1=[2,3,4,5,7]
list2=[1,6]

print(list1+list2)

for i in list1:
  print(f"square of element {i} in list1 ={i**2}")

#len of list

length_of_list1=len(list1)
print(f"No of elemnets in list1 = {length_of_list1}")

#replacing values through slicing

list1[0:3]=[1,4,9,16]
print(list1)
list1[0:6]=[]
print(list1)

#adding elements to the list through append method
#append adds an element at the last position
list1.append(8)
list1.append(20)
list1.append(2)
list1.append(33)
print(list1)
print("practice code snippets")
#removing an element from the list
# pop removes the last element present in the list
# list1.pop()
# print(list1)

#fibonaaci series- add two consecutive integers of the given sequence
# a=0               |     a=0        
# b=1               |     b=1        
# while a<5:        |     while a<5: 
#   print(a)        |       print(a) 
#   a,b=b,a+b       |       a=b
# results 0,1,1,2,3 | results 0,1,2,4

#sum of elements in the list
addup=[1,2,3,5]
sum=0
for i in addup:
  sum+=i
print(sum)


#multiply all the items in the list
mulup=[1,2,3,5]
mul=1
for x in mulup:
  mul*=x
print(mul)

#largest number from the list
maxnum=[23,53,322,434,244]
maximum=max(maxnum)
for maxi in maxnum:
  if maxi==maximum:
    print(maxi)

#smallest number from the list
minnum=[23,53,322,434,244]
minimum=min(minnum)
for mini in minnum:
  if mini==minimum:
    print(mini)

# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
print("matching the string and counting the matches")
words=['teja','ullu','3003','212','nandhu','4342']
count=0
for word in words:
  if len(word)>0 and word[0]==word[-1]:
    count+=1
print(count)