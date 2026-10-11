# Rock Paper Scissors Game
from tkinter import *
from PIL import Image, ImageTk
import random

# WINDOW SETUP
root = Tk()
root.title("Rock Paper Scissor")
root.geometry("800x680")

# CANVAS & LABELS 
canvas = Canvas(root, width=800, height=680)
canvas.pack()

label1 = Label(root, text="PLAYER", font=("Algerian", 25))
label2 = Label(root, text="COMPUTER", font=("Algerian", 25))
label3 = Label(root, text="Vs", font=("Algerian", 40))

label1.place(x=80, y=20)
label2.place(x=560, y=20)
label3.place(x=370, y=230)

# LOADING IMAGES 
default_img = Image.open("default.jpeg").resize((300, 300))
player_img = ImageTk.PhotoImage(default_img)
comp_img = ImageTk.PhotoImage(default_img.transpose(Image.FLIP_LEFT_RIGHT))

rock_raw = Image.open("rock.jpeg").resize((300, 300))
p_rock_img = ImageTk.PhotoImage(rock_raw)
c_rock_img = ImageTk.PhotoImage(rock_raw.transpose(Image.FLIP_LEFT_RIGHT))

paper_raw = Image.open("paper.jpeg").resize((300, 300))
p_paper_img = ImageTk.PhotoImage(paper_raw)
c_paper_img = ImageTk.PhotoImage(paper_raw.transpose(Image.FLIP_LEFT_RIGHT))

scissor_raw = Image.open("scissor.jpeg").resize((300, 300))
p_scissor_img = ImageTk.PhotoImage(scissor_raw)
c_scissor_img = ImageTk.PhotoImage(scissor_raw.transpose(Image.FLIP_LEFT_RIGHT))

# Loading button images
rock_btn_raw = Image.open("rock_button1.jpeg").resize((50, 50))
rock_button = ImageTk.PhotoImage(rock_btn_raw)
paper_btn_raw = Image.open("paper_button1.jpeg").resize((50, 50))
paper_button = ImageTk.PhotoImage(paper_btn_raw)
scissor_btn_raw = Image.open("scissors_button1.jpeg").resize((50, 50))
scissors_button = ImageTk.PhotoImage(scissor_btn_raw)

# player buttons imgs on canvas
canvas.create_image(90, 450, image=rock_button)
canvas.create_image(180, 450, image=paper_button)
canvas.create_image(260, 450, image=scissors_button)


# comp buttons imgs on canvas
canvas.create_image(530, 450, image=rock_button)
canvas.create_image(615, 450, image=paper_button)
canvas.create_image(710, 450, image=scissors_button)


# comp button labels
label1 = Label(root, text="ROCK", font=("Arial", 10, "bold"))
label2 = Label(root, text="PAPER", font=("Arial", 10, "bold"))
label3 = Label(root, text="SCISSOR", font=("Arial", 10, "bold"))


label1.place(x=510, y=485)
label2.place(x=595, y=485)
label3.place(x=680, y=485)


# CANVAS 
p_display = canvas.create_image(180, 250, image=player_img)
c_display = canvas.create_image(630, 250, image=comp_img)
result_display = canvas.create_text(390, 600, text="", font=("Algerian", 30))


# GAME LOGIC
def game(choice):
    select = [1, 2, 3]
    computer_val = random.choice(select)

    p_imgs = {1: p_rock_img, 2: p_paper_img, 3: p_scissor_img}
    canvas.itemconfig(p_display, image=p_imgs[choice])

    c_imgs = {1: c_rock_img, 2: c_paper_img, 3: c_scissor_img}
    canvas.itemconfig(c_display, image=c_imgs[computer_val])

    if choice == computer_val:
        result = "DRAW"
    elif (choice == 1 and computer_val == 3) or \
         (choice == 2 and computer_val == 1) or \
         (choice == 3 and computer_val == 2):
        result = "PLAYER WON"
    else:
        result = "COMPUTER WON"
    
    canvas.itemconfig(result_display, text=result)

def reset():
    canvas.itemconfig(p_display, image=player_img)
    canvas.itemconfig(c_display, image=comp_img)
    canvas.itemconfig(result_display, text="")



# BUTTONS 

# Create a container (Frame) to hold the buttons
button_frame = Frame(root)

canvas.create_window(180, 500, window=button_frame)

# Add buttons to the frame
btn_r = Button(button_frame, text="ROCK", font=("Arial", 10, "bold"), 
               width=8, command=lambda: game(1))
btn_r.pack(side=LEFT, padx=5)

btn_p = Button(button_frame, text="PAPER", font=("Arial", 10, "bold"), 
               width=8, command=lambda: game(2))
btn_p.pack(side=LEFT, padx=5)

btn_s = Button(button_frame, text="SCISSOR", font=("Arial", 10, "bold"), 
               width=8, command=lambda: game(3))
btn_s.pack(side=LEFT, padx=5)



# Clear Button
btn_clear = Button(root, text="CLEAR", font=("Arial", 10, "bold"), command=reset, width=12)
canvas.create_window(390, 50, window=btn_clear)


root.mainloop()
 