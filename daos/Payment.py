import psycopg2
class paymentDAO:
    global example_list, empty_list, id1, id2, id3
    example_list = []
    empty_list = []
    id1 = 0
    id2 = 0
    id3 = 0
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % ('dbname', 'user', 'passwd')
    #     self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = id1 #pID
        row[1] = id2 #reqID
        row[2] = id3 #sID
        row[3] = 420.69 #price
        row[4] = "culo" #payment type
        row[5] = "The single best piece of ass I've had" #account details
        example_list.append(row)

    def insert(self, reqid, sid, price, paymentType, acDetails):
        # cursor = self.conn.cursor()
        # query = "insert into payment(reqid, sid, price, paymentType, acDetail) values(%s, %s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (reqid, sid, price, paymentType, acDetail,))
        # pid = cursor.fetchone()
        # self.conn.commit()
        # return pid
        row = {}
        row[0] = ++id1
        row[1] = reqid
        row[2] = sid
        row[3] = price
        row[4] = paymentType
        row[5] = acDetails
        example_list.append(row)
        return row[0]

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from payment where pid = %s"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, pid, reqid, sid, price, paymentType, acDetails):
        cursor = self.conn.cursor()
        query = "update payment set reqid = %, sid = %s, price = %s, paymentType = %s, acDetail = %s where = %s;"
        cursor.execute(query, (reqid, sid, price, paymentType, acDetails, pid,))
        self.conn.commit()
        return pid

    def getAllPayments(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(example_list) == 0:
            self.first_time()
        return example_list

    def getPaymentByPaymentId(self, pid):
        # cursor = self.conn.cursor()
        # query = "select * from payment where pid = %s;"
        # cursor.execute(query, (pid,))
        # result = cursor.fetchone()
        # return result
        for row in example_list:
            if row[0] == pid:
                return row
        return empty_list

    def getPaymentsByRequestorId(self, reqid):
        # cursor = self.conn.cursor()
        # query = "select * from payment where reqid = %s;"
        # cursor.execute(query, (reqid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in example_list:
            if row[1] == reqid:
                row_list.append(row)
        return row_list

    def getPaymentsBySupplierId(self, sid):
        # cursor = self.conn.cursor()
        # query = "select * from payment where sid = %s;"
        # cursor.execute(query, (sid,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in example_list:
            if row[2] == sid:
                row_list.append(row)
        return row_list

    def getPaymentsByPrice(self, price):
        # cursor = self.conn.cursor()
        # query = "select * from payment where price = %s;"
        # cursor.execute(query, (price,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in example_list:
            if row[3] == price:
                row_list.append(row)
        return row_list

    def getPaymentsByType(self, paymentType):
        # cursor = self.conn.cursor()
        # query = "select * from payment where paymentType = %s;"
        # cursor.execute(query, (paymentType,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in example_list:
            if row[3] == paymentType:
                row_list.append(row)
        return row_list