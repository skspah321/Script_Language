import os
import sys
import urllib.request
import Client
import json
import glob
import Tk_GetImage

client_id = Client.client_id
client_secret = Client.client_secret


def Search_Blog(word,Search_number,data_sort):
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
        f = json.loads(response_body)
        return f

    else:
        pass
        #print("Error Code:" + rescode)


def Search_Cafe(word,Search_number,data_sort):
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
        f = json.loads(response_body)
        return f

    else:
        pass
        #print("Error Code:" + rescode)


def Search_All(word,Search_number,data_sort):
    f1 = Search_Blog(word,Search_number,data_sort)
    f2 = Search_Cafe(word,Search_number,data_sort)

    return f1,f2

def Search_Image(word,Search_number,data_sort):
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
        #print(response_body.decode('utf-8'))
        f = json.loads(response_body)
        return f

    else:
        print("Error Code:" + rescode)

def Search_Map(word,Search_number,data_sort):
    display_ = "&display=" + str(Search_number)  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(data_sort)  # 검색 순
    encText = urllib.parse.quote(word)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText + display_ + start_ + sort_  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        f = json.loads(response_body)
        return f

    else:
        pass

def Search_Map2():
    encText = urllib.parse.quote("서울특별시 관악구 신림동 1433-63")
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
    else:
        pass
        #print("Error Code:" + rescode)
