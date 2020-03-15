
# use pop 
coronavirus = {
    '上海': '现存确诊21例 累计确诊344例 死亡3例 治愈320例',
    '深圳': '现存确诊36例 累计确诊420例 死亡3例 治愈381例',
    '北京': '现存确诊93例 累计确诊435例 死亡8例 治愈334例',
}

result = coronavirus.pop('上海')
print(coronavirus)
print(result)

# use del
coronavirus = {
    '上海': '现存确诊21例 累计确诊344例 死亡3例 治愈320例',
    '深圳': '现存确诊36例 累计确诊420例 死亡3例 治愈381例',
    '北京': '现存确诊93例 累计确诊435例 死亡8例 治愈334例',
}
del coronavirus['上海']
print(coronavirus)


# popitem
coronavirus = {
    '上海': '现存确诊21例 累计确诊344例 死亡3例 治愈320例',
    '深圳': '现存确诊36例 累计确诊420例 死亡3例 治愈381例',
    '北京': '现存确诊93例 累计确诊435例 死亡8例 治愈334例',
}
result = coronavirus.popitem()
print(coronavirus)
print(result)

# clear
coronavirus = {
    '上海': '现存确诊21例 累计确诊344例 死亡3例 治愈320例',
    '深圳': '现存确诊36例 累计确诊420例 死亡3例 治愈381例',
    '北京': '现存确诊93例 累计确诊435例 死亡8例 治愈334例',
}
coronavirus.clear()
print(coronavirus)
