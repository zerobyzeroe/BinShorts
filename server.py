from flask import Flask
import requests
# url = 'http://newsapi.org/v2/top-headlines?country=in&category=business&apikey=c3adf6e89d0a4a2ea355b6aecab7e398&page=5&pageSize=20'
# app=Flask(__name__)
# @app.route('/members')
def members():
    url='https://newsapi.org/v2/top-headlines?country=us&apiKey=c3adf6e89d0a4a2ea355b6aecab7e398'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        print(articles[0])
        # for article in articles:
        #     title = article['title']
        #     author = article['author']
        #     print(f"Title: {title}")
        #     print(f"Author: {author}")
        #     print("----")
    else:
        print(f"Failed to fetch news: {response.status_code} - {response.text}")
    

members()

# if __name__=="__main__":
#     app.run(debug=True)
# https://newsapi.org/v2/top-headlines?country=us&apiKey=c3adf6e89d0a4a2ea355b6aecab7e398&page=5&pageSize=20