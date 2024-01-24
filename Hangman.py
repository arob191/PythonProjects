import random
import hangman_words
import hangman_art

# Our variabled:

end_of_game = False
users_lives = 7
hang_man = -1
chosen_word = random.choice(hangman_words.word_list)
chosen_word_list = []
for char in chosen_word:
    chosen_word_list.append(char)
word_len = len(chosen_word_list)

# Next display place holder for chosen word

print(hangman_art.logo)

place_holder = []

for n in range(word_len):
    place_holder.append("_")

print(f"{' '.join(place_holder)}")

# Next ask for the user input. 

users_answers = []

while not end_of_game and users_lives > 0:
    User_answer = input("Enter a letter:").lower()
    answer_check = word_len

    for position in range(word_len):
        letter = chosen_word_list[position]
        if letter == User_answer:
            place_holder[position] = User_answer
    
    if User_answer in users_answers:
        print(f"You already guessed {User_answer}")
    
    if User_answer in chosen_word_list and User_answer not in users_answers:
        print(f"{User_answer} is in the word!")
    
    users_answers.append(User_answer)

    if User_answer not in chosen_word_list:
        users_lives -= 1
        print(hangman_art.stages[users_lives])
        print(f"{User_answer} is not in the word.")

    print(f"{' '.join(place_holder)}")

    if '_' not in place_holder:
        end_of_game = True
        print("You Win!")
        print(f"The word was {chosen_word}!")

    if users_lives == 0:
        print("You Lose")
        print(f"The word was {chosen_word}!")