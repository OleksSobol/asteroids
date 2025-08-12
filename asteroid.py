import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # spawn 2 new asteroids with new random directions
            random_angle = random.uniform(20,  50)
            new_asteroid1_velocity = self.velocity.rotate(random_angle)
            new_asteroid2_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid_obj1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_obj2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_obj1.velocity = new_asteroid1_velocity * 1.2
            new_asteroid_obj2.velocity = new_asteroid2_velocity * 1.2
        