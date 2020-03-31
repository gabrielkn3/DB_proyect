from config.dbconfig import database_config
import psycopg2
from daos.user import userDAO
from daos.listing import ListingDAO
class SupplierDAO:
    global supplier_list, s_id
    supplier_list = []
    s_id = 0
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (database_config['dbname'],
    #                                                         database_config['user'],
    #                                                         database_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


    def first_time(self):
        row = {}
        row[0] = 1150
        row[1] = 12321
        row[2] = "Latitud: 0 || Longitud: 0"
        supplier_list.append(row)

    def getAllSuppliers(self):
        # cursor = self.conn.cursor()
        # query = "select * from supplier;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        if len(supplier_list)==0:
            self.first_time()
            return supplier_list
        return supplier_list

    def getSupplierById(self, sid):
            # cursor = self.conn.cursor()
            # query = "select * from supplier where sid = %s;"
            # cursor.execute(query, (sid,))
            # result = cursor.fetchone()
         result=[]
         for i in range(0, len(supplier_list)):
            for row in supplier_list:
                if row[0] == sid:
                    result.append(row)


         return result[0]

    def getSupplierByEmail(self, email):
        u = userDAO()
        return u.getUserByEmail(email)

#need tu test
    def getSuppliersByAddress(self, address):
        u = userDAO()
        return u.getUserByAddress(address)

    def getResourcesBySID(self,sid):
        l = ListingDAO()
        result = ListingDAO.getListingsBySupplierID(sid)
        resources=[]
        for i in range(0, len(result)):
            for row in result:
                resources.append(row['rname'])
        return resources


    def insert(self, uid, slocation):
        row={}
        row[0] = ++s_id
        row[1] = uid
        row[2] = slocation
        supplier_list.append(row)
        return s_id

    def delete(self, sid):
        for i in range(0, len(supplier_list)):
            for row in supplier_list:
                if row[0] == sid:
                    supplier_list.remove(row)
                    return sid
        return -1 #failed

    def update(self, sid, slocation):
        result = []
        for i in range(0, len(supplier_list)):
            for row in supplier_list:
                if row[0] == sid:
                    row[2] = slocation
                    result.append(row)

        return result
