# has 알고리즘 라이브러리
import pandas
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
#import pylab as pl #이 모듈에 대한 에러 때문에 잠시 주석처리
import math as mt
import time
import random
import Recommenders4 as Recommenders



def collaborative_filtering_weighting(user):
    
    # has
    ratings_metadata_file = 'has_movie.csv'
    ratings_df =  pd.read_csv(ratings_metadata_file)

        
    # has 알고리즘
    # Read rating movies  metadata
    # Cluster 0, 3 (40대)에 가중치 2.5 부여
    ratings_df['rating'].where((ratings_df['movieId']!='I-1020') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1022') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1019') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1021') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1016') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1010') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1048') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1012') | (ratings_df['ClusteringID']!=0)&(ratings_df['ClusteringID']!=3),ratings_df['rating']+2.5)

    # Cluster 1, 2 (20대)에 가중치 2.5 부여
    ratings_df['rating'].where((ratings_df['movieId']!='I-1048') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1052') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1068') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1078') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1057') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1077') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1045') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1093') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1069') | (ratings_df['ClusteringID']!=1)&(ratings_df['ClusteringID']!=2),ratings_df['rating']+2.5)

    # Cluster 4 (30대)에 가중치 2.5 부여
    ratings_df['rating'].where((ratings_df['movieId']!='I-1077') | (ratings_df['ClusteringID']!=4),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1069') | (ratings_df['ClusteringID']!=4),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1058') | (ratings_df['ClusteringID']!=4),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1057') | (ratings_df['ClusteringID']!=4),ratings_df['rating']+2.5)
    ratings_df['rating'].where((ratings_df['movieId']!='I-1078') | (ratings_df['ClusteringID']!=4),ratings_df['rating']+2.5)


    ### users
    users = ratings_df['userId'].unique()

    user_id = user

    is_model = Recommenders.item_similarity_recommender_py()
    is_model.create(ratings_df, 'userId', 'movieId')

    recom1 = is_model.recommend(user_id)
    a = list(recom1['movie'])





    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # userh = request.form['userh'] # 신규고객 로그인 아이디 입력받음
    # userh = str(userh)
    user_id2 = users[2]

    is_model2 = Recommenders.item_similarity_recommender_py()
    is_model2.create(ratings_df, 'userId', 'movieId')

    recom2 = is_model2.recommend(user_id2)
    b = list(recom2['movie'])



    send = [] # 리턴값으로 보낼 리스트
    send.append(a)
    send.append(b)



    return send




