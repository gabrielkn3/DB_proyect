import psycopg2
class adminDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % ('dbname', 'user', 'passwd')
        self.conn = psycopg2.connect(connection_url)

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
        cursor = self.conn.cursor()
        query = "select * from administrator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminByAdminId(self, aid):
        cursor = self.conn.cursor()
        query = "select * from administrator where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAdminByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from administrator where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result