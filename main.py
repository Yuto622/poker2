import pandas as pd
import random
from enum import Enum
#全種類のカードを生成するクラス


class Cards(Enum):
  SPADE_2 = {"suit": "spade", "number": "2", "looks": "♠2"}
  SPADE_3 = {"suit": "spade", "number": "3", "looks": "♠3"}
  SPADE_4 = {"suit": "spade", "number": "4", "looks": "♠4"}
  SPADE_5 = {"suit": "spade", "number": "5", "looks": "♠5"}
  SPADE_6 = {"suit": "spade", "number": "6", "looks": "♠6"}
  SPADE_7 = {"suit": "spade", "number": "7", "looks": "♠7"}
  SPADE_8 = {"suit": "spade", "number": "8", "looks": "♠8"}
  SPADE_9 = {"suit": "spade", "number": "9", "looks": "♠9"}
  SPADE_10 = {"suit": "spade", "number": "10", "looks": "♠10"}
  SPADE_J = {"suit": "spade", "number": "J", "looks": "♠J"}
  SPADE_Q = {"suit": "spade", "number": "Q", "looks": "♠Q"}
  SPADE_K = {"suit": "spade", "number": "K", "looks": "♠K"}
  SPADE_A = {"suit": "spade", "number": "A", "looks": "♠A"}

  HEART_2 = {"suit": "heart", "number": "2", "looks": "♥2"}
  HEART_3 = {"suit": "heart", "number": "3", "looks": "♥3"}
  HEART_4 = {"suit": "heart", "number": "4", "looks": "♥4"}
  HEART_5 = {"suit": "heart", "number": "5", "looks": "♥5"}
  HEART_6 = {"suit": "heart", "number": "6", "looks": "♥6"}
  HEART_7 = {"suit": "heart", "number": "7", "looks": "♥7"}
  HEART_8 = {"suit": "heart", "number": "8", "looks": "♥8"}
  HEART_9 = {"suit": "heart", "number": "9", "looks": "♥9"}
  HEART_10 = {"suit": "heart", "number": "10", "looks": "♥10"}
  HEART_J = {"suit": "heart", "number": "J", "looks": "♥J"}
  HEART_Q = {"suit": "heart", "number": "Q", "looks": "♥Q"}
  HEART_K = {"suit": "heart", "number": "K", "looks": "♥K"}
  HEART_A = {"suit": "heart", "number": "A", "looks": "♥A"}

  DIAMOND_2 = {"suit": "diamond", "number": "2", "looks": "♦2"}
  DIAMOND_3 = {"suit": "diamond", "number": "3", "looks": "♦3"}
  DIAMOND_4 = {"suit": "diamond", "number": "4", "looks": "♦4"}
  DIAMOND_5 = {"suit": "diamond", "number": "5", "looks": "♦5"}
  DIAMOND_6 = {"suit": "diamond", "number": "6", "looks": "♦6"}
  DIAMOND_7 = {"suit": "diamond", "number": "7", "looks": "♦7"}
  DIAMOND_8 = {"suit": "diamond", "number": "8", "looks": "♦8"}
  DIAMOND_9 = {"suit": "diamond", "number": "9", "looks": "♦9"}
  DIAMOND_10 = {"suit": "diamond", "number": "10", "looks": "♦10"}
  DIAMOND_J = {"suit": "diamond", "number": "J", "looks": "♦J"}
  DIAMOND_Q = {"suit": "diamond", "number": "Q", "looks": "♦Q"}
  DIAMOND_K = {"suit": "diamond", "number": "K", "looks": "♦K"}
  DIAMOND_A = {"suit": "diamond", "number": "A", "looks": "♦A"}

  CLUB_2 = {"suit": "club", "number": "2", "looks": "♣2"}
  CLUB_3 = {"suit": "club", "number": "3", "looks": "♣3"}
  CLUB_4 = {"suit": "club", "number": "4", "looks": "♣4"}
  CLUB_5 = {"suit": "club", "number": "5", "looks": "♣5"}
  CLUB_6 = {"suit": "club", "number": "6", "looks": "♣6"}
  CLUB_7 = {"suit": "club", "number": "7", "looks": "♣7"}
  CLUB_8 = {"suit": "club", "number": "8", "looks": "♣8"}
  CLUB_9 = {"suit": "club", "number": "9", "looks": "♣9"}
  CLUB_10 = {"suit": "club", "number": "10", "looks": "♣10"}
  CLUB_J = {"suit": "club", "number": "J", "looks": "♣J"}
  CLUB_Q = {"suit": "club", "number": "Q", "looks": "♣Q"}
  CLUB_K = {"suit": "club", "number": "K", "looks": "♣K"}
  CLUB_A = {"suit": "club", "number": "A", "looks": "♣A"}

