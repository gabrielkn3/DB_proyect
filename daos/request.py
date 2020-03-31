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

    def first_time(self):
        row = {}
        row[0] = 23
        row[1] = "In progress."
        row[2] = 456
        row[3] = 3499445
        row[4] = 7214
        row[5] = 1150
        row[6] = 45
        row[7] = "January 23"
        request_list.append(row)


    def getAllRequests(self):
        # cursor = self.conn.cursor()
        # query = "select * from requests;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        if len(request_list) ==0:
            self.first_time()
            return request_list[0]
        row = {};
        row[0] = 'Get'
        row[1] = 'All'
        row[2] = 'Requests'
        row[3] = 'Getting...'
        row[4] = 'Successful'

        return row

    def getRequestByID(self, RequestID):
        # cursor = self.conn.cursor()
        # query = "select * from requests where RequestID = %s;"
        # cursor.execute(query, (RequestID,))
        # result = cursor.fetchone()
        # return result
        if len(request_list) ==0:
            self.first_time()
            return request_list[0]
        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'ID'
        row[4] = 'Successful'

        return row

    def getRequestBysid(self, sid):
    #     cursor = self.conn.cursor()
    #     query = "select * from requests where sid = %s;"
    #     cursor.execute(query, (sid,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

        if len(request_list) == 0:
            self.first_time()
            return request_list[0]

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'Supplier ID'
        row[4] = 'Successful'

        return row

    def getRequestByreqID(self, reqID):
        # cursor = self.conn.cursor()
        # query = "select * from requests where reqID = %s;"
        # cursor.execute(query, (reqID,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(request_list) ==0:
            self.first_time()
            return request_list[0]
        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'Requestor ID'
        row[4] = 'Successful'

        return row

    def getRequestByRID(self, rid):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rid = %s;"
        # cursor.execute(query, (rid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'Resource ID'
        row[4] = 'Successful'

        return row

    def getRequestByStatus(self, status):
        # cursor = self.conn.cursor()
        # query = "select * from requests where status = %s;"
        # cursor.execute(query, (status,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'Status'
        row[4] = 'Successful'

        return row

    def getRequestByQuantity(self, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from requests where quantity = %s;"
        # cursor.execute(query, (quantity,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'Quantity'
        row[4] = 'Successful'

        return row

    def getRequestByRIDAndStatus(self, status, rid):
        # cursor = self.conn.cursor()
        # query = "select * from requests where status = %s and rid = %s;"
        # cursor.execute(query, (status,rid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'RID and Status'
        row[4] = 'Successful'

        return row

    def getRequestByRIDAndQuantity(self, status, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from requests where status = %s and quantity = %s;"
        # cursor.execute(query, (status,quantity,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

        row = {};
        row[0] = 'Get'
        row[1] = 'Request'
        row[2] = 'By'
        row[3] = 'RID and Quantity'
        row[4] = 'Successful'

        return row

    def insert(self, RequestID, status, rid, lid, reqID, sid, amount, date):
        # cursor = self.conn.cursor()
        # query = "insert into requests(RequestID, status, rid, lid, reqID, sid, amount, date) values (%s, %s, %s, %s, %s, %s, %s, %s) returning RequestID;"
        # cursor.execute(query, (RequestID, status, rid, lid, reqID, sid, amount, date,))
        # lid = cursor.fetchone()[0]
        # self.conn.commit()
        # return lid

        row = {};
        row[0] = 'Inserted'
        row[1] = 'Request'
        row[2] = 'Successfully'

        return row

    def delete(self, RequestID):
        # cursor = self.conn.cursor()
        # query = "delete from requests where RequestID = %s;"
        # cursor.execute(query, (RequestID,))
        # self.conn.commit()
        # return RequestID

        row = {};
        row[0] = 'Deleting'
        row[1] = 'Request'
        row[2] = 'Successful'

        return row

    def update(self, RequestID, status, rid, lid, reqID, sid, amount, date):
        # cursor = self.conn.cursor()
        # query = "update requests set RequestID = %s, status = %s, rid = %s, lid = %s, reqID = %s, sid = %s, amount = %s, date = %s where RequestID = %s;"
        # cursor.execute(query, (RequestID, status, rid, lid, reqID, sid, amount, date,))
        # self.conn.commit()
        # return lid

        row = {};
        row[0] = 'Updating'
        row[1] = 'Request'
        row[2] = 'Successfully'

        return row
