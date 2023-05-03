import csv
import psycopg2

from config import host, user, password, db_name


def connection_to_db():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    return connection


def insert_data(conn_i):
    cursor_i = conn_i.cursor()
    while True:
        name = input("Enter your name: ")
        number = input("Enter your phone number: ")
        x = isValid_KZ(number)

        if x:
            cursor_i.execute("SELECT EXISTS (SELECT 1 from numbers WHERE num=%s);", (number,))
            yes_or_no = cursor_i.fetchone()[0]
            if yes_or_no:
                print("This number is already exist, try again")
            else:
                query_create_num = "INSERT INTO numbers (f_name, num) VALUES (%s, %s) RETURNING id;"
                cursor_i.execute(query_create_num, (name, number))
                break

        else:
            print("Number is not in correct form, try again")

    conn_i.commit()
    cursor_i.close()
    conn_i.close()


def update_data(conn_u):
    cursor_u = conn_u.cursor()
    g = int(input("What do you want change phone - 1, name - 2: "))
    if g == 1:
        n = input("Enter your name to find you in DB: ")
        p = input("Enter your new phone number: ")
        query_update_num = "UPDATE numbers SET num = %s WHERE f_name = %s;"

        cursor_u.execute(query_update_num, (p, n))

    elif g == 2:
        n = input("Enter your phone number to find you in DB: ")
        p = input("Enter your new name: ")
        query_update_num = "UPDATE numbers SET f_name = %s WHERE num = %s;"

        cursor_u.execute(query_update_num, (p, n))

    conn_u.commit()
    cursor_u.close()
    conn_u.close()


def isValid_KZ(number):
    if number[0] == '+' and len(number) == 12:
        return True
    elif number[0] == '8' and len(number) == 11:
        return True

    return False


def delete_data(conn_d):
    cursor_d = conn_d.cursor()
    number = input("Enter your phone number to delete: ")
    cursor_d.execute("DELETE FROM numbers WHERE num = %s;", (number,))
    conn_d.commit()
    cursor_d.close()
    conn_d.close()


def get_all_data(conn_a):
    cursor_a = conn_a.cursor()
    cursor_a.execute("SELECT f_name, num FROM numbers")
    conn_a.commit()
    res = cursor_a.fetchall()

    for i in res:
        print(i)

    cursor_a.close()
    conn_a.close()


def get_data(conn_g):
    cursor_g = conn_g.cursor()
    i = int(input("Find by number - 1, find by name - 2: "))
    if i == 1:
        value = input("Enter phone number: ")
        cursor_g.execute("SELECT * from numbers where num = %s;", (value,))

    elif i == 2:
        value = input("Enter first name: ")
        cursor_g.execute("SELECT * from numbers where f_name = %s;", (value,))

    results = cursor_g.fetchall()
    conn_g.commit()
    for i in results:
        print(i)


def upload_from_csv(conn_f, path):
    cursor_f = conn_f.cursor()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor_f.execute("INSERT INTO numbers(f_name, num) VALUES (%s, %s)", (row[0], row[1]))
    conn_f.commit()
    cursor_f.close()
    conn_f.close()


def upload_data_from_list(names, numbers):
    conn_u = connection_to_db()
    cursor_u = conn_u.cursor()
    incorrect_data = []

    for i in range(len(names)):
        if numbers[i].startswith("+7") and len(numbers[i]) == 12 and numbers[i][1:].isdigit():
            cursor_u.execute("INSERT INTO numbers (f_name, num) VALUES (%s, %s)", (names[i], numbers[i]))
        else:
            incorrect_data.append((names[i], numbers[i]))

    conn_u.commit()
    cursor_u.close()
    conn_u.close()

    return incorrect_data


names = ["Rusik", "Mary", "Bob"]
phones = ["+77056777890", "+7 701 234 5678", "1234567890"]

while True:
    conn = connection_to_db()
    ch = int(input("Add new phone - 1, Update data - 2, Delete data - 3, Select Data - 4, upload data from csv file - 5, "
                   "get all data from DB - 6, upload data from list - 7, STOP - 0: "))
    path_to_file = "test.csv"

    if ch == 1:
        insert_data(conn)

    elif ch == 2:
        update_data(conn)

    elif ch == 3:
        delete_data(conn)

    elif ch == 4:
        get_data(conn)

    elif ch == 5:
        upload_from_csv(conn, path_to_file)

    elif ch == 6:
        get_all_data(conn)

    elif ch == 7:
        incorrect_data = upload_data_from_list(names, phones)
        if len(incorrect_data) > 0:
            print("The following data is incorrect:")
            for data in incorrect_data:
                print("Name: {}, Phone: {}".format(data[0], data[1]))
        else:
            print("All data was inserted successfully.")
    elif ch == 0:
        conn.close()
        print("See you next time (OSU)")
        break