#二人でプレーすると仮定してカードを配布する関数
def distibute_card() -> tuple:
  for card in Cards:
    print(card.value)



"""
def distibute_card() -> tuple:
  cards = make_cards()
  player_one = []
  player_two = []
  for _ in range(5):
    player_one.append(random.choice(cards))
  
  for _ in range(5):
    player_two.append(random.choice(cards))
  return player_one,player_two

[player_one,player_two] = distibute_card()
"""


#プレイヤー１が何個のペアを持っているか判定する関数
def judge_how_many_pair(player_one) -> tuple:
  player_one_numbers = []
  n = 0
  for _ in range(5):
    player_one_numbers.append(player_one[n][1:])
    n += 1

  how_many_pairs = []
  for player_one_number in player_one_numbers:
    how_many_pairs .append(player_one_numbers.count(player_one_number))

  number_pair = max(how_many_pairs)

  return number_pair,player_one_numbers

[number_pair, player_one_numbers] = judge_how_many_pair(player_one)
#print(f"このプレイヤーは{number_pair}ペアです")

#プレイヤー1の数字が連続しているか調べる関数
def judge_sequence(player_one_numbers)  -> bool:
  for i in range(4):
    if player_one_numbers[i] +1 !=  player_one_numbers[i+1]:
      print("ストレートではありません")
      return False
    
    else:
      return True
    
#プレイヤー１の数字を提供する関数
def provide_all_numbers(player_one):
  player_one_numbers = []
  n = 0
  for _ in range(5):

    try:
      player_one_numbers.append(int(player_one[n][1:]))
      n += 1

    except ValueError as error:
      if player_one[n][1:] == "J":
        player_one_numbers.append(11)

      elif player_one[n][1:] == "Q":
        player_one_numbers.append(12)

      elif player_one[n][1:] == "K":
        player_one_numbers.append(13)

      elif player_one[n][1:] == "A":
        player_one_numbers.append(1)
      n += 1

  player_one_numbers.sort()
  return player_one_numbers


#プレイヤー１がストレートか判断する関数
def judge_stright(player_one) -> bool:
  player_one_numbers = []
  n = 0
  for _ in range(5):

    try:
      player_one_numbers.append(int(player_one[n][1:]))
      n += 1

    except ValueError as error:
      if player_one[n][1:] == "J":
        player_one_numbers.append(11)

      elif player_one[n][1:] == "Q":
        player_one_numbers.append(12)

      elif player_one[n][1:] == "K":
        player_one_numbers.append(13)

      elif player_one[n][1:] == "A":
        player_one_numbers.append(1)
      n += 1

  player_one_numbers.sort()


  for i in range(4):
    if player_one_numbers[i] +1 !=  player_one_numbers[i+1]:
      print("ストレートではありません")
      return False
    
    else:
      return True
    
#プレイヤー１がフラシュか判断する関数
def judge_flush(player_one) -> bool:
  player_one_suit = []
  
  for n in range(5):
    player_one_suit.append(player_one[n][0])
  
  print(player_one_suit)

  for i in range(4):
    if player_one[i][0] != player_one[i + 1][0]:
      print("フラッシュではない")
      return False
    else:
      return True
    
#プレイヤー１フルハウスか判断する関数
def judge_fullhouse(player_one) -> bool:

  player_one_numbers = []
  n = 0
  for _ in range(5):
    player_one_numbers.append(player_one[n][1:])
    n += 1

  print(player_one_numbers)

  how_many_pairs = []
  for player_one_number in player_one_numbers:
    how_many_pairs .append(player_one_numbers.count(player_one_number))
  
  print(how_many_pairs)

  if (3 in how_many_pairs) and (2 in how_many_pairs):
    print("フルハウスです")
    return True
  else:
    return False

#プレーヤー1がフォーカードか判断する関数
def judge_four_cards(player_one) -> bool:
  player_one_numbers = []
  n = 0
  for _ in range(5):
    player_one_numbers.append(player_one[n][1:])
    n += 1

  print(player_one_numbers)

  how_many_pairs = []
  for player_one_number in player_one_numbers:
    how_many_pairs .append(player_one_numbers.count(player_one_number))
  
  print(how_many_pairs)
  number_pair = max(how_many_pairs)
  if number_pair == 4:
    print("フォーカードです")
    return True
  else:
    return False
  
#プレイヤー1がストレートフラッシュか判断する関数
def judge_stright_flush(player_one) -> bool:
  first_step = judge_sequence(player_one_numbers)
  second_step = judge_fullhouse(player_one)
  if first_step and second_step:
    print("これはストレートフラッシュです")
    return True
  
  else:
    return False
  
