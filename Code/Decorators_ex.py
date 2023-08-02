def response_to_mailman(func):
    def wrapper():
        print("A mailman is comming!!")
        func()
    return wrapper


@response_to_mailman
def bark():
    print("Woolf")


@response_to_mailman
def cat_response():
    print("Cat Crying")


bark()
cat_response()
