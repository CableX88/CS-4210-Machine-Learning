#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
X = []
Y = []
x_inputData =[]
y_inputdata =[]
inner_test = []
testSample_unclean = []
testSample = []
True_label_unclean = []
True_label = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):


    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here
    # X =
    
    instance = instance[:-1]
    x_inputData.append(instance)
    for row in x_inputData:
        temp_row = []
    for value in row:
        temp_row.append(int(value))
    X.append(temp_row)
del X[-1]
print(X)

    

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    # Y =
for line2 in db:
    line2 = line2[2:]
    y_inputdata.append(line2)
for row2 in y_inputdata:
    for value2 in row2:
        if value2 == '-':
             Y.append(1) 
        elif value2 == '+':
             Y.append(2)
        else:
            continue
Y = Y[:-1]
print(Y)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
for j in db:
    inner_test.append(j)
for k in j:
    testSample_unclean.append(k)
    
temp_sample = []
temp_label = testSample_unclean
True_label_unclean = temp_label[2:]
testSample_unclean = testSample_unclean[:-1]
#print(True_label_unclean)
#print(testSample_unclean)
for val in testSample_unclean:
    temp_sample.append(int(val))
testSample.append(temp_sample)
#print(temp_sample)
print(testSample)
    



    #fitting the knn to the data
clf = KNeighborsClassifier(n_neighbors=1, p=2)
clf = clf.fit(X, Y)


    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
class_predicted = clf.predict(testSample)
print(class_predicted)
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
print(True_label_unclean)
for p in True_label_unclean:
    if p == '-':
        True_label.append(1) 
    elif p == '+':
        True_label.append(2)
    else:
        continue

incorrect_predictions = 0
#print(True_label)    
for (a,b) in zip(class_predicted, True_label):
    if a != b:
        incorrect_predictions += 1
    else:
        continue
print(incorrect_predictions)
error_rate = incorrect_predictions/len(class_predicted)
#print the error rate
#--> add your Python code here
print('Error Rate: ',error_rate )






