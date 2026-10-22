def Number_Guessing_game():
    import random 

    Magic_Number = random.randint(1,150)


    for i in range (0,10):

        User_Number = int(input("Enter The Number :"))

        

        if User_Number < Magic_Number:

            print("My number is Higher !!")

        elif User_Number > Magic_Number :

            print("My number is Lesser!!")

        elif User_Number == Magic_Number :

            print("Congradulations your answer is correct !!")
            print(f"You have guessed the number { Magic_Number } in {i} attempts")
            break

        else:

            print("Your answer is wrong!!")

Number_Guessing_game()