class SceneManager:
    def __init__(self, input_handler):
        from scenes.menu import MenuScene
        self.current_scene = MenuScene(self, input_handler)
        self.input_handler = input_handler
        self.input_handler.attach(self.current_scene)
    
    def handle_events(self):
        self.current_scene.handle_events()

    def update(self, dt):
        self.current_scene.update(dt)

    def draw(self, screen):
        self.current_scene.draw(screen)

    def change_scene(self, new_scene):
        self.input_handler.detach(self.current_scene)
        self.input_handler.attach(new_scene)
        self.current_scene = new_scene
