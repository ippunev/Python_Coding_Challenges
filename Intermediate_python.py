"""
Letter Counter

Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.

Sample Input
hello

Sample Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
text = input()
dict = {}
#solution listed below
for x in text:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
print (dict )

"""
Decorators

You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
***
INVOICE #42
***
END OF PAGE
"""
def decor(func):
    def wrap(arg):
        print("***")
        func(arg)
        print("***")
        print('END OF PAGE')
    return wrap
    
    
@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input())


"""
Spelling Backwards

Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
"""
def spell(txt):
    #your code goes here
    if txt == "":
        return txt
    else:
        print(txt[-1])
        return spell(txt[:-1])

txt = input()
spell(txt)


"""
Shooting Game

You are creating a shooting game!
The game has two types of enemies, aliens and monsters. You shoot the aliens using your laser, and monsters using your gun.
Each hit decreases the lives of the enemies by 1.
The given code declares a generic Enemy class, as well as the Alien and Monster classes, with their corresponding lives count.
It also defines the hit() method for the Enemy class.

You need to do the following to complete the program:
1. Inherit the Alien and Monster classes from the Enemy class.
2. Complete the while loop that continuously takes the weapon of choice from user input and call the corresponding object's hit() method.

Sample Input
laser
laser
gun
exit

Sample Output
Alien has 4 lives
Alien has 3 lives
Monster has 2 lives
"""
class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'laser':
        a.hit()
    elif x == 'gun':
        m.hit()
    elif x == 'exit':
        break
    else :
      continue    
      
      
"""
Registration System

You are making a registration form for a website.
The form has a name field, which should be more than 3 characters long.
Any name that has less than 4 characters is invalid.
Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". Output "Account Created" if the name is valid.

Sample Input
abc

Sample Output
Invalid Name
"""

try:
    name = input()
    #your code goes here
    if len(name) >= 4:
        print('Account Created')
    else:
        raise NameError    
except:
    print("Invalid Name")
    
    
"""
Title Encoder

You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions, each on a new line.
"""
file = open("/usercode/files/books.txt", "r")

#your code goes here
for line in file:
    title = line.split()
    for word in title:
        print (word[0],end='')
    print()

file.close()
