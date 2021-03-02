from StoryModel import Story, StoryModel

class AdminController:
    def __init__(self, view):
        self.view = view
        self.model = StoryModel.get_instance()

    def add_story(self, title, content):
        story = Story(title, content)
        self.model.add(story)

    def remove_story(self, title):
        self.model.remove(title)