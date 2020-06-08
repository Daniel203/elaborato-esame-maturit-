import mysql.connector


class DBConnection:
    user: str
    password: str
    host: str
    db_name: str
    connection: mysql.connector.connection.MySQLConnection

    def __init__(self, user: str, password: str, host: str, db_name: str):
        self.user = user
        self.password = password
        self.host = host
        self.db_name = db_name

    def connect(self) -> None:
        if (
            self.host is not None
            and self.user is not None
            and self.password is not None
            and self.db_name is not None
        ):
            config = {
                "user": self.user,
                "password": self.password,
                "host": self.host,
                "database": self.db_name,
            }

            self.connection = mysql.connector.connect(**config)

    def close_connection(self) -> None:
        if self.connection is not None:
            self.connection.close()

    def get_cursor(self) -> mysql.connector.cursor.MySQLCursor:
        cursor = self.connection.cursor()
        return cursor
