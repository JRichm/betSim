from window import Window
from sim import Simulation

screen_width = 1800
screen_height = 980
fps = 60

window = Window(screen_width, screen_height, fps)

while window.running:
    window.update()

window.quit()