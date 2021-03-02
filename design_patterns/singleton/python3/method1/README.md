# Overview
- Decorator way to do singleton


https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


- Pros

Decorators are additive in a way that is often more intuitive than multiple inheritance.

- Cons

While objects created using MyClass() would be true singleton objects, MyClass itself is a a function, not a class, so you cannot call class methods from it. Also for