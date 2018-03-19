# coding: utf-8
'''
1900年1月1日は月曜日である.
9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
2月は28日まであるが, うるう年のときは29日である.
うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
'''


def main():
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    year = 1901
    month = 1
    day = 1
    cnt = 0
    while year < 2001:
        if month == 4 or month == 6 or month == 9 or month == 11:
            day += 2
            if day > 6:
                day -= 7
        elif month == 2:
            if year % 4 == 0:
                if not(year % 100 == 0 and year % 400 != 0):
                    day += 1
                    if day > 6:
                        day -= 7
        else:
            day += 3
            if day > 6:
                day -= 7
        month += 1
        if month == 13:
            month = 1
            year += 1
        print(str(year)+'年'+str(month)+'月1日:'+week[day])
        if day == 6:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
