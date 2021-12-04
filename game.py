from art import logo,vs
from game_data import data
import random
from replit import clear
comp2=random.choice(data)
score=0
guess=True
while guess:
  print(logo)
  print("Your current score is {}".format(score))
  comp1=comp2
  print("Compare A: {}, a {}, from {}".format(comp1['name'],comp1['description'],comp1['country']))
  #print(comp1['follower_count'])
  print(vs)
  comp2=random.choice(data)
  while comp1==comp2:
    comp2=random.choice(data)
    print("Against B: {}, a {}, from {}".format(comp2['name'],comp2['description'],comp2['country']))

  comp2=random.choice(data)
  print("Against B: {}, a {}, from {}".format(comp2['name'],comp2['description'],comp2['country']))

  #print(comp2['follower_count'])
  user_guess=input("Who has more followers? Type 'A' or 'B': ").upper()
  ans=comp1['follower_count']>comp2['follower_count']
  #print(ans)
  if user_guess=='A' and ans==True:
    score+=1
    print("You're right")
    clear()
  elif user_guess=='A' and ans==False:
    print("Wrong")
    print("Sorry, that's wrong. Your final score is {}".format(score))
    guess=False
  elif user_guess=='B' and ans==False:
    score+=1
    print("You're right")
    clear()
  elif user_guess=='B' and ans==True:
    print("Wrong")
    print("Sorry, that's wrong. Your final score is {}".format(score))
    guess=False
  else:
    pass



