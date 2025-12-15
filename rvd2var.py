x=5
name="Smantha"
print(x)
print(name)
x="Aditi Gupta"
a = n = u =y = 99

#type casting
"""int(), float(), str(), List(), tuple(), dict(), set(), ord(), chr()"""  
n = "100"   
print(type(n))

#type() gives the data type of a variable
type_of_n = type(n)
print(type_of_n)
#python creates objects(Location) of different data types automatically when we assign values to variables
#n become reference variable pointing to string object "100"
n = int(n)  #type casting string to integer
#swapping of two variables
a, b=3,7
a, b = b,a 
print(a, b)

#counting characters in a string
word = "Python"
length = len(word)
print(f"{length} is length of your given word")

price=100
tax=10
total_price=price-tax
print(f"your total earning is {total_price}.")
hi = "hello"
x=None
print(x)
