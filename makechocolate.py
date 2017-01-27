def permutations(amount, size, threshold):
  "Given the amount and size, it stores all possible sums of the values in a list"
  if amount == 1:
      return size #If there's only one chocolate bar
  combinations = []
  for i in range(1, amount + 1):
    combinations.append(size * i)
  if combinations[-1] == threshold:
      return combinations[-1]
  elif combinations[-1] > threshold:
      return combinations[-1] - threshold
  else:
      return combinations

def make_chocolate(small_amount, big_amount, goal):
    "Adjusts values for small and big chocolate bars until we find out whether there is a solution"
    if big_amount == 0 and small_amount == goal:
        return goal
    elif big_amount == 0 and small_amount != goal:
        return -1
    else:
        big_size = 5
        small_size = 1
        big_sums_list = permutations(big_amount, big_size, goal)
        big_sum = big_sums_list
        if type(big_sum) == list: #If none of the sums reached our goal
            new_threshold_value = goal - big_sums_list[-1] # We adjust the new threshold value for the permutations function
            small_sums_list = permutations(small_amount, small_size, goal) #Get all possible sums with our given small values
            small_sum = small_sums_list # If the sum of our small values has indeed equaled or exceeded our goal
            if type(small_sums_list) == list:  # If the sum of our small values has not equaled nor exceeded our goal
                small_sums_list = permutations(small_amount, small_size, new_threshold_value)
                small_sum = small_sums_list
                if type(small_sums_list) == list: # If the sum of small bars has not exceeded the threshold value
                    return -1
                elif small_sum == new_threshold_value:
                    return small_sum # Whichever value we choose will be correct (either small sum or new_threshold_value)
                elif small_sum > new_threshold_value:
                    return new_threshold_value # It is the number of small bars we have left before our goal that matters
            elif small_sum == goal:
                return small_sum # If the sum has equaled our goal, it is indiferent whether we choose one or the other variable
            elif small_sum > goal: # If the sum has exceeded our goal
                return goal #Since the size is one, we can return goal as the result
        elif big_sum >= goal:
            make_chocolate(small_amount, big_amount -1, goal) # We adjust the big_amount variable by - 1, to check for different combinations      
        elif big_sum == 5:
            new_threshold_value = goal - big_sum # We adjust the new threshold value for the permutations function
            small_sums_list = permutations(small_amount, small_size, new_threshold_value) #Get all possible sums with our given small values
            small_sum = small_sums_list # If the sum of our small values has indeed equaled or exceeded our goal
            if type(small_sum) == list:  # If the sum of our small values has not equaled nor exceeded our goal
                return small_sum
            elif small_sum == new_threshold_value:
                return small_sum # If the sum has equaled our goal, it is indiferent whether we choose one or the other variable
            elif small_sum > new_threshold_value: # If the sum has exceeded our goal
                return goal #Since the size is one, we can return goal as the result

print(make_chocolate(5, 2, 15))
