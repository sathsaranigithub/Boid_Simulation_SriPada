
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
NUM_AGENTS = 100
SEPARATION_RADIUS = 25
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 100
MAX_SPEED = 2
MAX_FORCE = 0.05

class Boid:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.random.rand(2) * 2 - 1  # Random velocity
        self.acceleration = np.zeros(2)

    def apply_force(self, force):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.velocity = self.limit(self.velocity, MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0  # Reset acceleration after applying

    def limit(self, vector, max_value):
        magnitude = np.linalg.norm(vector)
        if magnitude > max_value:
            vector = vector / magnitude * max_value
        return vector

    def edges(self):
        if self.position[0] > WIDTH:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = WIDTH
        if self.position[1] > HEIGHT:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = HEIGHT

    def flock(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohere(boids)
        separation = self.separate(boids)

        self.apply_force(alignment)
        self.apply_force(cohesion)
        self.apply_force(separation)

    def align(self, boids):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            if np.linalg.norm(self.position - boid.position) < ALIGNMENT_RADIUS:
                steering += boid.velocity
                total += 1
        if total > 0:
            steering /= total
            steering = self.limit(steering, MAX_SPEED)
            steering -= self.velocity
            steering = self.limit(steering, MAX_FORCE)
        return steering

    def cohere(self, boids):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            if np.linalg.norm(self.position - boid.position) < COHESION_RADIUS:
                steering += boid.position
                total += 1
        if total > 0:
            steering /= total
            steering -= self.position
            steering = self.limit(steering, MAX_SPEED)
            steering -= self.velocity
            steering = self.limit(steering, MAX_FORCE)
        return steering

    def separate(self, boids):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if distance < SEPARATION_RADIUS and distance > 0:
                diff = self.position - boid.position
                diff /= distance
                steering += diff
                total += 1
        if total > 0:
            steering /= total
        if np.linalg.norm(steering) > 0:
            steering = self.limit(steering, MAX_SPEED)
            steering -= self.velocity
            steering = self.limit(steering, MAX_FORCE)
        return steering

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    boids = [Boid(np.random.rand() * WIDTH, np.random.rand() * HEIGHT) for _ in range(NUM_AGENTS)]

    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for boid in boids:
            boid.flock(boids)
            boid.update()
            boid.edges()

            pygame.draw.circle(screen, (0, 0, 0), boid.position.astype(int), 3)

        pygame.display.flip()
        clock.tick(60)  # Set the framerate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    run_simulation()
