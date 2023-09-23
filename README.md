# bank_heist_challange
Coding Challenge
Problem 1
Part 1
It's night time, and you've successfully broken into the bank. You are standing in front of the
vault, when you realise you have left the vault password at home. Fortunately you can
remember some things about the password :
1. It is 6 digits long.
2. It is between 146810 and 612564.
3. Two adjacent digits are the same (like 22 in 122345).
4. Going from left to right, the digits never decrease. They only increase or stay the same
(like 111123 or 135679).


How many different passwords​ meet these criteria? ​Write a program to calculate this
answer.
Here are some examples that might help you:
● 222222 meets the criteria (never decreases, double 22).
● 223450 does not meet these criteria (decreasing pair of digits 50).
● 234789 does not meet these criteria (no double).



Part 2
With the siren blaring in the background, you know the police are closing in, and you need to
find this answer quickly. You look around and see your three accomplices just standing there,
idling. “What wasted resources”, you think to yourself. Wait a minute, they can be helping you
too! ​But how​? ​Update your previous program so it can be executed concurrently.




Problem 2
Part 1
After your successful heist, you find yourself in a conundrum: you are now on every wanted
poster at every police precinct. You need to go into hiding. Fortunately, with all the cash you
stole from the bank, you get to choose where to go. You managed to get a list of cities with
major successful police operations in the last 50 years, along with the year of each operation.
You want to use this list to help you determine a “safe” city to settle down. ​Write a program
that, given this list and a number N, tells you the city with the Nth most police operations.


Here is an example that might help you get started :
Considering this list :[
(‘Toronto’, 1994),
(‘Ottawa’, 2009),
(‘Ottawa’, 2002),
(‘Vancouver’, 1974),
(‘Toronto’, 2001),
(‘Schitt$ Creek’, 2021),
(‘Toronto’, 2019),
(‘Toronto’, 2018),
(‘Ottawa’, 1999),
(‘Vancouver’, 1982)
]
Your program should return ​‘Vancouver’​ when given that list and the number ​2​.
Your program should return ​‘Toronto’​ when given that list and the number ​0​.


Part 2
Now, taking into account the year of each operation, how would you determine the “safest” city
to settle? There is no coding required for this part, simply ​describe your approach and how
you designed this metric of measurement.
