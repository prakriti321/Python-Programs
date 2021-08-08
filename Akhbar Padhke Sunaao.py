# Akhbar Padhke Sunao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=3199a08fe55a4f0eb77a92cb0103ae3a"
    news=requests.get(url=url)
    news_page=news.json() #returns json encoded response of a request
    article=news_page['articles']

    result=[]
    for ar in article:
        result.append(ar['title'])

    for i in range(len(result)):
        print(i+1," : ",result[i])

    speak(result)
