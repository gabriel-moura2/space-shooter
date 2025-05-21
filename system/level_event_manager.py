class LevelEventManager:
    def __init__(self):
        self.observers = {}
    
    def attach(self, event_type, observer):
        self.observers[event_type].append(observer)
    
    def detach(self, event_type, observer):
        self.observers[event_type].remove(observer)

    def notify(self, event_type, event):
        for observer in self.observers[event_type]:
            observer.handle_event(event)