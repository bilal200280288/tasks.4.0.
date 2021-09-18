city = input('Введите ваш город: Kazakstan, Paris, UAR, Kyrgystan, San-Francisco, Germany, Moscow, Sweden: ')

if city.lower() == 'kazakstan':
    complaint = input('Введите жалобу: ')
    f = open('Kazakstan.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'paris':
    complaint = input('Введите жалобу: ')
    f = open('Paris.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'uar':
    complaint = input('Введите жалобу: ')
    f = open('UAR.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'kyrgystan':
    complaint = input('Введите жалобу: ')
    f = open('Kyrgystan.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'san-francisco':
    complaint = input('Введите жалобу: ')
    f = open('San-Francisco.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'germany':
    complaint = input('Введите жалобу: ')
    f = open('Germany.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'moscow':
    complaint = input('Введите жалобу: ')
    f = open('Moscow.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')

elif city.lower() == 'sweden':
    complaint = input('Введите жалобу: ')
    f = open('Sweden.txt', 'a', encoding='utf-8')
    f.write(f'\n{complaint}')