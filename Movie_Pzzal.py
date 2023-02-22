import random
movies =['troy','matrix','avenger','ocean','a team', 'the mammy','worng trun','taken','transport','fast furious','Transfermar','underworld','national treasure','deadpool','scorpion','ironman','lucy','man of steel','the equalizer','g i joe','thor']
def Create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(" ")
        else:
            temp.append("*")
    question=' '.join(str(x) for x in  temp )
    return question

def is_present(letter,movie):
    c=movie.count(letter) #count the latter in movie
    if c==0:
        return False
    else:
        return True
def unlock(question,movie,letter):
    ref=list(movie)
    qn_list=list(question)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]=='' or ref[i]=="letter":
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    question_new=''.join(str(x) for x in temp)
    return question_new
        
            
def player():
    p1_name=input("PLAYER 1 Please Enter Your Name:")
    p2_name=input("PLAYER 2 Please Enter Your Name:")
    point_p1=0
    point_p2=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            #player 1
            print(p1_name,"Its your Turn :")
            picked_movie=random.choice(movies)
            question=Create_question(picked_movie)
            print(question)
            modified_question=question
            not_said = True
            while(not_said):
                letter=input("Your Letter:")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_question = unlock(modified_question,picked_movie,letter)
                    print(modified_question)
                    d=int(input("Press 1 to gusses the movie or 2 unlock another letter")) #desion of question 
                    if(d==1):
                        ans=input("Your Answer:")
                        if(ans==picked_movie):
                            point_p1=point_p1+10
                            print("Correct")
                            not_said=False
                            print(p1_name,"Your Score",point_p1)
                        else:
                            print("Your Answer is wrong please try again")
                else:
                    print(letter,'Not found')
            c=int(input("Press 1 TO continue or 0 to quit"))
            if(c==0):
                print(p1_name,"Your Score",point_p1)
                print(p2_name,"Your Score",point_p2)
                print("Thank for Playing")
                print("Have a Nice day")
                willing = False                
        else:
            #player 2
            print(p2_name,"Its Your Turn :")
            picked_movie=random.choice(movies)
            question=Create_question(picked_movie)
            print(question)
            not_said=True
            while(not_said):
                letter=input("Your Letter: ")
                if(is_present(letter,picked_movie)):
                    modified_question=unlock(modified_question,picked_movie,letter)
                    print(modified_question)
                    d=int(input("Press 1 to gusses the movie or 2 unlock another letter"))
                    if(d==1):
                        ans = input("Your Answer :")
                        if(ans == picked_movie):
                            point_p2=point_p2+10
                            print("correct")
                            not_said = False
                            print(p2_name,"Your Score",point_p2)
                        else:
                            print("Your Answer is wrong please try again")
                    else:
                        print(letter,"Not Found")
            c=(input("Press 1 to continue of 0 to quit"))
            if(c==0):
                print(p2_name,"Your score",point_p2)
                print(p1_name,"Your Score ",point_p2)
                print("Thank for playing ")
                print("Have a Nice day ")
                willing=False
        turn=turn+1
            
player()