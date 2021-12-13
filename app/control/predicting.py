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


def predicting(music, hastag, follower, love_count):
    root_path = app.root_path
    path_name = 'control/analysis_file/data_tiktok 05122021.csv'


    trainData = pd.read_csv(os.path.join(root_path, path_name))
    print(trainData.head(4))

    LE_h = pickle.load(open(os.path.join(root_path,'control/analysis_file/label_hastag.txt'),"rb"))
    LE_m = pickle.load(open(os.path.join(root_path,'control/analysis_file/label_music.txt'),"rb"))
    random_forest = pickle.load(open(os.path.join(root_path,'control/analysis_file/model_random_forest.txt'),"rb"))

    dataframeTiktok = pd.DataFrame([[music,hastag,follower,love_count]],
                                   columns=['music', 'hastag_data','author_follower', 'author_heart'])


    dataframeTiktok['music'] = LE_m.transform(['Lazada 1212 Meriah'])
    dataframeTiktok['hastag_data'] = LE_h.transform(['lazada1212meriah'])
    print(dataframeTiktok)
    Y_prediction = random_forest.predict(dataframeTiktok.values)
    print(Y_prediction)

    return Y_prediction[0]

