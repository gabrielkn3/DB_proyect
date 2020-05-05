import psycopg2
import config.dbconfig
class userDAO:
    global elist, empty_list, eid
    elist = []
    empty_list = []
    eid = 0

    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'],
            config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = len(elist)
        row[1] = "GentleJerry"
        row[2] = "Hydration"
        row[3] = "Gentle"
        row[4] = "Jerry"
        row[5] = "gentle.jerry@gmail.gov"
        row[6] = 7874206969
        row[7] = "OurHearts"
        row[8] = "Gentelius"
        row[9] = "Hydrationville"
        row[10] = "Eich Tuo Street"
        row[11] = 83
        row[12] = "10301"

        elist.append(row)

    def insert(self, username, password, fname, lname, email, phone,
               state, city, neighborhood, street, housenumber, zipcode):
        # cursor = self.conn.cursor()
        # query = "insert into user(username, password, fname, lname, email, phone, state, city, neighborhood, street, housenumber, zipcode) " \
        #         "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning uid;"
        # cursor.execute(query, (username, password, fname, lname, email, phone, state, city, neighborhood, street, housenumber, zipcode,))
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
        row[6] = int(phone)
        row[7] = state
        row[8] = city
        row[9] = neighborhood
        row[10] = street
        row[11] = housenumber
        row[12] = "" + zipcode
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

    def update(self, uid, username, password, fname, lname, email, phone,
               state, city, neighborhood, street, housenumber, zipcode):
        # cursor = self.conn.cursor()
        # query = "update user set username = %s, password = %s, fname = %s, lname = %s, email = %s, phone = %s, " \
        #         "state = %s, city = %s, neighborhood = %s, street = %s, housenumber = %s, zipcode = %s where uid = %s;"
        # cursor.execute(query, (username, password, fname, lname, email, phone, state, city, neighborhood, street, housenumber, zipcode, uid,))
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
        # entry[7] = state
        # entry[8] = city
        # entry[9] = neighborhood
        # entry[10] = street
        # entry[11] = housenumber
        # entry[12] = zipcode
        for row in elist:
            if row[0] == uid:
                row[1] = username
                row[2] = password
                row[3] = fname
                row[4] = lname
                row[5] = email
                row[6] = phone
                row[7] = state
                row[8] = city
                row[9] = neighborhood
                row[10] = street
                row[11] = housenumber
                row[12] = "" + zipcode
                return row

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from user;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        # if len(elist)==0:
        #     self.first_time()
        # return elist

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from user where uID = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[0] == uid:
        #         return row
        # return empty_list


    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from user where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[1] == username:
        #         return row
        # return empty_list

    def getUserByFirstName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from user where fname = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in elist:
        #     if row[3] == fname:
        #         row_list.append(row)
        # return row_list

    def getUserByLastName(self, lname):
        cursor = self.conn.cursor()
        query = "select * from user where lname = %s;"
        cursor.execute(query, (lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in elist:
        #     if row[4] == lname:
        #         row_list.append(row)
        # return row_list

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from user where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[5] == email:
        #         return row
        # return empty_list

    def getUserByPhoneNumber(self, phone):
        cursor = self.conn.cursor()
        query = "select * from user where phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[6] == phone:
        #         return row
        # return empty_list

    def getUserByState(self, state):
        cursor = self.conn.cursor()
        query = "select * from user where state = %s;"
        cursor.execute(query, (state,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # for row in elist:
        #     if row[7] == state:
        #         return row
        # return empty_list

    def getUserByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from user where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # for row in elist:
        #     if row[8] == city:
        #         return row
        # return empty_list

    def getUserByNeighborhood(self, neighborhood):
        cursor = self.conn.cursor()
        query = "select * from user where neighborhood = %s;"
        cursor.execute(query, (neighborhood,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # for row in elist:
        #     if row[9] == neighborhood:
        #         return row
        # return empty_list

    def getUserByZipcode(self, zipcode):
        cursor = self.conn.cursor()
        query = "select * from user where zipcode = %s;"
        cursor.execute(query, (zipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # for row in elist:
        #     if row[12] == zipcode:
        #         return row
        # return empty_list

    def getUserByStateAndCity(self, state, city):
        cursor = self.conn.cursor()
        query = "select * from user where state = %s and city = %s;"
        cursor.execute(query, (state, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # for row in elist:
        #     if row[7] == state and row[8] == city:
        #         return row
        # return empty_list

