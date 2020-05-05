class RequestDAO:
    global request_list, request_id
    request_list = []
    request_id = 0
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


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

    def insert(self, status, rid, reqID, requantity, date):
        cursor = self.conn.cursor()
        query = "insert into requests(RequestID, status, rid, lid, reqID, sid, amount, date) values (%s, %s, %s, %s, %s, %s, %s, %s) returning RequestID;"
        cursor.execute(query, (RequestID, status, rid, lid, reqID, sid, amount, date,))
        lid = cursor.fetchone()[0]
        self.conn.commit()
        return lid


    def delete(self, RequestID):
        cursor = self.conn.cursor()
        query = "delete from requests where RequestID = %s;"
        cursor.execute(query, (RequestID,))
        self.conn.commit()
        return RequestID


    def update(self, RequestID, status, rid, reqID, amount, date):
        cursor = self.conn.cursor()
        query = "update requests set RequestID = %s, status = %s, rid = %s, lid = %s, reqID = %s, sid = %s, amount = %s, date = %s where RequestID = %s;"
        cursor.execute(query, (RequestID, status, rid, lid, reqID, sid, amount, date,))
        self.conn.commit()
        return lid

