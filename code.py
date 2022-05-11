#BYREDDY AKHILESWAR REDDDY CODE OF EMPLOYEE ATTENDENCE REPORT 
ID = int(input("enter employee id "))
name=str(input('enter name of employee'))
sal=float(input("enter salary of empolyee per day "))
intime=float(input("enter intime of employee must be ="))
outtime=float(input('enter outtime of employee must be ='))
totworking=[]
tothalfs=[]
totleaves=[]
import random

for i in range(0,31): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("january")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("january")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("january")
        print("no of leaves",len(totleaves))

for i in range(31,61): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("febraury")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("feb")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("feb")
        print("no of leaves",len(totleaves))

for i in range(61,91): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("march")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("march")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("march")
        print("no of leaves",len(totleaves))

for i in range(91,121): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("april")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("april")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("april")
        print("no of leaves",len(totleaves))

for i in range(121,151): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("may")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("may")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("may")
        print("no of leaves",len(totleaves))

for i in range(151,181): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("june")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("june")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("june")
        print("no of leaves",len(totleaves))

for i in range(181,211): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("july")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("july")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("july")
        print("no of leaves",len(totleaves))

for i in range(211,241): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("augest")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("augest")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("augest")
        print("no of leaves",len(totleaves))

for i in range(241,271): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("september")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("septemer")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("september")
        print("no of leaves",len(totleaves))

for i in range(271,301): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("october")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("octiber")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("october")
        print("no of leaves",len(totleaves))

for i in range(301,331): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("november")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("november")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("novober")
        print("no of leaves",len(totleaves))

for i in range(331,365): 
    daytime=random.randint(0,9)
    if daytime>=8:
        totworking.append(daytime)
        print("december")
        print("no of present days",len(totworking))


    if daytime==4 or daytime==5 or daytime==6 or daytime==7 :
        tothalfs.append(daytime)
        print("december")
        print("no of half leaves",len(tothalfs))

    if daytime<=4 :
        totleaves.append(daytime)
        print("decmeber")
        print("no of leaves",len(totleaves))       

totalsal= len(totworking)*sal + 2*len(tothalfs)*sal
print("total salary without cuttingsm includinng cuttings ",totalsal)
if len(totleaves) >= 20:
    totalsal=totalsal-(len(totleaves)-20)*sal
    print("totalsalary after cutting or final pay",totalsal)

else :
    totalsal=totalsal
    print("totalsalary after cutting or final pay",totalsal)
