# A function that takes a dictionary and returns the value of the "count" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]


vehicles = [
    {"name": "car", "count": 7},
    {"name": "plane", "count": 10},
    {"name": "boat", "count": 2},
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'count': 10}, {'name': 'car', 'count': 7}, {'name': 'boat', 'count': 2}]
