import random

set = ["-","+","*","/"]
can_divide = []


num1 = int
num2 = int
num3 = int

# process = random.choice(process)
# num1 = random.randint(1,101)
# num2 = random.randint(1,51)



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
    num1 = random.randint(1,101)
    num2 = random.randint(1,51)
    
    processes(num1,num2,process)
    a = input("press q to quit, prees enter to contunie\n")
    if a == "q":
        print("See you next time")
        break








