print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ")

if playing != "yes":
      print("Maybe next time. Goodbye!")
      exit()
print("Great! Let's get started :) " )

score = 0

answer = input("What does LLM stand for? ").lower()  # Convert the input to lowercase for case-insensitive comparison
if answer == "large language model":
      print("Correct!")
      score += 1
else:      
      print("Incorrect! The correct answer is 'Large Language Model'.")      

answer = input("What does API stand for? ").lower()  # Convert the input to lowercase for case-insensitive comparison

if answer == "application programming interface":
    print("Correct!")
    score += 1 
else:
    print("Incorrect! The correct answer is 'Application Programming Interface'.")

answer = input("What does AI stand for? ").lower()  # Convert the input to lowercase for case-insensitive comparison
if answer == "artificial intelligence":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Artificial Intelligence'.")

answer = input("What does ML stand for? ").lower()  # Convert the input to lowercase for case-insensitive comparison
if answer == "machine learning":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'Machine Learning'.")

answer = input("What does NLP stand for? ").lower()  # Convert the input to lowercase for case-insensitive comparison
if answer == "natural language processing":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'Natural Language Processing'.")

print(f"You got {score} out of 5 questions correct!")
print("Your score is " + str((score / 5) * 100) + "%.")

print("Thanks for playing the Quiz Game! Goodbye!")
exit()
