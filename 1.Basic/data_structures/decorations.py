def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("\nSprinkles added !🎊")
        func(*args, **kwargs)
    return wrapper


def random_words(func_name):
    def wrapper_name(*args, **kwargs):
        print("yo wassup !")
        func_name(*args, **kwargs)
    return wrapper_name


@add_sprinkles
def get_ice_creams(flavor):
    print(f"Here is your {flavor} flavor of ice cream ! 🍦\n")


@random_words
def calling_random_words(names):
    print(f"Calling random Words {names}!\n")


get_ice_creams("Chocolate")
calling_random_words(["krishna", "monkey", "Luffy"])
