class ReceiptDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReceipts(self):
        cursor = self.conn.cursor()
        query = "select * from Receipts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByID(self, oid):
        cursor = self.conn.cursor()
        query = "select * from Receipts where oid = %s;"
        cursor.execute(query, (oid,))
        result = cursor.fetchone()
        return result

    def getReceiptBySupplierID(self, sid):
        cursor = self.conn.cursor()
        query = "select * from Receipts where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByRequestorID(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from Receipts where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select * from Receipts where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from Receipts where quantity = %s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByStatus(self, status):
        cursor = self.conn.cursor()
        query = "select * from Receipts where status = %s;"
        cursor.execute(query, (status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByRIDAndStatus(self, status, rid):
        cursor = self.conn.cursor()
        query = "select * from Receipts where status = %s and rid = %s;"
        cursor.execute(query, (status,rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByRIDAndQuantity(self, status, quantity):
        cursor = self.conn.cursor()
        query = "select * from Receipts where status = %s and quantity = %s;"
        cursor.execute(query, (status,quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, oid, ReqID, sid, pid, rid, quantity, status):
        cursor = self.conn.cursor()
        query = "insert into Receipts(oid, ReqID, sid, pid, rid, quantity, status) values (%s, %s, %s, %s, %s, %s, %s) returning oid;"
        cursor.execute(query, (oid, ReqID, sid, pid, rid, quantity, status,))
        oid = cursor.fetchone()[0]
        self.conn.commit()
        return oid

    def delete(self, oid):
        cursor = self.conn.cursor()
        query = "delete from Receipts where oid = %s;"
        cursor.execute(query, (oid,))
        self.conn.commit()
        return oid

    def update(self, oid, ReqID, sid, pid, rid, quantity, status):
        cursor = self.conn.cursor()
        query = "update Receipts set oid = %s, ReqID = %s, sid = %s, pid = %s, rid = %s, quantity, status = %s where oid = %s;"
        cursor.execute(query, (oid, ReqID, sid, pid, rid, quantity, status,))
        self.conn.commit()
        return oid
