import sqlite3


class Database:
    """Class to model the 'multiplcation.db' database functions"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        """Connecting database and adding a cursor"""
        self.conn = sqlite3.connect("multiplication.db")  #  If DB doesn't exist it will be added
        self.c = self.conn.cursor()

    def close_connection(self):
        """Closing cursor and database connection"""
        self.c.close()  # Close the cursor
        self.conn.close()  # Close the db connection

    def create_table(self):
        """Creates a table where the usernames and password will be stored."""
        self.c.execute("CREATE TABLE IF NOT EXISTS userLoginDetails (username TEXT, password TEXT)")
    
    def create_admin(self):
        """Create an admin account"""
        self.c.execute("INSERT INTO userLoginDetails (username, password) VALUES (?, ?)", 
                        (self.username, self.password))
        self.conn.commit()  # Save db changes

    def verify_login(self):
        pass

    def create_student(self):
        pass

    def delete_student(self):
        pass

    def create_teacher(self):
        pass
    
    def delete_teacher(self):
        pass