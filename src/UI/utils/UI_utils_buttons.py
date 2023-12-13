import tkinter as tk


class DropdownButton(tk.Button):
    def __init__(self, master, text='None', button_commands=None,  **kwargs):
        super().__init__(
            master,
            fg='silver',
            text=text,
            font=('Arial', 12),
            bg='#484848',
            highlightthickness=0,
            bd=0,
            command=self.toggle_dropdown,
            borderwidth=0,
            relief="solid",
            background='#484848',
            **kwargs
        )
        self.is_expanded = False
        self.dropdown_frame = tk.Frame(master)
        self.dropdown_frame.configure(bg='#484848')
        self.buttons = []
        self.column: int
        self.name = text
        if button_commands:
            for command in button_commands:
                button_text = command.__doc__ if command.__doc__ else command.__name__
                button = tk.Button(self.dropdown_frame, text=button_text, fg='silver', font=('Arial', 12), bg='#484848', highlightthickness=0, bd=0, command=command)
                button.pack()
                self.buttons.append(button)

    def toggle_dropdown(self):
        if self.is_expanded:
            self.collapse_dropdown()
        else:
            self.expand_dropdown()

    def expand_dropdown(self):
        self.is_expanded = True
        self.dropdown_frame.grid(row=1, column=self.column, sticky="nsew")

    def collapse_dropdown(self):
        self.is_expanded = False
        self.dropdown_frame.grid_forget()