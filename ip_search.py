from qqwry import QQwry
import geoip2.database

q = QQwry()
# q.load_file('qqwry.dat') windows默认不区分大小写
q.load_file('QQWry.Dat')

reader = geoip2.database.Reader('GeoLite2-City.mmdb')

ip = '202.99.192.68'

try:
    geo = reader.city(ip)
    if geo.country.name == "China":
        # 使用纯真查询更精细城市
        location = q.lookup(ip)
        print("中国 IP，城市归属地：", location[0])
    else:
        print("国外 IP：", geo.country.name, geo.city.name)
except:
    print("IP 查询失败")