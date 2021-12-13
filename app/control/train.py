from app import app
from sklearn.preprocessing import LabelEncoder
import os
import pandas as pd
import pickle
#Metrics
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report

# Import Library Confussion Matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report


from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score

#Model Select
from sklearn.model_selection import KFold,train_test_split,cross_val_score

# Import Library Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

# from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def training():
    root_path = app.root_path
    path_name = 'control/analysis_file/data_tiktok 05122021.csv'
    path_vektor = 'control/model_file/vector_data_tfidf.txt'

    trainData = pd.read_csv(os.path.join(root_path, path_name))
    print(trainData.head(4))
    # s = (trainData.dtypes == 'object')
    # object_cols = list(s[s].index)
    # LE = LabelEncoder()
    # for i in object_cols:
    #     trainData[i] = trainData[[i]].apply(LE.fit_transform)
    LE_h = LabelEncoder()
    LE_m = LabelEncoder()
    trainData['music'] = LE_m.fit_transform(trainData['music'])
    trainData['hastag_data'] = LE_h.fit_transform(trainData['hastag_data'])
    # trainData = trainData.apply(LE.fit_transform)
    print(trainData)
    X = trainData.iloc[:, 1:5].values
    y = trainData.iloc[:, 5].values
    print(X)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(x_train, y_train)
    Y_prediction = random_forest.predict(x_test)
    accuracy_rf = round(accuracy_score(y_test, Y_prediction) * 100, 2)
    acc_random_forest = round(random_forest.score(x_train, y_train) * 100, 2)

    accuracy = accuracy_score(y_test, Y_prediction)
    precision = precision_score(y_test, Y_prediction, average='micro')
    recall = recall_score(y_test, Y_prediction, average='micro')
    f1 = f1_score(y_test, Y_prediction, average='micro')

    print('accuracy_random_Forest : %.3f' % accuracy)
    print('precision_random_Forest : %.3f' % precision)
    print('recall_random_Forest : %.3f' % recall)
    print('f1-score_random_Forest : %.3f' % f1)


    pickle.dump(LE_h, open(os.path.join(root_path, 'control/model_file/label_hastag.txt'), "wb"))
    pickle.dump(LE_m, open(os.path.join(root_path, 'control/model_file/label_music.txt'), "wb"))
    pickle.dump(random_forest, open(os.path.join(root_path, 'control/model_file/model_random_forest.txt'), "wb"))




    return "success"

