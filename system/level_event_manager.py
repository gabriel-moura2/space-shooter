class LevelEventManager:
    def __init__(self, level_scene):
        self.level_scene = level_scene

    def notify(self, event_type, event):
        getattr(self.level_scene, f"on_{event_type}")(event)