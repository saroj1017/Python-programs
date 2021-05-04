student_dict = {
  "student": ['saroj', 'bikas' , 'charan'],
  "score" : [98, 54, 75]
}

# normal looping through dict
for (key,value) in student_dict.items():
  print(value)
  
  
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

for (key,value) in student_data_frame.items():
  print(key)
  # print each columns individually so not very helpfull so we use the other method in pandas
  
#itterrows

for (index,row) in student_data_frame.itterrows():
  print(row) # pandas series object
  print(row.student)
  print(row.score)
  
  if row.student == 'saroj':
    print(row.score)
  
