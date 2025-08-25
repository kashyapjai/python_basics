# my first python program
print("hello jai!")

# variables in python
name = "jai"
age = 22
cgpa = 7.2

print("my name is", name)
print("i am",age,"years old")
print("my cgpa is", cgpa)

#tiny code
name = "jai"
age= 22
hobby= "bodybuilding"
print("my name is", name, "i am ", age, "years old","and i love", hobby) 

cgpa = "7.2"
cgpay_num = float(cgpa)
result= cgpay_num + 0.3
print(result)

print("hello jai, welcome to python")

name= "jai"
age= 22
cgpa= 7.2
print("my name is ",name)
print("i am",age,"years old")
print("my cgpa is",cgpa)



age_str = "22"
age_num= 22
print("As string:",age_str)
print("As number:",age_num + 1)

cgpa_txt= 7.2
cgpa_num= float(cgpa_txt)

print("orignal (string):", cgpa_txt)
print("after conversion:", cgpa_num + 0.3)

x ="22"
y= 22
print(type(x))
print(type(y))




#student profile generator
name= input("what is your name:")
age= int(input("what is your age:"))
cgpa= float(input("what is your cgpa"))
print("hello",name," you are", age," years old and your cgpa is",cgpa)
print("your age will be", age + 5, "in 5 years")
print("your cgpa will be", cgpa + 0.5," if it improves by 0.5")