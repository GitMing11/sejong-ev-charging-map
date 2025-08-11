import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import re

# CSV 파일 경로 설정
file_path = 'unique_addresses.csv'

# CSV 파일 불러오기
df = pd.read_csv(file_path)

# 정규표현식 패턴 설정: 괄호 이후의 문자열 제거
pattern = r'\(.+?\)'
df['address'] = df['address'].apply(lambda x: re.sub(pattern, '', x))

# Geopy를 사용하여 주소를 좌표로 변환
geolocator = Nominatim(user_agent="my_app")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# 주소를 위도와 경도로 변환하여 새로운 DataFrame 생성
coords = df['address'].apply(geocode).dropna().apply(lambda loc: (loc.latitude, loc.longitude))
coords_df = pd.DataFrame(coords.tolist(), columns=['latitude', 'longitude'])

# Folium을 사용하여 지도 생성
if not coords_df.empty:
    map_center = coords_df.mean().values.tolist()
    mymap = folium.Map(location=map_center, zoom_start=13)

    # 각 좌표에 대해 마커와 800m 반경을 표시
    for address, (lat, lon) in zip(df['address'], coords_df.values):

        folium.Circle(
            location=[lat, lon],
            radius=800,  # 800 meters
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(mymap)

    # 지도 저장
    mymap.save('map6.html')
    print("지도를 'map6.html' 파일로 저장했습니다.")
else:
    print("주소를 지오코딩하는데 실패했습니다. 유효한 주소가 있는지 확인하세요.")