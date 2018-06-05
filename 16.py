'''Exercise 16 (and Solution)

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

tips for a strong password 

http://mentalfloss.com/article/504786/8-tips-make-your-passwords-strong-possible

1. make your password long and complex
2. make a nonsense phrase. 
3. include numbers, symbols and uppercase lowercase
4. avoid using obvious personal information
5. do not reuse passwords 
6. start using a password manager 
7. keep your password inder wraps 
8. change your passwords regularly 



'''



import random 

# can i link to a file in this? 

# Can i do this from the 3000 most common english words. Can i generate it from the dictionary.

listwords = ['Gene', 'Bean', 'Supreme', 'Lean', 'Fighting-machine']

# Filter list of words to only contain words >= 6 characters 

# Make them all lowercase 

listwords2 = [j.lower() for j in listwords]

# Ask the user for the strength of the number

str = input('How strong do you want your password? 1 is mild, 2 is medium and 3 is super strong')

# Generate the random words

a = random.choice(listwords2)
b = random.choice(listwords2)
c = random.choice(listwords2)

x = ''

if int(str) == 1:
    x = a 
elif int(str) == 2:
    x = a + b 
elif int(str) == 3:
    x = a + b + c 
else:
    print('You didnt enter a valid number')
    


# Change Es to 3s, Os to 0s, i = 1
# include symbols @ ^ ~

s = 0
x1 = []
for i in x:
    if i == 'a':
        x1.append('@')
    elif i == 'e':
        x1.append('3') 
    elif i == 'o':
        x1.append('0')
    elif i == 'i':
        x1.append(1)
    else:
        x1.append(i)
        
    s = s+1
	


# Randomly change letters to uppercase 
y = len(x1)
z1 = random.randint(0,y-1)
z2 = random.randint(0,y-1)

try:
    x1[z1] = x1[z1].upper()
except:
    True
	
try:
    x1[z2] = x1[z2].upper()
except:
    True

# prefix with a random number

x1.insert(0,random.randint(0,100)) 

print(x1)

