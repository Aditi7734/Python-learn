"""name = input("Enter your name: ")
print("Hello",name,"welcome!")
print(f"{name}","welcome!")
print(f"{name}", "welcome!")
print("{} welcome!".format(name))
print("{} {}".format(name,"welcome!"))
s="Aditi"
age=20
city="Delhi"
print(s,age,city)
x, y =input("Enter two values: ").split()
print("values are:",x)
print("values are:",y)
x,y,z=input("Enter three values: ").split()
print("values are:",x)
print("values are:",y)  
print("values are:",z)
color = input("Enter your favorite color:   ")
print(f"{color}", "is beautiful choice!")
n= int(input("How many roses?"))
print(n)
price=float(input("Enter the price:"))
print(price)
a="Hello Aditi"
b=1
c=12.34
d=("Geeks", "for", "geeks")
e=["Geeks", "for", "geeks"]
f={"Geeks":1, "for":2, "geeks":3}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))"""
"""rvd2.py day 2 of practicing formatting
there are 3 ways of doing formatting in python
1. using % operator
2. using format() method
3. using f- strings
"""
"""print("Using % operator")
print("hello %s welcome!" % "Aditi")
print("hello %s welcome!" % input("Enter your name: "))
print("hello %s, you are %d years old and your height is %.2f meters." % (input("Enter your name: "), int(input("Enter your age: ")), float(input("Enter your height in meters: "))))"""

w = 71
name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
print("Hello %s, your age is %d, your score is %d" %(name, age, w))
print("%7.3o"%(25)) #print octal value
print("%10.3E"%(385.0999)) #print exponential

#using format() output introduced in Python2.6

print("I love {0} for \"{1}!\"".format("Geeks", "Geeks"))
print("I love {0} for reason {1}".format("Python","simplicity"))

hello = Supriya
#using f- strings (formatted string literals) introduced in Python3.6
print(f"{hello} is a good girl")
