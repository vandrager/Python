import folium, os
import pandas as pd
import json
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start= 12)

#tiles 지도 스타일 변경가능
seoul_map2 = folium.Map(location=[37.55, 126.98], tiles= 'stamen terrain', zoom_start= 12)
seoul_map3 = folium.Map(location=[37.55, 126.98], tiles= 'stamen toner', zoom_start= 15)

seoul_map.save("seoul.html")
seoul_map2.save("seoul2.html")
seoul_map3.save("seoul3.html")

#지도에 마커 표시하기
df = pd.read_excel("서울지역 대학교 위치.xlsx")
print(df.columns)
df.rename(columns={'Unnamed: 0': "학교명"}, inplace = True)
df.set_index("학교명", inplace = True)
print(df)
seoul_map = folium.Map(location=[37.55, 126.98], tiles= 'stamen terrain', zoom_start= 12)
for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup= name).add_to(seoul_map)

seoul_map.save("seoul_univ.html")

#지도에 원형 마커 표시하기
for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=10,
                        color='brown',
                        fill = True,
                        fill_color = 'blue',
                        fill_opacity = 0.5,
                        popup= name
                        ).add_to(seoul_map)

seoul_map.save("seoul_univ2.html")

#지도영역에 단계구분도 표시하기
file_path = "경기도인구데이터.xlsx"
df = pd.read_excel(file_path, index_col="구분")
df.columns = df.columns.map(int)
geo_path = "경기도행정구역경계.json"
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

g_map = folium.Map(location=[37.5502, 126.982],
                    tiles= 'stamen terrain',
                    zoom_start= 9)

folium.Choropleth(geo_data=geo_data, #지도 경계
                    data=df[2007], #표시하려는 데이터
                    columns= [df.index, df[2007]], #열 지정
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                    threshold_scale = [10000, 100000, 300000, 500000, 700000],
                    key_on="feature.properties.name",
                    ).add_to(g_map)

g_map.save("2007gyeonggido.html")