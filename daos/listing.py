class ListingDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllListings(self):
        cursor = self.conn.cursor()
        query = "select * from listings;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsById(self, lid):
        cursor = self.conn.cursor()
        query = "select * from listings where lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        return result

    def getListingsByType(self, rtype):
        cursor = self.conn.cursor()
        query = "select * from listings where rtype = %s;"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByPrice(self, lprice):
        cursor = self.conn.cursor()
        query = "select * from listings where lprice = %s;"
        cursor.execute(query, (lprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select * from listings where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByTypeAndPrice(self, rtype, lprice):
        cursor = self.conn.cursor()
        query = "select * from listings where rtype = %s and lprice = %s"
        cursor.execute(query, (rtype, lprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getListingsByRIDAndPrice(self, rid, lprice):
        cursor = self.conn.cursor()
        query = "select * from listings where rid = %s and lprice = %s"
        cursor.execute(query, (rid, lprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByListingid(self, lid):
        cursor = self.conn.cursor()
        query = "select uid from listings where lid = %s"
        cursor.execute(query, (lid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        cursor = self.conn.cursor()
        query = "insert into listings(lid, rid, rtype, postDate, uid, lprice, amount, rlocation) values (%s, %s, %s, %s, %s, %s, %s, %s) returning lid;"
        cursor.execute(query, (lid, rid, rtype, postDate, uid, lprice, amount, rlocation,))
        lid = cursor.fetchone()[0]
        self.conn.commit()
        return lid

    def delete(self, lid):
        cursor = self.conn.cursor()
        query = "delete from listings where lid = %s;"
        cursor.execute(query, (lid,))
        self.conn.commit()
        return lid

    def update(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        cursor = self.conn.cursor()
        query = "update listings set rid = %s, rtype = %s, postDate = %s, uid = %s, lprice = %s, amount = %s, rlocation = %s where pid = %s;"
        cursor.execute(query, (lid, rid, rtype, postDate, uid, lprice, amount, rlocation,))
        self.conn.commit()
        return lid
