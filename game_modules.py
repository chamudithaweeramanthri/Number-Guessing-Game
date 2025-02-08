import datetime
import random


#defind Function To Genarate Random Lifescore Number Between 1 & 50
def lifescore():
    life_score = random.randint(1,50)
    return life_score

#defind Finction To Genarate 5 Enemy Numbers
def enemy(x):
    #create empty list
    enemy_list = [ ]
    # run the programme 5 times using for loop and appending each 5 random numbers to the enemy_list
    for i in range (5):
        if x >= 1 and x <= 5:
            y = random.randint(15,100)
            enemy_list.append(y)
        elif x >= 6 and x <= 10:
            y=(random.randint(250,2000))
            enemy_list.append(y)
        elif x >= 11 and x <= 15:
            y=(random.randint(3000,10000))
            enemy_list.append(y)
        elif x >= 16 and x <= 20:
            y=(random.randint(20000,100000))
            enemy_list.append(y)
    return(enemy_list)
            
# Defind Function To Create The Name Of txt File
def filename():    
    Date = datetime.datetime.now().strftime("%Y_%m_%d")
    Time = datetime.datetime.now().strftime("%H_%M_%S")
    Random_number = random.randint(0000,9999)
    file_name = (f'{Date}_{Time}_{Random_number}.txt')
    return file_name
            
            



    