
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random

correct_guessing_fruit=""
numberOfChances=0

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load("Original PUBG game music with party video _موسيقة لعبة ببجي الاصليه مع فيديو للحفله _.mp3")
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()






def reset_game():
    global selectedFruit
    selectedFruit = ""
    selected_word_label.config(text="")
    select_button.config(state="normal")
    guess_button.config(state="normal")
    letter_input.delete("1.0", tk.END)
    letter_input.config(state="normal")
    check_status_label.config(text="")
    noOfChancesLabel.config(text="0")
    game_label.config(text=" Let's play Hangerman ")





def start_game():
    reset_game()
    main_frame.pack_forget()

    game_frame.pack(fill="both", expand=True)



def updateSelectedWord():
    global correct_guessing_fruit
    if len(selectedFruit)>0:
        new_word="__  "*len(selectedFruit)

        correct_guessing_fruit=new_word
        selected_word_label.config(text=new_word)





def back_to_main():
    game_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

selectedFruit=""
selectedFruitList=[]

def selectFruit():

    global selectedFruit
    global numberOfChances

    fruits = [
    "apple", "banana", "orange", "mango", "grapes",
    "strawberry", "pineapple", "watermelon", "lemon", "peach",
    "cherry", "blueberry", "raspberry", "blackberry", "kiwi",
    "papaya", "pear", "plum", "apricot", "pomegranate",
    "avocado", "coconut", "fig", "lychee", "guava",
    "melon","starfruit"]

    selectedFruit=random.choice(fruits)
    updateSelectedWord()
    noOfChancesLabel.config(text=len(selectedFruit)+2)
    numberOfChances=len(selectedFruit)+2
    print(selectedFruit)

def guessLetter():

    global correct_guessing_fruit
    global selectedFruitList
    global numberOfChances

    myLetter = letter_input.get("1.0", tk.END).strip()
    selectedFruitList = correct_guessing_fruit.split("  ")
    if myLetter in selectedFruit:
        check_status_label.config(text="correct letter",fg="green")
        if selectedFruit.count(myLetter) > 1:
            for i in range(len(selectedFruit)):
                if selectedFruit[i] == myLetter:
                    selectedFruitList[i] = myLetter
                    correct_guessing_fruit = "  ".join(selectedFruitList)
                    selected_word_label.config(text=correct_guessing_fruit)
        else:
            index_letter = selectedFruit.index(myLetter)
            print(index_letter)

            selectedFruitList[index_letter] = myLetter
            correct_guessing_fruit = "  ".join(selectedFruitList)
            print(selectedFruitList)
            selected_word_label.config(text=correct_guessing_fruit)


    else:
        print("this letter not in the fruit")
        check_status_label.config(text=" this letter not in the word ", fg="red")
    letter_input.delete("1.0", tk.END)

    numberOfChances -= 1
    noOfChancesLabel.config(text=numberOfChances)

    gameOver()
    winGame()


def gameOver():
    if numberOfChances<=0:
        check_status_label.config(text=" Game Over restart the game ",fg="red")
        select_button.config(state="disabled")
        guess_button.config(state="disabled")
        letter_input.config(state="disabled")
        return False
    return True

def winGame():
    myGuessedWord="".join(selectedFruitList)
    if myGuessedWord==selectedFruit:
        check_status_label.config(text=" You Are Win The Game ", fg="green")
        select_button.config(state="disabled")
        guess_button.config(state="disabled")
        letter_input.config(state="disabled")
        return False
    return True


def restartGame():
    reset_game()




root = tk.Tk()
play_music()
root.title("Hangman Game")
root.geometry("600x550")

# Load the background image
background_image = Image.open("Game-Background-Graphics-76306020-1.jpg")
background_photo = ImageTk.PhotoImage(background_image)


main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)


main_canvas = tk.Canvas(main_frame, width=600, height=400)
main_canvas.pack(fill="both", expand=True)
main_canvas.create_image(0, 0, image=background_photo, anchor="nw")


text_label = tk.Label(main_frame, text="Welcome to the Hangman Game", font=("Arial", 18), fg="white", bg="black")
main_canvas.create_window(300, 150, anchor="center", window=text_label)


start_button = tk.Button(main_frame, text="Start Game", command=start_game, font=("Arial", 16), bg="green", fg="white")
main_canvas.create_window(300, 250, anchor="center", window=start_button)


end_button = tk.Button(main_frame, text="End Game", command=root.destroy, font=("Arial", 16), bg="red", fg="white")
main_canvas.create_window(300, 300, anchor="center", window=end_button)


game_frame = tk.Frame(root)


game_canvas = tk.Canvas(game_frame, width=600, height=400)
game_canvas.pack(fill="both", expand=True)
game_canvas.create_image(0, 0, image=background_photo, anchor="nw")


game_label = tk.Label(game_frame, text=" Let's play Hangerman ", font=("Arial", 18), fg="white", bg="black")
game_canvas.create_window(300, 80, anchor="center", window=game_label)

select_button = tk.Button(game_frame, text="Select Fruit",command=selectFruit, font=("Arial", 16), bg="green", fg="white")

game_canvas.create_window(300, 150, anchor="center", window=select_button)


selected_word_label = tk.Label(game_frame, text="", font=("Arial", 18), fg="white", bg="black")
game_canvas.create_window(300, 240, anchor="center", window=selected_word_label)

noOfChancesWordLabel=tk.Label(game_frame,text="Number Of Chances: ",font=("Arial", 16), fg="white", bg="black")
game_canvas.create_window(250, 300, anchor="center", window=noOfChancesWordLabel)

noOfChancesLabel=tk.Label(game_frame,text=numberOfChances,font=("Arial", 16), fg="white", bg="black")
game_canvas.create_window(400, 300, anchor="center", window=noOfChancesLabel)

enter_letter_label= tk.Label(game_frame, text="guess one letter: ", font=("Arial", 14), fg="white", bg="black")
game_canvas.create_window(250, 430, anchor="center", window=enter_letter_label)

letter_input = tk.Text(game_frame, height=1, width=5, font=("Arial", 16))
game_canvas.create_window(370, 430, anchor="center", window=letter_input)

guess_button = tk.Button(game_frame, text="Guess",command=guessLetter, font=("Arial", 16), bg="green", fg="white")

game_canvas.create_window(300, 480, anchor="center", window=guess_button)




back_button = tk.Button(game_frame, text="Main Menu", command=back_to_main, font=("Arial", 16), bg="blue", fg="white")
game_canvas.create_window(70, 30, anchor="center", window=back_button)



check_status_label= tk.Label(game_frame, text="", font=("Arial", 16), fg="blue", bg="black")
game_canvas.create_window(300, 360, anchor="center", window=check_status_label)

restart_button = tk.Button(game_frame, text="Restart", command=restartGame, font=("Arial", 16), bg="green", fg="white")
game_canvas.create_window(50, 520, anchor="center", window=restart_button)



root.mainloop()
