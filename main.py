import tkinter as tk
from tkinter import messagebox
from kju_aphorisms import get_kju_aphorism as aphorism
from scheduler import *
import re
import threading
import datetime
import time
import winsound


def alarm_watch():
    pass


def new_schedule():
    schedule_window = tk.Toplevel(main_window)
    schedule_window['bg'] = 'lightgray'
    schedule_window.title("Set Schedule")
    schedule_window.resizable(False, False)
    schedule_window.focus()
    schedule_window.grab_set()

    schedule_label = tk.Label(schedule_window, text='Set a new time for your daily aphorism:', background='lightgray', padx=20, pady=10)
    schedule_label.grid(row=0, column=0, columnspan=2)

    input_box = tk.Entry(schedule_window, width=6)
    input_box.grid(row=1, column=0, sticky='e', padx=20, pady=10)

    instructions_label = tk.Label(schedule_window, text='e.g. 8:00 or 15:30', background='lightgray')
    instructions_label.grid(row=1, column=1, sticky='w')

    set_button = tk.Button(schedule_window, text='Set New Time', justify='center')
    set_button.grid(row=2, column=0, columnspan=2, pady=10)
    set_button.bind('<ButtonRelease-1>', lambda event: check_input(schedule_window, input_box.get()))


def check_input(window, user_input):
    clock_format = r'^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$'
    user_input = user_input.strip()
    if user_input and user_input[0] == '0':
        user_input = user_input[1:]
    if re.match(clock_format, user_input):
        schedule_info.configure(text=f'Current Schedule: {user_input}')
        set_schedule(user_input)
        window.destroy()
    else:
        tk.messagebox.showerror(title='Invalid Entry', message='Please enter a valid time.')


if __name__ == '__main__':
    # Window Configuration
    main_window = tk.Tk()
    main_window.title("KJU: Aphorism of the Day")
    main_window['bg'] = 'lightgray'
    main_window.resizable(False, False)
    photo = tk.PhotoImage(file='dprk_pub_logo.png')
    main_window.iconphoto(False, photo)

    # Aphorism and Author Text Labels
    aphorism_text = tk.Label(text=aphorism(), padx=20, pady=20, background='lightgray', wraplength=300, justify='center')
    aphorism_text.grid(row=0, column=0, columnspan=2)
    author_text = tk.Label(text="-Kim Jong Un", background='lightgray', padx=20)
    author_text.grid(row=2, column=0, sticky='e', columnspan=2)

    # Scheduling Options
    schedule_button = tk.Button(text="Set Schedule")
    schedule_button.grid(row=3, column=1, sticky='e', padx=20, pady=10)
    schedule_button.bind('<ButtonRelease-1>', lambda event: new_schedule())
    current_schedule = f"Current Schedule: {get_schedule()}"
    schedule_info = tk.Label(text=current_schedule, background='lightgray', padx=20, pady=10)
    schedule_info.grid(row=3, column=0, sticky='w')

    # t1 = threading.Thread(task=alarm_watch, name='t1')

    main_window.mainloop()
