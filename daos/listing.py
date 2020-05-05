class ListingDAO:
    global listing_list, l_id
    listing_list=[]
    l_id=0
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)


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

    def insert(self, rid, rtype, postDate, uid, lprice, amount, rlocation):
        cursor = self.conn.cursor()
        query = "insert into listings(lid, rid, rtype, postDate, uid, lprice, amount, rlocation) values (%s, %s, %s, %s, %s, %s, %s, %s) returning lid;"
        cursor.execute(query, (rid, rtype, postDate, uid, lprice, amount, rlocation,))
        lid = cursor.fetchone()[0]
        self.conn.commit()


    def delete(self, lid):

        cursor = self.conn.cursor()
        query = "delete from listings where lid = %s;"
        cursor.execute(query, (lid,))
        self.conn.commit()


    def update(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        cursor = self.conn.cursor()
        query = "update listings set rid = %s, rtype = %s, postDate = %s, uid = %s, lprice = %s, amount = %s, rlocation = %s where pid = %s;"
        cursor.execute(query, (lid, rid, rtype, postDate, uid, lprice, amount, rlocation,))
        self.conn.commit()
        return lid