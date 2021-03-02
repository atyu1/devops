from observer import Observer

class Story:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f'{{title: {self.title}, content: {self.content}}}'


class StoryModel:
    #StoryModel is now Singleton
    _instance = None

    @staticmethod
    def get_instance():
        if StoryModel._instance is None:
            StoryModel()
        return StoryModel._instance

    def __init__(self):
        if StoryModel._instance is not None:
            raise Exception('Object instance exists, cannot create new one in Singelton')
        else:
            self.__stories = []
            self.__observers = []
            StoryModel._instance = self

    def add(self, story):
        self.__stories.append(story)
        self.notify()

    def remove(self, story):
        self.__stories.remove(story)
        self.notify() 
    
    def get(self):
        return self.__stories

    def notify(self):
        for observer in self.__observers:
            observer.update()

    def subscribe(self, observer):
        if isinstance(observer, Observer):
            self.__observers.append(observer)
        else:
            raise Exception(f'{observer} does not inherit interface Observer')