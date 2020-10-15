from class_examples import Examples

"""
    Small example using class syntax...
    ....
"""


def main():
    print("hello from main!")
    x = Examples(99)
    y = Examples(-1)
    print(f"x: {str(x)}")
    print(f"y: {str(y)}")
    x.class_method()
    x.new_field = 0
    print(f"x: {x}, x.new_field: {x.new_field}")
    # print(f"y: {y}, x.new_field: {y.new_field}")
    Examples.shared = 33  # Not access the class variable __shared, what?????
    print(f"Examples.shared is: {Examples.shared}")
    print(f"x now has a class field 'shared': {x.shared}")
    z = Examples(345)
    del z
    print(f"y: {str(y)}")
    print(f"x: {str(x)}")
    x.static_method()
    x.class_method()
    print(f"x: {str(x)}")


if __name__ == '__main__':
    main()
