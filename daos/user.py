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

    def insert(self, username, password, firstname, lastname, email, phone,
               country, city, saddress, zipcode):
        cursor = self.conn.cursor()

        # Inserting new user into user table
        query = "insert into useraccounts(username, password, firstname, lastname, email, " \
                "country, city, saddress, zip) " \
                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (username, password, firstname, lastname, email,
                               country, city, saddress, zipcode,))
        uid = cursor.fetchone()
        self.conn.commit()

        #### Inserting user's phone number into phonenumber table ####
        query = "insert into phonenumber(uid, phone) values(%s, %s);"
        cursor.execute(query, (uid, phone,))
        self.conn.commit()

        return uid

    def insertUserPhone(self, uid, phone):
        cursor = self.conn.cursor()
        query = "insert into phonenumber(uid, phone) values(%s, %s);"
        cursor.execute(query, (uid, phone,))
        self.conn.commit()

    def delete(self, uid):
        # cursor = self.conn.cursor()
        # query = "delete from useraccounts where uid = %s;"
        # cursor.execute(query, (uid,))
        # self.conn.commit()
        # return uid
        for row in elist:
            if row[0] == uid:
                elist.remove(row)
                return uid

    def deleteUserPhone(self, uid, phone):
        cursor = self.conn.cursor()
        query = "delete from phonenumber where uid = %s and phone = %s;"
        cursor.execute(query, (uid, phone,))
        self.conn.commit()
        return phone

    def update(self, uid, username, password, firstname, lastname, email,
               country, city, address, zipcode):
        cursor = self.conn.cursor()
        query = "update useraccounts set username = %s, password = %s, firstname = %s, lastname = %s, email = %s, " \
                "country = %s, city = %s, saddress = %s, zip = %s where uid = %s;"
        cursor.execute(query, (username, password, firstname, lastname, email, country, city, address, zipcode, uid,))
        self.conn.commit()
        return uid

    def updateUserPhone(self, uid, oldPhone, newPhone):
        cursor = self.conn.cursor()
        query = "update phonenumber set phone = %s where uid = %s and phone = %s;"
        cursor.execute(query, (newPhone, uid, oldPhone,))
        self.conn.commit()
        return {uid, newPhone}

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserByFirstName(self, firstname):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where firstname = %s;"
        cursor.execute(query, (firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLastName(self, lastname):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where lastname = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserPhoneNumber(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, phone, firstname, lastname, email from phonenumber natural inner join useraccounts where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByCountry(self, country):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where country = %s;"
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByCity(self, city):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByAddress(self, address):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where saddress = %s;"
        cursor.execute(query, (address,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByZipcode(self, zipcode):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where zip = %s;"
        cursor.execute(query, (zipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByCountryAndCity(self, country, city):
        cursor = self.conn.cursor()
        query = "select * from useraccounts where country = %s and city = %s;"
        cursor.execute(query, (country, city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllPhones(self):
        cursor = self.conn.cursor()
        query = "select uid, phone, firstname, lastname, email from phonenumber natural inner join useraccounts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def validateUserPhoneNumber(self, uid, phone):
        cursor = self.conn.cursor()
        query = "select * from phonenumber where uid = %s and phone = %s;"
        cursor.execute(query, (uid, phone,))
        result = cursor.fetchone()
        if not result:
            return False
        else:
            return True
