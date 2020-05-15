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

    def update(self, uid, username, password, firstname, lastname, email, phone,
               country, city, neighborhood, street, housenumber, zipcode):
        # cursor = self.conn.cursor()
        # query = "update user set username = %s, password = %s, firstname = %s, lastname = %s, email = %s, phone = %s, " \
        #         "country = %s, city = %s, neighborhood = %s, street = %s, housenumber = %s, zipcode = %s where uid = %s;"
        # cursor.execute(query, (username, password, firstname, lastname, email, phone, country, city, neighborhood, street, housenumber, zipcode, uid,))
        # self.conn.commit()
        # return uid
        # entry = {}
        # entry[0] = uid
        # entry[1] = username
        # entry[2] = password
        # entry[3] = firstname
        # entry[4] = lastname
        # entry[5] = email
        # entry[6] = phone
        # entry[7] = country
        # entry[8] = city
        # entry[9] = neighborhood
        # entry[10] = street
        # entry[11] = housenumber
        # entry[12] = zipcode
        for row in elist:
            if row[0] == uid:
                row[1] = username
                row[2] = password
                row[3] = firstname
                row[4] = lastname
                row[5] = email
                row[6] = phone
                row[7] = country
                row[8] = city
                row[9] = neighborhood
                row[10] = street
                row[11] = housenumber
                row[12] = "" + zipcode
                return row

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts;"
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
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[0] == uid:
        #         return row
        # return empty_list


    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result
        # for row in elist:
        #     if row[1] == username:
        #         return row
        # return empty_list

    def getUserByFirstName(self, firstname):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where firstname = %s;"
        cursor.execute(query, (firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in elist:
        #     if row[3] == firstname:
        #         row_list.append(row)
        # return row_list

    def getUserByLastName(self, lastname):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, email, city, country, saddress, zip from useraccounts where lastname = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in elist:
        #     if row[4] == lastname:
        #         row_list.append(row)
        # return row_list

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

    def test(self, uid):
        cursor = self.conn.cursor()
        query = "select uid from useraccounts where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()[0]
        print("DAO = " + str(result))
        return str(result)