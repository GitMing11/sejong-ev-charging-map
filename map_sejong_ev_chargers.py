import geopandas as gpd
import folium
import pandas as pd

# GeoJSON 파일 불러오기
geojson_path = 'hangjeongdong_세종특별자치시.geojson'
sejong_gdf = gpd.read_file(geojson_path)

# Folium 지도 객체 생성
m = folium.Map(location=[36.4808, 127.289], zoom_start=12)

# GeoDataFrame을 folium에 추가
folium.GeoJson(sejong_gdf).add_to(m)

# 엑셀 파일 경로
excel_path = '20240516_with_coordinates2.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(excel_path)

# DataFrame의 각 위치에 마커 추가
for index, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['charging_station']}<br>{row['address']}",
        tooltip=row['charging_station']
    ).add_to(m)

# 지도 저장
m.save('sejong_charging_stations_map.html')

# 지도 보여주기
m
