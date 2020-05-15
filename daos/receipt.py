import config.dbconfig
import psycopg2
class ReceiptDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'],
            config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def getAllReceipts(self):
        cursor = self.conn.cursor()
        query = "select * from orders;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReceiptByID(self, oid):
        cursor = self.conn.cursor()
        query = "select * from orders where oid = %s;"
        cursor.execute(query, (oid,))
        result = cursor.fetchone()
        return result

    def getReceiptBySupplierID(self, sid):
        cursor = self.conn.cursor()
        query = "select * from orders where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReceiptByRequestorID(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from orders where reqid = %s;"
        cursor.execute(query, (reqID,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getReceiptByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select oid, ostatus, reqid, sid, pid from orders natural inner join belongs where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReceiptByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from orders natural inner join belongs where rquantity = %s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReceiptByStatus(self, status):
        cursor = self.conn.cursor()
        query = "select * from orders where ostatus = %s;"
        cursor.execute(query, (status,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReceiptByRIDAndStatus(self, status, rid):
        cursor = self.conn.cursor()
        query = "select * from orders natural inner join belongs where ostatus = %s and rid = %s;"
        cursor.execute(query, (status,rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReceiptByRIDAndQuantity(self, rid, quantity):
        cursor = self.conn.cursor()
        query = "select * from orders natural inner join belongs where rid = %s and rquantity = %s;"
        cursor.execute(query, (quantity,rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, ostatus, reqid, sid, pid):
        cursor = self.conn.cursor()
        query = "insert into orders(ostatus, reqid, sid, pid) values (%s, %s, %s, %s) returning oid;"
        cursor.execute(query, (ostatus, reqid, sid, pid,))
        oid = cursor.fetchone()[0]
        self.conn.commit()


    def delete(self, oid):
        cursor = self.conn.cursor()
        query = "delete from orders where oid = %s;"
        cursor.execute(query, (oid,))
        self.conn.commit()


    def update(self, oid, ReqID, sid, pid, rid, quantity, status):
        cursor = self.conn.cursor()
        query = "update orders set ostatus = %s, ReqID = %s, sid = %s, pid = %s where oid = %s;"
        cursor.execute(query, (oid, ReqID, sid, pid, rid, quantity, status,))
        self.conn.commit()
