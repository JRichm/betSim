import random
import math

from bird import Bird

class Simulation:
    def __init__(self, window_instance):

        # initialize simulation variables
        self.window = window_instance
        self.border_size = 30
        self.num_birds = 150
        self.sim_birds = []

        # spawn birds
        self.spawn_birds()

    def update(self):
        self.update_birds()

    def spawn_birds(self):
        for bird in range(self.num_birds):

            # set new birds position to random point on screen within bounds
            rand_x_pos = random.randint(self.border_size, self.window.width - self.border_size)
            rand_y_pos = random.randint(self.border_size, self.window.height - self.border_size)

            # set new birds direction to random angle
            rand_angle = random.uniform(0, 2*math.pi)
            rand_x_dir = math.cos(rand_angle)
            rand_y_dir = math.sin(rand_angle)

            # spawn bird
            new_bird = Bird([rand_x_pos, rand_y_pos], [rand_x_dir, rand_y_dir], self.window)
            self.sim_birds.append(new_bird)

    def update_birds(self):

        # calculate average position and direction of all birds
        avg_position = self.calculate_avg_position()
        avg_direction = self.calculate_avg_direction()

        # update each bird individually 
        for bird in self.sim_birds:
            bird.update(self.sim_birds, avg_position, avg_direction)

    def calculate_avg_position(self):

        # initialize position variables
        avg_x = 0
        avg_y = 0

        # add up all positional variables 
        for bird in self.sim_birds:
            avg_x += bird.position[0]
            avg_y += bird.position[1]

        # find and return average
        avg_x /= self.num_birds
        avg_y /= self.num_birds

        return [avg_x, avg_y]
    
    def calculate_avg_direction(self):

        # initialize direction variables
        avg_x = 0
        avg_y = 0

        # add up all directional variables 
        for bird in self.sim_birds:
            avg_x += bird.direction[0]
            avg_y += bird.direction[1]

        # find and return average
        avg_x /= self.num_birds
        avg_y /= self.num_birds

        return [avg_x, avg_y]