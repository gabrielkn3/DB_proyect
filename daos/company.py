from config.dbconfig import database_config
import psycopg2
class CompanyDAO: 
    def __init__(self):

        connection_url = "dbname=%s user=%s host = '*' password=%s" % (database_config['dbname'],
                                                            database_config['user'],
                                                            database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllCompanies(self):
        cursor = self.conn.cursor()
        query = "select * from company;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getCompanyById(self, cid):
        cursor = self.conn.cursor()
        query = "select * from company where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result


    def getCompanyBySid(self, sid):
        cursor = self.conn.cursor()
        query = "select * from company where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result


    def getCompanyByName(self, cname):
        cursor = self.conn.cursor()
        query = "select * from company where companyname = %s;"
        cursor.execute(query, (cname,))
        result = cursor.fetchone()
        return result


    def getCompanyByType(self, btype):
        cursor = self.conn.cursor()
        query = "select * from company where businesstype = %s;"
        cursor.execute(query, (btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, companyname, businesstype, cdescription, sid):
        cursor = self.conn.cursor()
        query = "insert into company(companyname, businesstype, cdescription, sid) values(%s, %s, %s, %s) returning cid;"
        cursor.execute(query, (companyname, businesstype, cdescription, sid,))
        cid = cursor.fetchone()
        self.conn.commit()
        return cid




   ###################################################################################################################################################################
    def delete(self, cid):
        # cursor = self.conn.cursor()
        # query = "delete from Company where uid = %s;"
        # cursor.execute(query, (uid,))
        # self.conn.commit()
        # return uid
        return None

    # def update(self, uid, sid, cname, btype, description):
    #     cursor = self.conn.cursor()
    #     query = "update Company set sid = %s, cname = %s, btype = %s, description = %s, email = %s, phone = %s, address = %s where uid = %s;"
    #     cursor.execute(query, (sid, cname, btype, description, email, phone, address, uid,))
    #     self.conn.commit()
    #     return uid
    #     entry = {}
    #     entry[0] = uid
    #     entry[1] = sid
    #     entry[2] = cname
    #     entry[3] = btype
    #     entry[4] = description
    #     entry[5] = email
    #     entry[6] = phone
    #     entry[7] = address
