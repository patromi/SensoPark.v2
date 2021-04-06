from flask import *
from app import db, ma
from app import models
from app import create_app
import os
import datetime
from datetime import datetime, timedelta, date

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()


def alcorythm_reservation(id, start, end):
    print('poczatek algorytmu:', id, start, end)
    lista_poczatkowa = []
    lista_koncowa = []
    lista_proponowanyczas = []
    parking = models.Parking.query.filter_by(id=id).first_or_404()
    x = parking.number_of_parkings
    print('ilosc parkingów', x)
    reservation = models.Parking_reservation.query.filter_by(parking_id=id).all()
    start = datetime.strptime(start, '%Y-%m-%d %H:%M')
    end = datetime.strptime(end, '%Y-%m-%d %H:%M')
    for i in reservation:
        print(i)
        ye = datetime.combine(i.date_reservation, i.start_time_reservation)
        d = datetime.combine(i.date_reservation, i.end_time_reservation)
        strpoczatek = ye.strftime('%Y-%m-%d')
        strend = start.strftime('%Y-%m-%d')
        print(strpoczatek)

        print(strend)
        if strpoczatek == strend:
            lista_poczatkowa.append(ye)
            lista_koncowa.append(d)
    print(lista_poczatkowa)
    print(lista_koncowa)
    a = 0
    b = 0
    c = 0

    # print(start)
    # print(end)
    if start > end:
        return False
    for i in range(len(lista_poczatkowa)):
        # try:
        print('start pętli', start)
        print('lista_początkowa ', lista_poczatkowa[i], 'lista_końcowa ', lista_koncowa[i])
        if start >= lista_poczatkowa[i] and start <= lista_koncowa[i]:
            lista_proponowanyczas.append(lista_koncowa[i])
            a += 1
        #      print(lista_poczatkowa)
        #    print('end=',end)
        if end > lista_poczatkowa[i] and end < lista_koncowa[i]:
            #          print(lista_poczatkowa[i])

            #           print('spelnione')
            b += 1
        if start <= lista_poczatkowa[i] and end >= lista_koncowa[i]:
            c += 1

    # except:
    #   print('koniec')

    print('a= ', a)
    print('b= ', b)
    print('c=', c)
    if a < int(x) and b < int(x) and c < int(x):
        return True
    elif a > int(x):
        lista_proponowanyczas.sort()
        return False  # lista_proponowanyczas[0]
    else:
        return False


def alcorythm_reservation_max_function(id, start, end, reservation):
    list = []
    for i in reservation:
        ye = datetime.combine(i.date_reservation, i.start_time_reservation)
        d = datetime.combine(i.date_reservation, i.end_time_reservation)
    try:
        data_startowa = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        data_koncowa = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        data_koncowa -= timedelta(seconds=1)

    except:
        return False

    for i in range(48):
        lista_poczatkowa = []
        lista_koncowa = []
        lista_proponowanyczas = []
        try:
            for i in reservation:
                ye = datetime.combine(i.date_reservation, i.start_time_reservation)
                d = datetime.combine(i.date_reservation, i.end_time_reservation)
                lista_poczatkowa.append(ye)
                lista_koncowa.append(d)


        except:
            return False
        a = 0
        b = 0
        c = 0
        # print(type(start))

        for i in range(len(lista_poczatkowa)):
            # try:
            # print('start', start)
            # print('lista1 ', lista_poczatkowa[i], 'lista_koncowa ', lista_koncowa[i])
            if data_startowa >= lista_poczatkowa[i] and data_startowa < lista_koncowa[i]:
                lista_proponowanyczas.append(lista_koncowa[i])
                a += 1
            #   print(lista_poczatkowa)
            #  print('end=', end)
            if data_koncowa > lista_poczatkowa[i] and data_koncowa < lista_koncowa[i]:
                # print(lista_poczatkowa[i])

                # print('spelnione')
                b += 1
            if data_startowa <= lista_poczatkowa[i] and data_koncowa >= lista_koncowa[i]:
                c += 1

        # except:
        #   pass

        # print('a= ', a)
        # print('b= ', b)
        # print('c=', c)
        maximum = max(a, max(b, c))
        # print(maximum)
        list.append(maximum)

        data_startowa += timedelta(minutes=30)
        data_koncowa += timedelta(minutes=30)
        # print(f"data_startowa",{data_startowa},"data_koncowa",{data_koncowa})

    return list

# print(alcorythm_reservation(9, '2021-02-13 00:09', '2021-02-13 00:30'))
# """start 17.05 reservacja1 17=18
#02-13-21
