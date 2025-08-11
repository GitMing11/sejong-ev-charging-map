import pandas as pd
from geopy.geocoders import Nominatim

# 엑셀 파일 경로 설정
file_path = '세종20240516.xlsx'

# 엑셀 파일 불러오기
df = pd.read_excel(file_path, engine='openpyxl')

# 중복 제거를 위해 drop_duplicates() 메서드 사용
unique_addresses = df['address'].drop_duplicates()

# 중복 제거된 주소 개수 출력
unique_address_count = unique_addresses.shape[0]
print(f"중복을 제외한 주소 개수: {unique_address_count}")

# 중복 제거된 주소 출력
for address in unique_addresses:
    print(address)

# 중복 제외한 주소를 CSV 파일로 저장
unique_addresses.to_csv('unique_addresses.csv', index=False, header=True)

print("중복을 제외한 주소를 'unique_addresses.csv' 파일로 저장했습니다.")

