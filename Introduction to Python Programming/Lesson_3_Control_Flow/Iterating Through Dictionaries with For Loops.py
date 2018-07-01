# You would like to count the number of fruits in your basket. In order to do this,
# you have the following dictionary and list of fruits. Use the dictionary and list
# to count the total number of fruits, but you do not want to count the other items
# in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary

# if the key is in the list of fruits, add the value (number of fruits) to result
for element in basket_items:
    if element in fruits:
        result += basket_items[element]

print(result)

# for fruit, count in basket_items.items():
#   if fruit in fruits:
#       result += count

# print("There are {} fruits in the basket.".format(result))

# Try the loop for each of the dictionaries below to make sure it always works.
    # Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for element in basket_items:
    if element in fruits:
        result += basket_items[element]

print(result)

# Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for element in basket_items:
    if element in fruits:
        result += basket_items[element]

print(result)

# Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for element in basket_items:
    if element in fruits:
        result += basket_items[element]

print(result)

# Use the dictionary and list to count the total number of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
# if the key is in the list of fruits, add to fruit_count.
# if the key is not in the list, then add to the not_fruit_count

for element in basket_items:
    if element in fruits:
        fruit_count += basket_items[element]
    else:
        not_fruit_count += basket_items[element]

print(fruit_count, not_fruit_count)

# for fruit, count in basket_items.items():
#    if fruit in fruits:
#       fruit_count += count
#    else:
#        not_fruit_count += count

# print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))
