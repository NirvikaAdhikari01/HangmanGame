import random
selected_words=("Cat","Dog","Elephant","Whale","Shark")
hangman_={0:("   ",
             "   ",
             "   "),
          1:(" o ",
             "   ",
             "   "),
          2:(" o ",
             " | ",
             "   ",
             ),
          3:(" o ",
             "/| ",
             "   "),
          4:(" o ",
             "/|\\",
             "   "),
          5:(" o ",
             "/|\\",
             "/  "),
          6:(" o ",
             "/|\\",
             "/ \\")}
def show_hangman(incorrect_guess):
    for line in hangman_[incorrect_guess]:
        print(line)
def show_hints(answer_hints):
    print(" ".join(answer_hints))
def show_the_answers(correct_answer):
    print(" ".join(correct_answer))
def main():
    answer=random.choice(selected_words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running:
        show_hangman(wrong_guesses)
        show_hints(hint)
        guess=input("Enter a letter ")
        if len(guess)!=1 or not guess.isalpha():
            print('input is invalid')
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)
        if guessed_letters in answer:
          for i in range(len(answer)):
            if answer[i] ==guess:
                hint[i]=guess
        else:
            wrong_guesses+=1
        if "__" not in hint:
            show_hangman(wrong_guesses)
            show_the_answers(answer)
            print("Congratulatiins!you won")
            is_running=False
        elif wrong_guesses >= len(hangman_) -1:
            show_hangman(wrong_guesses)
            show_the_answers(answer)
            print("SORRY! YOU LOSE")
            is_running=False
        
            
if __name__=="__main__":
    main()