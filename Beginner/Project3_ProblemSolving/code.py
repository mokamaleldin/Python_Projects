#Problem solving




str="print only the words that start with s in this sentence"

for letter in str.split():
    if(letter[0] == "s"):
        print(letter)


#use range() to print all the even numbers form 0 to 10

for num in range(10):
    if num % 2 ==1:
        print(num)

#use a list comperhension to create a list of all numbers between 1 adn 50 that are divisivle by 3
mylist=[num for num in range(50) if num %3 == 0]

print(mylist)
