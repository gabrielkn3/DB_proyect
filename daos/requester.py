# from config.dbconfig import database_config
# import psycopg2

from daos.user import userDAO
from daos.request import RequestDAO
class RequesterDAO:
    global req_list, req_id
    req_list = []
    req_id = 0
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (database_config['dbname'],
    #                                                         database_config['user'],
    #                                                         database_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


    def first_time(self):
        row = {}
        row[0] = 7214
        row[1] = 50
        row[2] = "Ponce"
        req_list.append(row)

    def getAllRequesters(self):
        # cursor = self.conn.cursor()
        # query = "select * from supplier;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        if len(req_list) == 0:
            self.first_time()
            return req_list
        return req_list

    def getRequesterById(self, reqid):
            # cursor = self.conn.cursor()
            # query = "select * from supplier where sid = %s;"
            # cursor.execute(query, (sid,))
            # result = cursor.fetchone()
        if len(req_list) == 0:
            self.first_time()
            return req_list
        result = []
        for i in range(0, len(req_list)):
            for row in req_list:
                if row[0] == reqid:
                 result.append(row)
        return result[0]

    def getRequesterByEmail(self, email):
        u = userDAO()
        return u.getUserByEmail(email)


    def getRequesterByAddress(self, address):
        u = userDAO()
        return u.getUserByAddress(address)


    def getResourcesByREQID(self,reqid):
        r = RequestDAO()
        if self.getRequesterById(reqid):
            requests = r.getRequestByreqID(reqid)
            return requests
        else:
            return None

    def getRequestersByLocation(self, reqlocation):
        requesters = self.getAllRequesters()
        result = []
        for i in range(0, len(requesters)):
            for row in requesters:
                if row[2] == reqlocation:
                    result.append(row)
        return result

    def insert(self, uid, reqlocation):
        row={}
        row[0] = ++req_id
        row[1] = uid
        row[2] = reqlocation
        req_list.append(row)
        return req_id

    def update(self, reqid, reqlocation):
        result = []
        for i in range(0, len(req_list)):
            for row in req_list:
                if row[0] == reqid:
                    row[2] = reqlocation
                    result.append(row)

        return result

    def delete(self, reqid):
        for i in range(0, len(req_list)):
            for row in req_list:
                if row[0] == reqid:
                    req_list.remove(row)
                    return reqid
        return -1 #failed