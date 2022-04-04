from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from kju_aphorisms import get_kju_aphorism as aphorism
from scheduler import *
import re
import threading
import datetime
import time
import winsound


class App:
    def __init__(self, root):
        # Window Configuration
        self.root = root
        self.root.title("KJU: Aphorism of the Day")
        self.root['bg'] = 'lightgray'
        self.root.resizable(False, False)
        self.photo = PhotoImage(file='dprk_pub_logo.png')
        self.root.iconphoto(False, self.photo)

        # Aphorism and Author Text Labels
        self.aphorism_text = ttk.Label(text=aphorism(), background='lightgray', wraplength=300,
                                 justify='center')
        self.aphorism_text.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.author_text = ttk.Label(text="-Kim Jong Un", background='lightgray')
        self.author_text.grid(row=2, column=0, sticky='e', columnspan=2, padx=20)

        # Scheduling Options
        self.schedule_button = ttk.Button(text="Set Schedule")
        self.schedule_button.grid(row=3, column=1, sticky='e', padx=20, pady=10)
        self.schedule_button.bind('<ButtonRelease-1>', lambda event: self.new_schedule())
        self.current_schedule = f"Current Schedule: {get_schedule()}"
        self.schedule_info = ttk.Label(text=self.current_schedule, background='lightgray')
        self.schedule_info.grid(row=3, column=0, sticky='w', padx=20, pady=10)

    def alarm_watch(self):
        pass

    def new_schedule(self):
        self.schedule_window = Toplevel(self.root)
        self.schedule_window['bg'] = 'lightgray'
        self.schedule_window.iconphoto(False, self.photo)
        self.schedule_window.title("Set Schedule")
        self.schedule_window.resizable(False, False)
        self.schedule_window.focus()
        self.schedule_window.grab_set()

        schedule_label = ttk.Label(self.schedule_window, text='Set a new time for your daily aphorism:',
                                   background='lightgray')
        schedule_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        input_box = ttk.Entry(self.schedule_window, width=6)
        input_box.grid(row=1, column=0, sticky='e', padx=20, pady=10)

        instructions_label = ttk.Label(self.schedule_window, text='e.g. 8:00 or 15:30', background='lightgray')
        instructions_label.grid(row=1, column=1, sticky='w')

        set_button = ttk.Button(self.schedule_window, text='Set New Time')
        set_button.grid(row=2, column=0, columnspan=2, pady=10)
        set_button.bind('<ButtonRelease-1>', lambda event: self.check_input(input_box.get()))

    def check_input(self, user_input):
        clock_format = r'^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$'
        user_input = user_input.strip()
        if user_input and user_input[0] == '0':
            user_input = user_input[1:]
        if re.match(clock_format, user_input):
            self.schedule_info.configure(text=f'Current Schedule: {user_input}')
            set_schedule(user_input)
            self.schedule_window.destroy()
            self.alarm_watch()
        else:
            messagebox.showerror(title='Invalid Entry', message='Please enter a valid time.')


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
