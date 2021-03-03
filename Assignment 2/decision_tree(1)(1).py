#-------------------------------------------------------------------------
# AUTHOR: David Brown
# FILENAME: Decision Tree
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: 10 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dbTraining = []
x_inputData =[]
y_inputdata =[]
dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    X = []
    Y = []
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0:#skipping the header
                 dbTraining.append (row)
                
print(len(dbTraining))
    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
age = {
    "Young": 1,
    "Presbyopic": 2,
    "Prepresbyopic": 3,
}

spectacle = {
    "Myope": 1,
    "Hypermetrope": 2,
}

astigmatism = {
    "Yes": 1,
    "No": 2,
}

tear = {
    "Normal": 1,
    "Reduced": 2,
}

for data in dbTraining:
    X.append([age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]])
print('X:',X)
print('X size:',len(X))

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
lenses = {
    "Yes": 1,
    "No": 2,
}

for data in dbTraining:
    Y.append(lenses[data[4]])

print('Y:',Y)
print('Y size:',len(Y))
all_accuracy = []
    #loop your training and test tasks 10 times here
for i in range (10):
    True_label =[]
    
    #fitting the decision tree to the data setting max_depth=3
    clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
    clf = clf.fit(X, Y)
         #read the test data and add this data to dbTest
        #--> add your Python code here
    dbTest = []
    test_prediction = []
    with open('contact_lens_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:#skipping the header
                dbTest.append (row)
    age = {
        "Young": 1,
        "Presbyopic": 2,
        "Prepresbyopic": 3,
    }

    spectacle = {
        "Myope": 1,
        "Hypermetrope": 2,
    }

    astigmatism = {
        "Yes": 1,
        "No": 2,
    }

    tear = {
        "Normal": 1,
        "Reduced": 2,
    }
for data in dbTest:
    test_prediction.append([age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]])  
         
            #print(test_prediction)
    class_predicted = clf.predict(test_prediction)
    
    print(class_predicted)
    #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
    #--> add your Python code here
    lenses = {
        "Yes": 1,
        "No": 2,
    }
    for data in dbTest:
        True_label.append(lenses[data[4]])
    
    print( 'True label',True_label)
    correct_predictions = 0
    print('class predicted: ', class_predicted)
    print('True Label: ',True_label )
    for (i,j) in zip(class_predicted, True_label):
        if i == j:
            correct_predictions += 1
        else:
            continue
        print(correct_predictions)
        Accuracy = correct_predictions/len(True_label)
        print('Accuracy: ',Accuracy)
        all_accuracy.append(Accuracy)
        print(all_accuracy)
        print('Size: ', len(all_accuracy))
        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
final_accuracy_DS1 = []
final_accuracy_DS2 = []
final_accuracy_DS3 = []

final_accuracy_DS1 = all_accuracy[:8]
#print(len(final_accuracy_DS1))
final_accuracy_DS2 = all_accuracy[8:20]
#print(len(final_accuracy_DS2))
final_accuracy_DS3 = all_accuracy[20:]
#print(len(final_accuracy_DS3))


    

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:
         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here

print('final accuracy when training on contact_lens_training_1.csv: ',min(final_accuracy_DS1))
print('final accuracy when training on contact_lens_training_2.csv: ',min(final_accuracy_DS2))
print('final accuracy when training on contact_lens_training_3.csv: ',min(final_accuracy_DS3))




