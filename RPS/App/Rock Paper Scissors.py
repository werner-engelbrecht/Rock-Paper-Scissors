import threading as th
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random


computer_choices = ["rock", "paper", "scissors"]

player_winCount = 0
computer_winCount = 0

window = tk.Tk()
window.geometry("1000x500")
window.resizable(False, False)
window.title("Rock Paper Scissors")

title = Text(height=20, font=("Fresh Steak", 36,
                              "bold"), background="#00ABF0")
title.tag_configure("tag_name", justify="center", foreground='white')
title.insert('1.0', "ROCK PAPER SCISSORS!")
title.configure(state=DISABLED)
title.tag_add("tag_name", "1.0", "end")
title.pack()

score1 = Button(window, command=None, text='SCORE', font=('Fresh Steak', 20, 'bold'),
                fg='white', bd=0, bg='#00ABF0', activebackground='#00ABF0', activeforeground='white')
score2 = Button(window, command=None, text='SCORE', font=('Fresh Steak', 20, 'bold'),
                fg='white', bd=0, bg='#00ABF0', activebackground='#00ABF0', activeforeground='white')


ellipsis = Image.open("Assets/ellipsis.png")
resized_ellipsis = ellipsis.resize((100, 100), Image.Resampling.LANCZOS)
new_ellipsis = ImageTk.PhotoImage(resized_ellipsis)

check = Image.open("Assets/check.png")
resized_check = check.resize((100, 100), Image.Resampling.LANCZOS)
new_check = ImageTk.PhotoImage(resized_check)


