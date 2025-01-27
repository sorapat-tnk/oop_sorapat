import requests

API_Key ="W9si6tefeK9wH0rWcVl4feGWqvNaV2xjXnTnKXbK"

cam = input("ใส่ชื่อกล้องที่ต้องการดูภาพที่ต้องการดู(กล้องที่มี(FHAZ:RHAZ:MAST:CHEMCAM)) :  ")

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera={cam}&api_key={API_Key}'
#https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=FHAZ&api_key=W9si6tefeK9wH0rWcVl4feGWqvNaV2xjXnTnKXbK


result = requests.api.get(url).json()

id = result['photos'][0]['camera']['rover_id']
full_name = result['photos'][0]['camera']['full_name']
status = result['photos'][0]['rover']['status']
landing_date = result['photos'][0]['rover']['landing_date']
launch_date = result['photos'][0]['rover']['launch_date']
img_src = result['photos'][0]['img_src']


print(f"ไอดีกล้อง{id}")
print(f"ชื่อกล้อง{full_name}")
print(f"สถานะกล้อง{status}")
print(f"วันที่ลงจอด{landing_date}")
print(f"วันที่ปล่อยจากโลก{launch_date}")
print(f"urlกล้อง{img_src}")