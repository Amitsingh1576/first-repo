print("welcome to my quize game!")
playing = input("do you want to pla??: ")

if playing.lower() != "yes":
    quit()

print("okay! lets play")
score = 0

answer = input("what does cpu stand for?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input("what does GPU stand for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("what does RAM stand for?: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stand for?: ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct !")