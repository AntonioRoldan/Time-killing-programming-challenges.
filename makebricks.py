def make_bricks(small, big, goal):
 small_size = 1
 big_size = 5
 formula = (small_size * small) + (big_size * big)
 adjustment_value = formula - goal
 if not formula % goal or not goal % formula:
   return True
 else if formula > goal:
       if big_size % adjustment_value == 0 or small_size % adjustment_value == 0:
         return True
       else if adjustment_value % big_size == 0 or adjustment_value % small_size == 0:
         return True
 else:
   return False 
