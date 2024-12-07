import pygame
# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Constants for zones
TILE_SIZE = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    def __init__(self, position):
        self.position = position
        self.color = RED
        self.size = (TILE_SIZE, TILE_SIZE)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

class GameMap:
    def __init__(self):
        self.zones = {
            'lobby': {
                'position': (350, 500),
                'color': GREEN,
                'size': (100, 100),
                'name': 'Starting Lobby'
            },
            'zone1': {
                'position': (200, 300),
                'color': BLUE,
                'size': (80, 80),
                'name': 'Zone 1 - Basic Math'
            },
            'zone2': {
                'position': (350, 300),
                'color': YELLOW,
                'size': (80, 80),
                'name': 'Zone 2 - Advanced Math'
            },
            'zone3': {
                'position': (500, 300),
                'color': RED,
                'size': (80, 80),
                'name': 'Zone 3 - Expert Math'
            },
            'final': {
                'position': (350, 100),
                'color': WHITE,
                'size': (120, 120),
                'name': 'Final Test'
            }
        }
        
    def draw(self, screen):
        # Draw connections between zones
        for zone in self.zones.values():
            pygame.draw.rect(screen, zone['color'], 
                           (zone['position'][0], zone['position'][1], 
                            zone['size'][0], zone['size'][1]))
            
        # Draw paths connecting zones
        pygame.draw.line(screen, WHITE, 
                        (self.zones['lobby']['position'][0] + 50, self.zones['lobby']['position'][1]),
                        (self.zones['zone2']['position'][0] + 40, self.zones['zone2']['position'][1] + 80), 3)
        
        # Connect zone1, zone2, zone3 to final
        for zone in ['zone1', 'zone2', 'zone3']:
            pygame.draw.line(screen, WHITE,
                           (self.zones[zone]['position'][0] + 40, self.zones[zone]['position'][1]),
                           (self.zones['final']['position'][0] + 60, self.zones['final']['position'][1] + 120), 3)
    

# Example usage:
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Math Challenge Map")
    clock = pygame.time.Clock()
    game_map = GameMap()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)  # Clear screen with black background
        game_map.draw(screen)  # Draw the game map
        pygame.display.flip()  # Update the display
        
    pygame.quit()

if __name__ == "__main__":
    main()
