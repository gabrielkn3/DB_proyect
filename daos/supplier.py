from config.dbconfig import database_config
import psycopg2
from daos.user import userDAO

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host = '*' password=%s" % (database_config['dbname'],
                                                            database_config['user'],
                                                            database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select sid, firstname, lastname, email, city, country, saddress, zip from supplier natural inner join useraccounts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, firstname, lastname, email, city, country, saddress, zip from supplier natural inner join useraccounts where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result


    def getSupplierByEmail(self, email):
        u = userDAO()
        return u.getUserByEmail(email)


    def getResourcesBySID(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rtype from resource natural inner join stocks where stocks.sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLocation(self, slocation):
        query = "select sid, firstname, lastname, email, city, country, saddress, zip from supplier natural inner join useraccounts where slocation = %s;"
        cursor = self.conn.cursor()
        cursor.execute(query, (slocation,))
        result = []
        for row in cursor:
            result.append(row)
        return result










################################################################################################################################################################################
    def insert(self, uid, slocation):

        return None

    def delete(self, sid):

        return None #failed

    def update(self, sid, slocation):


        return None
