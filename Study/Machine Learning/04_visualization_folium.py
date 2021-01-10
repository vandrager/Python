import folium, os
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start= 12)
seoul_map.save("seoul.html")