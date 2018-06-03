import os
import sys
import urllib.request
import Client
import Reduce_URL
import json

client_id = Client.client_id
client_secret = Client.client_secret

def Search_Blog(*args):
    display_ = "&display=" + str(args[1])  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(args[2])  # 검색 순
    encText = urllib.parse.quote(args[0])
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


def Search_Cafe(*args):
    display_ = "&display=" + str(args[1])  # 20개 찾음
    start_ = "&start=1"  # 첫번째 부터
    sort_ = "&sort=" + str(args[2])  # 검색 순
    encText = urllib.parse.quote(args[0])
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


def Search_All(*args):
    f = json.loads(Search_Blog(args[0],args[1],args[2]))
    for item in f["items"]:
        print(item["title"])

    f = json.loads(Search_Cafe(args[0],args[1],args[2]))
    for item in f["items"]:
        print(item["title"])


#링크 뽑아내기
#f = json.loads(Search_Blog("신림역 코다차야"))
#for item in f["items"]:
#    item["link"].replace("?Redirect=Log&amp;logNo=", "/")

Search_number = 10   # 검색 개수 설정
data_sort = "sim"   # 최신순 or 정확도순

Search_All("신림역 맛집",Search_number,data_sort)
