from config.dbconfig import database_config
import psycopg2
from daos.user import userDAO

class RequesterDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host ='*' password=%s" % (database_config['dbname'],
                                                            database_config['user'],
                                                            database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select * from requester;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(self, reqid):
        cursor = self.conn.cursor()
        query = "select * from requester where reqid = %s;"
        cursor.execute(query, (reqid,))
        result = cursor.fetchone()
        return result

    def getRequesterByEmail(self, email):
        u = userDAO()
        return u.getUserByEmail(email)


    def getResourcesByREQID(self,reqid):                           #------REQUESTED RESOURCES
        query = "select rid, rname, rtype from resource where rid IN (select rid from request where reqid=%s);"
        cursor = self.conn.cursor()
        cursor.execute(query, (reqid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByLocation(self, reqlocation):
        query = "select * from requester where reqlocation=%s;"
        cursor = self.conn.cursor()
        cursor.execute(query, (reqlocation,))
        result = []
        for row in cursor:
            result.append(row)
        return result






#-----------------------------------------------------------------------------------------------------------------------
    def insert(self, uid, reqlocation):
        return None

    def update(self, reqid, reqlocation):
        # result = []
        # for i in range(0, len(req_list)):
        #     for row in req_list:
        #         if row[0] == reqid:
        #             row[2] = reqlocation
        #             result.append(row)

        return None

    def delete(self, reqid):
        # for i in range(0, len(req_list)):
        #     for row in req_list:
        #         if row[0] == reqid:
        #             req_list.remove(row)
        #             return reqid
        return None #failed