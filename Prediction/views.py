from django.http import HttpResponse
from django.shortcuts import render
import wikipedia
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from keras.models import Sequential
import keras
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from catboost import CatBoostClassifier, Pool


def Home(request):
    return render(request, 'Home.html')

def PredictCovid(request):
    return render(request, 'PredictCovid.html')

def DoctorBox(request):
    return render(request, 'DoctorBox.html')

def PredictDiabetes(request):
    return render(request, 'PredictDiabetes.html')

def PredictHeart(request):
    return render(request, 'PredictHeart.html')

def Home_Covid(request):
    return render(request, 'Home_Covid.html')

def result(request):
    df = pd.read_csv('C:/Users/MSI/Desktop/Projects/Python/DataSets/Covid Dataset.csv')
    X = df.iloc[:, 0:20].values
    Y = df.iloc[:, -1].values
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.25,random_state=0)

    def get_user_input():
        Breathing_Problem = float(request.GET['n1'])
        Fever = float(request.GET['n2'])
        Dry_Cough = float(request.GET['n3'])
        Sore_throat = float(request.GET['n4'])
        Running_Nose = float(request.GET['n5'])
        Asthma = float(request.GET['n6'])
        Chronic_Lung_Disease = float(request.GET['n7'])
        Headache = float(request.GET['n8'])
        Heart_Disease = float(request.GET['n9'])
        Diabetes = float(request.GET['n10'])
        Hyper_Tension = float(request.GET['n11'])
        Fatigue = float(request.GET['n12'])
        Gastrointestinal = float(request.GET['n13'])
        Abroad_travel = float(request.GET['n14'])
        Contact_with_COVID_Patient = float(request.GET['n15'])
        Attended_Large_Gathering = float(request.GET['n16'])
        Visited_Public_Exposed_Places = float(request.GET['n17'])
        Family_working_in_Public_Exposed_Places = float(request.GET['n18'])
        Wearing_Masks = float(request.GET['n19'])
        Sanitization_from_Market = float(request.GET['n20'])

        user_data = {
            'Breathing_Problem':Breathing_Problem,
            'Fever':Fever,
            'Dry_Cough':Dry_Cough,
            'Sore_throat':Sore_throat,
            'Running_Nose':Running_Nose,
            'Asthma':Asthma,
            'Chronic_Lung_Disease':Chronic_Lung_Disease,
            'Headache':Headache,
            'Heart_Disease':Heart_Disease,
            'Diabetes':Diabetes,
            'Hyper_Tension':Hyper_Tension,
            'Fatigue':Fatigue,
            'Gastrointestinal':Gastrointestinal,
            'Abroad_travel':Abroad_travel,
            'Contact_with_COVID_Patient':Contact_with_COVID_Patient,
            'Attended_Large_Gathering':Attended_Large_Gathering,
            'Visited_Public_Exposed_Places':Visited_Public_Exposed_Places,
            'Family_working_in_Public_Exposed_Places':Family_working_in_Public_Exposed_Places,
            'Wearing_Masks':Wearing_Masks,
            'Sanitization_from_Market':Sanitization_from_Market
            }

