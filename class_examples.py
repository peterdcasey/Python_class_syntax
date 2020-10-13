
class Examples:
    __shared = 1  # class variable, similar to Java static

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"shared is {Examples.__shared}, self.value is {self.value}"

    # Example using 'this' rather than 'self'
    # noinspection PyMethodParameters
    def __del__(this):
        """ Destructor example """
        print(f"{this.__class__.__name__} object with value {this.value} is about to be destroyed")

    @classmethod
    def class_method(cls):
        """
          Similar to Java static method, access to class variable not instance
        :return:
        """
        class_variables = cls.__dict__
        print(f"{cls.__name__} class method, class variable is {cls.__shared}")
        print(f"{cls.__name__} has attributes: {class_variables}")
        cls.__shared = 333

    @staticmethod
    def static_method():
        """
          A normal function scoped to the class
        :return:
        """
        print("static method, no instance or class access")
