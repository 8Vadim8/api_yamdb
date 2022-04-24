# import sqlite3
#
# def insert_multiple_records(records):
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sqlite_insert_query = """INSERT INTO sqlitedb_developers
#                                  (id, name, email, joining_date, salary)
#                                  VALUES (?, ?, ?, ?, ?);"""
#
#         cursor.executemany(sqlite_insert_query, records)
#         sqlite_connection.commit()
#         print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
#         sqlite_connection.commit()
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")