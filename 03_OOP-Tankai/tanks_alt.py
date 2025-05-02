import pyglet
import threading

# Create a window
window = pyglet.window.Window(800, 600)

# Create a thread for game logic
def game_logic_thread():
    while True:
        # Your game logic here
        pass
rectangle = pyglet.shapes.Rectangle(x=100, y=100, width=100, height=100, color=(255, 0, 0))

@window.event
def render_thread():
    while not window.has_exit:
        window.clear()
        rectangle.draw()
        window.flip()

# Create and start game logic and render threads
# logic_thread = threading.Thread(target=game_logic_thread)
# render_thread = threading.Thread(target=render_thread)
#
# logic_thread.start()
# render_thread.start()
render_thread()
# Start the Pyglet main event loop
pyglet.app.run()
