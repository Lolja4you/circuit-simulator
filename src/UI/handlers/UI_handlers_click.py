def handle_click(event, node):
    for component in node:
        if component.contains(event.x, event.y): # and not component.selected
            component.select()
            component.draw()

        else:
            component.deselect()
            component.draw()
