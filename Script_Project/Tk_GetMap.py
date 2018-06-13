import Client
import Enter_Webbrowser

def Open_Map(mapx,mapy,num):
    i = int(num)
    url = 'https://openapi.naver.com/v1/map/staticmap.bin?clientId='+Client.client_id+'&url=http://www.naver.com&crs=NHN:128&center='+mapx[i]+','+mapy[i]+'&level=14&w=800&h=800&baselayer=default&markers='+mapx[i]+','+mapy[i]
    Enter_Webbrowser.Open_Webbrowser(url)


