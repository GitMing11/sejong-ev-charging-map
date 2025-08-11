import geopandas as gpd
import folium

# GeoJSON 파일 불러오기
geojson_path = 'hangjeongdong_세종특별자치시.geojson'
sejong_gdf = gpd.read_file(geojson_path)

# Folium 지도 객체 생성
m = folium.Map(location=[36.4808, 127.289], zoom_start=12)

# GeoDataFrame을 folium에 추가
folium.GeoJson(sejong_gdf).add_to(m)

# 지도 저장
m.save('sejong_map.html')

# 지도 보여주기
m
