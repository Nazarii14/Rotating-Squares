from drawer import *

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    drawer = Drawer(screen, 2)
    drawer.run()
