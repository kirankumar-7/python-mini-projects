#king,queen,jack-10
#ace-11

import random
def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card


def calc_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards)==21 and len(cards)==2:                        #here the sum(cards) is card "11" and "10"
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)                                           #sum in python gives the sum of all the numbers 

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose,Opponent has a Blackjack"
    elif user_score==0:
        return  "Win with a BlackJack"
    elif user_score >21:
        return "You wnet over.You lose"
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
        

user_cards=[]
computer_cards=[]
is_game_over=False

for _ in range(2):                                               #new_card=deal_card()
  user_cards.append(deal_card())                                 #user_card.append(new_card)  can be written like this also                      
  computer_cards.append(deal_card())                       

#loop for user
while not is_game_over:
    
    user_score=calc_score(user_cards)
    computer_score=calc_score(computer_cards)
    print(f"Your cards: {user_cards},current_score:{user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal =="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True
#loop for computer
while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calc_score(computer_cards)
print(f"Your final hand:{user_cards},final score:{user_score}")
print(f"Computer's final hand: {computer_cards}, final score:{computer_score}")
print(compare(user_score,computer_score))



