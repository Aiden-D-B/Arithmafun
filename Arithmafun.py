import random 
num1 = random.randint(1,15) 
num2 = random.randint(1,15) 
question = int(input("What is "+str(num1)+"+"+str(num2)+":")) 
print(question) 
ans = num1+num2 
if question ==ans: 
    print("Well done! That's the right answer") 
elif question !=ans: 
    print("Thats not the correct answer! Try again")
