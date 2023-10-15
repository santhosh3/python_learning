import sys
import random
from enum import Enum

# game_count = 0

def rps(name='PlayerOne'):
     game_count = 0
     player_wins = 0
     python_wins = 0

     def play_rps():
          nonlocal name
          nonlocal player_wins
          nonlocal python_wins

          class RPS(Enum):
               ROCK = 1
               PAPER = 2
               SCISSORS = 3

     
          # print(RPS(2))
          # print(RPS.ROCK)
          # print(RPS['ROCK'])
          # print(RPS.ROCK.value)
          # sys.exit()

          print("")
          playerChoice = input(
               f"{name} please enter...\n1 for Rock,\n2 for paper,or\n3 for Seissors:\n\n")

          if playerChoice not in ["1","2","3"]:
               print(f"{name},please enter 1,2 or 3.")
               return play_rps()
          player = int(playerChoice)

          computerChoice = random.choice("123")

          computer = int(computerChoice)

          print(f"\n{name},you chose {str(RPS(player)).replace('RPS.','').title()}.\n")
          print(f"python chose {str(RPS(computer)).replace('RPS.','').title()}.\n")

          def decide_winner(player,computer):
               nonlocal name
               nonlocal player_wins
               nonlocal python_wins
               if player == 1 and computer == 3:
                    player_wins += 1
                    return f"🕎 {name}, you win!" 
               elif player == 2 and computer == 1:
                    player_wins += 1
                    return f"🕎 {name}, you win!"
               elif player == 3 and computer == 2:
                    player_wins += 1
                    return f"🕎 {name}, you win!"
               elif player == computer:
                    return "Tie game!"
               else:
                    python_wins += 1
                    return f"🐍 Python wins! \n Sorry, {name}...... 🤯"

          game_result = decide_winner(player,computer)

          print(game_result) 

          nonlocal game_count
          game_count += 1

          print(f"\nGame count: {game_count}")
          print(f"\n {name}'s Player wins: {player_wins}")
          print(f"\nPython wins: {python_wins}")
          print(f"\nPlay again, {name}?")

          while True:
               playagain = input("\nY for Yes or \nQ to Quit \n\n")
               if playagain.lower() not in ["y","q"]:
                    continue
               else:
                    break

          if playagain.lower() == "y":
               return play_rps()
          else:
               print('\n🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸\n')
               print("Thank you for playing!\n")
               sys.exit(f'bye,{name}! 👌')

     return play_rps



if __name__ == "__main__":

     import argparse

     parser = argparse.ArgumentParser(
          description="Provides a personalized game experience."
     )

     parser.add_argument(
          "-n", "--name", metavar="name",
          required=True, help="The name of person plying the game."
     )

     args = parser.parse_args()

     rock_paper_scissor = rps(args.name) 
     rock_paper_scissor() 