# Sejong EV Charging Map
세종특별자치시의 전기자동차 충전소 위치 데이터를 기반으로,  
주소를 정제하고 지오코딩하여 Folium을 활용해 인터랙티브 지도 위에 시각화한 프로젝트입니다.

## 주요 기능
- 충전소 주소 정제 및 중복 제거
- 지오코딩(주소 → 위도/경도) 처리
- GeoJSON 기반 행정경계 지도 표시
- Folium을 이용한 지도 시각화 및 마커/반경 표시
- 지도 HTML 파일로 저장

## 사용된 기술
- Python (Pandas, GeoPandas, Folium, Geopy)
- Excel/CSV/GeoJSON 데이터 처리
- HTML 지도 시각화
