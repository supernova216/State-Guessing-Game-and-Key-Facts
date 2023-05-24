#US Population Challenge - www.101computing.net/us-population/
import random

#Open text file in read mode
file = open("USStates.txt","r")

# Create a dictionary that will have state and population
pop_dict = {}

# Create a blank list that will be populated with states and a blank list for state code which will be used for the game
state_list = []
state_code_list = []

#Loop through the text file, line by line.
for line in file:
  stateFields = line.split(",")
  state=stateFields[0]
  code=stateFields[1]
  #For the last field we cast to an integer
  population=int(stateFields[2])
  # append to dictionary and lists
  pop_dict[state] = population
  state_list.append(state)
  state_code_list.append(code)

  # print(state + " (" + code + "): " + str(population))

total_population = sum(pop_dict.values())
average_population = total_population/51
max_population = max(pop_dict, key = pop_dict.get('population'))
min_population = min(pop_dict, key = pop_dict.get('population'))

total_pop = sum(pop_dict.values())
for state in pop_dict:
  print('%s: population %d, population perc %.2f' % (state, pop_dict[state], 100*pop_dict[state]/total_pop))
print('/n/n')

def states_game():
  #create blank variable to track score
  #create a list of indexes for the states that will be randomly selected
  score = 0
  nums = list(range(0,51))
  print("Each correct answer will give you a point, while each incorrect will cost a point. Get 2 points to win!")
  while score<2:
    #pick random numbers and pull the states and codes from the corresponding index
    random.shuffle(nums)
    rand1 = nums[0]
    rand2 = nums[1]
    state1 = state_list[rand1]
    state2 = state_list[rand2]
    code1 = state_code_list[rand1]
    code2 = state_code_list[rand2]
    #prompt user to select between two
    guess = input(f"Which state has a higher population: {state1}:{code1} or {state2}:{code2}? Please input the two letter state code of your answer)")
    #User will be stuck if they don't pick one of the two state codes
    while guess.lower()!= code1.lower() and guess.lower()!=code2.lower():
      guess = input(f"Please choose one of the two state codes. Which state has a higher population: {state1}:{code1} or {state2}:{code2}? Please input the two letter state code of your answer)")
    #if they get it right, score goes up, otherwise score goes down
    if pop_dict[state1]>pop_dict[state2]:
      if guess.lower() == code1.lower():
        score+=1
        print(f"Correct! Your score is {score}.")
      else:
        score-=1
        print(f"Nope! Your score is {score}.")
    else:
      if guess.lower() == code2.lower():
        score+=1
        print(f"Correct! Your score is {score}.")
      else:
        score-=1
        print(f"Nope! Your score is {score}.")

states_game()