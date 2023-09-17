import csv
from random import randint


FILENAME = "players.csv"

surnames = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов',
            'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев', 'Виноградов',
            'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселёв',
            'Макаров', 'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов', 'Куликов',
            'Алексеев', 'Степанов', 'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров', 'Борисов', 'Королёв',
            'Герасимов', 'Пономарёв', 'Григорьев']

players = []
for surname in surnames:
    players.append(dict([("Спортсмен", surname), ("Количество побед", randint(0, 100)),
                         ("Доп. показатель", randint(0, 1000))]))


with open(FILENAME, "w", newline="") as file:
    columns = ["Спортсмен", "Количество побед", "Доп. показатель"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(players)

players = []
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for line in reader:
        players.append(dict([("Спортсмен", line["Спортсмен"]), ("Количество побед", int(line["Количество побед"])),
              ("Доп. показатель", int(line["Доп. показатель"]))]))

players.sort(key=lambda player: (player["Количество побед"], player["Доп. показатель"]), reverse=True)

place = 1
i, cnt = 0, 1
result = [{"Спортсмен": players[0]["Спортсмен"], "Место": place}]
while i < len(players) - 1:
    while i < len(players) - 1 and (players[i]["Количество побед"], players[i]["Доп. показатель"]) == (players[i+1]["Количество побед"], players[i+1]["Доп. показатель"]):
        result.append({"Спортсмен": players[i+1]["Спортсмен"], "Место": place})
        i += 1
        cnt += 1
    place += max(cnt, 1)
    cnt = 1
    if i < len(players) - 1:
        result.append({"Спортсмен": players[i+1]["Спортсмен"], "Место": place})
    i += 1

with open("results.csv", "w", newline="") as file:
    columns = ["Спортсмен", "Место"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(result)
