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



        


  




