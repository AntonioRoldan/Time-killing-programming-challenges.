# Time-killing-programming-challenges.

Solutions to random problemes I find on the internet. 

1. Google interview demonstration
   Given an array A and a number N, tell whether not there's a matching pair of numbers within A whose sum gives us N. 

2. Make chocolate
   We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
   Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done
   make_chocolate(4, 1, 9) = 4
   make_chocolate(4, 1, 10) = -1
   make_chocolate(4, 1, 7) = 2
   
3. Make bricks
   We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks
   (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
   This is a little harder than it looks and can be done WITHOUT loops. 
   make_bricks(3, 1, 8) = True
   make_bricks(3, 1, 9) = False
   make_bricks(3, 2, 10) = True
