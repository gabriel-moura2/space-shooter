class SceneManager:
    def __init__(self):
        from scenes.menu import MenuScene
        self.current_scene = MenuScene(self)
    
    def handle_events(self):
        self.current_scene.handle_events()

    def update(self):
        self.current_scene.update()

    def draw(self, screen):
        self.current_scene.draw(screen)

    def change_scene(self, new_scene):
        self.current_scene = new_scene
