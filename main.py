import tkinter as tk
from tkinter import ttk     # import Tk themed widgets (new widgets from 2007)

buttons_GP = ["Save", "Save as", "Load", "Export", "LaTeX", "PDF"]
buttons_SP = ["Choose Columns", "Add Column", "Remove Column", "Add Row", "Remove Row"]

class ButtonGeneral(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # grid layout manager
        self.columnconfigure(index=0, weight=1)
        self.__create_widgets()


    def __create_widgets(self):
        i = 0
        for button in buttons_GP:
            ttk.Button(self, text=button).grid(row=i, column=0)
            i += 1


class ButtonSpecific(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # grid layout manager
        self.columnconfigure(index=1, weight=1)
        self.__create_widgets()


    def __create_widgets(self):
        i = 0
        for button in buttons_SP:
            ttk.Button(self, text=button).grid(row=0, column=i)
            i += 1
        ttk.Checkbutton(self, text="Single Plot").grid(row=0, column=i)


class ButtonThemes(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        container.style = ttk.Style(container)
        container.selected_theme = tk.StringVar()

        def change_theme():
            container.style.theme_use(container.selected_theme.get())

        theme_frame = ttk.LabelFrame(self, text="Theme")
        theme_frame.grid(row=2, column=0)

        for theme_name in container.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=container.selected_theme,
                command=change_theme
            )
            rb.pack(expand=True, anchor='sw')


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
        button_general.grid(column=0, row=0, rowspan=2, sticky=tk.NW)

        button_specific = ButtonSpecific(self)
        button_specific.grid(column=1, row=0, columnspan=2, sticky=tk.N)

        button_themes = ButtonThemes(self)
        button_themes.grid(column=0, row=2, sticky=tk.SW)


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
