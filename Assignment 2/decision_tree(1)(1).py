#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    x_inputData =[]
    y_inputdata =[]
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)
    print(dbTraining)
    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
for line in dbTraining:
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
#print(X)   

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
for line2 in dbTraining:
    line2 = line2[4:]
    y_inputdata.append(line2)
for row2 in y_inputdata:
    for value2 in row2:
        if value2 == 'Yes':
             Y.append(1) 
        elif value2 == 'No':
             Y.append(2)
        else:
            continue
#print(Y)
Lowest_accuracy = []
    #loop your training and test tasks 10 times here
for i in range (10):
    #fitting the decision tree to the data setting max_depth=3
    clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
    clf = clf.fit(X, Y)
       #read the test data and add this data to dbTest
       #--> add your Python code here
    dbTest = []
    with open('contact_lens_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTest.append (row)
        #print(dbTest)

        test_prediction = []
        for data in dbTest:
            testData = []
            #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            data = data[:-1]
            testData.append(data)
            for row3 in testData:
                temp_row3 = []
                for value3 in row3:
                    if value3 == 'Young':
                        temp_row3.append(1) 
                    elif value3 == 'Prepresbyopic':
                        temp_row3.append(2)
                    elif value3 == 'Presbyopic':
                        temp_row3.append(3)
                    elif value3 == 'Myope':
                        temp_row3.append(1)
                    elif value3 == 'Hypermetrope':
                        temp_row3.append(2)
                    elif value3 == 'No':
                        temp_row3.append(2)
                    elif value3 == 'Yes':
                        temp_row3.append(1)
                    elif value3 == 'Reduced':
                        temp_row3.append(1)
                    elif value3 == 'Normal':
                        temp_row3.append(2)
                    else:
                        continue
            test_prediction.append(temp_row3)
                
            #print(test_prediction)
            class_predicted = clf.predict(test_prediction)
    
            print(class_predicted)
               #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
               #--> add your Python code here
        label_input = []
        true_label = []
        for line3 in dbTest:
            line3 = line3[4:]
            label_input.append(line3)
        print(label_input)
        for row4 in label_input:
            for v in row4:
                if v == 'Yes':
                     true_label.append(1) 
                elif v == 'No':
                     true_label.append(2)
                else:
                    continue
        print(true_label)
        correct_predictions = 0
        print('class predicted: ', class_predicted)
        print('True Label: ',true_label )
        for (i,j) in zip(class_predicted, true_label):
            if i == j:
                correct_predictions += 1
            else:
                continue
        #print(correct_predictions)
        Accuracy = correct_predictions/len(true_label)
        print(Accuracy)
        Lowest_accuracy.append(Accuracy)
        print(Lowest_accuracy)
        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
    

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:
         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here




