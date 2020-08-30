days_of_week = ['pon', 'śro', 'pią', 'sob']
newList = ['pon', 'wto', 'śro', 'czw', 'pią', 'sob', 'nie']

for day in newList:
    if not day in days_of_week:
        days_of_week.insert(newList.index(day), day)

print(days_of_week)

Lista_zakupów = {'piekarnia': ['chleb', 'bułki', 'pączek'], 'warzywniak': ['marchew', 'seler', 'rukola']}
counter = 0
print('Lista zakupów')
for shop in Lista_zakupów:
    print('Idę do %s, kupuję tu następujące rzeczy: %s' % (shop, Lista_zakupów[shop]))
    for food_item in Lista_zakupów[shop]:
        counter = counter + Lista_zakupów[shop].count(food_item)
print('W sumię kupuję %d produktów.' % counter)

start_num = 1
end_num = 101
num_list = []
power_list = []

for num in range(start_num, end_num):
    if num % 5 == 0:
        num_list.append(num)
        power_list.append(num ** 3)

print('Lista liczb z zakresu od %d do %d, podzielnych przez 5:' % (start_num, end_num), num_list)
print('Lista liczb z zakresu od %d do %d, podniesionych do potęgi 3:' % (start_num, end_num), power_list)