symbols = {}
length = 0
try:
    with open("article_rus.txt", "r", encoding='utf-8') as article:
        data = article.read().lower()
        for elem in data:
            if 'а' <= elem <= 'я' or elem == 'ё':
                symbols[elem] = symbols.get(elem, 0) + 1
            length += 1
except FileNotFoundError:
    print("Файл не найден!")
else:
    for symbol in symbols:
        symbols[symbol] /= length

    result = sorted(symbols.items(), key=lambda x: x[1], reverse=True)

    with open("article_rus_solve.txt", "w", encoding="utf-8") as output:
        for line in result:
            print(f"{line[0]}: {line[1]}", file=output)

