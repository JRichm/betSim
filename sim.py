import random
import math

from bird import Bird

class Simulation:
    def __init__(self, window_instance):
        self.window = window_instance
        self.border_size = 50
        self.num_birds = 200
        self.sim_birds = []

        self.spawn_birds()

    def update(self):
        self.update_birds()

    def spawn_birds(self):
        for bird in range(self.num_birds):
            rand_x_pos = random.randint(self.border_size, self.window.width - self.border_size)
            rand_y_pos = random.randint(self.border_size, self.window.height - self.border_size)

            rand_angle = random.uniform(0, 2*math.pi)
            rand_x_dir = math.cos(rand_angle)
            rand_y_dir = math.sin(rand_angle)

            new_bird = Bird([rand_x_pos, rand_y_pos], [rand_x_dir, rand_y_dir], self.window)
            self.sim_birds.append(new_bird)

    def update_birds(self):
        avg_position = self.calculate_avg_position()
        avg_direction = self.calculate_avg_direction()

        for bird in self.sim_birds:
            bird.update(self.sim_birds, avg_position, avg_direction)

    def calculate_avg_position(self):
        avg_x = 0
        avg_y = 0

        for bird in self.sim_birds:
            avg_x += bird.position[0]
            avg_y += bird.position[1]

        avg_x /= self.num_birds
        avg_y /= self.num_birds

        return [avg_x, avg_y]
    
    def calculate_avg_direction(self):
        avg_x = 0
        avg_y = 0

        for bird in self.sim_birds:
            avg_x += bird.direction[0]
            avg_y += bird.direction[1]

        avg_x /= self.num_birds
        avg_y /= self.num_birds

        return [avg_x, avg_y]