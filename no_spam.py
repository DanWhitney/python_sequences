menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# reverse removal
#
# for index1, dish in enumerate(menu):
#     mumberOfItemsInDish = len(dish)
#     print(dish)
#     for index2, item in enumerate(reversed(dish)):
#         if item == "spam":
#             positionToDelete = (mumberOfItemsInDish - 1) - index2
#             print(positionToDelete)
#             del menu[index1][positionToDelete]
#
# print(menu)


for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

