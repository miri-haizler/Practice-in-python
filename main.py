# תרגילים קצרים ופשוטים
#---------1----------
# def withoutA (arr):
#     arr.sort()
#     while(arr[0]=='a'):
#         arr.remove(arr[0])
#     print(arr)

#---------2----------
# def age(a):
#     if a<14:
#         print("kid")
#     elif a<20:
#         print("teen")
#     else:
#         print("adult")


# תרגול קלט ופלט
#---------1----------
# def ageInMoth(age):
#     while True:
#         if float(age):
#             print(age * 12)
#         else:
#             print("error")
#             ageInMoth(input("enter your age"))

# תרגילים קצרים ופשוטים
#---------1----------
# arr=['a','p','b','a','d']
# withoutA(arr)

#---------2----------
# a=int(input("enter your age"))
# age(a)

#---------3----------
# x=input("enter your first name")
# y=input("enter your last name")
# z=int(input("enter your age"))
# print(f"the name is {x} {y} and the age is {z}")

#---------4----------
#a="miri haizler"
#print(a.find("r",0,10))#מציאת מיקום ראשון בטווח הנתון
#print(a.isdigit())#בדיקה האם ישנם מספרים

# תרגול קלט ופלט
#---------1----------
#ageInMoth(input("enter your age"))

#---------2----------

# liners=[]
# while True:
#     line=input("enter sentence")
#     if line=="":
#         break
#     liners.append(line)
# print()
# for i in reversed (liners):
#     print(i)

#---------3----------
def sMal(x,y):
    return x*y
solution=input("enter 2 numbers ")
x=solution.split(",")
y=solution[2]
if x.isdigit() and y.isdigit():
    if float(xMalben) % 1 == 0 and float(yMalben) % 1 == 0:
        print(sMal(int(xMalben), int(yMalben)))
    else:
        print("false")
else:
    print("false")

#---------4----------
# count=0
# while True:
#     marks=input("enter your mark")
#     if marks==-1:
#         break
#     sum+=marks
#     count+=1
# print(sum/count)

#---------5----------
input("enter number")

#---------6----------
# miri=60
# malki=60
# while miri!=0 | malki!=0:
#     malki+=miri/2
#     miri/=2
#     if miri==malki:
#         print("win!!!")
#         break
#     miri+=malki/2
#     malki/=2
#     if miri==malki:
#         print("win!!!")
#         break

#תרגול מחרוזות
#---------1----------
# a=input("enter str")
# a2=a[::-1]
# print(a==a2)

#---------2----------

# str=input("enter str")
# print(str.isspace())

#---------3----------
# str=input("enter str")
# print(str.isupper())

#---------4----------
# str=input("enter str")
# str2=input("enter str")
# print(str.__contains__(str2))

#---------5----------
# str=input("enter str")
# print(str.count('s',0,len(str)))

#---------6--------
# str=input("enter str")
# print(str.isdigit())

#---------7--------
# str=input("enter str")
# x=str[len(str)-1].upper()
#
# print(str)

#---------8--------
# str=input("enter address")
# print(str[len(str)-1])

#---------9--------
#str=input("enter email address")
#x=str.index('.',0,len(str))#מצא את הנקודה הראשונה
#print(str.index('.',x,len(str)))
#print(str.rindex('.',x,len(str)))#מצא את הנקודה השניה
# str.index('.',0,len(str))


