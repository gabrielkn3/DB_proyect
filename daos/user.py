import psycopg2
class userDAO:
    global elist, empty_list, eid
    elist = []
    empty_list = []
    eid = 0
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % ('dbname', 'user', 'passwd')
    #     self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = len(elist)
        row[1] = "GentleJerry"
        row[2] = "Hydration"
        row[3] = "Gentle"
        row[4] = "Jerry"
        row[5] = "gentle.jerry@godisdead.gov"
        row[6] = 7874206969
        row[7] = "InsideOurHearts"
        elist.append(row)

    def insert(self, username, password, fname, lname, email, phone, address):
        # cursor = self.conn.cursor()
        # query = "insert into user(username, password, fname, lname, email, phone, address) values(%s, %s, %s, %s, %s, %s, %s) returning uid;"
        # cursor.execute(query, (username, password, fname, lname, email, phone, address,))
        # uid = cursor.fetchone()
        # self.conn.commit()
        # return uid
        row = {}
        row[0] = len(elist)
        row[1] = username
        row[2] = password
        row[3] = fname
        row[4] = lname
        row[5] = email
        row[6] = phone
        row[7] = address
        elist.append(row)
        return row[0]

    def delete(self, uid):
        # cursor = self.conn.cursor()
        # query = "delete from user where uid = %s;"
        # cursor.execute(query, (uid,))
        # self.conn.commit()
        # return uid
        for row in elist:
            if row[0] == uid:
                elist.remove(row)
                return uid

    def update(self, uid, username, password, fname, lname, email, phone, address):
        # cursor = self.conn.cursor()
        # query = "update user set username = %s, password = %s, fname = %s, lname = %s, email = %s, phone = %s, address = %s where uid = %s;"
        # cursor.execute(query, (username, password, fname, lname, email, phone, address, uid,))
        # self.conn.commit()
        # return uid
        # entry = {}
        # entry[0] = uid
        # entry[1] = username
        # entry[2] = password
        # entry[3] = fname
        # entry[4] = lname
        # entry[5] = email
        # entry[6] = phone
        # entry[7] = address
        for row in elist:
            if row[0] == uid:
                row[1] = username
                row[2] = password
                row[3] = fname
                row[4] = lname
                row[5] = email
                row[6] = phone
                row[7] = address
                elist.append(row)
                return row

    def getAllUsers(self):
        # cursor = self.conn.cursor()
        # query = "select * from user;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(elist)==0:
            self.first_time()
        return elist

    def getUserById(self, uid):
        # cursor = self.conn.cursor()
        # query = "select * from user where uID = %s;"
        # cursor.execute(query, (uID,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[0] == uid:
                return row
        return empty_list


    def getUserByUsername(self, username):
        # cursor = self.conn.cursor()
        # query = "select * from user where username = %s;"
        # cursor.execute(query, (username,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[1] == username:
                return row
        return empty_list

    def getUserByFirstName(self, fname):
        # cursor = self.conn.cursor()
        # query = "select * from user where fname = %s;"
        # cursor.execute(query, (fname,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in elist:
            if row[3] == fname:
                row_list.append(row)
        return row_list

    def getUserByLastName(self, lname):
        # cursor = self.conn.cursor()
        # query = "select * from user where lname = %s;"
        # cursor.execute(query, (lname,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in elist:
            if row[4] == lname:
                row_list.append(row)
        return row_list

    def getUserByEmail(self, email):
        # cursor = self.conn.cursor()
        # query = "select * from user where email = %s;"
        # cursor.execute(query, (email,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[5] == email:
                return row
        return empty_list

    def getUserByPhoneNumber(self, phone):
        # cursor = self.conn.cursor()
        # query = "select * from user where phone = %s;"
        # cursor.execute(query, (phone,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[6] == phone:
                return row
        return empty_list

    def getUserByAddress(self, address):
        # cursor = self.conn.cursor()
        # query = "select * from user where address = %s;"
        # cursor.execute(query, (address,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        for row in elist:
            if row[7] == address:
                return row
        return empty_list