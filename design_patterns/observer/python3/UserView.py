from observer import Observer

class UserView(Observer):
    def __init__(self, model):
        self.stories = []
        self.model = model

    def read_story(self, title):
        for story in self.stories:
            if story.title == title:
                print(story.content)
                break

    def list_stories(self):
        print(self.stories)

    def update(self):
        self.stories = self.model.get()
        print('User state sunced!')