import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def national(movie_name):

    df_meta = pd.read_csv("movie_natlang.csv")

    db = df_meta[["title", "natlang"]]

   
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(db['natlang'])

    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    
    title = movie_name
    title2index = pd.Series(data=db.index, index= db['title']).drop_duplicates()
    index = title2index[title]
    
    sim_scores = list(enumerate(cosine_sim[index]))
    
    sim_scores.sort(key=lambda x: x[1], reverse=True)
    top10 = sim_scores[1:11]
    top10_index = [x[0] for x in top10]
    # print("<<Result>>")
    # print(top10_index)
    # print(db['title'].iloc[top10_index] , "\n\n영화내용:\n" , db['natlang'].iloc[top10_index])
        
        
                    
                # book = int(input("관심있는 책의 번호를 적어주세요: "))

                # print("\n [제목]:", db['title'].loc[book],"\n\n","[설명]:",db['natlang'].loc[book])

    return list(df_meta['movie_id'].iloc[top10_index]) 
        
