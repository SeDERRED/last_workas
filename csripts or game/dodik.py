import tkinter as tk
import random
import time
from threading import Thread

def lighten_color(color, amount=0.5):
    """
    Делает цвет светлее.
    color - строка цвета (имя или hex)
    amount - насколько светлее (0 - без изменений, 1 - белый)
    """
    # Преобразуем цвет в RGB (0-255)
    rgb = root.winfo_rgb(color)
    # winfo_rgb возвращает (r*256, g*256, b*256), переводим в 0-255
    r = rgb[0] // 256
    g = rgb[1] // 256
    b = rgb[2] // 256

    # Смещаем цвет к белому по формуле
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)

    return f"#{r:02x}{g:02x}{b:02x}"

class SimonSaysGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simon Says")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.colors = ["green", "red", "purple", "blue"]
        self.light_colors = [lighten_color(c, 0.5) for c in self.colors]  # светлые оттенки
        self.buttons = []
        self.sequence = []
        self.player_input = []
        self.level = 0
        self.is_playing_sequence = False

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        for i, color in enumerate(self.colors):
            btn = tk.Button(frame, bg=color, activebackground=self.light_colors[i], width=10, height=5,
                            command=lambda i=i: self.player_click(i), relief="raised")
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.buttons.append(btn)

        self.start_button = tk.Button(self.root, text="Начать игру", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="Нажмите 'Начать игру' чтобы начать", font=("Arial", 12))
        self.status_label.pack()

    def start_game(self):
        self.sequence = []
        self.player_input = []
        self.level = 0
        self.status_label.config(text="Игра началась! Следи за последовательностью...")
        self.next_round()

    def next_round(self):
        self.level += 1
        self.player_input = []
        self.sequence.append(random.randint(0, 3))
        self.status_label.config(text=f"Уровень {self.level}. Запоминай!")
        self.is_playing_sequence = True
        Thread(target=self.play_sequence).start()

    def play_sequence(self):
        for index in self.sequence:
            self.highlight_button(index)
            time.sleep(0.6)
            self.unhighlight_button(index)
            time.sleep(0.2)
        self.is_playing_sequence = False
        self.status_label.config(text="Твой ход! Повтори последовательность.")

    def highlight_button(self, index):
        # Меняем цвет кнопки на светлый оттенок
        self.buttons[index].config(bg=self.light_colors[index])
        self.buttons[index].update()

    def unhighlight_button(self, index):
        # Возвращаем оригинальный цвет
        self.buttons[index].config(bg=self.colors[index])
        self.buttons[index].update()

    def player_click(self, index):
        if self.is_playing_sequence:
            return

        # Подсветка кнопки светлым цветом на 300мс
        self.highlight_button(index)
        self.root.after(300, lambda: self.unhighlight_button(index))

        self.player_input.append(index)
        current_step = len(self.player_input) - 1

        if self.player_input[current_step] != self.sequence[current_step]:
            self.status_label.config(text=f"Неверно! Игра окончена. Ты достиг уровня {self.level}.")
            self.sequence = []
            return

        if len(self.player_input) == len(self.sequence):
            self.status_label.config(text="Правильно! Подготовься к следующему уровню...")
            self.root.after(1500, self.next_round)



root = tk.Tk()
game = SimonSaysGame(root)
root.mainloop()