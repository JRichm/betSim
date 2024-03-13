import pygame

from sim import Simulation

class Window:
    def __init__(self, width, height, fps):

        # initialize pygame window
        pygame.init()
        # self.clock = pygame.time.Clock()

        # set window properties
        self.running = True
        self.height = height
        self.width = width
        self.fps = fps

        # open window
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("sim")

        # initialize pygame surfaces for drawing
        self.draw_surface = pygame.Surface((width, height))
        self.black_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.black_surface.fill((0, 0, 0))
        self.black_surface.set_alpha(25)

        # create simulation instance
        self.simulation = Simulation(self)


    def update(self):

        # update window and handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # clear screen
        self.screen.fill("Black")
        self.draw_surface.blit(self.black_surface, (0, 0))

        # update simulation and draw result
        self.simulation.update()
        self.screen.blit(self.draw_surface, (0, 0))

        # flip screen buffer
        pygame.display.flip()
        # self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()