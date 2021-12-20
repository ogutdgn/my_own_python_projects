print("If you enter your identity number program will understand that is it true or false.")
# You can find TC id formation conditions : https://tr.wikipedia.org/wiki/T.C._Kimlik_Numaras%C4%B1

tc = input("Tc Identity :")

def tc_identify(tc):
    
    while True:
        
        if len(tc) == 11:
            first_variable = True
        else: 
            print("Missing Number")
            break


        first_situation = (int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])) 
        x = first_situation * 7
        second_situation = (int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7]))
        y = second_situation * 9


        sum = str(x + y)
        if sum[-1] == str(tc[9]):
            second_variable = True
        else: 
            print("This cant be a correct identification number")
            break


        sum2 = str(8 * first_situation)
        if sum2[-1] == tc[-1]:
            third_variable = True
        else: 
            print("This cant be a correct identification number")
            break


        sum3 = str(int(tc[0]) +int(tc[1]) +int(tc[2]) +int(tc[3]) +int(tc[4]) +int(tc[5]) +int(tc[6]) +int(tc[7]) +int(tc[8]) +int(tc[9])) 
        if sum3[-1] == tc[10]:
            fourth_variable = True
        else:
            print("This cant be a correct identification number")
            break


        if first_variable and second_variable and third_variable and fourth_variable == True:
            print("This might be a correct identification number")
            break
        else:
            print("This cant be a correct identification number")
            break

tc_identify(tc)