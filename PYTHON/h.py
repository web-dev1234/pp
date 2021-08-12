#print("Enter your first number")
#inpnum=input()
#print("Enter your second number")
#inpnum2 = input()
#print("Sum of these two numbers is", int(inpnum) + int(inpnum2))



#grocery=("Apple, Banana, Cat")
#print(grocery)


#print("Welcome to my dictionary")
#Dictionary = {"Mutable":"can change","Immutable":"can not change","Harshit":"me"}
#print("The required word is:")
#Word=input()
#Word=Word.capitalize()
#print("The required meaning is:")
#if Word in Dictionary:
 #   print(Dictionary[Word])
#else:
 #   print("Word not found")

#print("Enter your age:")
#Age=int(input())
#if Age>100:
#    print("Should be in between 10 to 100")
#elif Age<10:
#    print("Should be in between 10 to 100")
#elif Age>18:
#    print("Eligible to drive")
#elif Age<18:
#    print("Not eligible to drive")
#else:
#    print("Cannot decide give a test")


"""wrong={"45*3":555, "56+9":77, "55/6":4}
print("Enter your first number")
n1=int(input())
print("Enter your operation")
opr=input("Choose from +,-,*,/\n")
print("Enter your second number")
n2=int(input())
final=str(n1)+opr+str(n2)
if final in wrong:
    print("Your answer is")
    print(wrong[final])
else:
    print("Your answer is")
    print(eval(final))
"""    

#list=(int,float,"Harshit",5,10,20,30,40,50,60)
#for item in list:
#    if str(item).isnumeric() and item>6:
#        print(item)

#while(True):
#    inp=int(input("Enter a number:\n"))
#    if inp>100:
#        print("Congrats you have given a number greater than 100\n")
#        break
#    else:
#        print("Try again!")
#        continue

#n=18
#Number_of_chances=1
#print("You have only 5 chance to guess the number\n")
#while(Number_of_chances<=5):
#    inp=int(input("Your number:\n"))
#    if inp>18:
#        print("Your entered number is greater than my number:\n")
#    elif inp<18:
#        print("Your entered number is lesser than my number:\n")
#    else:
#        print("Congrats you have won the game")
#        print(Number_of_chances,"no of chances he took to finish")
#       break
#    print(5-Number_of_chances,"no. of chance left")
#   Number_of_chances=Number_of_chances+1

#   if Number_of_chances>5:
#        print("Game Over!!")

"""print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print() """

client_list={1:"Harry",2:"Rohan",3:"Hammad"}
lock_list={1:"Exercise",2:"Diet"}
def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Your name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected name : ", client_list[your_name], "\n", end="")

    print("Press 1 for lock")
    print("Press 2 for Reterive")
    op = int(input())

    if op is 1:
        for key, value in lok_list.items():
            print("Press", key, "for" , value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[" + str(getdate()))


