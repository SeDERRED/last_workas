import tkinter as tk
import time
import random

class ReactionGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Игра на реакцию (Круги)")
        self.master.geometry("250x400")

        self.label = tk.Label(master, text="Нажми 'Старт' и жди круга", font=("Arial", 14))
        self.label.pack(pady=0)

        self.canvas = tk.Canvas(master, width=200, height=230)
        self.canvas.pack(pady=10)
        self.circle = self.canvas.create_oval(50, 50, 150, 150, fill="gray")  # начальный круг (серый)

        self.canvas.tag_bind(self.circle, "<Button-1>", self.react)

        self.start_button = tk.Button(master, text="Старт", command=self.start_game, font=("Arial", 12))
        self.start_button.pack(pady=30)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=2)

        self.ready_to_click = False
        self.start_time = 0

    def start_game(self):
        self.result_label.config(text="")
        self.canvas.itemconfig(self.circle, fill="red")  # серый круг до сигнала
        self.ready_to_click = False
        wait_time = random.randint(2000, 5000)
        self.label.config(text="Готовься нужн будет\n нажать на зелёный круг")
        self.master.after(wait_time, self.show_circle)

    def show_circle(self):
        self.canvas.itemconfig(self.circle, fill="green")  # зелёный круг — сигнал
        self.label.config(text="Кликай по кругу!")
        self.start_time = time.time()
        self.ready_to_click = True

    def react(self, event):
        if self.ready_to_click:
            reaction_time = time.time() - self.start_time
            self.label.config(text="Нажми 'Старт' и жди круга")
            self.result_label.config(text=f"Время реакции: {reaction_time:.3f} секунд")
            self.canvas.itemconfig(self.circle, fill="gray")
            self.ready_to_click = False
        else:
            self.result_label.config(text="Слишком рано! Жди зелёный круг!")


root = tk.Tk()
game = ReactionGame(root)
root.mainloop()