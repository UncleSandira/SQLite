import sqlite3

DATABASE = 'Cars.db'
print('hello world')

def print_allcars():
    speed = input('What speed: ')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = " SELECT carname,topspeed FROM car WHERE topspeed > ?; "
        cursor.execute(sql, (speed, ))
        results = cursor.fetchall()
        # print results nicely
        for car in results:
            print(f'Car: {car[0]} TopSpeed: {car[1]}')


if __name__ == '__main__':
    print_allcars()
