'''
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: 156, 178, 165, 171, 187

Example Output
171
'''

class My_Ambiguity_Error(Exception):
    pass

student_heights = input("Input a list of student heights: ").split()

try:
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
        if(student_heights[n]<=0):
            raise My_Ambiguity_Error
except ValueError:
    print("INVALID TYPE.PLEASE CHECK AND TRY AGAIN.\n   One or more of the input heights is of invalid type.\n   Expected type: <class 'int'>")
    exit()

except My_Ambiguity_Error:
    print("INVALID INTEGER VALUE FOR HEIGHT.CHECK AND TRY AGAIN.\n  One or more of the input heights is invalid value. (Zero or Less)")
    exit()


total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = total_height / number_of_students
average_height = round( average_height )
print(f"Average height is = {average_height} ")

