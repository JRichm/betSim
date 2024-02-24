from window import Window
from sim import Simulation

screen_width = 800
screen_height = 600
fps = 60

window = Window(screen_width, screen_height, fps)

simulation = Simulation(window)

while window.running:
    window.update()
    simulation.update()

window.quit()