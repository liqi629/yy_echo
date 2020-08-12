from faker import Faker


f = Faker(locale='zh_cn')


a = f.date_time(tzinfo=None)

# fake.city() # 城市名称
# North Karen
#
# f.street_name() # 街道名称
# Lopez Dale
#
# f.country_code() # 国家编号
# ML
#
# f.longitude() # 经度
# 109.213240
#
# f.address() # 地址
# 7927 Christopher Lake
# Thomasmouth, ME 73174
#
# f.latitude() # 纬度
# -79.2992145
#
# f.street_address() # 街道地址
# 7775 Jacob Wall Apt. 561
#
# f.city_suffix() # 市
# view
#
# f.postcode() # 邮政编码
# 34098
#
# f.country() # 国家
# Estonia
#
# f.street_suffix() # 街道后缀
# River
#
# f.building_number() # 建筑编号
# 5330
#
# f.license_plate() # 车牌号
# Q97 2BU
#
# f.rgb_css_color() #颜色RGB
# rgb(220,140,229)
#
# f.safe_color_name() # 颜色名称
# white
#
# f.company() # 公司名
# Roberts, Bates and Parker
#
# f.credit_card_number(card_type=None) # 信用卡卡号
# 3568612931335293
#
# f.date_time(tzinfo=None) # 随机日期时间
# 1996-07-18 02:05:39
#
# f.file_extension(category=None) # 文件扩展信息
# bmp
#
# f.ipv4(network=False) # ipv4地址
# 96.137.50.163
import datetime
import time
ts = time.time()
print(int(ts))

from PageLocators.homePage_locator import HomePageLocator as loc
a = loc.app_manager
print(a)