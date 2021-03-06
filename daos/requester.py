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
        query = "select reqid, firstname, lastname, email, city, country, saddress, zip from requester natural inner join useraccounts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(self, reqid):
        cursor = self.conn.cursor()
        query = "select reqid, firstname, lastname, email, city, country, saddress, zip from requester natural inner join useraccounts where reqid = %s;"
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
        query = "select reqid, firstname, lastname, email, city, country, saddress, zip from requester natural inner join useraccounts where reqlocation=%s;"
        cursor = self.conn.cursor()
        cursor.execute(query, (reqlocation,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, reqlocation, uid):
        cursor = self.conn.cursor()
        query = "insert into requester(reqlocation, uid) " \
                "values(%s, %s) returning reqid;"
        cursor.execute(query, (reqlocation, uid,))
        reqid = cursor.fetchone()
        self.conn.commit()
        return reqid



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

    def validateID(self, reqid):
        cursor = self.conn.cursor()
        query = "select * from requester where reqid = %s;"
        cursor.execute(query, (reqid,))
        result = cursor.fetchone()
        if not result:
            return False
        else:
            return True