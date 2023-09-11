"""
Looping through a dataframe and iterting

"""

import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}
"""
for (key, value) in student_dict.items():
    print(key, value)

"""

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)


#Looping through dataframe
for(index, row) in student_data_frame.iterrows():
    print(row.student)
