import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
DELAY = 150  # Задержка обновления (мс)
SIZE = 20    # Размер блока змейки и яблока

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Змейка на tkinter")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.start_screen()

    def start_screen(self):
        self.clear_frame()
        start_label = tk.Label(self.frame, text="Змейка", font=("Arial", 30))
        start_label.pack(pady=20)

        start_button = tk.Button(self.frame, text="Старт", font=("Arial", 20), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        self.clear_frame()
        self.canvas = tk.Canvas(self.frame, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.snake = [(WIDTH//2, HEIGHT//2)]
        self.direction = 'Right'
        self.food = None
        self.create_food()

        self.score_text = self.canvas.create_text(50, 10, fill="white", font=("Arial", 16), text=f"Счёт: {self.score}")

        self.root.bind("<Key>", self.change_direction)
        self.running = True
        self.game_loop()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def create_food(self):
        possible_positions = []
        for x in range(0, WIDTH, SIZE):
            for y in range(0, HEIGHT, SIZE):
                if (x, y) not in self.snake:
                    possible_positions.append((x, y))
        self.food = random.choice(possible_positions)

    def change_direction(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE
        elif self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE

        # Обработка выхода за границы — перенос на противоположную сторону
        if head_x < 0:
            head_x = WIDTH - SIZE
        elif head_x >= WIDTH:
            head_x = 0
        if head_y < 0:
            head_y = HEIGHT - SIZE
        elif head_y >= HEIGHT:
            head_y = 0

        new_head = (head_x, head_y)

       
        if new_head in self.snake:
            self.game_over()
            return False

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.create_food()
            self.canvas.itemconfig(self.score_text, text=f"Счёт: {self.score}")
        else:
            self.snake.pop()

        return True

    def game_loop(self):
        if self.running:
            alive = self.move_snake()
            if alive:
                self.draw()
                self.root.after(DELAY, self.game_loop)

    def draw(self):
        self.canvas.delete("all")

        x, y = self.food
        self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="red", outline="")

        for i, (x, y) in enumerate(self.snake):
            color = "green" if i == 0 else "lightgreen"
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color, outline="")

        self.canvas.create_text(50, 10, fill="white", font=("Arial", 16), text=f"Счёт: {self.score}")

    def game_over(self):
        self.running = False
        self.clear_frame()

        game_over_label = tk.Label(self.frame, text="Игра окончена!", font=("Arial", 30), fg="red")
        game_over_label.pack(pady=20)

        score_label = tk.Label(self.frame, text=f"Твой счёт: {self.score}", font=("Arial", 20))
        score_label.pack(pady=10)

        restart_button = tk.Button(self.frame, text="Играть снова", font=("Arial", 20), command=self.start_game)
        restart_button.pack(pady=20)


root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
