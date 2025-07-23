import tkinter as tk
from tkinter import ttk     # import Tk themed widgets (new widgets from 2007)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('data visualizer')

        window_width = 600
        window_height = 400

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # test run of setting a label
        label = ttk.Label(self)
        label.config(text='Themed label')
        label.pack()

        # first test of a button with action
        # pass command function without parentheses () to not call it at the start of the program
        ttk.Button(self, text='Click Me', command=button_clicked).pack()

        # Ensure icon is in the assets folder
        # TODO: create assets folder
        # TODO: prepare icon in .ico format
        # self.iconbitmap('./assets/pythontutorial.ico')


# test function for button interaction
# arguments can be passed using lambda expressions, see
# https://www.pythontutorial.net/tkinter/tkinter-command/
def button_clicked():
    print('Button clicked')


if __name__ == '__main__':
    app = App()
    app.mainloop()
