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


    def first_run(self):
        row = {}
        row[0] = 0
        row[1] = 34567
        row[2] = 1150
        row[3] = "Tools"
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3
        listing_list.append(row)



    def getAllListings(self):
        # cursor = self.conn.cursor()
        # query = "select * from listings;"
        # cursor.execute(query)
        if len(listing_list) == 0:
            self.first_run()

        return listing_list

    def getListingsById(self, lid):
        # cursor = self.conn.cursor()
        # query = "select * from listings where lid = %s;"
        # cursor.execute(query, (lid,))
        # result = cursor.fetchone()
        # return result
        if len(listing_list) == 0:
            self.first_run()
            return listing_list[0]
        row = {};
        row[0] = 'Listing'
        row[1] = 'By'
        row[2] = 'ID'
        row[3] = 'Tested'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3
        return row

    def getListingsByType(self, rtype):
        # cursor = self.conn.cursor()
        # query = "select * from listings where rtype = %s;"
        # cursor.execute(query, (rtype,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Listing'
        row[1] = 'By'
        row[2] = 'Resource'
        row[3] = 'Type'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return row

    def getListingsByPrice(self, lprice):
        # cursor = self.conn.cursor()
        # query = "select * from listings where lprice = %s;"
        # cursor.execute(query, (lprice,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Listings'
        row[2] = 'By'
        row[3] = 'Price'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return row

    def getListingsByRID(self, rid):
        # cursor = self.conn.cursor()
        # query = "select * from listings where rid = %s;"
        # cursor.execute(query, (rid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(listing_list) == 0:
            self.first_run()
            return listing_list[0]

        row = {};
        row[0] = 'Get'
        row[1] = 'Listings'
        row[2] = 'By'
        row[3] = 'Resource ID'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return row

    def getListingsBySupplierID(self, sid):
        # cursor = self.conn.cursor()
        # query = "select * from listings where sid = %s;"
        # cursor.execute(query, (sid,))
        if len(listing_list) == 0:
            self.first_run()
            return listing_list[0]
        result = []
        row = {};
        row[0] = 'Get'
        row[1] = 'Listings'
        row[2] = 'By'
        row[3] = 'Resource ID'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3
        result.append(row)
        # for row in cursor:
        #     result.append(row)
        # return result
        return result

    def getListingsByTypeAndPrice(self, rtype, lprice):
        # cursor = self.conn.cursor()
        # query = "select * from listings where rtype = %s and lprice = %s"
        # cursor.execute(query, (rtype, lprice,))
        result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Listings'
        row[2] = 'By'
        row[3] = 'ResourceType and Price'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        result.append(row)

        return result

    def getListingsByRIDAndPrice(self, rid, lprice):
        # cursor = self.conn.cursor()
        # query = "select * from listings where rid = %s and lprice = %s"
        # cursor.execute(query, (rid, lprice,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Listings'
        row[2] = 'By'
        row[3] = 'RID and price'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return row

    def getSuppliersByListingid(self, lid):
        # cursor = self.conn.cursor()
        # query = "select uid from listings where lid = %s"
        # cursor.execute(query, (lid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Suppliers'
        row[2] = 'From'
        row[3] = 'Listing ID'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return row

    def insert(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        # cursor = self.conn.cursor()
        # query = "insert into listings(lid, rid, rtype, postDate, uid, lprice, amount, rlocation) values (%s, %s, %s, %s, %s, %s, %s, %s) returning lid;"
        # cursor.execute(query, (lid, rid, rtype, postDate, uid, lprice, amount, rlocation,))
        # lid = cursor.fetchone()[0]
        # self.conn.commit()

        row = {};
        row[0] = 'listing id'
        row[1] = 'listing rid'
        row[2] = 'listing rtype'
        row[3] = 'listing post date'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return lid

    def delete(self, lid):
        # cursor = self.conn.cursor()
        # query = "delete from listings where lid = %s;"
        # cursor.execute(query, (lid,))
        # self.conn.commit()

        row = {};
        row[0] = 'deleting id'
        row[1] = 'deleting rid'
        row[2] = 'deleting rtype'
        row[3] = 'deleting post date'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return lid

    def update(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        # cursor = self.conn.cursor()
        # query = "update listings set rid = %s, rtype = %s, postDate = %s, uid = %s, lprice = %s, amount = %s, rlocation = %s where pid = %s;"
        # cursor.execute(query, (lid, rid, rtype, postDate, uid, lprice, amount, rlocation,))
        # self.conn.commit()
        # return lid

        row = {};
        row[0] = 'new listing id'
        row[1] = 'new listing rid'
        row[2] = 'new listing rtype'
        row[3] = 'new listing post date'
        row[4] = "February 10"
        row[5] = "10.00"
        row[6] = 3

        return lid
