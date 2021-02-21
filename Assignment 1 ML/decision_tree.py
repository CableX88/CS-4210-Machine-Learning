#-------------------------------------------------------------------------
# AUTHOR: David Brown
# FILENAME: decision_tree
# SPECIFICATION:This program will create a decision tree out of our data in contact lense.csv
# FOR: CS 4200- Assignment #1
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays
#importing some Python libraries

from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []
x_inputData =[]
y_inputdata =[]
#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)

#transfor the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
#print(db)

for line in db:
    line = line[:-1]
    x_inputData.append(line)
for row in x_inputData:
    temp_row = []
    for value in row:
        if value == 'Young':
             temp_row.append(1) 
        elif value == 'Prepresbyopic':
             temp_row.append(2)
        elif value == 'Presbyopic':
             temp_row.append(3)
        elif value == 'Myope':
             temp_row.append(1)
        elif value == 'Hypermetrope':
             temp_row.append(2)
        elif value == 'No':
             temp_row.append(2)
        elif value == 'Yes':
             temp_row.append(1)
        elif value == 'Reduced':
             temp_row.append(1)
        elif value == 'Normal':
             temp_row.append(2)
        else:
            continue
    X.append(temp_row)
print(X)


#transfor the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for line2 in db:
    line2 = line2[4:]
    y_inputdata.append(line2)
print(y_inputdata)
for row2 in y_inputdata:
    for value2 in row2:
        if value2 == 'Yes':
             Y.append(1) 
        elif value2 == 'No':
             Y.append(2)
        else:
            continue
print(Y)
#fiiting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


