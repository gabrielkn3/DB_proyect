import psycopg2
class userDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % ('dbname', 'user', 'passwd')
        self.conn = psycopg2.connect(connection_url)

    def insert(self, username, password, fname, lname, email, phone, address):
        cursor = self.conn.cursor()
        query = "insert into user(username, password, fname, lname, email, phone, address) values(%s, %s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (username, password, fname, lname, email, phone, address,))
        uid = cursor.fetchone()
        self.conn.commit()
        return uid

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from user where uid = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid

    def update(self, uid, username, password, fname, lname, email, phone, address):
        cursor = self.conn.cursor()
        query = "update user set username = %s, password = %s, fname = %s, lname = %s, email = %s, phone = %s, address = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return uid

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from user;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from user where uID = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from user where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserByFirstName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from user where fname = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLastName(self, lname):
        cursor = self.conn.cursor()
        query = "select * from user where lname = %s;"
        cursor.execute(query, (lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from user where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserByPhoneNumber(self, phone):
        cursor = self.conn.cursor()
        query = "select * from user where phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        return result

    def getUserByAddress(self, address):
        cursor = self.conn.cursor()
        query = "select * from user where address = %s;"
        cursor.execute(query, (address,))
        result = []
        for row in cursor:
            result.append(row)
        return result