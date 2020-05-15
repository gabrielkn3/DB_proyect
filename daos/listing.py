import psycopg2
import config.dbconfig

class ListingDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllListings(self):
        cursor = self.conn.cursor()
        query = "select * from listing;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingById(self, lid):
        cursor = self.conn.cursor()
        query = "select * from listing where lid = %s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByType(self, rtype):
        cursor = self.conn.cursor()
        query = "select * from listing where rtype = %s;"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByResourceName(self, rname):
        cursor = self.conn.cursor()
        query = "select lid, postDate, lprice, lquantity, llocation, sid, rid from listing natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByPrice(self, lprice):
        cursor = self.conn.cursor()
        query = "select * from listing where lprice = %s;"
        cursor.execute(query, (lprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByRID(self, rid):

        cursor = self.conn.cursor()
        query = "select * from listing where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getListingsBySupplierID(self, sid):

        cursor = self.conn.cursor()
        query = "select * from listing where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByTypeAndPrice(self, rtype, lprice):
         cursor = self.conn.cursor()
         query = "select * from listing where rtype = %s and lprice = %s;"
         cursor.execute(query, (rtype, lprice,))
         result = []
         for row in cursor:
             result.append(row)
         return result


    def getListingsByRIDAndPrice(self, rid, lprice):

        cursor = self.conn.cursor()
        query = "select * from listing where rid = %s and lprice = %s;"
        cursor.execute(query, (rid, lprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSuppliersByListingId(self, lid):
        cursor = self.conn.cursor()
        query = "select sid, slocation, uid from supplier natural inner join listing where lid = %s;"
        cursor.execute(query, (lid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, postDate, lprice, lquantity, llocation, sid, rid):
        cursor = self.conn.cursor()
        query = "insert into listing(postDate, lprice, lquantity, llocation, sid, rid) values (%s,%s,%s,%s,%s,%s) returning lid;"
        cursor.execute(query, (postDate, lprice, lquantity, llocation, sid, rid,))
        lid = cursor.fetchone()[0]
        self.conn.commit()


    def delete(self, lid):

        cursor = self.conn.cursor()
        query = "delete from listings where lid = %s;"
        cursor.execute(query, (lid,))
        self.conn.commit()


    def update(self, postDate, lprice, lquantity, llocation, sid, rid):
        cursor = self.conn.cursor()
        query = "update listing set postDate = %s, lprice = %s, lquantity = %s, llocation = %s, sid = %s, rid = %s returning lid;"
        cursor.execute(query, (postDate, lprice, lquantity, llocation, sid, rid,))
        self.conn.commit()