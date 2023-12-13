import tkinter as tk

class DropdownButton(tk.Button):
    def __init__(self, master, text="None", button_commands=None, **kwargs):
        super().__init__(
            master,
            text=text,
            fg='silver',
            font=('Arial', 12),
            bg='#484848',
            highlightthickness=0,
            bd=0,
            command=self.toggle_dropdown,
            borderwidth=2,
            relief="solid",
            background='#484848',
            **kwargs
        )
        self.is_expanded = False

        self.dropdown_frame = tk.Frame(master)
        self.buttons = []
        if button_commands:
            for command in button_commands:
                button = tk.Button(self.dropdown_frame, text=command.__name__, fg='silver', font=('Arial', 12), bg='#484848', highlightthickness=0, bd=0, command=command)
                button.pack()
                self.buttons.append(button)

    def toggle_dropdown(self):
        if self.is_expanded:
            self.collapse_dropdown()
        else:
            self.expand_dropdown()

    def expand_dropdown(self):
        self.is_expanded = True
        self.dropdown_frame.pack()

    def collapse_dropdown(self):
        self.is_expanded = False
        self.dropdown_frame.pack_forget()


root = tk.Tk()



def open_report():
    print("Opening report window...")

def open_vector():
    print("Opening vector window...")

dropdown_button = DropdownButton(
                    master=root, 
                    text='Memasiki',
                    button_commands=[open_report, open_vector]
)
dropdown_button.pack()

root.mainloop()