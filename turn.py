
import random
def play_human_turn(n):
    
    human= int(input("What is your move? 1, 2, or 3? "))
    while human <1 or human > 3:
        human= int(input("Please pick a nuber from this option: 1, 2, or 3? "))
    n = n - human
    if n <= 0:
        print("You win!")
        return 0
    else:
         return n

    pass

def play_computer_turn(n):
   


    if n%4== 0:
        computer = random.randint(1, 3)
        n= n- computer
    elif n%4 ==1:
        computer = 1
        n= n- computer
    elif n%4 == 2:
        computer = 2
        n= n- computer
    elif n%4 ==3:
        computer = 3
        n= n- computer
    else:
        return n

    
    if n<=0:
        print("Computer wins!")
        return 0
    else:
        return n

    
    pass
