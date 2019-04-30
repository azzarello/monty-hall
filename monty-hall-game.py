from random import choices  # allows us to randomize the game every time

# instantiates a list that indicates each of three doors
doors = ['1', '2', '3']

# picks one door at random for the prize to be behind
prize = choices(doors)

# cont variable that indicates 'continue' that controls whether the user
# should be prompted again for their door selection
cont = True
print('Which door do you choose?')

# this is accomplished by using a while loop proceeding under the
# condition that cont is True, so a correct input should make cont False
while (cont):
    choice = input()
    # if the users input isn't within doors list instantiated above
    # give an error message and try again
    if choice not in doors:
        print('Invalid Input: Please input either 1, 2, or 3 and press enter')
    else: # if it is valid, end the while loop
        cont = False
        
'''choice is now equal to the list element that corresponds to the door chosen
since the user entered a string it must be converted to an int to use as an index
1 should be subtracted from the index because arrays start at 0'''
choice = doors.pop(int(choice) - 1) 
while(cont == False):
    monty_choice = choices(doors)
    monty_choice = doors.pop(int(monty_choice[0]) - 1)
    if (monty_choice != prize):
        cont = True
str = 'There is no prize behind door {} would you like to switch choices?'
print(str.format(monty_choice[0]))
while(cont):
    response = input('[y/n]')
    if response == 'y' or response == 'n':
        cont = False
    else:
        print('Invalid Input: Please input either y or n and press enter')

if response == 'y':
    choice = doors

if choice == prize:
    print('Congrats you won!')
else:
    print('You did not win, try again')



