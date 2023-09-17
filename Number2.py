def is_valid_mask(m):
    parts = m.split('.')
    if len(parts) == 4:
        try:
            for part in parts:
                if not(0 <= int(part) <= 255):
                    return False
            return True
        except ValueError:
            return False
    return False


def input_mask():
    print("Введите маску подсети: ", end='')
    m = input()
    while not is_valid_mask(m):
        print("Маска не соответствует формату!")
        print("Введите заново: ", end='')
        m = input()
    return m


try:
    file = open('ip.log', 'r', encoding='utf-8')
    ips = file.readlines()
    mask = input_mask()
    network_addresses = []
    for ip in ips:
        ip_parts, mask_parts = ip.split('.'), mask.split('.')
        network_address = []
        for ip_part, mask_part in zip(ip_parts, mask_parts):
            network_address.append(str(int(ip_part) & int(mask_part)))
        network_addresses.append('.'.join(network_address))

    with open('ip_solve.log', 'w', encoding='utf-8') as output:
        for network_address in network_addresses:
            print(network_address, file=output)

except FileNotFoundError:
    print('Файл не найден!')
