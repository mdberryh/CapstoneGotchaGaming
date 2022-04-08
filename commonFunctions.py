import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from google_play_scraper import app, Sort, reviews_all, permissions

import pickle


def getReviewsDf():
    mypath = 'sentReviews/'

    from os import listdir, path
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    reviews_df = None
    for app_id in onlyfiles:

        temp_df = None
        if path.exists(mypath + app_id):
            temp_df = pd.read_pickle(mypath + app_id, compression='gzip')

        if temp_df is None:
            continue
        if reviews_df is None:
            reviews_df = temp_df
        else:
            reviews_df = pd.concat([reviews_df,temp_df], axis=0, ignore_index=True)
    return reviews_df
