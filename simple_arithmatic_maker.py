import random

processes = ["+","-","*","/"]
non_primes = []

chance = 3
points = 0
print("Hi! This is a game that makes randomly question. You can press p to pass, press q to quit out the program")
for num in range(1,101):
    non_primes.append(num)
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            non_primes.remove(num)

while chance > 0:
    num1 = random.randint(1,101)
    num2 = random.randint(1,51)
    process = random.choice(processes)

    if process == "+":
        print("\n\n{} + {} ".format(num1,num2))
        admin_input = input("Answer : ")
        if admin_input == str(num1 + num2):
            points += 5
            print("\nYour points : ",points)

        elif admin_input == "p":
            print("You passed the question.")
            pass
        elif admin_input == "point":
            print("Your points : ",points)
        elif admin_input == "q":
            print("Total Point : ",points)
            break
        else:
            print("Your answer is false.Truth was ",num1+num2)
            chance -= 1
            points -= 2
            print("Your points : {}\nYou have {} chances left".format(points,chance))
    if process == "-":
        print("\n\n{} - {} ".format(num1,num2))
        admin_input = input("Answer : ")
        if admin_input == str(num1 - num2):
            points += 5
            print("\nYour points : ",points)

        elif admin_input == "p":
            print("You passed the question.")
            pass
        elif admin_input == "point":
            print("Your points : ",points)
        elif admin_input == "q":
            print("Total Point : ",points)
            break
        else:
            print("Your answer is false.Truth was ",num1-num2)
            chance -= 1
            points -= 2
            print("Your points : {}\nYou have {} chances left".format(points,chance))
    if process == "*":
        print("\n\n{} * {} ".format(num1,num2))
        admin_input = input("Answer : ")
        if admin_input == str(num1 * num2):
            points += 5
            print("\nYour points : ",points)

        elif admin_input == "p":
            print("You passed the question.")
            pass
        elif admin_input == "point":
            print("Your points : ",points)
        elif admin_input == "q":
            print("Total Point : ",points)
            break
        else:
            print("Your answer is false.Truth was ",num1*num2)
            chance -= 1
            points -= 2
            print("Your points : {}\nYou have {} chances left".format(points,chance))
    if process == "/":
        can_divide = []
        num3 = random.choice(non_primes)
        for i in range(1,51):
            if num3 % i == 0:
                can_divide.append(i)
        num4 = random.choice(can_divide)

        print("\n\n{} / {} ".format(num3,num4))
        admin_input = input("Answer : ")
        if admin_input == str(int(num3 / num4)):
            points += 5
            print("\nYour points : ",points)

        elif admin_input == "p":
            print("You passed the question.")
            pass
        elif admin_input == "point":
            print("Your points : ",points)
        elif admin_input == "q":
            print("Total Point : ",points)
            break
        else:
            print("Your answer is false.Truth was ",num3/num4)
            chance -= 1
            points -= 2
            print("Your points : {}\nYou have {} chances left".format(points,chance))
        
        
        









