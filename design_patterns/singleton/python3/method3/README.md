# Overview
- metaclass way
- example only for Python3
- from https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


In general, it makes sense to use a metaclass to implement a singleton. A singleton is special because is created only once, and a metaclass is the way you customize the creation of a class. Using a metaclass gives you more control in case you need to customize the singleton class definitions in other ways.

Your singletons won't need multiple inheritance (because the metaclass is not a base class), but for subclasses of the created class that use multiple inheritance, you need to make sure the singleton class is the first / leftmost one with a metaclass that redefines __call__ This is very unlikely to be an issue. The instance dict is not in the instance's namespace so it won't accidentally overwrite it.