def printOptions():

    global text
    text = Button(window, command=None, text="Take your pick", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    text.place(x=170, y=180)

    global rock_button
    rock_button = Button(window, image=new_rock, command=Rock,
                         borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    rock_button.place(x=100, y=100)

    global paper_button
    paper_button = Button(window, image=new_paper, command=Paper,
                          borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    paper_button.place(x=200, y=100)

    global scissors_button
    scissors_button = Button(window, image=new_scissors, command=Scissors,
                             borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    scissors_button.place(x=300, y=100)


def printCheck():

    ellipsis_button.destroy()
    opponent_text.destroy()

    global check_button
    check_button = Button(window, image=new_check, command=None,
                          borderwidth=0, bg="#00ABF0", activebackground="#00ABF0")
    check_button.place(x=700, y=85)

    global text_done
    text_done = Button(window, command=None, text="Computer has picked", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')

    text_done.place(x=625, y=180)


def printEllipsis():

    global opponent_text
    opponent_text = Button(window, command=None, text="Computer is picking", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    opponent_text.place(x=625, y=180)

    global ellipsis_button
    ellipsis_button = Button(window, image=new_ellipsis, command=None,
                             borderwidth=0, bg="#00ABF0", activebackground="#00ABF0")
    ellipsis_button.place(x=700, y=80)

    th.Timer(2.0, printCheck).start()


def computer():

    check_button.destroy()
    text_done.destroy()

    global computer_decision
    computer_decision = random.choice(computer_choices)

    global opponent_rockButton
    opponent_rockButton = Button(window, image=opponent_new_rock, command=None,
                                 borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    global opponent_paperButton
    opponent_paperButton = Button(window, image=opponent_new_paper, command=None,
                                  borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    global opponent_scissorsButton
    opponent_scissorsButton = Button(window, image=opponent_new_scissors, command=None,
                                     borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')

    if computer_decision == "rock":
        global chosen_text
        opponent_rockButton.place(x=705, y=100)
        chosen_text = Button(window, command=None, text="Computer has picked Rock", font=(
            "Munich", 14), fg='white', bd=0, bg='#00ABF0', activebackground='#00ABF0', activeforeground='white')
        chosen_text.place(x=625, y=180)

    elif computer_decision == "paper":
        opponent_paperButton.place(x=705, y=100)
        chosen_text = Button(window, command=None, text="Computer has picked Paper", font=(
            "Munich", 14), fg='white', bd=0, bg='#00ABF0', activebackground='#00ABF0', activeforeground='white')
        chosen_text.place(x=625, y=180)

    else:
        opponent_scissorsButton.place(x=710, y=100)
        chosen_text = Button(window, command=None, text="Computer has picked Scissors", font=(
            "Munich", 14), fg='white', bd=0, bg='#00ABF0', activebackground='#00ABF0', activeforeground='white')
        chosen_text.place(x=625, y=180)


def Rock():

    paper_button.destroy()
    scissors_button.destroy()
    text.destroy()
    rock_button.configure(state=DISABLED)
    global new_text
    new_text = Button(window, command=None, text="You have picked Rock", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    new_text.place(x=170, y=180)

    th.Timer(2.0, computer).start()

    def winner1():
        global final
        global player_winCount
        global computer_winCount
        global computer_decision

        if computer_decision == 'rock':
            final = Button(window, command=None, text="IT'S A TIE!", font=(
                "Plastic Love", 36), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
        elif computer_decision == 'paper':
            final = Button(window, command=None, text="COMPUTER WINS!", font=(
                "Plastic Love", 36), fg='red', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='red')
            computer_winCount += 1
            if computer_winCount == 1:
                computer_star_button1.place(x=730, y=250)
            elif computer_winCount == 2:
                computer_star_button2.place(x=750, y=250)
            elif computer_winCount == 3:
                computer_star_button3.place(x=770, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()

        else:
            final = Button(window, command=None, text="YOU WIN!", font=(
                "Plastic Love", 36), fg='blue', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='blue')
            player_winCount += 1
            if player_winCount == 1:
                star_button1.place(x=260, y=250)
            elif player_winCount == 2:
                star_button2.place(x=280, y=250)
            elif player_winCount == 3:
                star_button3.place(x=300, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()
        final.place(x=500, y=360, anchor='center')

    th.Timer(3.0, winner1).start()
    th.Timer(5.0, destroyRock).start()
    th.Timer(5.0, nextRound).start()


def Paper():

    rock_button.destroy()
    scissors_button.destroy()
    text.destroy()
    paper_button.configure(state=DISABLED)
    global new_text
    new_text = Button(window, command=None, text="You have picked Paper", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    new_text.place(x=170, y=180)

    th.Timer(2.0, computer).start()

    def winner2():
        global final
        global player_winCount
        global computer_winCount
        global computer_decision

        if computer_decision == 'rock':
            final = Button(window, command=None, text="YOU WIN!", font=(
                "Plastic Love", 36), fg='blue', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='blue')
            player_winCount += 1
            if player_winCount == 1:
                star_button1.place(x=260, y=250)
            elif player_winCount == 2:
                star_button2.place(x=280, y=250)
            elif player_winCount == 3:
                star_button3.place(x=300, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()

        elif computer_decision == 'paper':
            final = Button(window, command=None, text="IT'S A TIE!", font=(
                "Plastic Love", 36), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
        else:
            final = Button(window, command=None, text="COMPUTER WINS!", font=(
                "Plastic Love", 36), fg='red', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='red')
            computer_winCount += 1
            if computer_winCount == 1:
                computer_star_button1.place(x=730, y=250)
            elif computer_winCount == 2:
                computer_star_button2.place(x=750, y=250)
            elif computer_winCount == 3:
                computer_star_button3.place(x=770, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()

        final.place(x=500, y=360, anchor='center')

    th.Timer(3.0, winner2).start()
    th.Timer(5.0, destroyPaper).start()
    th.Timer(5.0, nextRound).start()


def Scissors():

    paper_button.destroy()
    rock_button.destroy()
    text.destroy()
    scissors_button.configure(state=DISABLED)
    global new_text
    new_text = Button(window, command=None, text="You have picked Scissors", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    new_text.place(x=170, y=180)

    th.Timer(2.0, computer).start()

    def winner3():
        global final
        global player_winCount
        global computer_winCount
        global computer_decision

        if computer_decision == 'scissors':
            final = Button(window, command=None, text="IT'S A TIE!", font=(
                "Plastic Love", 36), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
        elif computer_decision == 'rock':
            final = Button(window, command=None, text="COMPUTER WINS!", font=(
                "Plastic Love", 36), fg='red', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='red')
            computer_winCount += 1
            if computer_winCount == 1:
                computer_star_button1.place(x=730, y=250)
            elif computer_winCount == 2:
                computer_star_button2.place(x=750, y=250)
            elif computer_winCount == 3:
                computer_star_button3.place(x=770, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()

        else:
            final = Button(window, command=None, text="YOU WIN!", font=(
                "Plastic Love", 36), fg='blue', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='blue')
            player_winCount += 1
            if player_winCount == 1:
                star_button1.place(x=260, y=250)
            elif player_winCount == 2:
                star_button2.place(x=280, y=250)
            elif player_winCount == 3:
                star_button3.place(x=300, y=250)
                th.Timer(1.0, finalScreen).start()
                exit()
        final.place(x=500, y=360, anchor='center')

    th.Timer(3.0, winner3).start()
    th.Timer(5.0, destroyScissors).start()
    th.Timer(5.0, nextRound).start()


def destroyRock():
    rock_button.destroy()


def destroyPaper():
    paper_button.destroy()


def destroyScissors():
    scissors_button.destroy()


rock = Image.open("Assets/rock.png")
paper = Image.open("Assets/paper.png")
scissors = Image.open("Assets/scissors.png")

resized_rock = rock.resize((75, 75), Image.Resampling.LANCZOS)
resized_paper = paper.resize((75, 75), Image.Resampling.LANCZOS)
resized_scissors = scissors.resize((75, 75), Image.Resampling.LANCZOS)

new_rock = ImageTk.PhotoImage(resized_rock)
new_paper = ImageTk.PhotoImage(resized_paper)
new_scissors = ImageTk.PhotoImage(resized_scissors)

opponent_rock = Image.open("Assets/rock.png")
opponent_paper = Image.open("Assets/paper.png")
opponent_scissors = Image.open("Assets/scissors.png")

resized_opponent_rock = opponent_rock.resize(
    (75, 75), Image.Resampling.LANCZOS)
resized_opponent_paper = opponent_paper.resize(
    (75, 75), Image.Resampling.LANCZOS)
resized_opponent_scissors = opponent_scissors.resize(
    (75, 75), Image.Resampling.LANCZOS)

opponent_new_rock = ImageTk.PhotoImage(resized_opponent_rock)
opponent_new_paper = ImageTk.PhotoImage(resized_opponent_paper)
opponent_new_scissors = ImageTk.PhotoImage(resized_opponent_scissors)

star_outline = Image.open('Assets/star_outline.png')
star = Image.open('Assets/star.png')

star_outline = ImageTk.PhotoImage(star_outline)
star = ImageTk.PhotoImage(star)

star_outline_button1 = Button(window, image=star_outline, command=None,
                              borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
star_outline_button2 = Button(window, image=star_outline, command=None,
                              borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
star_outline_button3 = Button(window, image=star_outline, command=None,
                              borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
star_button1 = Button(window, image=star, command=None,
                      borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
star_button2 = Button(window, image=star, command=None,
                      borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
star_button3 = Button(window, image=star, command=None,
                      borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')

computer_star_outline_button1 = Button(window, image=star_outline, command=None,
                                       borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
computer_star_outline_button2 = Button(window, image=star_outline, command=None,
                                       borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
computer_star_outline_button3 = Button(window, image=star_outline, command=None,
                                       borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
computer_star_button1 = Button(window, image=star, command=None,
                               borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
computer_star_button2 = Button(window, image=star, command=None,
                               borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
computer_star_button3 = Button(window, image=star, command=None,
                               borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')

vertical = Frame(window, bg='white', height=440, width=3)
vertical.place(x=500, y=60)

horizontal = Frame(window, bg='white', height=5, width=1000)
horizontal.place(x=0, y=60)


def score():
    star_outline_button1.place(x=260, y=250)
    star_outline_button2.place(x=280, y=250)
    star_outline_button3.place(x=300, y=250)

    computer_star_outline_button1.place(x=730, y=250)
    computer_star_outline_button2.place(x=750, y=250)
    computer_star_outline_button3.place(x=770, y=250)

    score1.place(x=150, y=230)
    score2.place(x=620, y=230)


def nextRound():

    opponent_rockButton.destroy()
    opponent_paperButton.destroy()
    opponent_scissorsButton.destroy()
    final.destroy()
    new_text.destroy()
    chosen_text.destroy()

    th.Timer(0.0, printEllipsis).start()

    global text
    text = Button(window, command=None, text="Take your pick", font=(
        "Munich", 14), fg='white', bg='#00ABF0', bd=0, activebackground='#00ABF0', activeforeground='white')
    text.place(x=170, y=180)

    global rock_button
    rock_button = Button(window, image=new_rock, command=Rock,
                         borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    rock_button.place(x=100, y=100)

    global paper_button
    paper_button = Button(window, image=new_paper, command=Paper,
                          borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    paper_button.place(x=200, y=100)

    global scissors_button
    scissors_button = Button(window, image=new_scissors, command=Scissors,
                             borderwidth=0, bg='#00ABF0', activebackground='#00ABF0')
    scissors_button.place(x=300, y=100)


def Game():
    printOptions()
    printEllipsis()
    score()


def finalScreen():

    window.withdraw()

    global top
    if player_winCount == 3 or computer_winCount == 3:
        top = Tk()
        top.resizable(False, False)
        top.configure(bg='#00ABF0')
        top.geometry("500x300")

        frame1 = Frame(top, highlightbackground="white",
                       highlightthickness=2, bg='#00ABF0')
        frame1.pack(padx=20, pady=100)

        score = Text(top, bd=0, font=("Fresh Steak", 36,
                                      "bold"), background="#00ABF0", fg='white')
        score.insert('1.0', f"{player_winCount}:{computer_winCount}")
        score.configure(state=DISABLED)
        score.place(x=220, y=10)

        winner = Text(top, bd=0, font=("Fresh Steak", 24,
                                       "bold"), background="#00ABF0", fg='white')
        if player_winCount == 3:
            winner.insert('1.0', "YOU WIN!")
            winner.place(x=175, y=80)
        elif computer_winCount == 3:
            winner.insert('1.0', "COMPUTER WINS")
            winner.place(x=115, y=80)
        winner.configure(state=DISABLED)

        exit_button = Button(top, width=15, fg='white',  command=close_win, bg='#00ABF0', text="EXIT", font=("Fresh Steak",
                                                                                                             12, "bold"), activeforeground='white', activebackground='#00ABF0').place(x=165, y=180)
        top.mainloop()


def close_win():
    top.destroy()
    window.destroy()
    exit()


if __name__ == '__main__':
    Game()

window.mainloop()
