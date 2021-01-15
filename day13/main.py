def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def win_game():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#for step in range(0,6):
 #   win_game()
number_of_hurdels = 6
while number_of_hurdels > 0 :
    number_of_hurdels -= 1
    win_game()
#number_of_hurdels = 6
#while number_of_hurdels > 0 :
 #   number_of_hurdels -= 1
  #  win_game()
#while at_goal() != True:
while not at_goal():
    win_game()

while not at_goal():
    if wall_in_front():
        win_game()
    else:
        move()
        