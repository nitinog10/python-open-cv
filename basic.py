# mobilPrice = 10000
# discount_percent = 10

# discount_amount = (mobilPrice * discount_percent) / 100

# final_price = mobilPrice - discount_amount

# print("Discount Amount is : ", discount_amount)
# print(" Final Price is : ", final_price)



# msg = "Hello All"
# print(msg[0:9:2])



###      LIST -    

# marks =[20,54.1, True, 'Hello'] 
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[-2:])



# marks = [23, 25, 89, 43, 16]
# # print(marks[::-1])
# print(sum(marks))
# print(min(marks))
# print(max(marks))
# print(sum(marks[-3:]))


# #  append => Elements add at End

# marks.append(91)
# marks.append(15)
# marks.append(40)
# marks.pop()      # pop => remove the last element
# print(marks)



# list = []
# age1 = int(input("Enter your age1: "))
# age2 = int(input("Enter your age2: "))
# age3 = int(input("Enter your age3: "))
# age4 = int(input("Enter your age4: "))

# list.append(age1)
# list.append(age2)
# list.append(age3)
# list.append(age4)

# print(sum(list))


# ages= [12, 25, [20, 25, 74] ]
# print(ages[2][1])

# ages = [ [20, 2], [14, 41, 20], [45] ]
# print(ages[2][0])


# == , != , < , > , <= , >=
## list , string - in, not in

# msg = "Hello all"
# print("all" in msg)
# print("Hello" in msg)
# print("hello" in msg)

# print("Hello" not in msg)
# print("hello" not in msg)




###########   CONDITIONAL STATEMENT   ################

# age = 19
# if age>=18:
#     print('You can vote')
# else:
#     print('You are not eligiable')    


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Your are eligibile for license")
# else:
#      print("Your are not eligibile for license") 



# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("It is a even number")
# else:
#     print("It is a odd number")    



# age = int(input("Enter age:"))
# if age < 12:
#     print("cost: 150")
# elif age > 60:
#     print("Cost: 200")
# else:
#     print("Cost: 300")     




# time = int(input("Enter time: "))
# if time > 9 and time < 18:
#     print("Store is open")
# else:
#     print("Store is Closed")    



# user = input("Enter: ")

# if user == user[::-1]:
#     print("it is a palidrom")
# else:
#     print("it is not a palidrom")


# weather = input("Enter weather: ")
# if weather == "raining":
#     print("Take an umbrella ☂️")
# elif weather == "snowing":
#     print("Wear boots 👢")
# else:
#     print("Enjoy your day 😄")        




# price = input("Enter your fruit: ")
# if price == "apple":
#     print("300")
# elif price == "banana":
#     print("100")
# elif price == 'orange':
#     print("200")
# else:
#     print("Price is unknown")         



#    loops


# for i in range(0,10,2):
#     print(i)

# list = []
# for i in range(20,0,-1):
#     if i %3 == 0:
#        list.append(i)
# print(sum(list))
# print(sum(list)/len(list))


# marks = [21, 34, 43, 91, 38, 16]
# # for i in range(0, len(marks)):
# #     print(marks[i]**2)

# # for mark in marks:
# #     print(marks)

# for mark in marks[::-1]:
#     print(mark)




# face = [[143, 91, 138, 18], [116, 202, 137, 200], [134, 115, 134, 221]]
# for faces in face:
#     x,y,z,w = faces
#     print(x+w, y+z)
   

# names = ["Himesh", "Pankaj", "Mannu", "Mayank","Prakhar","Om"]
# for name in names:
#      if len(name) %2 == 0:
#         print(name.upper())
#      else:
#         print(name.lower())        



# a = 1
# while a < 10:
#     print(a)
#     a = a + 1


# a = 1
# while True:
#     print(a)
#     a = a + 1

#     if a > 10:
#         break



# isPaymentDone = False

# while True:
#     status = input("Your payment Status : [Pending, Success, Failed] : ")

#     if status == "Success":
#         isPaymentDone == True
#         break
#     elif status == "Failed":
#         isPaymentDone == False
#         break
# print(isPaymentDone)        




import math
###  sqrt, ceil, floor, sin

print(math.sqrt(16))


