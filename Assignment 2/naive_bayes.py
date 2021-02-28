#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
X = []
Y = []
dbTraining = []
dbTest = []
x_inputData =[]
y_inputdata =[]
dbTest = []
#reading the training data
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTraining.append (row)
    print(dbTraining)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
for line in dbTraining:
        line = line[1:-1]
        x_inputData.append(line)
for row in x_inputData:
    temp_row = []
    for value in row:
        if value == 'Sunny':
            temp_row.append(1) 
        elif value == 'Overcast':
            temp_row.append(2)
        elif value == 'Rain':
            temp_row.append(3)
        elif value == 'Hot':
            temp_row.append(1)
        elif value == 'Mild':
            temp_row.append(2)
        elif value == 'Cool':
            temp_row.append(3)
        elif value == 'High':
            temp_row.append(1)
        elif value == 'Normal':
            temp_row.append(2)
        elif value == 'Weak':
            temp_row.append(1)
        elif value == 'Strong':
            temp_row.append(2)
        else:
            continue
    X.append(temp_row)
print(X)   
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for line2 in dbTraining:
    line2 = line2[5:]
    y_inputdata.append(line2)
for row2 in y_inputdata:
    for value2 in row2:
        if value2 == 'Yes':
             Y.append(1) 
        elif value2 == 'No':
             Y.append(2)
        else:
            continue
print(Y)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append (row)
    print(dbTest)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]


