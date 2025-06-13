#настройки,размеры,скорость
from random import *
from turtle import *
from freegames import vector
#Начальные значения для сброса
INITIAL_BALL_SPEED = 5
INITIAL_KIVI_SPEED = 3

#Настройки скорости 
ball_speed = INITIAL_BALL_SPEED  # Начальная скорость черных шаров
kivi_speed = INITIAL_KIVI_SPEED
speed_increase_amount = 0.2 # На сколько увеличивается скорость
speed_increase_interval_ms = 6000 # Интервал увеличения скорости в миллисекундах (6 секунды)
maxspeed_baal = 8
maxspeed_kivi = 7


#Состояние игры 
game_state = 'playing'

bird = vector(0, 0)
balls = []
kivis = []

bgcolor("lightblue")

def tap(x, y):
    if game_state == 'playing': # Разрешаем прыжок только если игра идет
        up = vector(0, 40)
        bird.move(up)


def inside(point):
    return -200 < point.x < 200 and -200 < point.y < 200

def draw():
    clear()

    if game_state == 'playing':
        goto(bird.x, bird.y)
        write('🦉', align='center', font=('Arial', 16, 'normal')) # Птица всегда "жива" в состоянии playing

        for ball in balls:
            goto(ball.x, ball.y)#обекты об которых ты умераешь 
            dot(20, 'black')
        
        for kivi in kivis:
            goto(kivi.x, kivi.y)
            dot(30, 'grey')
    elif game_state == 'game_over':
        # Отображаем сообщение о проигрыше
        goto(0, 20) 
        write("Вы проиграли!", align="center", font=("Arial", 24, "bold"))
        goto(0, -20)
        write("Нажмите 'R' для перезапуска", align="center", font=("Arial", 16, "normal"))
        
        # Отображаем "мертвую" птицу на месте гибели
        goto(bird.x, bird.y)
        write('🪶', align='center', font=('Arial', 16, 'normal'))

    update()


def increase_speed():
    global ball_speed, kivi_speed # kivi_speed также глобальная

    if game_state != 'playing': # Останавливаем увеличение скорости, если игра окончена
        return

    ball_speed += speed_increase_amount
    if ball_speed > maxspeed_baal:
        ball_speed = maxspeed_baal
    
    kivi_speed += speed_increase_amount
    if kivi_speed > maxspeed_kivi:
        kivi_speed = maxspeed_kivi
    
    # Планируем следующее увеличение только один раз и если игра продолжается
    if game_state == 'playing':
        ontimer(increase_speed, speed_increase_interval_ms)

def move():
    global game_state # Мы будем изменять game_state

    if game_state != 'playing': # Останавливаем игровой цикл, если игра окончена
        return
    
    bird.y -= 5
    for ball in balls:
        ball.x -= ball_speed #движения обектов ob kotorЫx tõ умрёшь (используем переменную скорости)
    
    for kivi in kivis:
        kivi.x -= kivi_speed

    if randrange(10) == 0:
        y = randrange(-199, 199) #рандомное появления по высоте
        ball = vector(199, y)
        balls.append(ball)
        
        y= randrange(-199, 199)
        kivi = vector(199, y)
        kivis.append(kivi)


    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)
    # Добавим удаление для kivis, если они выходят за экран
    while len(kivis) > 0 and not inside(kivis[0]):
        kivis.pop(0)

    if not inside(bird):
        game_state = 'game_over'
        draw() # Отображаем экран "Game Over"
        return

    for ball in balls:
        if abs(ball - bird) < 13: #размер хитбокса
            game_state = 'game_over'
            draw() # Отображаем экран "Game Over"
            return
        #add
    for kivi in kivis:
        if abs(kivi - bird) < 20: #размер хитбокса
            game_state = 'game_over'
            draw() # Отображаем экран "Game Over"
            return

    # Если дошли сюда, игра продолжается
    draw() # Отрисовываем текущее состояние игры
    if game_state == 'playing': # Планируем следующий кадр только если игра все еще идет
        ontimer(move, 30)

def restart_game():
    """Сбрасывает состояние игры для нового начала."""
    global game_state, bird, balls, kivis, ball_speed, kivi_speed

    # Перезапускаем только если игра действительно окончена
    if game_state == 'game_over':
        game_state = 'playing'
        
        # Сброс птицы
        bird.x = 0
        bird.y = 0
        
        # Очистка препятствий
        balls.clear()
        kivis.clear()
        
        # Сброс скоростей
        ball_speed = INITIAL_BALL_SPEED
        kivi_speed = INITIAL_KIVI_SPEED
        
        # Запускаем игровой цикл и таймер ускорения заново
        # Первый вызов move() также выполнит первую отрисовку (draw())
        move()
        increase_speed()

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen() # Начинаем слушать события клавиатуры
onkey(restart_game, 'r') # Привязываем к маленькой 'r'
onkey(restart_game, 'R') # Привязываем к большой 'R'
increase_speed() # Запускаем таймер увеличения скорости
onscreenclick(tap)
move()
done()
