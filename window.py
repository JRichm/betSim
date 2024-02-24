import pygame

class Window:
    def __init__(self, width, height, fps):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.running = True
        self.height = height
        self.width = width
        self.fps = fps

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("sim")


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        pygame.display.flip()
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()