#Tranform data into dataframe

        features = pd.DataFrame(user_data, index = [0])
        return features

    #Store the user input into a variable
    user_input = get_user_input()




    #All five models are used in this program RandomForest/LogisticRegression/KNN/Gaussian/CatBoost

    #Create and train the model with Random Forest
    #RandomForestClassifier = RandomForestClassifier()
    #RandomForestClassifier.fit(X_train,Y_train)

    #Create and train the model with LogisticRegression
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X_train, Y_train)

    # instantiate the model with the best known parameters
    knn = KNeighborsClassifier(n_neighbors=15)
    knn.fit(X_train, Y_train)

    #Create and train the model with Gaussian Classifier 
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)

    #Create and train the model with CatBoost 
    catboost  = CatBoostClassifier(iterations=10,
    #     verbose=5,
    )
    catboost.fit(X_train, Y_train,)

    #RandomForest
    #score1 = accuracy_score(Y_test,RandomForestClassifier.predict(X_test))
    #LogisticRegession
    score2 = logisticRegr.score(X_test, Y_test)
    #KNN
    K = knn.predict(X_test)
    score3 = metrics.accuracy_score(Y_test,K)
    #Gaussin
    G = gnb.predict(X_test)
    score4 = metrics.accuracy_score(Y_test, G)

    #CatBoost
    C = catboost.predict(X_test)
    score5 = accuracy_score(Y_test, C)


    def Max(*T):
      max=0
      for n in T:
        if n>max:
            max=n
      return(max)

    Maxx = Max(score2,score3,score4,score5)



    #Store the model precition in a variable based on accruacy from each model 
    #if (Maxx == score1):
     #   prediction = RandomForestClassifier.predict(user_input)
        
    if (Maxx == score2):
        prediction = logisticRegr.predict(user_input)
        
    if (Maxx == score3):
        prediction = knn.predict(user_input)
        
    if (Maxx == score4):
        prediction = gnb.predict(user_input)
        
    if (Maxx == score5):
        prediction = catboost.predict(user_input)

    if(prediction):
    	result1 = ("you are most propably sick , We advice you to go as soon as possible to a doctor ")
    else:
	    result1 = ("You have no risk of having this disease , stay safe and take care")
		

    return render(request, 'ResultCovid.html', {"result2":result1})



def resultD(request):
    df = pd.read_csv('C:/Users/MSI/Desktop/Projects/Python/DataSets/diabetes-dataset.csv')
    X = df.iloc[:, 0:8].values
    Y = df.iloc[:,-1].values
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.25,random_state=0)

    def get_user_input():
        pregnancies = float(request.GET['n1'])
        glucose = float(request.GET['n2'])
        blood_Pressure = float(request.GET['n3'])
        skin_Thickness = float(request.GET['n4'])
        insulin = float(request.GET['n5'])
        BMI = float(request.GET['n6'])
        DBF = float(request.GET['n7'])
        age = float(request.GET['n8'])

        user_data = {
            'pregnancies':pregnancies,
            'glucose':glucose,
            'blood_Pressure':blood_Pressure,
            'skin_Thickness':skin_Thickness,
            'insulin':insulin,
            'BMI':BMI,
            'DBF':DBF,
            'age':age
            }

#Tranform data into dataframe

        features = pd.DataFrame(user_data, index = [0])
        return features

    #Store the user input into a variable
    user_input = get_user_input()




    #All five models are used in this program RandomForest/LogisticRegression/KNN/Gaussian/CatBoost

    #Create and train the model with Random Forest
    #RandomForestClassifier = RandomForestClassifier()
    #RandomForestClassifier.fit(X_train,Y_train)

    #Create and train the model with LogisticRegression
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X_train, Y_train)

    # instantiate the model with the best known parameters
    knn = KNeighborsClassifier(n_neighbors=15)
    knn.fit(X_train, Y_train)

    #Create and train the model with Gaussian Classifier 
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)

    #Create and train the model with CatBoost 
    catboost  = CatBoostClassifier(iterations=10,
    #     verbose=5,
    )
    catboost.fit(X_train, Y_train,)

    #RandomForest
    #score1 = accuracy_score(Y_test,RandomForestClassifier.predict(X_test))
    #LogisticRegession
    score2 = logisticRegr.score(X_test, Y_test)
    #KNN
    K = knn.predict(X_test)
    score3 = metrics.accuracy_score(Y_test,K)
    #Gaussin
    G = gnb.predict(X_test)
    score4 = metrics.accuracy_score(Y_test, G)

    #CatBoost
    C = catboost.predict(X_test)
    score5 = accuracy_score(Y_test, C)


    def Max(*T):
      max=0
      for n in T:
        if n>max:
            max=n
      return(max)

    Maxx = Max(score2,score3,score4,score5)



    #Store the model precition in a variable based on accruacy from each model 
    #if (Maxx == score1):
     #   prediction = RandomForestClassifier.predict(user_input)
        
    if (Maxx == score2):
        prediction = logisticRegr.predict(user_input)
        
    if (Maxx == score3):
        prediction = knn.predict(user_input)
        
    if (Maxx == score4):
        prediction = gnb.predict(user_input)
        
    if (Maxx == score5):
        prediction = catboost.predict(user_input)

    if(prediction):
    	result1 = ("you are most propably sick , We advice you to go as soon as possible to a doctor ")
    else:
	    result1 = ("You have no risk of having this disease , stay safe and take care")
		

    return render(request, 'ResultDiabetes.html', {"resultD2":result1})


