from tkinter import *
from tkinter import ttk
# from methods import *
import turtle

import methods


class User:
    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.task = []
        self.task_left = 0

    def set_task_left(self, n):
        self.task_left = n

    def add(self, obj):
        self.task.append(obj)

    def remove(self):
        pass


class Task:
    def __init__(self, name, due_date, description):
        self.name = name
        self.due_date = due_date
        self.description = description


root = Tk()
root.title("Task Tracker by Thanat")
root.geometry("400x400")

# login_root = Tk()
# login_root.title("Task Tracker by Thanat")
# login_root.geometry("400x400")


# class Login:
#     def __init__(self, master):
#         self.welcome_frame = Frame(master)
#         self.welcome_frame.grid(row=0, column=0)


class Tracker:
    def __init__(self, master):
        # Creating main frame
        self.main_frame = Frame(master)
        self.main_frame.pack(fill=BOTH, expand=1)

        # Main Canvas where we are actually scrolling
        self.main_canvas = Canvas(self.main_frame)
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Creating scrollbar
        self.scroll_bar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

        # Link canvas scrolling to actually scrolling the window
        self.main_canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.config(scrollregion=self.main_canvas.bbox(ALL)))

        # Creating frame which is inside the main canvas / This is the intro frame
        self.scroll_frame = Frame(self.main_canvas)
        self.main_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        # Sub frames inside scroll frame (which is inside scollable canvas)
        self.intro_frame = Frame(self.scroll_frame)
        self.intro_frame.grid(row=0, column=0)

        # Intro frame
        self.say_hi = Label(self.intro_frame, text="HI! USER")
        self.say_hi.grid(row=0, column=0)
        self.task_left = Label(self.intro_frame, text=f"You have {admin.task_left} task left !")
        self.task_left.grid(row=1, column=0)

        # Graph frame (canvas)
        self.graph_canvas = Canvas(self.scroll_frame, bg='white', height=225)
        self.graph_canvas.grid(row=1, column=0)
        t = turtle.RawTurtle(self.graph_canvas)
        t.penup()
        t.goto(-100, -50)
        t.pendown()
        t.left(90)
        t.fd(150)
        t.penup()
        t.goto(-100, -50)
        t.pendown()
        t.seth(0)
        t.fd(200)
        # Display task frame
        self.display_task_frame = Frame(self.scroll_frame)
        self.display_task_frame.grid(row=2, column=0)

    def add_task(self):
        pass


admin = User("Thanat", "Suppagornmongkol", "tracker123")
tracker = Tracker(root)
python_hw = Task("Python project", "15/12/2021", "semester 1 project")
admin.add(python_hw)
root.mainloop()
