import tkinter as tk
import random

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_var.set("You win!")
        user_score_var.set(user_score_var.get() + 1)
        user_score_label.config(text=f"Your Score: {user_score_var.get()}")
    else:
        result_var.set("Computer wins!")
        computer_score_var.set(computer_score_var.get() + 1)
        computer_score_label.config(text=f"Computer Score: {computer_score_var.get()}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")  
root.configure(bg='lightblue')  

choices = ["Rock", "Paper", "Scissors"]

user_choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg='lightblue', font=("Arial", 12))
user_choice_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

user_choice_option = tk.OptionMenu(root, user_choice_var, *choices)
user_choice_option.pack()

play_button = tk.Button(root, text="Play", command=play_game, bg='lightgreen', font=("Arial", 12))
play_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg='blue', bg='lightblue')
result_label.pack()

user_score_var = tk.IntVar()
user_score_var.set(0)
user_score_label = tk.Label(root, text=f"Your Score: {user_score_var.get()}", bg='lightblue', font=("Arial", 12))
user_score_label.pack()

computer_score_var = tk.IntVar()
computer_score_var.set(0)
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score_var.get()}", bg='lightblue', font=("Arial", 12))
computer_score_label.pack()

root.mainloop()
