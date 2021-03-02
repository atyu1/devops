from AdminController import AdminController
from observer import Observer

class AdminView(Observer):
    def __init__(self, model):
        self.stories = []
        self.model = model
        self.controller = AdminController(self)

    def add_story(self, story):
        title = story['title']
        content = story['content']
        self.controller.add_story(title, content)

    def remove_story(self, title):
        self.controller.remove_story(title)

    def list_stories(self):
        print(f'stories: {self.stories}')

    def update(self):
        # triggered by publisher
        self.stories = self.model.get()
        print('Admin state synced!')