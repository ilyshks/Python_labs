def generate_ipv4(count=10000):
    ip = ['0.0.0.0']
    for i in range(count-1):
        previous_ip = ip[-1]
        one, two, three, four = map(int, previous_ip.split('.'))
        if four < 255:
            four += 1
        elif three < 255:
            three += 1
            four = 0
        elif two < 255:
            three = 0
            two += 1
        else:
            two = 0
            one += 1
        ip.append('.'.join(map(str, [one, two, three, four])))
    return ip


my_ips = generate_ipv4()
with open('ip.log', 'w', encoding='utf-8') as output:
    for my_ip in my_ips:
        print(my_ip, file=output)