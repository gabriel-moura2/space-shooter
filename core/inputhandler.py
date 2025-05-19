import pygame

class InputHandler:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def handle_events(self):
        for event in pygame.event.get():
            for observer in self.observers:
                observer.handle_event(event)
    
    def handle_keys(self):
        pressed_keys = pygame.key.get_pressed()
        for observer in self.observers:
            observer.handle_keys(pressed_keys)