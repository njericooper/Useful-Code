# Write 10 print() statements below! 

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")


''''Lesson 2'''

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sports in sport_games:
  print(sports)

'''Lesson 3 - Range'''  

promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

'''Lesson 4 - While Loops'''

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")  


'''While Loops: Lists'''

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 


length = len(python_topics)
index = 0

while index < length:
  print("I am learning about" , python_topics[index])
  index += 1


'''Lesson 5 - Infinite Loops'''

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_A.append(student)
  print(student)

'''Lesson 6 - Loop Control: Break'''

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

  ''''Loop Control: Continue'''

  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue 
  print(age)

  ''''Nested Loops'''
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for scoops in location:
    scoops_sold+= scoops
print(scoops_sold)

'''List Comprehensions: Introduction'''

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades =[ grade + 10 for grade in grades]
print(scaled_grades)


''''List Comprehensions: Conditionals'''
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

'''''Review'''

"""""Create a list called single_digits that consists of the numbers 0-9 (inclusive)."""

# Your code below:

single_digits = range(10)
#Print each digit
for digit in single_digits:
  print(digit)

  # Your code below:

single_digits = range(10)
#Create a list cale squares

squares=[]
for digit in single_digits:
  print(digit)
#cubes
# Your code below:

single_digits = range(10)
#Create a list cale squares

squares=[]
cubes = []
for digit in single_digits:
  squares.append(digit**2)
  print(digit, squares)

for digit in single_digits:
    cubes.append(digit**3)
    print(cubes)