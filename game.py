# importing modules in python file
import game_modules as mod

#Initialize Variable
Attampt = 0
name = ""
fight_number = ""
num = 0
life_score = 0

#Asking User Name
name = input("Player name : ")

#calling for lifescore function
life_score = mod.lifescore()


#run the game 20 times using for loop
for i in range(20): 
    Attampt +=1
    print(f'Attampt {Attampt}')
    #Calling For enemy function
    enemy_numbers = mod.enemy(Attampt)
    print(f'{name}\'s Life Score : {life_score}')
    
    #print the 5 enemy numbers in one line
    for values in enemy_numbers:
        print(values,end=" ")
    print()

    # get user input number for fight with enemy numbers 
    fight_number = input("Select a number to fight : ")
    
    #Check The User Input Is Number Or Not
    try:
        num = int(fight_number)

        #check if the user input fight number is in enemy numbers list or not 
        if num in enemy_numbers:

            #then check the fight number is less than or equal for life score
            if num <= life_score:
                print(f'{name} Killed {num}')
                print()
                # fight number is adding to the user's life score
                life_score +=num
                
            # if fight number is not less than or equal for life score then game will stop (break)    
            else:
                print(f'{num} killed {name}')
                print()
                print("Game status".center(17,"*"))
                print(f'Player name : {name}')
                print(f'Total attempts : {Attampt}')
                print(f'Final life score :{life_score}')
                message =(f'{name} was defeated')
                print(message)
                break

        # if the user input fight number not in enemy numbers game is stopped (break)
        else:
            print("No such enemy")
            print()
            print("Game status".center(17,"*"))
            print(f'Player name: {name}')
            print(f'Total attempts: {Attampt}')
            print(f'Final score: {life_score}')
            message = (f'{name} was defeated!!!')
            print(message)
            break
            
    # if user will insert other character than number Game is stop (break)
    except ValueError:
        print("Invalid input!")
        print("Game status".center(17,"*"))
        print(f'Player name: {name}')
        print(f'Final score: {life_score}')
        print(f'Total attempts: {Attampt}')
        message =(f'{name} was defeated!!!')
        print(message) 
        break
        
else:
    #when user complete 20 attempts successfully this statements are display
    print("Game status".center(17,"*"))
    print(f'Player name: {name}')
    print(f'Total attempts: {Attampt}')
    print(f'Final score: {life_score}')
    message =(f'{name} saved letter-kind!')
    print(message)
    
# open file and Write The Game Status
f0 = open(mod.filename(),"w")
f0.write("***Game status***\n")
f0.write(f'Player name : {name}\n')
f0.write(f'Final score: {life_score}\n')
f0.write(f'Total attempts: {Attampt}\n')
f0.write(f'{message}')
f0.close()
    

            
                    
                






