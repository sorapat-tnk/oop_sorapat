import requests

API_Key ="oxOpKsvmI5WfXkJCSqOcjXf6AxzYJQAwHrCuWAgu"
date = input("ใส่ละติจูด (ตัวอย่าง ละติจูดของจังหวัดนครศรีธรรมราช : ละติจูด (Latitude): ประมาณ 8.4304)")

url = f'https://api.nasa.gov/planetary/apod?date={date}api_key=oxOpKsvmI5WfXkJCSqOcjXf6AxzYJQAwHrCuWAgu'
#ลองใส่
#http://api.openweathermap.org/data/2.5/air_pollution?lat=8.4304&lon=99.9631&appid=3a088efa39cad1105ca569846ce3da4b

result = requests.api.get(url).json()

#ใส่ค่า
latti = result['lat']
longi = result['lon']
co = result['co']
no = result['no']
no2 = result['no2']
o3 = result['o3']
so2 = result['so2']
pm2_5 = result['pm2_5']
pm10 = result['pm10']
nh3 = result['nh3']

print(f"ค่าละติจูด{lat} ลองจิจูด{lon}")
print(f"คาร์บอนมอนอกไซด์ {co} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"ไนโตรเจนมอนอกไซด์ {no} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"ไนโตรเจนไดออกไซด์ {no2} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"โอโซน {o3} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"ซัลเฟอร์ไดออกไซด์ {so2} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"ฝุ่นละอองขนาดเล็กกว่า 2.5 ไมครอน {pm2_5} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"ฝุ่นละอองขนาดเล็กกว่า 10 ไมครอน {pm10} ไมโครกรัมต่อลูกบาศก์เมตร")
print(f"แอมโมเนีย {nh3} ไมโครกรัมต่อลูกบาศก์เมตร")