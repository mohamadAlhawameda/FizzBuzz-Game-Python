while True:
    #Setting num_fizz/num_puzz/num_fizPuzz to 0
    num_fizz = 0
    num_puzz = 0
    num_fizPuzz = 0
    num_elements = int(input("Please Enter num elm: "))
    #Making for loop for let user enter a number and it gives the range and the FizzBuzz/Puzz/Fizz between the range of the number entered
    for i in range(num_elements):
        print(i)
        if(i% 5 ==0 and i% 3 == 0):
            num_fizPuzz +=1
            print("FizzPuzz")
        elif(i% 5 ==0 ):
            num_puzz +=1
            print("Puzz")
        elif(i% 3 == 0):
            num_fizz +=1
            print("Fizz")
    print(f"number of fizz {num_fizz} and num of puzz {num_puzz} and fizzPuzz {num_fizPuzz} ")
    #Giving user option if they would like to play again byt typing y/n
    continute_play = input("Would u like to play again? (y/n)")
    #Checking if input is equal to n and it does then we break and if yes we start again
    if(continute_play == "n"):
        print("Thank you for playing")

        break
