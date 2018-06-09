import os
import sys
import urllib.request
import Client
import json

client_id = Client.client_id
client_secret = Client.client_secret

Search_number = 10   # 검색 개수 설정
data_sort = "sim"   # 최신순 or 정확도순

def Search_Blog(word):
    display_ = "&display=" + str(Search_number)  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(data_sort)  # 검색 순
    encText = urllib.parse.quote(word)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + display_ + start_ + sort_  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()


    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        return response_body

    else:
        print("Error Code:" + rescode)


def Search_Cafe(word):
    display_ = "&display=" + str(Search_number)  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(data_sort)  # 검색 순
    encText = urllib.parse.quote(word)
    url = "https://openapi.naver.com/v1/search/cafearticle.json?query=" + encText + display_ + start_ + sort_  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        return response_body

    else:
        print("Error Code:" + rescode)


def Search_All(word):
    f = json.loads(Search_Blog(word))
    for item in f["items"]:
        print(item["title"])

    f = json.loads(Search_Cafe(word))
    for item in f["items"]:
        print(item["title"])

def Searh_Image(word):
    display_ = "&display=" + str(Search_number)  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(data_sort)  # 검색 순
    encText = urllib.parse.quote(word)
    url = "https://openapi.naver.com/v1/search/image?query=" + encText + display_ + start_ + sort_  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        return response_body

    else:
        print("Error Code:" + rescode)


#링크 뽑아내기
#f = json.loads(Search_Blog("신림역 코다차야"))
#for item in f["items"]:
#    item["link"].replace("?Redirect=Log&amp;logNo=", "/")


#Search_All("한강진역 맛집",Search_number,data_sort)
Searh_Image("한강진역 맛집")
