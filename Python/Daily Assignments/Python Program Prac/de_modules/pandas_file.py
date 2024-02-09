# reading entire file
import pandas as pd
import numpy as np

data = pd.read_csv("de_modules\Salary_Data.csv")
print(data)

# reading column names

print(data.columns)

salary_col = data.Salary
print(salary_col)





# Creating Dictionary 
dict = { 
    'series': ['Friends', 'Money Heist', 'Marvel'], 
    'episodes': [200, 50, 45], 
    'actors': [' David Crane', 'Alvaro', 'Stan Lee'] 
} 

# Creating Dataframe 
df = pd.DataFrame(dict) 
print(df)



data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
print(myvar.loc[1]) # loc will find and return the specified row from the data frame
 
myvar = pd.DataFrame(data,index = ['a','b','c'])

print(myvar)

NaN = np.nan
dataframe = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
                                   'Vimal', 'Sourabh',
                                   'Rahul', 'Shobhit'],
                          'Physics': [11, 12, 13, 14, NaN, 11],
                          'Chemistry': [10, 14, NaN, 18, 20, 10],
                          'Math': [13, 10, 15, NaN, NaN, 13]})
 
 
print(dataframe.count())
print(dataframe.isnull().sum())
 
# it will give the total null
# values present in our dataframe
print("Total Null values count: ",
      dataframe.isnull().sum().sum())

# Creating dataframe using dictionary
NaN = np.nan
dataframe = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
                                  'Vimal', 'Sourabh',
                                  'Rahul', 'Shobhit'],
                         'Physics': [11, 12, 13, 14, NaN, 11],
                         'Chemistry': [10, 14, NaN, 18, 20, 10],
                         'Math': [13, 10, 15, NaN, NaN, 13]})
 
print("Created Dataframe")
print(dataframe)
 
# finding Count of all columns
print("Count of all values wrt columns")
print(dataframe.count())
 
# Count according to rows
print("Count of all values wrt rows")
print(dataframe.count(axis=1))
print(dataframe.count(axis='columns'))
 
# count of null values
print("Null Values counts ")
print(dataframe.isnull().sum())
print("Total null values",
     dataframe.isnull().sum().sum())
 
# count of student with greater
# than 11 marks in physics
print("Count of students with physics marks greater than 11 is->",
     dataframe[dataframe['Physics'] > 11]['Name'].count())
 
# resultant of above dataframe
print(dataframe[dataframe['Physics'] > 11])
print("Count of students ->",
     dataframe[(dataframe['Physics'] > 10) &
               (dataframe['Chemistry'] > 11) &
               (dataframe['Math'] > 9)]['Name'].count())
 
print(dataframe[(dataframe['Physics'] > 10) &
               (dataframe['Chemistry'] > 11) &
               (dataframe['Math'] > 9)])