def draw_source_icon(canvas):
    canvas.create_polygon(0, 0, 30, 0, 15, 30, fill="red")

def draw_node_icon(canvas):
    canvas.create_oval(0, 0, 30, 30, fill="blue")

def draw_resistor_icon(canvas):
    canvas.create_rectangle(0, 10, 30, 20, fill="green")

def draw_capacitor_icon(canvas):
    canvas.create_arc(0, 0, 30, 30, start=0, extent=180, fill="yellow")

def draw_inductor_icon(canvas):
    canvas.create_line(0, 15, 30, 15, fill="purple")
    canvas.create_arc(0, 0, 30, 30, start=0, extent=180, fill="white")

def draw_voltmeter_icon(canvas):
    canvas.create_rectangle(5, 0, 25, 30, fill="orange")
    canvas.create_line(15, 0, 15, 30, fill="black")

def draw_ammeter_icon(canvas):
    canvas.create_rectangle(0, 5, 30, 25, fill="pink")
    canvas.create_line(0, 15, 30, 15, fill="black")