# Overview 
- base class method
- from: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

---
- Pros

It's a true class

- Cons

Multiple inheritance - eugh! __new__ could be overwritten during inheritance from a second base class? One has to think more than is necessary.