import psycopg2
import config.dbconfig
class stocksDAO:
    global example_list, empty_list, id1, id2, id3, id4, number
    example_list = []
    empty_list = []
    id1 = 0
    id2 = 0
    id3 = id1
    id4 = id2
    number = 69
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'],
            config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = id1 #sid
        row[1] = id2 #rid
        row[2] = number #squantity
        example_list.append(row)

    def insert(self, sid, rid, squantity):
        # cursor = self.conn.cursor()
        # query = "insert into stocks(sid, rid, squantity) values(%s, %s, %s) returning primary key;"
        # cursor.execute(query, (sid, rid, squantity,))
        # pkey = cursor.fetchone()
        # self.conn.commit()
        # return pkey
        row = {}
        row[0] = int(sid)
        row[1] = int(rid)
        row[2] = int(squantity)
        example_list.append(row)
        return row

    def delete(self, sid, rid):
        # cursor = self.conn.cursor()
        # query = "delete from stocks where sid = %s and rid = %s;"
        # cursor.execute(query, (sid, rid,))
        # self.conn.commit()
        # return {sid, rid}
        for row in example_list:
            if row[0] == sid and row[1] == rid:
                example_list.remove(row)
                return {sid, rid}

    def update(self, sid, rid, squantity):
        # cursor = self.conn.cursor()
        # query = "update payment set squantity = %s where sid = %s and rid = %s;"
        # cursor.execute(query, (squantity, sid, rid))
        # self.conn.commit()
        # return {sid, rid}
        for row in example_list:
            if row[0] == sid and row[1] == rid:
                row[2] = squantity
                return {sid, rid}

    def getAllStocks(self):
        cursor = self.conn.cursor()
        query = "select * from stocks;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        # if len(example_list) == 0:
        #     self.first_time()
        # return example_list

    def getStocksBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from stocks where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for row in example_list:
        #     if row[0] == sid:
        #         result.append(row)
        # return result

    def getStocksByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from stocks where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for row in example_list:
        #     if row[1] == rid:
        #         result.append(row)
        # return result

    def getStocksBysQuantity(self, squantity):
        cursor = self.conn.cursor()
        query = "select * from stocks where squantity = %s;"
        cursor.execute(query, (squantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for row in example_list:
        #     if row[2] == squantity:
        #         result.append(row)
        # return result

    def getStocksByStockId(self, sid, rid):
        cursor = self.conn.cursor()
        query = "select * from stocks where sid = %s and rid = %s;"
        cursor.execute(query, (sid, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for row in example_list:
        #     if row[0] == sid and row[1] == rid:
        #         result.append(row)
        # return result

    def getStocksByResourceIdAndQuantity(self, rid, squantity):
        cursor = self.conn.cursor()
        query = "selct * from stocks where rid = %s and squantity = %s;"
        cursor.exectue(query, (rid, squantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        # result = []
        # for row in example_list:
        #     if row[1] == rid and row[2] == squantity:
        #         result.append(row)
        # return result


