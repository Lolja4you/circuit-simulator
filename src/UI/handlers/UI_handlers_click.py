def handle_click(event, node):
    for component in node:
        if component.contains(event.x, event.y) and event.num == 1 : # and not component.selected
            component.select()
            component.draw()
        elif component.contains(event.x, event.y) and event.num == 3:
            print('mem')
            component.select()
            component.draw()
            component.change_features()

        else:
            component.deselect()
            component.draw()
