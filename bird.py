import pygame
import math
import random

class Bird:
    def __init__(self, position, direction, window_instance):

        # initialize bird variables
        self.position = position
        self.direction = direction
        self.window =  window_instance
        self.speed = 2
        
        self.self.separation_radius = 20

        self.separation_strength = 0.8
        self.cohesion_strength = 0.01
        alignment_strength = 0.05

        self.sprite = pygame.Surface((3, 3))

        # set color of bird
        self.sprite.fill((255, 255, 255))

        # rValue = random.randint(0, 255)
        # gValue = random.randint(0, 255)
        # bValue = random.randint(0, 255)
        # self.sprite.fill((rValue, gValue, bValue))

    def update(self, all_birds, avg_position, avg_direction):

        # move and draw bird on screen
        self.move_bird(all_birds, avg_position, avg_direction)
        self.window.draw_surface.blit(self.sprite, self.position)

    
    def move_bird(self, all_birds, avg_position, avg_direction):

        ## use boids algorithm to calculate birds next move

        # steer to avoid crowding and collision with other birds
        separation_force = self.calculate_separation_force(all_birds)

        # steer towards the average heading of other birds
        cohesion_force = self.calculate_cohesion_force(avg_position)

        # steer towards the center mass of all birds
        alignment_force = self.calculate_alignment_force(avg_direction)

        # apply steering force
        steering_force = [
            separation_force[0] + 0.5 * cohesion_force[0] + 0.1 * alignment_force[0],
            separation_force[1] + 0.5 * cohesion_force[1] + 0.1 * alignment_force[1]
        ]

        # update birds direction
        self.direction[0] += steering_force[0]
        self.direction[1] += steering_force[1]

        # clamp birds velocity
        magnitude = math.sqrt(self.direction[0]**2 + self.direction[1]**2)
        if magnitude > 0:
            self.direction[0] /= magnitude
            self.direction[1] /= magnitude

        # set birds new position
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed

        # check if bird collides with border
        # fix bug related to birds getting stuck to border
        if self.position[0] < self.window.simulation.border_size or self.position[0] > self.window.width - self.window.simulation.border_size:
            self.direction[0] = -self.direction[0]

        if self.position[1] < self.window.simulation.border_size or self.position[1] > self.window.height - self.window.simulation.border_size:
            self.direction[1] = -self.direction[1]

    def calculate_separation_force(self, all_birds):

        # initialize separation vector
        separation_vector = [0, 0]

        # calculate separation force using positions of all other birds
        for other_bird in all_birds:
            if other_bird != self:

                # get distance to other bird
                distance = math.sqrt((self.position[0] - other_bird.position[0])**2 + (self.position[1] - other_bird.position[1])**2)

                # only update separation vector if other bird is within separation radius
                if distance < self.separation_radius:

                    # add separation force based on other birds distance and separation strength
                    separation_force = [(self.position[0] - other_bird.position[0]) / distance,
                                        (self.position[1] - other_bird.position[1]) / distance]
                    
                    separation_force[0] *= self.separation_strength / distance
                    separation_force[1] *= self.separation_strength / distance

                    # update separation vector
                    separation_vector[0] += separation_force[0]
                    separation_vector[1] += separation_force[1]

        return separation_vector
    
    def calculate_cohesion_force(self, avg_position):

        # calculate cohesion vector
        cohesion_vector = [avg_position[0] - self.position[0], avg_position[1] - self.position[1]]

        # get distance from center mass
        distance = math.sqrt(cohesion_vector[0]**2 + cohesion_vector[1]**2)

        # calculate cohesion force based on distance and cohesion strength
        cohesion_force = [cohesion_vector[0] * self.cohesion_strength / distance,
                          cohesion_vector[1] * self.cohesion_strength / distance]

        return cohesion_force
    

    def calculate_alignment_force(self, avg_direction):

        # calculate alignment force
        alignment_force = [avg_direction[0] - self.direction[0], avg_direction[1] - self.direction[1]]

        # calculate magnitude of direction vector
        magnitude = math.sqrt(alignment_force[0]**2 + alignment_force[1]**2)

        # calculate alignment force based on magnitude and alignment strength
        alignment_force = [alignment_force[0] * self.alignment_strength / magnitude,
                           alignment_force[1] * self.alignment_strength / magnitude]
        
        return alignment_force