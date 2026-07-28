def pizza(size, *toppings, **details):
    print(f"The size of pizza is {size} with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

    print(f"\nThe order has some details: ")
    for keys, values in details.items():
        print(f"- {keys}: {values}")


# pizza("large", "pineapple", "pepperoni", "olives", name="Krishna Kumar Mandal", destination="Biratnagar")


def human_details(name, *gfs, **exes):
    print(f"The person's name is: {name}\n")

    print(f"{name} has following gfs: ")
    for gf in gfs:
        print(f"- {gf}")

    print(f"\n{name} has following exes: ")
    for keys, values in exes.items():
        print(f"- {keys} : {values}")


human_details("Adolf Hitler", "Hawa", "Pani", "Aago", first="Plastic", second="Iphone", third="Homo Sapiens")
