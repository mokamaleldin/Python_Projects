# task 1
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))


lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)





# task 2
def animal_crackers(text):
    wordlist=text.split()

    first=wordlist[0]
    second=wordlist[1]
    if first[0] == second[0]:
        return True
    else:
        return False

print(animal_crackers("Crazy Kangaroo"))
print(animal_crackers("Levelheaded Llama"))






# task 3
def makes_twenty(a,b):
    if a==20 or b==20:
        return True
    elif a+b==20:
        return True
    else:
        return False
    
print(makes_twenty(20,29))
print(makes_twenty(12,8))
print(makes_twenty(5,2))





#task 4
def old_macdonald(name):
    first=name[0]
    inbetween=name[1:3]
    forth=name[3]
    rest=name[4:]
    print(first.upper() + inbetween + forth.upper() +rest)

old_macdonald('macdonald')





#task 5
def master_yoda(name):
    myWord=name.split()
    myWord.reverse()
    myWord=" ".join(myWord)
    print(myWord)

master_yoda('I am home')
master_yoda('We are ready')