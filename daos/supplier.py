from config.dbconfig import database_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (database_config['dbname'],
                                                            database_config['user'],
                                                            database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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
            query = "select * from supplier where sid = %s;"
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result

    def getSupplierByEmail(self, semail):
        cursor = self.conn.cursor()
        query = "select * from supplier where semail = %s;"
        cursor.execute(query, (semail,))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rtypte, rdescription, rlocation from resource natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAddress(self, address):
        cursor = self.conn.cursor()
        query = "select * from supplier where saddress = %s;"
        cursor.execute(query, (address,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def insert(self, stype, sname, semail, sphone, saddress,sfinance,):
        cursor = self.conn.cursor()
        query = "insert into supplier(stype, sname, semail, sphone, saddress, sfinance) values (%s, %s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (stype, sname, semail, sphone, saddress, sfinance))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid