import pyglet as p
from pyglet.window import mouse

window = p.window.Window()

label = p.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button, modifiers)
    if button == mouse.LEFT:
        print("The left mouse button was pressed.")

p.app.run()