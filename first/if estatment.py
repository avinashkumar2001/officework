'''name=input("enter your name? ")
if len(name)<=3:
    print("too shot name")
elif len(name)>=10:
    print("your name is to long")
else:
    print("thats good");
'''


no1= int(input("enter no.1 "))
no2= int(input("enter no.1 "))
sign=input("enter sign /*-+")

if sign=='+':
    print(f"your ans is {no1+no2}")
elif sign=='/':
    print(f"your ans is {no1/no2}")
elif sign=='*':
    print(f"your ans is {no1*no2}")
elif sign=='-':
    print(f"your ans is {no1-no2}")
else:
    print("wrong input")