#プレイヤー１がロイヤルストレートフラッシュか判断する関数
def judge_loyal_stright_flush(player_one):
  first_judge = judge_fullhouse(player_one)
  player_one_numbers = provide_all_numbers(player_one)
  if ([1, 10, 11, 12, 13] == player_one_numbers) and first_judge:
    print("ロイヤルストレートフラッシュです")
    return True

  else:
    return False
#カードを交換する関数
def change_cards_one(player_one):
  how_many_card_change = int(input("何枚のカードを交換したいですか"))
  cards = make_cards()
  for _ in range(how_many_card_change):
    location_card= int(input("何番目のカードを交換したいですか"))
    player_one[location_card - 1] = random.choice(cards)
  return print(player_one)

#宣言する関数
def confident():
  check_confident = input("もういけますか?!")
  if check_confident == "はい":
    return True
  else:
    return False

#カードを交換する関数
def change_cards_two(player_two):
  how_many_card_change = int(input("何枚のカードを交換したいですか"))
  cards = make_cards()
  for _ in range(how_many_card_change):
    location_card= int(input("何番目のカードを交換したいですか"))
    player_two[location_card - 1] = random.choice(cards)
  return print(player_two)

#どっちが勝ったか判定する関数
def which_win(situation_one, situation_two) -> str:
  if situation_one[0] > situation_two[0]:
    return print("プレイヤー１の勝ちです")
  elif situation_one[0] < situation_two[0]:
    return print("プレイヤー2の勝ちです")
  elif situation_one[0] == situation_two[0]:
    return print("引き分けです")
  


def main():
  cards = make_cards() 
  [player_one,player_two] = distibute_card()
  print(player_one,player_two)



  while True:
    print(player_one)
    change_cards_one(player_one)
    confident_one = confident()
    print(player_two)
    change_cards_two(player_two)
    confident_two = confident()

   

    if confident_one:
      [number_pair, player_one_numbers] = judge_how_many_pair(player_one)
      situation_one = []
      if 1 <= number_pair <=3:
        situation_one.append(number_pair)

      elif judge_stright(player_one):
        situation_one.append(4)
      elif judge_flush(player_one):
        situation_one.append(5)
      elif judge_fullhouse(player_one):
        situation_one.append(6)
      elif judge_four_cards(player_one):
        situation_one.append(7)
      elif judge_stright_flush(player_one):
        situation_one.append(8)
      elif judge_loyal_stright_flush(player_one):
        situation_one.append(9)

      print(situation_one)

      [number_pair, player_two_numbers] = judge_how_many_pair(player_two)
      situation_two = []
      if 1 <= number_pair <=3:
        situation_two.append(number_pair)

      elif judge_stright(player_two):
        situation_two.append(4)
      elif judge_flush(player_two):
        situation_two.append(5)
      elif judge_fullhouse(player_two):
        situation_two.append(6)
      elif judge_four_cards(player_two):
        situation_two.append(7)
      elif judge_stright_flush(player_two):
        situation_two.append(8)
      elif judge_loyal_stright_flush(player_two):
        situation_two.append(9)

      print(situation_two)
      which_win(situation_one, situation_two)


      
      
      


      break
    if confident_two:
      print(player_one)
      change_cards_one(player_one)

      [number_pair, player_one_numbers] = judge_how_many_pair(player_one)
      situation_one = []
      if 1 <= number_pair <=3:
        situation_one.append(number_pair)

      elif judge_stright(player_one):
        situation_one.append(4)
      elif judge_flush(player_one):
        situation_one.append(5)
      elif judge_fullhouse(player_one):
        situation_one.append(6)
      elif judge_four_cards(player_one):
        situation_one.append(7)
      elif judge_stright_flush(player_one):
        situation_one.append(8)
      elif judge_loyal_stright_flush(player_one):
        situation_one.append(9)

      print(situation_one)

      [number_pair, player_two_numbers] = judge_how_many_pair(player_two)
      situation_two = []
      if 1 <= number_pair <=3:
        situation_two.append(number_pair)

      elif judge_stright(player_two):
        situation_two.append(4)
      elif judge_flush(player_two):
        situation_two.append(5)
      elif judge_fullhouse(player_two):
        situation_two.append(6)
      elif judge_four_cards(player_two):
        situation_two.append(7)
      elif judge_stright_flush(player_two):
        situation_two.append(8)
      elif judge_loyal_stright_flush(player_two):
        situation_two.append(9)

      print(situation_two)
      which_win(situation_one, situation_two)


      break

  

if __name__ == "__main__":
  main()
