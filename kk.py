import time
global x
global y
 
## X is always going to be the name of player one and Y is always going to be the name for player 2
 
print("Welcome to Rock-Paper-Scissors thebeastglasser Style!")
time.sleep(2)
 
print( " ")
 
print("Please when answering, make sure that your answer is spelled correctly and is in all lowercase letters. Your options consist of \"rock\" \"paper\" and \"scissors\" without the quotation marks of course. ;)")
 
time.sleep(6)
 
print("Ok, now for the fun part, naming.")
 
time.sleep(2)
 
print( " ")
 
x = raw_input("Player 1, please enter the name you're going to use: ")
 
time.sleep(1)
 
print( " ")
 
print( "Name has been entered!")
 
time.sleep(2)
 
print( " ")
 
print( " ")
 
y = raw_input("Ok player 2, please enter your name as well: ")
 
time.sleep(1)
 
print( " ")
 
print( "Name has been entered!")
 
time.sleep(2)
 
print(" ")
 
print("Alright, so today in the arena, it's going to be", x, "versus", y + "!")
 
time.sleep(3)
 
print(" ")
 
print("Please wait a moment while the game renders.")
 
print("Loading resources...")
 
print("")
 
time.sleep(3)
 
#below is the class that actually plays the game
 
def ROCKPAPERSCISSORS():
 
  #move is entered here
 
  winx = 0
 
  winy = 0
 
  print( x)
 
  player1 = raw_input(" please enter your move: ")
 
  print( "rockpaperscissors" * 900)
 
  time.sleep(1)
 
  print("")
 
  print(y)
 
  player2 = raw_input( "please enter your move: ")
 
  print( " ")
 
  #decides who wins the game
 
  if player1 == "rock" and player2 == "paper" :
    print( "Paper beats rock,", y, "wins!")
    winy + 1
 
  #under each, there is a + 1 for the variable it should be added to
   
  elif player2 == "rock" and player1 == "paper":
    print( "Paper beats rock,", x, "wins!")
    winx + 1
   
  elif player1 == "rock" and player2 == "scissors":
    print( "Rock beats scissors,", x, "wins!")
    winx + 1
   
  elif player2 == "rock" and player1 == "scissors":
    print( "Rock beats scissors,", y, "wins!")
    winy + 1
 
  elif player1 == "rock" and player2 == "rock":
    print( "It's a tie, that's boring. Play again to see if you can win!")
 
  elif player1 == "rock" and player2 == "spock":
    print( "Spock vaporizes rock,", y, "wins!")
    winy + 1
 
  elif player2 == "rock" and player1 == "spock":
    print( "Spock vaporizes rock,", x, "wins!")
    winx + 1
 
  elif player1 == "rock" and player2 == "lizard":
    print( "Rock crushes lizard,", x, "wins!")
    winx + 1
 
  elif player2 == "rock" and player1 ==  "lizard":
    print( "Rock crushes lizard,", y, "wins!")
    winy + 1
 
  elif player1 == "scissors" and player2 == "paper":
    print( "Scissors beats paper,", x, "wins!")
    winx + 1
 
  elif player1 == "paper" and player2 == "scissors":
    print( "Scissors beats paper,", y, "wins!")
    winy + 1
 
  elif player1 == "scissors" and player2 == "spock":
    print( "Spock smashes scissors,", y, "wins!")
    winy + 1
 
  elif player1 == "spock" and player2 == "scissors":
    print( "Spock smashes scissors,", x, "wins!")
    winx + 1
 
  elif player1 == "scissors" and player2 == "lizard":
    print( "Scissors decapitates lizard,", x, "wins!")
    winx + 1
 
  elif player1 == "lizard" and player2 == "scissors":
    print( "Scissors decapitates lizard,", y, "wins!")
    winy + 1
 
  elif player1 == "scissors" and player2 == "scissors":
    print( "It's a tie, that's boring. Play again to see if you can win!")
 
  elif player1 == "paper" and player2 == "paper":
    print( "It's a tie, that's boring. Play again to see if you can win!")
 
  elif player1 == "paper" and player2 == "spock":
    print( "Paper disproves Spock,", x, "wins!")
    winx + 1
 
  elif player1 == "spock" and player2 == "paper":
    print( "Paper disproves Spock,", y, "wins!")
    winy + 1
 
  elif player1 == "spock" and player2 == "lizard":
    print( "Lizard poisons Spock,", y, "wins!")
    winy + 1
 
  elif player1 == "lizard" and player2 == "spock":
    print( "Lizard poisons Spock,", x, "wins!")
    winx + 1
 
  elif player1 == "spock" and player2 == "spock":
    print( "Spock has met his evil clone! The world ends!")
 
  elif player1 == "lizard" and player2 == "lizard":
    print( "The lizards bite off each other's tails, but it's ok, because lizard tails always grow back.")
 
  elif player1 == "lizard" and player2 == "paper":
    print( "Lizard eats paper,", x, "wins!")
    winx + 1
 
  elif player1 == "paper" and player2 == "lizard":
    print( "Lizard eats paper,", y, "wins!")
    winy + 1
 
  else:
    print("One of you screwed up, nice job. Play again and see if you can type \"rock\" \"paper\" or \"scissors\" correctly next time.")
 
  time.sleep(2)
 
  #below is where it should add up how many times a player has won
 
  print( x, "has won", winx, "times!")
 
  time.sleep(2)
 
  print( y, "has won", winy, "times!")
 
  time.sleep(2)
 
  #here it decides who is in the lead
 
  if winx > winy:
    print( x, "is in the lead!")
 
  elif winy > winx:
    print( y, "is in the lead!")
 
  else:
    print( "It's a tie game!")
 
  time.sleep(1)
 
  print( "Want to play again?")
 
  time.sleep(1)
 
  replay = raw_input("Press <ENTER> to quit, or type \"again\" to play another round: ")
 
  while replay == "again" :
    ROCKPAPERSCISSORS()
 
  else:
    quit()
ROCKPAPERSCISSORS()
