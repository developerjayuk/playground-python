class ClassTest:
    # instance methods are used for most things
    def instace_method(self):
        print("instance method called", self)

    # used often as factories
    @classmethod
    def class_method(cls):
        print("class method called", cls)
        cls.hello(cls)

    # used when you want to do something that doesn't need access to the class or instance
    # not used often, but can be useful for utility functions
    @staticmethod
    def static_method():
        print("static method called")

    def hello(self):
        print("Hello from instance method")


test = ClassTest()
test.instace_method()
ClassTest.class_method()
ClassTest.static_method()
