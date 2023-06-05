import pandas as pd
import random
from enum import Enum
from cards import Cards
from typing import List, Dict

#カード全種類を生成する関数
def cards_options() -> list:
    added_cards_options = []
    for card in Cards:
        added_cards = card.value
        added_cards_options.append(added_cards)
    return added_cards_options

added_cards_options: List[str] = cards_options()

#二人でプレーすると仮定してカードを配布する関数
def distribute_card(added_cards_options) -> tuple:
    player_one = []
    player_two = []
    while len(set(player_one)) < 5:
        player_one.append(random.choice(added_cards_options)["looks"])
    while len(set(player_two)) < 5:
        player_two.append(random.choice(added_cards_options)["looks"])
    return player_one, player_two

[player_one, player_two] = distribute_card(added_cards_options)



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
  added_cards_options = cards_options()
  for _ in range(how_many_card_change):
    location_card= int(input("何番目のカードを交換したいですか"))
    player_one[location_card - 1] = random.choice(added_cards_options)["looks"]
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
  added_cards_options = cards_options()
  for _ in range(how_many_card_change):
    location_card= int(input("何番目のカードを交換したいですか"))
    player_two[location_card - 1] = random.choice(added_cards_options)["looks"]
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
  added_cards_options = cards_options()
  [player_one,player_two] =  distribute_card(added_cards_options)
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
