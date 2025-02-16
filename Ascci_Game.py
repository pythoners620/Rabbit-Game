import random
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """
paper_ascii = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
-______(____)
    """
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

print("Welcome to the Rock, Paper, Scissors game")
confirm = input("Press enter to continue or type (Help) for the rules: ").capitalize()
if confirm == "Help":
  print("""\n\t********* RULES *********
  1) You choose and the computer chooses
  2) Rock smashes Scissors -> Rock wins
  3) Scissers cut Paper -> Scissors win
  4) Paper covers Rock -> Paper wins""")  

user_choice = input("\nEnter your choice (Rock, Paper, Scissors): ").capitalize()
if user_choice not in ["Rock", "Paper", "Scissors"]:
  print("Invalid choice. Please run the program again and choose Rock, Paper, or Scissors")

  if user_choice == "Rock":
    print(f"\nYou chose:\n{rock_ascii} ")
  elif user_choice == "Paper":
    print(f"\nYou chose:\n{paper_ascii} ")
  else:
    print(f"\nYou chose:\n{scissors_ascii} ")

computer_choice = random.choice(["Rock", "Paper", "Scissors"])

if computer_choice == "Rock":
  print(f"\nComputer chose:\n{rock_ascii} ")

elif computer_choice == "Paper":
  print(f"\nComputer chose:\n{paper_ascii} ")

else:
  print(f"\nComputer chose:\n{scissors_ascii} ")

if user_choice == computer_choice:
  print("It's a tie!")

elif (
  (user_choice == "Rock" and computer_choice == "Scissors")
  or
  (user_choice == "Paper" and computer_choice == "Rock")
  or
  (user_choice == "Scissors" and computer_choice == "Paper")
):
  print(f"You win! {user_choice} beats {computer_choice} ")
