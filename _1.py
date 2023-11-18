###########   Task 1 #################

print("Task 1")

for i in range(1, 11):
    print(i)

###########  Task 2 ###############

print("\n *** Task 2 *** \n")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')

    print()

###########  Task 3 ###############

print("\n *** Task 3 *** \n")


#
# x = int(input("Enter number "))
# fac = 1
#
#
# for i in range (1 , x+1):
#     fac = fac * i
#
# print(fac)

def factorial(x):
    if (x == 0 or x == 1):
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))

###########  Task 4 ###############
#Create a function with variable length of arguments
print("\n *** Task 4 *** \n")

def add_variable_len(*num):
    add = 0
    for i in num:
        print(i)

    return add

result = add_variable_len(1,2,3,4,5,6,7,8,9)
print(result)


#Return multiple values from a function
print("\n *** Task 5 *** \n")

def multiple_values():
    x = 5
    z = 9
    return x+z, x-z, x*z, x/z

add, sub, mul, div = multiple_values()
print(f"""
Add is {add}
sub is {sub}
mul is {mul}
div is {div}""")


#Create a function with default argument
print("\n *** Task 6 *** \n")

def default_arg(name, age=22):
    return name, age

print(default_arg("Hussain",23))



#Find the largest item from a given list
print("\n *** Task 7 *** \n")

lists = [10,20,30,40,50]
print(max(lists))


#Write a program to count the total number of digits in a number
print("\n *** Task 8 *** \n")

x = 12.345
print(len(str(x)))


#Reverse a given integer number
print("\n *** Task 9 *** \n")

x1 = 123456789
temp = str(x1)

rev = temp[::-1]
print(rev)

for i in rev:
    print(i)


# Below are the two lists convert it into the dictionary
print("\n *** Task 10 *** \n")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]

merge = dict(zip (keys,values))
print(merge)

# in list
merge_l = list(zip(keys,values))
print(merge_l)



#Merge following two Python dictionaries into one
print("\n *** Task 11 *** \n")

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30,'Fifty':500}
dict2 = {'Thirty': 30, 'Fourty': 40,'Fifty':50}

#Sol1   union
merge1 = dict1 | dict2  # 1st dic repeating element will eleminate
print(merge1)

#sol2   star
merge2 = {**dict1,**dict2}
print(merge2)                     # 1st dic repeating element will eleminate

#sol3    copy update
dict3 = dict1.copy()
dict3.update(dict2)             # 1st dic repeating element will eleminate
print(dict3)

# 1st dic repeating element will *** not *** eleminate
dict4 = dict2.copy()
dict4.update(dict1)
print(dict4)

#short    for  dict2 superiority    // it will directly update   not copying
dict2.update(dict1)
print(dict2)

# dict1.update(dict1)
# print(dict1)


#practice is instance
print("\n \n ****** practice *******")
a = [10,20,30,40]
print(isinstance(a, dict))
print(isinstance(a,list))

#  Access the value of key ‘history’ from the below
print("\n *** Task 12 *** \n")

sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

def find_val(dictionary, my_key):
    for key , value in dictionary.items():
        if key == my_key:
            return key, value

        elif  isinstance(value, dict):   # if  value is dictionary type
            return find_val(value,my_key)

key, val = find_val(sampleDict,"history")
print(key, "=>", val)

#simple method
print(sampleDict["class"]["student"]["marks"]["history"])


#Delete set of keys from a dictionary
sampleDict2 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]


# result2 = sampleDict2.copy()
# for key,val in sampleDict2.items():
#     for j in keysToRemove:
#         if (key == j):
#             del result2[key]
# print(result2)

for key in keysToRemove:
    if key in sampleDict2:
        del sampleDict2[key]

print(sampleDict2)


sampleDict3 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keysToRemove1 = ["name", "salary"]

for key in keysToRemove1:
    if key in sampleDict3:
        sampleDict3.pop(key)

print(sampleDict3)


#Check if a value 200 exists in a dictionary
sampleDict4 = {'a': 100, 'b': 200, 'c': 300}

if 200 in sampleDict4.values():
    print("true")


#Rename key city to location in the following dictionary
sampleDict5 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city":"Newyork"
}

sampleDict5["location"] = sampleDict5.pop(key)
print(sampleDict5)



#Get the key of a minimum value from the following dictionary
sampleDict6 = {
  'Physics': 82,
  'Math': 65,
 'history':75
}

min = min(sampleDict6.values())
max = max(sampleDict6.values())
print(min)
print(max)


#Change Brad’s salary to 8500 from a given Python dictionary

sampleDict7 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict7["emp3"]["salary"] = 8500
print(sampleDict7)
