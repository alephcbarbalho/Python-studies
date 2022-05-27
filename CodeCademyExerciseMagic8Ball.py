import random
print("Hello! I'm a Magic 8 Ball!")
name = input("What is your name? ")
question = "."
random_number = random.randint(1, 9)
answer1 = "Yes!"
answer2 = "No!"
answer3 = "Maybe..."
answer4 = "I don't know..."
answer5 = "It's impossible to know!"
answer6 = "Not even God knows!"
answer7 = "I am certain of that!"
answer8 = "For sure!"
answer9 = "42!"
if name == "":
    question = input("Okay, mysterious one... what do you want to know about? ")
else:
    question = input("What do you want to know about, " + name + "? ")

if question == "":
    print("I'm sorry, but I can't answer if you don't ask.")
else:
    print("I've thought and now I see the number " + str(random_number) + ", so:")
    if random_number == 1:
        print(answer1)
    elif random_number == 2:
        print(answer2)
    elif random_number == 3:
        print(answer3)
    elif random_number == 4:
        print(answer4)
    elif random_number == 5:
        print(answer5)
    elif random_number == 6:
        print(answer6)
    elif random_number == 7:
        print(answer7)
    elif random_number == 8:
        print(answer8)
    else:
        print(answer9)

