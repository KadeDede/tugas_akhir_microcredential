from app import app
import os
import pandas as pd
import pickle

def get_music():
    root_path = app.root_path
    path_name = 'control/analysis_file/data_tiktok 05122021.csv'


    trainData = pd.read_csv(os.path.join(root_path, path_name))


    data_music = []
    data_hastag = []

    for data in trainData['music'].unique():
        data_music.append(data)
    for data in trainData['hastag_data'].unique():
        data_hastag.append(data)
    return {
        'music':data_music,
        'hastag':data_hastag
    }
