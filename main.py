import random

def main():
    user_points = 0
    machine_points = 0
    commands = [
        '''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        ''',

        '''
            _______
        ---'   ____)__
                ______)
                _______)
                _______)
        ---.__________)
        ''',

        '''
            _____
        ---'   __)____
                ______)
            __________)
            (_____)
        ---.__(__)
        '''
    ]
    
    while True:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

        if(user_choice >= len(commands) or user_choice == -1):
            print("The game is over! Goodbye")
            break
        else:
            machine_choice = random.randint(0, len(commands) - 1)
            print("\n\n\n\n\n")

            print("You chose: \n" + commands[user_choice] + "\n\n\n")
            print("Machine chose \n" + commands[machine_choice])

            #check if the choices are tie
            if(user_choice == machine_choice):
                print("Draw!")
            else:
                # possibilities to user wins
                if((user_choice == 0 and machine_choice == 2) or (user_choice == 1 and machine_choice == 0) or (user_choice == 2 and machine_choice == 1)):
                    print("You win!")
                    user_points+=1
                else:
                    print("\n\nMachine wins :(")
                    machine_points+=1
                
            print("                 ***** Scoreboard *****\n")
            print(f"Your points: {user_points}\n")
            print(f"Machine points: {machine_points}\n\n\n\n\n\n")


main()