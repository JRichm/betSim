import pygame
import math
import random

class Bird:
    def __init__(self, position, direction, window_instance):
        self.position = position
        self.direction = direction
        self.window =  window_instance
        self.speed = 3

        self.x_border_enter_angle = None
        self.y_border_enter_angle = None

        self.sprite = pygame.Surface((3, 3))

        rValue = random.randint(0, 255)
        gValue = random.randint(0, 255)
        bValue = random.randint(0, 255)

        self.sprite.fill((rValue, gValue, bValue))

    def update(self, all_birds, avg_position, avg_direction):
        self.move_bird(all_birds, avg_position, avg_direction)

        self.window.draw_surface.blit(self.sprite, self.position)

    
    def move_bird(self, all_birds, avg_position, avg_direction):
        separation_force = self.calculate_separation_force(all_birds)
        cohesion_force = self.calculate_cohesion_force(avg_position)
        alignment_force = self.calculate_alignment_force(avg_direction)

        steering_force = [
            separation_force[0] + 0.5 * cohesion_force[0] + 0.1 * alignment_force[0],
            separation_force[1] + 0.5 * cohesion_force[1] + 0.1 * alignment_force[1]
        ]

        self.direction[0] += steering_force[0]
        self.direction[1] += steering_force[1]

        
        magnitude = math.sqrt(self.direction[0]**2 + self.direction[1]**2)
        if magnitude > 0:
            self.direction[0] /= magnitude
            self.direction[1] /= magnitude

        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed

        if self.position[0] < self.window.simulation.border_size or self.position[0] > self.window.width - self.window.simulation.border_size:
            self.direction[0] = -self.direction[0]

        if self.position[1] < self.window.simulation.border_size or self.position[1] > self.window.height - self.window.simulation.border_size:
            self.direction[1] = -self.direction[1]

    def calculate_separation_force(self, all_birds):
        separation_radius = 20
        separation_strength = 0.8

        separation_vector = [0, 0]

        for other_bird in all_birds:
            if other_bird != self:
                distance = math.sqrt((self.position[0] - other_bird.position[0])**2 + (self.position[1] - other_bird.position[1])**2)

                if distance < separation_radius:
                    separation_force = [(self.position[0] - other_bird.position[0]) / distance,
                                        (self.position[1] - other_bird.position[1]) / distance]
                    
                    separation_force[0] *= separation_strength / distance
                    separation_force[1] *= separation_strength / distance

                    separation_vector[0] += separation_force[0]
                    separation_vector[1] += separation_force[1]

        return separation_vector
    
    def calculate_cohesion_force(self, avg_position):
        cohesion_vector = [avg_position[0] - self.position[0], avg_position[1] - self.position[1]]

        distance = math.sqrt(cohesion_vector[0]**2 + cohesion_vector[1]**2)
        cohesion_strength = 0.05
        cohesion_force = [cohesion_vector[0] * cohesion_strength / distance,
                          cohesion_vector[1] * cohesion_strength / distance]

        return cohesion_force
    

    def calculate_alignment_force(self, avg_direction):
        alignment_force = [avg_direction[0] - self.direction[0], avg_direction[1] - self.direction[1]]

        magnitude = math.sqrt(alignment_force[0]**2 + alignment_force[1]**2)
        alignment_strength = 0.15
        alignment_force = [alignment_force[0] * alignment_strength / magnitude,
                           alignment_force[1] * alignment_strength / magnitude]
        
        return alignment_force