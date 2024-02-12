#CS175
#David Thomas
#restaurant


class Restaurant:
    def __init__(self, name, vegetarian, vegan, gluten_free):
        self.name = name
        self.vegetarian = vegetarian
        self.vegan = vegan
        self.gluten_free = gluten_free

restaurants = [
    Restaurant("Joe's Gourmet Burgers", False, False, False),
    Restaurant("Main Street Pizza Company", True, False, True),
    Restaurant("Corner Café", True, True, True),
    Restaurant("Mama's Fine Italian", True, False, False),
    Restaurant("The Chef's Kitchen", True, True, True)
]

def filter_restaurants(vegetarian, vegan, gluten_free):
    available_restaurants = []
    for restaurant in restaurants:
        if (not vegetarian or restaurant.vegetarian) and \
           (not vegan or restaurant.vegan) and \
           (not gluten_free or restaurant.gluten_free):
            available_restaurants.append(restaurant.name)
    return available_restaurants

def main():
    vegetarian_input = input("Is anyone vegetarian? (yes/no): ").lower()
    vegan_input = input("Is anyone vegan? (yes/no): ").lower()
    gluten_free_input = input("Is anyone gluten-free? (yes/no): ").lower()

    vegetarian = vegetarian_input == "yes"
    vegan = vegan_input == "yes"
    gluten_free = gluten_free_input == "yes"

    available_restaurants = filter_restaurants(vegetarian, vegan, gluten_free)

    print("Restaurants available:")
    for restaurant in available_restaurants:
        print(restaurant)

if __name__ == "__main__":
    main()
