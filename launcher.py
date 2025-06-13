import tkinter as tk # Это позволяет использовать элементы графического интерфейса пользователя (GUI), которые предоставляет tkinter, в своем коде, обращаясь к ним через имя tk.
from tkinter import messagebox, PhotoImage # Он предназначен для работы с диалоговыми окнами и изображениями в GUI (графическом интерфейсе пользователя) программ.
from PIL import Image, ImageTk, __version__ as PILLOW_VERSION
import webbrowser # Для открытия URL
import subprocess
import sys # Для sys.executable
import os

# --- Цветовая схема и шрифты (в стиле Steam) ---
BG_COLOR = "#1b2838"  # Темно-синий фон, как у Steam
FRAME_BG_COLOR = "#2a3f54" # Чуть светлее для внутренних рамок
TEXT_COLOR = "#c7d5e0"  # Светло-голубовато-серый текст
ACCENT_COLOR = "#66c0f4" # Яркий голубой для акцентов
EXIT_BUTTON_BG_COLOR = "#c94c4c" # Красный для кнопки выхода
BUTTON_BG_COLOR = "#4a6e8a" # Темнее синий для кнопок
BUTTON_FG_COLOR = TEXT_COLOR
SUPPORT_BUTTON_BG_COLOR = "#556b2f" # Пример: оливково-зеленый для поддержки
ABOUT_BUTTON_BG_COLOR = "#4f5b62"   # Пример: серо-синий для кнопки "О программе"
BUTTON_ACTIVE_BG_COLOR = "#5e8bb0" # Цвет кнопки при наведении/нажатии

FONT_FAMILY_MAIN = "Segoe UI" # Или "Arial", "Calibri"
FONT_SIZE_NORMAL = 10
FONT_SIZE_MEDIUM = 12
FONT_SIZE_LARGE = 16
FONT_BOLD = "bold"

# --- Конфигурация игр ---
GAMES = [
    {
        "name": "Trips-traps-trull", # Уточнили название, если это игра reak.py
        "path": "..\\oleg2007\\csripts or game\\reak.py", # Относительный путь, если reak.py в C:\oleg2007
        "description": """🎮 Тест на реакцию!
Мини-игра для проверки скорости реакции. Нажми кнопку после сигнала.

🏆 Особенности: уровни, статистика, минимализм.
Тренирует реакцию, внимание. Полезно для ума!""",
        "cover_path": "..\\oleg2007\\image\\AIM.jpg" # Этот путь уже был относительным и правильным
    },
    {
        "name": "Guess number",
        "path": "..\\oleg2007\\csripts or game\\guess.py", # Используем raw string
        "description": """🔢 Угадай число!
Компьютер загадал число от 1 до 100. Попробуй угадать его за наименьшее количество попыток!""",
        "cover_path": "..\\oleg2007\\image\\chis.jpg"
    },
{
        "name": "Snake",
        "path": "..\\csripts or game\\sneak.py", # Используем raw string
        "description": """🐍 Классическая игра 'Змейка'.
Управляй змейкой, собирай еду и расти. Не врезайся в себя или стены!""",
        "cover_path": "..\\oleg2007\\image\\snake.jpg"
    },
{
        "name": "Simon",
        "path": "..\\.\\oleg2007\\csripts or game\\dodik.py",
        "description": """🧠 Simon: игра на память.
Повторяй последовательность цветов.

Развивает память и внимание. Есть уровни и звуки.""",
        "cover_path": "..\\oleg2007\\image\\simon.jpg"
    },
    {
        "name": "Flappy Bird",
        "path": "..\\oleg2007\\csripts or game\\gamesam.py", # Укажите правильный путь, если он другой
        "description": """🐦 Flappy Bird!
Управляй птичкой, пролетая между трубами. Набери как можно больше очков!
Просто кликай, чтобы птичка взлетала.""",
        "cover_path": "..\\oleg2007\\image\\flapy.jpg" # Укажите путь к обложке или None
    },
]


class GameLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam")
        self.root.geometry("800x550") # Немного увеличим окно для лучшего вида
        self.root.configure(bg=BG_COLOR)

        # --- Стили для кнопок ---
        self.button_style = {
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL),
            "bg": BUTTON_BG_COLOR,
            "fg": BUTTON_FG_COLOR,
            "activebackground": BUTTON_ACTIVE_BG_COLOR,
            "activeforeground": TEXT_COLOR,
            "relief": "flat",
            "borderwidth": 0, # Ширина рамки
            "width": 22, # Уменьшили ширину кнопки списка игр
            "anchor": "w",
            "padx": 10,
            "compound": tk.LEFT, # Для отображения иконки слева от текста
        }
        self.launch_button_style = self.button_style.copy()
        self.launch_button_style.update({
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM, FONT_BOLD),
            "bg": ACCENT_COLOR,
            "fg": "#FFFFFF", # Белый текст на яркой кнопке
            "activebackground": "#55b0e4", # Чуть темнее при наведении
            "width": 20,
            "anchor": "center",
        })
        self.exit_button_style = self.button_style.copy()
        self.exit_button_style.update({
            "bg": EXIT_BUTTON_BG_COLOR,
            "activebackground": "#4b1f1f", # Темнее красный при наведении
            "fg": "#FFFFFF",
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD),
            "anchor": "center", # Центрируем текст на кнопке выхода
        })
        self.support_button_style = self.button_style.copy()
        self.support_button_style.update({
            "bg": SUPPORT_BUTTON_BG_COLOR, # Новый цвет для кнопки поддержки
            "activebackground": "#38441F", # Чуть светлее при наведении
            "fg": "#FFFFFF",
            "anchor": "center",
        })
        self.about_button_style = self.button_style.copy()
        self.about_button_style.update({
            "bg": ABOUT_BUTTON_BG_COLOR,
            "activebackground": "#3e4a52", # Темнее при наведении
            "fg": "#FFFFFF",
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD),
            "anchor": "center",
        })



        # Главный фрейм, содержащий список игр и панель деталей
        main_frame = tk.Frame(root, bg=BG_COLOR)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Левый фрейм для списка игр
        self.games_list_frame = tk.Frame(main_frame, width=250, bg=FRAME_BG_COLOR, relief="solid", borderwidth=1)
        self.games_list_frame.pack(side="left", fill="y", padx=(0, 10))
        # self.games_list_frame.pack_propagate(False) # Закомментируем или удалим, чтобы кнопка выхода не влияла на размер списка
        
        tk.Label(
            self.games_list_frame,
            text="Игры:",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM, FONT_BOLD),
            bg=FRAME_BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=10, padx=10, anchor="w")

        # Фрейм для кнопок игр, чтобы кнопка выхода была отдельно внизу
        self.game_buttons_frame = tk.Frame(self.games_list_frame, bg=FRAME_BG_COLOR)
        self.game_buttons_frame.pack(fill="x", expand=False) # expand=False чтобы не растягивался

        # Кнопка выхода
        exit_button = tk.Button(
            self.games_list_frame,
            text="Выход",
            command=self.root.destroy,
            **self.exit_button_style
        )
        exit_button.pack(side="bottom", pady=(1,10), padx=10, fill="x") # Нижний отступ 10, чтобы не прилипала к краю

        # Кнопка Поддержка (теперь будет выше кнопки Выход)
        support_button = tk.Button(
            self.games_list_frame,
            text="Поддержка",
            command=self.open_support_chat,
            **self.support_button_style
        )
        support_button.pack(side="bottom", pady=(1,1), padx=10, fill="x")

        # Новая кнопка "О программе" (выше кнопки Поддержка)
        about_button = tk.Button(
            self.games_list_frame,
            text="О программе",
            command=self.show_about_info,
            **self.about_button_style
        )
        about_button.pack(side="bottom", pady=(10,1), padx=10, fill="x") # Отступ сверху 10, снизу 1

        # Правый фрейм для деталей игры
        self.details_frame = tk.Frame(main_frame, bg=FRAME_BG_COLOR, relief="solid", borderwidth=1)
        self.details_frame.pack(side="right", fill="both", expand=True)

        # --- Заполнение списка игр ---
        for game_info in GAMES:
            icon_image = None 
            icon_path_from_config = game_info.get("icon_path")
            print(f"\n[INFO] Версия Pillow: {PILLOW_VERSION}")
            print(f"\n[ИГРА: {game_info['name']}] Обработка icon_path: '{icon_path_from_config}'")

            if icon_path_from_config:
                # Собираем полный путь, если иконка в той же директории, что и лаунчер
                # __file__ указывает на текущий файл (launcher.py)
                # Если icon_path_from_config абсолютный, os.path.join его не изменит.
                # Если он относительный, он будет объединен с директорией скрипта.
                # Поскольку мы используем абсолютный путь в icon_path, мы можем его нормализовать
                # и использовать напрямую. Убедимся, что строка пути корректна.
                
                # Шаг 1: Нормализуем путь, указанный в конфигурации
                normalized_path_from_config = os.path.normpath(icon_path_from_config)
                print(f"  Нормализованный icon_path из конфига: '{normalized_path_from_config}'")

                # Шаг 2: Определяем, является ли путь абсолютным. Если нет, делаем его абсолютным.
                if os.path.isabs(normalized_path_from_config):
                    actual_path_to_check = normalized_path_from_config
                else:
                    # Если путь относительный, он будет относительно директории скрипта
                    current_script_dir = os.path.dirname(os.path.abspath(__file__))
                    actual_path_to_check = os.path.join(current_script_dir, normalized_path_from_config)
                    actual_path_to_check = os.path.normpath(actual_path_to_check) # Еще раз нормализуем после join

                print(f"  Финальный проверяемый АБСОЛЮТНЫЙ путь к иконке: '{actual_path_to_check}'")

                if os.path.exists(actual_path_to_check):
                    print(f"  Файл иконки НАЙДЕН по пути: '{actual_path_to_check}'")
                    try:
                        pil_image = Image.open(actual_path_to_check)
                        print(f"  Pillow Image.open УСПЕШНО. Объект: {pil_image}")
                        print(f"    Размер: {pil_image.size}, Формат: {pil_image.format}, Режим: {pil_image.mode}")
                        # Если хотите изменить размер иконки, например, до 32x32 пикселей:
                        # pil_image = pil_image.resize((32, 32), Image.Resampling.LANCZOS)
                        # print(f"  Pillow Image после resize (если было). Размер: {pil_image.size}")
                        icon_image = ImageTk.PhotoImage(pil_image)
                        print(f"  ImageTk.PhotoImage УСПЕШНО. Объект: {icon_image}")
                    except Exception as e: # Ловим более общие ошибки, включая ошибки Pillow
                        print(f"  [ОШИБКА ЗАГРУЗКИ ИКОНКИ] Путь: {actual_path_to_check}. Ошибка: {e}")
                        icon_image = None
                else:
                    print(f"  [ФАЙЛ ИКОНКИ НЕ НАЙДЕН] по пути: '{actual_path_to_check}'")
                    icon_image = None
            else:
                print(f"  icon_path не указан в конфигурации для игры '{game_info['name']}'.")

            print(f"  Перед созданием кнопки, icon_image: {icon_image}")
            btn = tk.Button(
                self.game_buttons_frame, # Добавляем кнопки игр в отдельный фрейм
                text=game_info["name"],
                image=icon_image, # Устанавливаем иконку
                **self.button_style, # Применяем стиль
                command=lambda gi=game_info: self.show_game_details(gi)
            )
            if icon_image: # Важно сохранить ссылку на изображение!
                btn.image = icon_image
            btn.pack(pady=3, padx=10, fill="x") # Увеличил padx для лучшего вида с иконкой

        # --- Элементы на панели деталей (будут обновляться) ---
        self.cover_label = tk.Label(
            self.details_frame, text="Обложка игры",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM),
            bg="#334B61", fg=TEXT_COLOR,  # Темнее фон для плейсхолдера обложки
            relief="solid", borderwidth=1 # Убраны фиксированные height и width
        )
        self.cover_label.pack(pady=20, padx=20)

        self.game_title_label = tk.Label(
            self.details_frame, text="Название игры",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_LARGE, FONT_BOLD),
            bg=FRAME_BG_COLOR, fg=ACCENT_COLOR
        )
        self.game_title_label.pack(pady=(0,10))

        self.game_description_text = tk.Label(
            self.details_frame, text="Описание игры...",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL),
            bg=FRAME_BG_COLOR, fg=TEXT_COLOR,
            wraplength=450, justify="left"
        )
        self.game_description_text.pack(pady=10, fill="x", padx=20)

        self.launch_button = tk.Button(self.details_frame, text="ЗАПУСТИТЬ", state="disabled", **self.launch_button_style)
        self.launch_button.pack(pady=20)

        # Показываем детали первой игры по умолчанию, если список не пуст
        if GAMES:
            self.show_game_details(GAMES[0])
        else:
            self.game_title_label.config(text="Нет игр для отображения")

    def show_game_details(self, game_info):
        """Обновляет панель деталей информацией о выбранной игре."""
        self.current_game_path = game_info["path"]
        self.current_game_name = game_info["name"]

        self.game_title_label.config(text=game_info["name"])
        self.game_description_text.config(text=game_info.get("description", "Описание отсутствует."))

        # --- Загрузка и отображение обложки ---
        cover_path_from_config = game_info.get("cover_path")
        loaded_cover_image = None

        if cover_path_from_config:
            # Определяем абсолютный путь к обложке
            if os.path.isabs(cover_path_from_config):
                actual_cover_path = os.path.normpath(cover_path_from_config)
            else:
                # Если путь относительный, он будет относительно директории скрипта
                current_script_dir = os.path.dirname(os.path.abspath(__file__))
                actual_cover_path = os.path.join(current_script_dir, cover_path_from_config)
                actual_cover_path = os.path.normpath(actual_cover_path) # Нормализуем после join

            self.log_message(f"  [ОБЛОЖКА] Попытка загрузки из: '{actual_cover_path}'")

            if os.path.exists(actual_cover_path):
                try:
                    pil_image = Image.open(actual_cover_path)
                    # --- Опционально: изменение размера обложки ---
                    # Увеличим отображаемый размер обложки (было 60)
                    desired_width = 280 # Новая ширина обложки в пикселях
                    aspect_ratio = pil_image.height / pil_image.width
                    desired_height = int(desired_width * aspect_ratio)
                    pil_image = pil_image.resize((desired_width, desired_height), Image.Resampling.LANCZOS)
                    self.log_message(f"    Размер обложки после resize: {pil_image.size}")
                    # --- Конец опционального изменения размера ---
                    loaded_cover_image = ImageTk.PhotoImage(pil_image)
                    self.log_message(f"    Обложка успешно загружена: {pil_image}")
                except Exception as e:
                    self.log_message(f"  [ОШИБКА ЗАГРУЗКИ ОБЛОЖКИ] Путь: {actual_cover_path}. Ошибка: {e}")
                    loaded_cover_image = None
            else:
                self.log_message(f"  [ФАЙЛ ОБЛОЖКИ НЕ НАЙДЕН] по пути: {actual_cover_path}")
        else:
            self.log_message(f"  cover_path не указан в конфигурации для игры '{game_info['name']}'.")

        if loaded_cover_image:
            self.cover_label.config(image=loaded_cover_image, text="") # Убираем текст, если есть картинка
            self.cover_label.image = loaded_cover_image # ВАЖНО: Сохраняем ссылку на изображение!
        else:
            # Если обложки нет, показываем текст-заглушку
            self.cover_label.config(image="", text=f"Обложка для\n{game_info['name']}")
            self.cover_label.image = None # Сбрасываем ссылку, если картинки нет
            
        self.launch_button.config(state="normal", command=self.launch_current_game)

    def launch_current_game(self):
        """Запускает игру, информация о которой сейчас на панели деталей."""
        if not hasattr(self, 'current_game_path') or not self.current_game_path:
            messagebox.showerror("Ошибка", "Игра не выбрана или путь не указан.")
            return

        game_name_to_launch = self.current_game_name
        game_path_from_config = self.current_game_path

        # Определяем абсолютный путь к файлу игры
        if not os.path.isabs(game_path_from_config):
            current_script_dir = os.path.dirname(os.path.abspath(__file__))
            absolute_game_path = os.path.normpath(os.path.join(current_script_dir, game_path_from_config))
        else:
            absolute_game_path = os.path.normpath(game_path_from_config)

        self.log_message(f"Попытка запуска: {game_name_to_launch} (Конфиг: '{game_path_from_config}', Абсолютный: '{absolute_game_path}')")
        try:
            if not os.path.exists(absolute_game_path):
                messagebox.showerror("Ошибка Запуска", f"Файл для игры '{game_name_to_launch}' не найден по пути:\n{absolute_game_path}")
                self.log_message(f"Ошибка: Файл не найден - {absolute_game_path}")
                return
            
            # Определяем, как запускать игру
            if absolute_game_path.lower().endswith(".py"):
                # Запускаем .py скрипт через интерпретатор Python
                # Устанавливаем рабочую директорию (cwd) в папку, где лежит сам скрипт игры.
                game_script_directory = os.path.dirname(absolute_game_path)
                subprocess.Popen([sys.executable, absolute_game_path], cwd=game_script_directory)
            else:
                subprocess.Popen(absolute_game_path) # Запускаем как обычный исполняемый файл
            self.log_message(f"Игра '{game_name_to_launch}' успешно запущена.")
        except OSError as e:
            messagebox.showerror("Ошибка Запуска", f"Не удалось запустить игру '{game_name_to_launch}'.\nОшибка: {e}")
            self.log_message(f"OSError при запуске {game_name_to_launch}: {e}")
        except Exception as e:
            messagebox.showerror("Неизвестная Ошибка", f"Произошла неизвестная ошибка при запуске '{game_name_to_launch}'.\nОшибка: {e}")
            self.log_message(f"Exception при запуске {game_name_to_launch}: {e}")

    def log_message(self, message):
        print(f"[Лаунчер] {message}")

    def open_support_chat(self):
        """Открывает ссылку на чат поддержки в браузере."""
        support_url = "https://t.me/turkell" 
        self.log_message(f"Открытие чата поддержки: {support_url}")
        webbrowser.open_new_tab(support_url)

    def show_about_info(self):
        """Отображает окно с информацией о программе."""
        about_window = tk.Toplevel(self.root)
        about_window.title("О программе")
        about_window.configure(bg=FRAME_BG_COLOR)
        about_window.resizable(False, False)

        # Задаем размеры окна перед центрированием
        window_width = 450
        window_height = 800 # Немного увеличим высоту для большего текста

        # Центрирование окна "О программе" относительно главного окна
        self.root.update_idletasks() # Убедимся, что размеры главного окна обновлены
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        x = root_x + (root_width // 2) - (window_width // 2)
        y = root_y + (root_height // 2) - (window_height // 2)
        about_window.geometry(f'{window_width}x{window_height}+{x}+{y}')

        about_window.transient(self.root) # Делает окно модальным по отношению к родительскому
        about_window.grab_set() # Перехватывает все события

        info_frame = tk.Frame(about_window, bg=FRAME_BG_COLOR, padx=20, pady=20)
        info_frame.pack(expand=True, fill="both")

        title_label = tk.Label(
            info_frame,
            text="Copy Steam",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_LARGE, FONT_BOLD),
            bg=FRAME_BG_COLOR,
            fg=ACCENT_COLOR
        )
        title_label.pack(pady=(0, 15))

        info_text_content = [
            ("Версия:", "0.1.0"),
            ("Создатели:", "Jegor Samsonov \nEduard Garusov "),
            ("Описание:", "Этот игровой лаунчер был разработан для обеспечения удобного и приятного доступа к вашей коллекции мини-игр."),
            ("Технологии:", "Python 3, Tkinter, Pillow"),
            ("Особенности:", "- Запуск игр одним кликом\n- Просмотр описаний и обложек\n- Стильный дизайн, вдохновленный известным лаунчером Steam"),
            ("Благодарности:", "Особая благодарность всем, кто участвовал в тестировании, предлагал идеи и оказывал поддержку на всех этапах разработки."),
            ("Начало разработки:", "01.06.2025"),
            ("Релиз:", "ХХ.ХХ.ХХХХ")
        ]

        for header, text in info_text_content:
            header_label = tk.Label(
                info_frame, text=header, font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD),
                bg=FRAME_BG_COLOR, fg=TEXT_COLOR, anchor="nw", justify="left"
            )
            header_label.pack(fill="x", pady=(7,0))

            text_label = tk.Label(
                info_frame, text=text, font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL),
                bg=FRAME_BG_COLOR, fg=TEXT_COLOR, wraplength=380,
                anchor="nw", justify="left"
            )
            text_label.pack(fill="x", pady=(0,10))

        close_button = tk.Button(
            info_frame, text="Закрыть", command=about_window.destroy,
            font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL), bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
            activebackground=BUTTON_ACTIVE_BG_COLOR, relief="flat", width=10
        )
        close_button.pack(pady=(20,0))



root_window = tk.Tk()
app = GameLauncherApp(root_window)
root_window.mainloop()
