import random

set = ["-","+","*","/"]
can_divide = []
non_primes = []

num1 = int
num2 = int
num3 = int

upper = int(input("Wich range do you want to try : "))
for i in range(1,upper + 1):
    non_primes.append(i)
for num in range(1,upper + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            non_primes.remove(num)

def processes(num1,num2,process):
    points = 0
    if process == "+":
        print("What is the value of {} + {}".format(num1,num2))
        admin_input = input("Enter your result : ")
        if int(admin_input) == num1 + num2:
            print("You had 5 points!")
            points += 5
        else:
            print("You lost 2 points :(")
            points -= 2
    if process == "-":
        print("What is the value of {} - {}".format(num1,num2))
        admin_input = input("Enter your result : ")
        if int(admin_input) == num1 - num2:
            print("You had 5 points!")
            points += 5
        else:
            print("You lost 2 points :(")
            points -= 2
    if process == "*":
        print("What is the value of {} * {}".format(num1,num2))
        admin_input = input("Enter your result : ")
        if int(admin_input) == num1 * num2:
            print("You had 5 points!")
            points += 5
        else:
            print("You lost 2 points :(")
            points -= 2
    if process == "/":
        if num1 % num2 == 0:
            print("What is the value of {} / {}".format(num1,num2))
            admin_input = input("Enter your result : ")
            if int(admin_input) == num1 + num2:
                print("You had 5 points!")
                points += 5
            else:
                print("You lost 2 points :(")
                points -= 2
        else:
            for i in range(1,51):
                if num1 % i == 0:
                    can_divide.append(i)
            num3 = random.choice(can_divide)
            print("What is the value of {} / {}".format(num1,num3))
            admin_input = input("Enter your result : ")
            if int(admin_input) == num1 / num3:
                print("You had 5 points!")
                points += 5
            else:
                print("You lost 2 points :(")
                points -= 2

while True:
    process = random.choice(set) 
    num1 = random.choice(non_primes)
    num2 = random.choice(non_primes)
    
    processes(num1,num2,process)
    a = input("press q to quit, prees enter to contunie\n")
    if a == "q":
        print("See you next time")
        break







