import random
def choose():
    Words = ['rainbow','computer','science','programing','python','java','information','Anlysis','Coding','Hacking','BlackBox','Testing','Puzzled','Random','General','Laptop','Thinking','Mobile','Geforce','Behavious','Gesture']
    pick= random.choice(Words)
    return pick

def Jumbled(Word):
    Jumbled ="".join(random.sample(Word,len(Word)))
    return Jumbled
def Thank(playerName1,playerName2,p1_score,p2_score):
    print(playerName1,'Your Score is',p1_score)
    print(playerName2,'Your Score is',p2_score)
    print("Thank for paticapation")
    print("Please Come To agine ")

def Play():
    playerName1 = input("Enter Name Player1 Name:")
    playerName2 = input("Enter Name Player2 Name:")
    turn=0
    p1_score=0
    p2_score=0
    while(1):
        picked_Word=choose()
        qn = Jumbled(picked_Word)
        print(qn)
    #Player 1
        if(turn%2==0):
            print(playerName1," Its Your Turn:")
            ans=input("What is own your mind:")
            if (ans == picked_Word):
                p1_score=p1_score+1
                print("Your Score is:", p1_score)
            else:
                print("Better Luck Next Time..., i Thought picked Word is",picked_Word)            
            c = input("Press 1 to Continue and 0 to Quite: ")
            if(c==0):
                Thank(playerName1,playerName2,p1_score,p2_score)
                break
    #Player
        else:
            print(playerName2,"Its  Your Turn:")
            ans=input("What is own your mind:")
            if(ans == picked_Word):
                p2_score=p2_score+1
                print("Your Score Is:",p2_score)
            else:
                print("Better Luck Next Time... i Thought picked word is ",picked_Word)
            c =input("Press 1 to Continue and 0 to Quite: ")
            if(c== 0):
                Thank(playerName1,playerName2,p1_score,p2_score)
                break
        turn=turn+1
