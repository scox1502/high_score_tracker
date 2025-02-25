# TASK: Create a high score tracker that keeps the top 5 scores.
high_score = []
max_score = 5

# Define a function that takes a list of scores and a new score
while max_score < 6:
    choice = input("would you like to add a score? [y/n] ").strip().lower()

    if choice == "y":
        score = (input(f"What score did you get?  "))
        high_score.append(score)
        max_score -= 1
        break

    elif choice == "n":
        print("ok goodbye")
        break

    else:
        print("that is not an option")
        pass



while True:
    while max_score < 5:
        choice = input("whould you like to add another score or view your score bored? [add/view] ")

        if choice == "add":
            score = (input(f"What score did you get?  "))
            high_score.append(score)
            max_score -= 1
            pass
    
        elif choice == "view":
            print(f"your score bored is: {high_score}")
            pass

    else:
        print("that is not an option")
        pass


    while max_score == 0:
        print("")



# Append the new score to the list


# Sort the list in descending order



# Keep only the top 5 scores


# Return the updated list


# Start with an empty high scores list


# Use a loop to let the user enter scores until they type -1


# Call the function with each new score and display the updated top 5 scores
