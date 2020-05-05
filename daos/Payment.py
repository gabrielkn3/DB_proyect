import psycopg2
import config.dbconfig
class paymentDAO:
    global example_list, empty_list, id1, id2, id3
    example_list = []
    empty_list = []
    id1 = 0
    id2 = 0
    id3 = 0
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'],
            config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = len(example_list) #pID
        row[1] = id2 #reqID
        row[2] = id3 #sID
        row[3] = 420 #pamaount
        row[4] = "credit" #payment type
        row[5] = "Used a Bank of America card" #account details
        example_list.append(row)

    def insert(self, reqid, sid, pamaount, paymentType, paymentdetails):
        # cursor = self.conn.cursor()
        # query = "insert into payment(reqid, sid, pamaount, paymentType, paymentdetails) values(%s, %s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (reqid, sid, pamaount, paymentType, paymentdetail,))
        # pid = cursor.fetchone()
        # self.conn.commit()
        # return pid
        row = {}
        row[0] = len(example_list)
        row[1] = reqid
        row[2] = sid
        row[3] = pamaount
        row[4] = paymentType
        row[5] = paymentdetails
        example_list.append(row)
        return row[0]

    def delete(self, pid):
        # cursor = self.conn.cursor()
        # query = "delete from payment where pid = %s"
        # cursor.execute(query, (pid,))
        # self.conn.commit()
        # return pid
        for row in example_list:
            if row[0] == pid:
                example_list.remove(row)
                return pid

    def update(self, pid, reqid, sid, pamaount, paymentType, paymentdetails):
        # cursor = self.conn.cursor()
        # query = "update payment set reqid = %s, sid = %s, pamaount = %s, paymentType = %s, paymentdetails = %s where = %s;"
        # cursor.execute(query, (reqid, sid, pamaount, paymentType, paymentdetails, pid,))
        # self.conn.commit()
        # return pid
        for row in example_list:
            if row[0] == pid:
                row[1] = reqid
                row[2] = sid
                row[3] = pamaount
                row[4] = paymentType
                row[5] = paymentdetails
                return row

    def getAllPayments(self):
        cursor = self.conn.cursor()
        query = "select * from payment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        # if len(example_list) == 0:
        #     self.first_time()
        # return example_list

    def getPaymentByPaymentId(self, pid):
        cursor = self.conn.cursor()
        query = "select * from payment where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result
        # for row in example_list:
        #     if row[0] == pid:
        #         return row
        # return empty_list

    def getPaymentsByRequestorId(self, reqid):
        cursor = self.conn.cursor()
        query = "select * from payment where reqid = %s;"
        cursor.execute(query, (reqid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in example_list:
        #     if row[1] == reqid:
        #         row_list.append(row)
        # return row_list

    def getPaymentsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from payment where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in example_list:
        #     if row[2] == sid:
        #         row_list.append(row)
        # return row_list

    def getPaymentsByPrice(self, pamaount):
        cursor = self.conn.cursor()
        query = "select * from payment where pamaount = %s;"
        cursor.execute(query, (pamaount,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in example_list:
        #     if row[3] == pamaount:
        #         row_list.append(row)
        # return row_list

    def getPaymentsByType(self, paymentType):
        cursor = self.conn.cursor()
        query = "select * from payment where paymentType = %s;"
        cursor.execute(query, (paymentType,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # row_list = []
        # for row in example_list:
        #     if row[4] == paymentType:
        #         row_list.append(row)
        # return row_list