"""write a List Comprehension to create a new list called squared_numbers. 
This new list should contain every number in the list numbers but each number should be squared."""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]

print(squared_numbers)


"""write a List Comprehension to create a new list called result.
This new list should only contain the even numbers from the list numbers"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num%2==0]

print(result)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}


print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)




