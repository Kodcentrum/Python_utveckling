import pygame


class SwedishKeyMapper:
    def __init__(self, key_state):
        self.key_state = key_state
        self.key_mapping = {
           "vänsterpil": self.key_state[pygame.K_LEFT],
           "högerpil": self.key_state[pygame.K_RIGHT],
           "nedåtpil": self.key_state[pygame.K_DOWN],
           "uppåtpil": self.key_state[pygame.K_UP]
        }

    def på(self, key):
        key_press = self.key_mapping.get(key)
        if key_press:
            return key_press
