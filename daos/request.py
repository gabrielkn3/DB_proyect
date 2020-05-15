import psycopg2
import config.dbconfig
class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByID(self, RequestID):
        cursor = self.conn.cursor()
        query = "select * from request where RequestID = %s;"
        cursor.execute(query, (RequestID,))
        result = cursor.fetchone()
        return result


    # By Requester's ID
    def getRequestByreqID(self, reqID):

        cursor = self.conn.cursor()
        query = "select * from request where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # By Resource's ID
    def getRequestByRID(self, rid):

        cursor = self.conn.cursor()
        query = "select * from request where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByrname(self, rname):

        cursor = self.conn.cursor()
        query = "select requestID, requestStatus,requestQuantity, requestDate, rid, reqid from request natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # pending / paid
    def getRequestByStatus(self, status):
        cursor = self.conn.cursor()
        query = "select * from request where requeststatus = %s;"
        cursor.execute(query, (status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from request where requestquantity = %s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestByRIDAndStatus(self, status, rid):

        cursor = self.conn.cursor()
        query = "select * from request where requeststatus = %s and rid = %s;"
        cursor.execute(query, (status,rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestByRIDAndQuantity(self, status, quantity):

        cursor = self.conn.cursor()
        query = "select * from request where requeststatus = %s and requestquantity = %s;"
        cursor.execute(query, (status,quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByDate(self, date):

        cursor = self.conn.cursor()
        query = "select * from request where requestdate = %s"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, requeststatus, requestquantity, requestdate, rid, reqid):
        cursor = self.conn.cursor()
        query = "insert into request(requeststatus, requestquantity, requestdate, rid, reqid) values (%s, %s, %s, %s, %s) returning RequestID;"
        cursor.execute(query, (requeststatus, requestquantity, requestdate, rid, reqid,))
        lid = cursor.fetchone()[0]
        self.conn.commit()
        return lid


    def delete(self, RequestID):
        cursor = self.conn.cursor()
        query = "delete from requests where RequestID = %s;"
        cursor.execute(query, (RequestID,))
        self.conn.commit()
        return RequestID


    def update(self, requeststatus, requestquantity, requestdate, rid, reqid):
        cursor = self.conn.cursor()
        query = "update requests set requeststatus = %s, requestquantity = %s, requestdate = %s, rid = %s, reqid = %s where RequestID = %s;"
        cursor.execute(query, (requeststatus, requestquantity, requestdate, rid, reqid,))
        self.conn.commit()

    #