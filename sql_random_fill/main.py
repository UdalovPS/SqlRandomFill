import sqlite3


class SQLiteDB:
    """This class need for work in SQLite DB"""
    def __init__(self, db_name="db.sqlite3"):
        """:arg
        db_name - Database name
        """
        self.db_name = db_name

    def connect_db(self) -> sqlite3.Connection:
        """This method connect to db"""
        return sqlite3.connect(self.db_name)


class SqlRandomFill:
    """This contains all method requests to database"""
    def __init__(self, db_class=SQLiteDB, verbose=False):
        """:arg
        db_class - Class of db with you work (default - SQLite)
        verbose - flag for print logging information
        """
        self.db = db_class()
        self.verbose = verbose

    def create_cursor(self, connect: sqlite3.Connection):
        """This method create cursor"""
        return connect.cursor()

    def execute_request(self, request: str) -> None:
        """This method execute request to DB
        :arg request - string request in SQL language"""
        try:
            with self.db.connect_db() as connect:           # connect to DB
                if self.verbose:
                    print(f"[INFO] connect to db -> {self.db.db_name}")
                cursor = self.create_cursor(connect)        # create cursor
                cursor.execute(request)                     # execute request to DB
                if self.verbose:
                    print(f"[INFO] execute request to DB -> {request}")

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connect:
                connect.close()                             # close DB
                print(f"[INFO] close db -> {self.db.db_name}")


if __name__ == '__main__':
    request = "SELECT sqlite_version();"
    db = SqlRandomFill(SQLiteDB, verbose=True)
    db.execute_request(request)

