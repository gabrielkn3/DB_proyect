class RequestDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByID(self, RequestID):
        cursor = self.conn.cursor()
        query = "select * from requests where RequestID = %s;"
        cursor.execute(query, (RequestID,))
        result = cursor.fetchone()
        return result

    def getRequestBysid(self, sid):
        cursor = self.conn.cursor()
        query = "select * from requests where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByreqID(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from requests where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select * from requests where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByStatus(self, status):
        cursor = self.conn.cursor()
        query = "select * from requests where status = %s;"
        cursor.execute(query, (status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from requests where quantity = %s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByRIDAndStatus(self, status, rid):
        cursor = self.conn.cursor()
        query = "select * from requests where status = %s and rid = %s;"
        cursor.execute(query, (status,rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByRIDAndQuantity(self, status, quantity):
        cursor = self.conn.cursor()
        query = "select * from requests where status = %s and quantity = %s;"
        cursor.execute(query, (status,quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, RequestID, status, rid, lid, reqID, sid, amount, date):
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

    def update(self, RequestID, status, rid, lid, reqID, sid, amount, date):
        cursor = self.conn.cursor()
        query = "update requests set RequestID = %s, status = %s, rid = %s, lid = %s, reqID = %s, sid = %s, amount = %s, date = %s where RequestID = %s;"
        cursor.execute(query, (RequestID, status, rid, lid, reqID, sid, amount, date,))
        self.conn.commit()
        return lid
