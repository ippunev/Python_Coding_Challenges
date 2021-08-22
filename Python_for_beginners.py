"""
Simple Operations

Ever wondered how many seconds are there in a month (30 days)?
Write a program to calculate and output the answer.
"""
print(30*24*60*60)


"""
Flight Time

You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, covering a distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.
Calculate and output the total flight time in hours.

Hint
The result should be a float.
"""
print(7425/550)


"""
Strings

You need to make a program for a leaderboard.
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
...
"""
for i in range(1,10):
    print (str(i)+'.')

    
"""
Tip Calculator


When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.
Your program needs to take the bill amount as input and output the tip as a float.

Sample Input
50

Sample Output
10.0
"""
bill = int(input())
#my solution listed below
tip= 0.2*bill
print (tip)


"""
BMI Calculator

Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
"""
weight= input()
height= input()
BMI= int(weight)/float(height)**2
if BMI>30:
    print("Obesity")
elif BMI>25:
    print("Overweight")
elif BMI>18.5:
    print("Normal")
else:
    print ("Underweight")

"""
Sum of Consecutive Numbers

No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.
Let’s save some time by creating a program to do the calculation for you!
Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
"""

N = int(input())
#my solution is below
for i in range(N):
    N= N+i
print(N)


"""
Search Engine

You’re working on a search engine. Watch your back Google!
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
"""
text = input()
word = input()

def search(x,y):
    if y in x:
        return "Word found"
    else:
        return "Word not found" 

print(search(text, word))
