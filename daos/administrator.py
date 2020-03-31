import psycopg2
class adminDAO:
    global elist, empty_list, eid1, eid2
    elist = []
    eid1 = 0
    eid2 = 0
    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s" % ('dbname', 'user', 'passwd')
    #     self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = eid1
        row[1] = eid2
        elist.append(row)

    def insert(self, uid):
        cursor = self.conn.cursor()
        query = "insert into administrator(uid) values(%s) returning aid;"
        cursor.execute(query, (uid,))
        aid = cursor.conn.commit()
        return aid

    def delete(self, aid):
        cursor = self.conn.cursor()
        query = "delete from administrator where aid = %s;"
        cursor.execute(query, (aid,))
        self.conn.commit()
        return aid

    #update not necessary

    def getAllAdmins(self):
        # cursor = self.conn.cursor()
        # query = "select * from administrator;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(elist) == 0:
            self.first_time()
        return elist

    def getAdminByAdminId(self, aid):
        # cursor = self.conn.cursor()
        # query = "select * from administrator where aid = %s;"
        # cursor.execute(query, (aid,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[0] == aid:
                return row
        return empty_list

    def getAdminByUserId(self, uid):
        # cursor = self.conn.cursor()
        # query = "select * from administrator where uid = %s;"
        # cursor.execute(query, (uid,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[1] == uid:
                return row
        return empty_list