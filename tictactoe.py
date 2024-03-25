import turtle
import tkinter as tk

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Tic Tac Toe - @mateo1mc")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('light gray')
screen.tracer(0, 0)
turtle.hideturtle()
messagebox = None

def draw_board():
    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3, -1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3, 1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(x, y):
    turtle.up()
    turtle.goto(x, y - 0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=100)

def draw_x(x, y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)

def draw_piece(i, j, p):
    if p == 0:
        return
    x, y = 2 * (j - 1), -2 * (i - 1)
    if p == 1:
        draw_x(x, y)
    else:
        draw_circle(x, y)

def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i, j, b[i][j])
    screen.update()

def gameover(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]:
        return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]:
        return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]:
        return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]:
        return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]:
        return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]:
        return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]:
        return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9:
        return 3
    else:
        return 0

def show_game_over(result):
    global messagebox
    messagebox = tk.Toplevel()
    messagebox.title("Game Over!")
    
    label = tk.Label(messagebox, text="Game Over")
    label.pack()
    
    if result == 1:
        label = tk.Label(messagebox, text="X won!")
    elif result == 2:
        label = tk.Label(messagebox, text="O won!")
    else:
        label = tk.Label(messagebox, text="Tie!")
    label.pack()

    play_again_button = tk.Button(messagebox, text="Play Again", command=play_again)
    play_again_button.pack()

    quit_button = tk.Button(messagebox, text="Quit Game", command=quit_game)
    quit_button.pack()

    # Center the messagebox on the screen
    messagebox.update_idletasks()
    screen_center_x = screen.window_width() // 2
    screen_center_y = screen.window_height() // 2
    x_offset = screen_center_x - messagebox.winfo_reqwidth() // 2
    y_offset = screen_center_y - messagebox.winfo_reqheight() // 2
    messagebox.geometry(f"+{x_offset}+{y_offset}")

def play_again():
    global b, turn, messagebox
    # Clear the Turtle screen and reset drawing state
    turtle.clearscreen()
    turtle.reset()
    
    # Reinitialize the game board
    b = [[0, 0, 0] for _ in range(3)]
    draw(b)
    
    # Reset the turn to 'x'
    turn = 'x'
    
    # Destroy the messagebox if it exists
    if messagebox:
        messagebox.destroy()
        messagebox = None
    
    # Set up the screen again
    screen.setup(800, 800)
    screen.title("Tic Tac Toe - @mateo1mc")
    screen.setworldcoordinates(-5, -5, 5, 5)
    screen.bgcolor('light gray')
    screen.tracer(0, 0)
    turtle.hideturtle()
    
    # Bind the onclick event to the play function
    screen.onclick(play)
    turtle.mainloop()



def quit_game():
    screen.bye()

def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0:
        return
    if turn == 'x':
        b[i][j], turn = 1, 'o'
    else:
        b[i][j], turn = 2, 'x'
    draw(b)
    result = gameover(b)
    if result in {1, 2, 3}:
        show_game_over(result)

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw(b)
turn = 'x'
screen.onclick(play)
turtle.mainloop()
