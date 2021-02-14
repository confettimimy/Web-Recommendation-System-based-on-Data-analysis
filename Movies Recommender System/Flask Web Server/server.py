'''-*- coding: utf-8 -*-'''
# 플라스크 패키지 가져오기
from flask import Flask, render_template, request
import base64


import collaborative_filtering


# model폴더의 natural.py -> 자연어처리 모듈
import natural_processing







app = Flask(__name__)

# 메인 페이지
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받는다.
        user = request.form['user'] # 기존고객 로그인 아이디 입력받음
        user = str(user)






        ls = collaborative_filtering.collaborative_filtering_weighting(user)
        # ls에는 [기존고객에게 추천하는 영화 콘텐츠 목록 리스트] , [신규고객에게 추천하는 영화 콘텐츠 목록 리스트]가 담겨올 것이다.
        
        a = ls[0]
        b = ls[1]



        

        
        i=0
        for i in range(len(a)):
            a[i] = a[i]+'.jpg'


        

        j=0
        for j in range(len(b)):
            b[j] = b[j]+'.jpg'

            
        return render_template('index.html', image_file=a, image_file2=b, user_id = user)




# 줄거리 기반 추천 알고리즘
# 새 html에 띄우기
@app.route('/new', methods=['GET', 'POST']) 
def new():
        movie = 'Up'
        movie = str(movie)


        c = natural_processing.national(movie)

        k=0
        for k in range(len(c)):
            c[k] = c[k]+'.jpg'
        
        
        return render_template('new_frame.html', image_file3 = c)

@app.route('/2', methods=['GET', 'POST']) 
def new2():
        movie = 'The Martian'
        movie = str(movie)


        d = natural_processing.national(movie)

        k=0
        for k in range(len(d)):
            d[k] = d[k]+'.jpg'
        
        
        return render_template('new_frame2.html', image_file4 = d)



        
if __name__ == '__main__':
    app.run(debug = True)
