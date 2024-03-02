from window import Window
from sim import Simulation

screen_width = 1280
screen_height = 720
fps = 60

window = Window(screen_width, screen_height, fps)

while window.running:
    window.update()

window.quit()