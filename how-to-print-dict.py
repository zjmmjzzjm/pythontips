# 打印一线城市 新冠状病毒 现状
coronavirus = {
    '上海': '现存确诊21例 累计确诊344例 死亡3例 治愈320例',
    '深圳': '现存确诊36例 累计确诊420例 死亡3例 治愈381例',
    '北京': '现存确诊93例 累计确诊435例 死亡8例 治愈334例',
}
# 直接打印
print('# 直接打印')
print(coronavirus)

# 遍历打印
print('# 遍历打印')
for k, v in coronavirus.items():
    print(k, v)

# 遍历打印
print('# 遍历打印')
for k in coronavirus:
    print(k, coronavirus[k])

extr = {
    '广东' :'现存确诊12例 累计确诊135例 死亡3例 治愈314例',
    '北京': '现存确诊100例 累计确诊435例 死亡8例 治愈334例',
}

coronavirus.update(extr)
print(coronavirus['123'])