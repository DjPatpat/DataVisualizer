import tkinter as tk
from tkinter import ttk     # import Tk themed widgets (new widgets from 2007)

class ButtonGeneral(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # grid layout manager
        self.columnconfigure(index=0, weight=1)

        self.__create_widgets()


    def __create_widgets(self):
        ttk.Button(self, text="1").grid(row=0, column=0)
        ttk.Button(self, text="2").grid(row=1, column=0)
        ttk.Button(self, text="3").grid(row=2, column=0)
        ttk.Button(self, text="4").grid(row=3, column=0)


class App(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.title('DataVisualizer')
        self.__set_size(width, height)

        # Ensure icon is in the assets folder
        # TODO: create assets folder
        # TODO: prepare icon in .ico format
        # self.iconbitmap('./assets/pythontutorial.ico')

        # Layout on the root window
        # Cols
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)
        self.columnconfigure(index=2, weight=3)
        # Rows
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=5)

        self.__create_widgets()


    def __set_size(self, window_width, window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    def __create_widgets(self):
        button_general = ButtonGeneral(self)
        button_general.grid(column=0, row=0, columnspan=2)


# test function for button interaction
# arguments can be passed using lambda expressions, see
# https://www.pythontutorial.net/tkinter/tkinter-command/
# pass command function without parentheses () to not call it at the start of the program
# e.g. button = ttk.Button(self, text='Click Me', command=button_clicked)
def button_clicked():
    print('Button clicked')


if __name__ == '__main__':
    app = App(width=600, height=400)
    app.mainloop()
