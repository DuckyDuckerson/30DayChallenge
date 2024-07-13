import subprocess



#----------------------------------------------


def displaymenu():
  print("Main Menu")
  print("1. Play Hangman!")
  print("2. Play RPS ")
  print("3. Play TicTacToe")


displaymenu()
user_choice = input("Enter your choice: ")

if user_choice == "1":
  subprocess.run(["python", "games/hangman.py"])
elif user_choice == "2":
  subprocess.call(["python", "games/rps.py"])
elif user_choice == "3":
  subprocess.call(["python", "games/tictactoe.py"])
else:
  print ("Please input correct number")
  


