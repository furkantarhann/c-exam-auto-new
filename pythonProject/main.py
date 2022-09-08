scorepointer=[1,2,3,4,5]
question1=[]
question2=[]
question3=[]
question4=[]
question5=[]
def soru1():
    print("1-What is the function that output text to the screen")
    print("A)print()                       B)output()           ")
    print("C)printf()                      D)outputf()          \n")
    answer1 = 0
    while answer1 != 1:
        answer1 = input("Do you want to answer? (Y) or (N) ")
        if answer1 == "Y" or answer1 == "y":
            answer2 = 0
            while answer2 != 1:
                answer2 = input("Your answer: ")
                if answer2 == "C" or answer2 == "c":
                    scorepointer.append("")
                    print("Your answer is correct.")
                    question1.append("a")
                    answer2 = 1
                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                    scorepointer.pop(0)
                    print("Your answer was incorrect.Correct answer is 'C'")
                    answer2 = 1
                    question1.append("a")
                else:
                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
            answer1 = 1
        elif answer1 == "N" or answer1 == "n":
            print("You skipped the question.You can try again when you finished the exam.")
            answer1 = 1
        else:
            print("Wrong letter.Be sure that you enter the correct letter and try again!")
def soru2():
    print("\n2-What is the function that gets information from the user?")
    print("A)scanf()                       B)input()         ")
    print("C)scan()                        D)inputf()        \n")
    answer1 = 0
    while answer1 != 1:
        answer1 = input("Do you want to answer? (Y) or (N) ")
        if answer1 == "Y" or answer1 == "y":
            answer2 = 0
            while answer2 != 1:
                answer2 = input("Your answer: ")
                if answer2 == "A" or answer2 == "a":
                    scorepointer.append("")
                    print("Your answer is correct.")
                    answer2 = 1
                    question2.append("a")
                elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                    scorepointer.pop(0)
                    print("Your answer was incorrect.Correct answer is 'A'")
                    answer2 = 1
                    question2.append("a")
                else:
                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
            answer1 = 1
        elif answer1 == "N" or answer1 == "n":
            print("You skipped the question.You can try again when you finished the exam.")
            answer1 = 1
        else:
            print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
def soru3():
    print("\n3-What is the most necessary function?")
    print("A)main                      B)def           ")
    print("C)void                      D)while         \n")
    answer1 = 0
    while answer1 != 1:
        answer1 = input("Do you want to answer? (Y) or (N) ")
        if answer1 == "Y" or answer1 == "y":
            answer2 = 0
            while answer2 != 1:
                answer2 = input("Your answer: ")
                if answer2 == "A" or answer2 == "a":
                    scorepointer.append("")
                    print("Your answer is correct.")
                    question3.append("a")
                    answer2 = 1
                elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                    scorepointer.pop(0)
                    print("Your answer was incorrect.Correct answer is 'A'")
                    answer2 = 1
                    question3.append("a")
                else:
                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
            answer1 = 1
        elif answer1 == "N" or answer1 == "n":
            print("You skipped the question.You can try again when you finished the exam.")
            answer1 = 1
        else:
            print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
def soru4():
    print("\n4-What is the variable that stores single characters?")
    print("A)double                   B)float           ")
    print("C)int                      D)char            \n")
    answer1 = 0
    while answer1 != 1:
        answer1 = input("Do you want to answer? (Y) or (N) ")
        if answer1 == "Y" or answer1 == "y":
            answer2 = 0
            while answer2 != 1:
                answer2 = input("Your answer: ")
                if answer2 == "D" or answer2 == "d":
                    scorepointer.append("")
                    print("Your answer is correct.")
                    answer2 = 1
                    question4.append("a")
                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "c" or answer2 == "C":
                    scorepointer.pop(0)
                    print("Your answer was incorrect.Correct answer is 'D'")
                    answer2 = 1
                    question4.append("a")
                else:
                    print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
            answer1 = 1
        elif answer1 == "N" or answer1 == "n":
            print("You skipped the question.You can try again when you finished the exam.")
            answer1 = 1
        else:
            print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
def soru5():
    print("\n5-What is the format specifier that uses for integers?")
    print("A)%s                        B)%lf            ")
    print("C)%d                        D)%f            \n")
    answer1 = 0
    while answer1 != 1:
        answer1 = input("Do you want to answer? (Y) or (N) ")
        if answer1 == "Y" or answer1 == "y":
            answer2 = 0
            while answer2 != 1:
                answer2 = input("Your answer: ")
                if answer2 == "C" or answer2 == "c":
                    scorepointer.append("")
                    print("Your answer is correct.")
                    answer2 = 1
                    question5.append("a")
                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                    scorepointer.pop(0)
                    print("Your answer was incorrect.Correct answer is 'C'")
                    answer2 = 1
                    question5.append("a")
                else:
                    print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
            answer1 = 1
        elif answer1 == "N" or answer1 == "n":
            print("You skipped the question.You can try again when you finished the exam.")
            answer1 = 1
        else:
            print("Wrong letter.Be sure that you enter the correct letter and try again!")
print("**************************************************")
print("                     C  EXAM                      ")
print("**************************************************\n\n")
soru1()
soru2()
soru3()
soru4()
soru5()
answer3 = 0
while answer3 != 1:
    answer3 = input("\nDo you want to answer the questions that you skipped?")
    if answer3 == "y" or answer3 == "Y":
        answer4 = "m"
        while answer4 != "k":
            answer4 = input("\nWhich is the question that you want to answer?")
            if answer4 == "1":
                if question1.count("a")!=1:
                    soru1()
                    answer4 = "k"
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
            if answer4 == "2":
                if question2.count("a")!=1:
                    soru2()
                    answer4 = "k"
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
            if answer4 == "3":
                if question3.count("a")!=1:
                    soru3()
                    answer4 = "k"
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
            if answer4 == "4":
                if question4.count("a")!=1:
                    soru4()
                    answer4 = "k"
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
            if answer4 == "5":
                if question5.count("a")!=1:
                    soru5()
                    answer4 = "k"
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
    elif answer3 == "N" or answer3=="n":
        answer4 = "k"
        answer3 = 1
    else:
        print("Wrong letter.Be sure that you enter the correct letter and try again!\n")
print("Your exam is done.Your total score:"+ str(len(scorepointer)-5))
