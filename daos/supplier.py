from config.dbconfig import database_config
import psycopg2
from daos.user import userDAO

class SupplierDAO:
    global supplier_list, s_id, removed
    supplier_list = []
    s_id = 0
    removed=0
    def __init__(self):

        connection_url = "dbname=%s user=%s host = '*' password=%s" % (database_config['dbname'],
                                                            database_config['user'],
                                                            database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def first_time(self):
        row = {}
        row[0] = 1150
        row[1] = 12321
        row[2] = "Lares"
        supplier_list.append(row)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select sid, uid, slocation from supplier where sid = %s;"
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
        query = "select sid, uid, slocation from supplier where slocation = %s;"
        cursor = self.conn.cursor()
        cursor.execute(query, (slocation,))
        result = cursor.fetchone()
        return result










################################################################################################################################################################################
    def insert(self, uid, slocation):
        row={}
        row[0] = len(supplier_list)
        row[1] = uid
        row[2] = slocation
        supplier_list.append(row)
        return s_id

    def delete(self, sid):
        for i in range(0, len(supplier_list)):
            for row in supplier_list:
                if row[0] == sid:
                    supplier_list.remove(row)
                    removed =1
                    return sid
        return None #failed

    def update(self, sid, slocation):
        result = []
        for i in range(0, len(supplier_list)):
            for row in supplier_list:
                if row[0] == sid:
                    row[2] = slocation
                    result.append(row)

        return result
