import pygame

from sim import Simulation

class Window:
    def __init__(self, width, height, fps):
        pygame.init()
        # self.clock = pygame.time.Clock()

        self.running = True
        self.height = height
        self.width = width
        self.fps = fps

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("sim")

        self.draw_surface = pygame.Surface((width, height))
        self.black_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.black_surface.fill((0, 0, 0))
        self.black_surface.set_alpha(1)

        self.simulation = Simulation(self)


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill("Black")
        self.draw_surface.blit(self.black_surface, (0, 0))

        self.simulation.update()
        self.screen.blit(self.draw_surface, (0, 0))

        pygame.display.flip()
        # self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()