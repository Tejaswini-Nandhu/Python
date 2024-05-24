# class testClass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def __str__(self):
#         return f"{self.name},{self.age}"
    
# person1=testClass("Tejaswini",22)

# print(person1.name)
# print(person1.age)

# print(person1)

class Greeting:
    def __init__(self,name,wish):
        self.name=name
        self.wish=wish
    
    def greet(abc):
        return f"Good {abc.wish} {abc.name}"

greeting1=Greeting("Tejaswini","Evening")

greeting1.wish="morning"
print(greeting1.greet())