from replit import clear
from art import logo
def black_jack(): 
  import random
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_pick = []
  computer_pick = []
  def check_if_21(pick):
    for i in range(0, len(pick)):
      if pick[i] == 11 and sum(pick) > 21:
        pick[i] = 1
  def user_inital():
    user_pick.extend(random.choices(cards, k = 2))
    check_if_21(user_pick)
    user_sum = sum(user_pick)
    print(f'  Your cards are: {user_pick}, current score: {user_sum}')
  def computer_inital():
    z = random.choice(cards)
    computer_pick.append(z)
    print(f"  Computer's first hand: {z}")
  def computer_final():
    x = sum(computer_pick)
    while x < 17:
      computer_pick.append(random.choice(cards))
      check_if_21(computer_pick)
      x = sum(computer_pick)
    print(f"  Computer's final hand: {computer_pick}, final score {sum(computer_pick)}") 
  def user_score():
    hit = sum(user_pick)
    while hit < 21:
      x = input("Type 'y' for another card, type 'n' to pass: ")
      if x == 'y':
        z = random.choice(cards)
        user_pick.append(z)
        check_if_21(user_pick) 
        hit = sum(user_pick)
        
        print(f'  Your cards: {user_pick}, current score: {sum(user_pick)}')
      else:
        break
    print(f'  Your final hand: {user_pick}, final score {sum(user_pick)}')
  def check_winner():
    u = sum(user_pick)
    c = sum(computer_pick)
    if c > 21 and u > 21:
      print("draw")
    elif c > 21 and u < 21:
      print("You win, opponent went over")
    elif u > 21 and c < 21:
      print("You Lose, you went over")
    elif c == 21:
      print("You lose from a Blackjack")
    elif u == 21:
      print("You win from a BlackJack")
    elif c > u:
      print("You Lose")
    elif u > c:
      print("You Win")
    else:
      print("Draw, WHAT ARE THE ODDS")
  user_inital()
  computer_inital()
  user_score()
  computer_final()
  check_winner()
print(logo)
play = True 
while play == True:
  want_to_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
  if want_to_play.lower() == 'y':
    clear()
    print(logo)
    black_jack()
  elif want_to_play.lower() == 'n':
    clear()
    print('\nThanks for playing!')
    play = False
  else:
    print("\ninvalid input\n")