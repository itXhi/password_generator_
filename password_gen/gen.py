import random 
import os

strength = input("ENTER THE STENGTH  OF THE PASSWORD : EASY(E) / MEDIUM(M)/HARD(H) : ")
password = []
easy = [1,2,3,4,5,6,7,8,9,"a","b","c"]
medium = [1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h" ,"i" ,"j" ,"k" ]
hard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 '0','1','2','3','4','5','6','7','8','9', '!', '@', '#', '$', '%', '&', '*']


# Check if save.txt exists and read last password first
if os.path.exists("save.txt"):
    with open("save.txt", "r") as f:
        last_saved = f.read()
        print(f"Your last saved password was : {last_saved}")
else:
    print("No saved password found yet.")


if strength == "E" or strength == "e" :
    for i in range(0,5):
        element = random.choice(easy)
        password.append(element)
      

elif strength == "M" or strength == "m" :
    for i in range(0,9):
        element = random.choice(medium)
        password.append(element)
    

elif strength == "H" or strength == "h" :
    for i in range(0,11):
        element = random.choice(hard)
        password.append(element)
      


# Join the password list into a string
password_str = ''.join(str(e) for e in password)

# Show the password
print("Your password is:", password_str)


with open("save.txt","w") as f:
    f.write(password_str)



