import tkinter as tk
import random

class NumberGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")
        self.master.geometry("300x250")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Я загадал число от 1 до 100.\nПопробуй угадать!", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.check_button = tk.Button(master, text="Проверить", command=self.check_guess, font=("Arial", 12))
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(master, text="Заново", command=self.restart_game, font=("Arial", 10))
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Введите число!")
            return

        self.attempts += 1


        if guess<self.secret_number:
            self.result_label.config(text='больше')
           

        elif guess> self.secret_number:
            self.result_label.config(text="меньше")
        else:
            self.result_label.config(text=f"Угадал за {self.attempts} попыток!")

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.label.config(text="Я загадал число от 1 до 100.\nПопробуй угадать!")


root = tk.Tk()
game = NumberGuessGame(root)
root.mainloop()
