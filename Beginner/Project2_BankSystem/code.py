x=1000
password=12345
email="mkee@gamil.com"

ema=input("Enter your Email: ")
passwor=int(input("Enter your Password: "))

if ema==email and passwor==password:
    y=int(input("Enter the number you want to get: ")) 
    print(x-y)
else:
    print("you Enter a wrong password or Email")