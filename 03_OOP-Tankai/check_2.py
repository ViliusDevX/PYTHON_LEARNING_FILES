import pyglet

# Create a window
window = pyglet.window.Window(800, 600)

# Create a rectangle shape
rectangle = pyglet.shapes.Rectangle(x=100, y=100, width=100, height=100, color=(255, 0, 0))

@window.event
def on_draw():
    window.clear()
    rectangle.draw()

# Start the Pyglet main event loop
pyglet.app.run()