def resultH(request):
    df = pd.read_csv('C:/Users/MSI/Desktop/Projects/Python/DataSets/heart_failure_clinical_records_dataset.csv')
    X = df.iloc[:, 0:11].values
    Y = df.iloc[:,-1].values
    X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.25,random_state=0)

    def get_user_input():
        age = float(request.GET['n1'])
        anaemia = float(request.GET['n2'])
        creatinine_phosphokinase = float(request.GET['n3'])
        diabetes = float(request.GET['n4'])
        ejection_fraction = float(request.GET['n5'])
        high_blood_pressure = float(request.GET['n6'])
        platelets = float(request.GET['n7'])
        serum_creatinine = float(request.GET['n8'])
        serum_sodium = float(request.GET['n9'])
        sex = float(request.GET['n10'])
        smoking = float(request.GET['n11'])

        user_data = {
            'age':age,
            'anaemia':anaemia,
            'creatinine_phosphokinase':creatinine_phosphokinase,
            'diabetes':diabetes,
            'ejection_fraction':ejection_fraction,
            'high_blood_pressure':high_blood_pressure,
            'platelets':platelets,
            'serum_creatinine':serum_creatinine,
            'serum_sodium':serum_sodium,
            'sex':sex,
            'smoking':smoking
            }

#Tranform data into dataframe

        features = pd.DataFrame(user_data, index = [0])
        return features

    #Store the user input into a variable
    user_input = get_user_input()




    #All five models are used in this program RandomForest/LogisticRegression/KNN/Gaussian/CatBoost

    #Create and train the model with Random Forest
    #RandomForestClassifier = RandomForestClassifier()
    #RandomForestClassifier.fit(X_train,Y_train)

    #Create and train the model with LogisticRegression
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X_train, Y_train)

    # instantiate the model with the best known parameters
    knn = KNeighborsClassifier(n_neighbors=15)
    knn.fit(X_train, Y_train)

    #Create and train the model with Gaussian Classifier 
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)

    #Create and train the model with CatBoost 
    catboost  = CatBoostClassifier(iterations=10,
    #     verbose=5,
    )
    catboost.fit(X_train, Y_train,)

    #RandomForest
    #score1 = accuracy_score(Y_test,RandomForestClassifier.predict(X_test))
    #LogisticRegession
    score2 = logisticRegr.score(X_test, Y_test)
    #KNN
    K = knn.predict(X_test)
    score3 = metrics.accuracy_score(Y_test,K)
    #Gaussin
    G = gnb.predict(X_test)
    score4 = metrics.accuracy_score(Y_test, G)

    #CatBoost
    C = catboost.predict(X_test)
    score5 = accuracy_score(Y_test, C)


    def Max(*T):
      max=0
      for n in T:
        if n>max:
            max=n
      return(max)

    Maxx = Max(score2,score3,score4,score5)



    #Store the model precition in a variable based on accruacy from each model 
    #if (Maxx == score1):
     #   prediction = RandomForestClassifier.predict(user_input)
        
    if (Maxx == score2):
        prediction = logisticRegr.predict(user_input)
        
    if (Maxx == score3):
        prediction = knn.predict(user_input)
        
    if (Maxx == score4):
        prediction = gnb.predict(user_input)
        
    if (Maxx == score5):
        prediction = catboost.predict(user_input)

    if(prediction):
    	result1 = ("you are most propably sick , We advice you to go as soon as possible to a doctor ")
    else:
	    result1 = ("You have no risk of having this disease , stay safe and take care")
		

    return render(request, 'ResultHeart.html', {"resultH2":result1})


def resultDB(request):
    search = str(request.GET['n1'])
    result1 = wikipedia.summary(search)
    return render(request, 'DoctorBoxResult.html', {"resultDB2":result1})