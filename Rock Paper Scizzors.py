playerone=input("player 1?")
playertwo=input("player 2?")

if (playerone == "rock" and
    playertwo == "rock"):
    print("It's a tie")

elif (playerone == "rock" and
    playertwo == "scizzors"):
    print("player 1 wins!")

elif (playerone == "rock" and
      playertwo == "paper"):
      print("Player 2 wins!")

elif (playerone == "paper" and
      playertwo == "paper"):
      print("It's a tie!")

elif (playerone == "paper" and
      playertwo == "scizzors"):
      print("Player 2 wins!")

elif (playerone == "paper" and
      playertwo == "rock"):
      print("Player 1 wins!")

elif (playerone == "scizzors" and
      playertwo == "scizzors"):
      print("It's a tie!")
  
elif (playerone == "scizzors" and
      playertwo == "rock"):
      print("Player 2 wins!")

elif (playerone == "scizzors" and
      playertwo == "paper"):
      print("Player 1 wins!")

else: print("this is not a valid object selection")
