import random
print("Hello you can do new year raffle in this program. If you want to quit just press q and enter 2 times")
# first of all we importes random because we will take names by randomly.
while True:
    #we oppend a while loop so that the program not stop
    gifts = (input("How many : "))
    names_of_peoples = input("Give me names please : ")
    if gifts == "q":
        print("GoodBye!!")
        break
    #we taked 2 inputs that we need 
    buyer = names_of_peoples.split()
    seller = names_of_peoples.split()
    #we created 2 list with split funtion. What is Split function ?? https://www.w3schools.com/python/ref_string_split.asp
    n = 1   
    while True:
        #program will work until its return false
        if int(gifts) <= 1:
            print("You need to give me more names")
            break
        elif int(gifts) == 2:
            print("\n",buyer[0],"to",buyer[1],"\n",buyer[1],"to",buyer[0])
            break
        # I did this because you cant make a raffle in 2 person. There is only 2 options person 1 to 2 or person 2 to 1 :)
        for i in range(1,int(gifts) + 1):
            print("{}-)".format(n))
            n += 1
            first_person = random.choice(buyer)
            #we are taking a random name from buyers list
            for i in seller:
                if i == first_person:
                    seller.remove(i)
            #we removed the name (which we choosed from buyers) from sellers because if we dont the buyer and the seller can be the same person
            second_person = random.choice(seller)
            #we are taking a random name from sellers list
            seller.append(first_person)
            #and we append the first person to sellers because we removed it . if we dont append it again that person cant buy a gift to someone

            if first_person != second_person:
                print(first_person,"to",second_person)
                buyer.remove(first_person)
                seller.remove(second_person)
                #in this code block we are checking that first person and second persons are different. and if they are different we print it 
                #to terminal and we remove them from the list because we need them only one time
                    
            
            #and if there is something else we are breaking the loop

        break
    

