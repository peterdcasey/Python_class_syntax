from class_examples import Examples


def main():
    print("hello from main")
    x = Examples(99)
    y = Examples(-1)
    print(f"x: {str(x)}")
    print(f"y: {str(y)}")
    Examples.shared = 33
    z = Examples(345)
    del z
    print(f"y: {str(y)}")
    print(f"x: {str(x)}")
    x.static_method()
    x.class_method()
    print(f"x: {str(x)}")




if __name__ == '__main__':
    main()