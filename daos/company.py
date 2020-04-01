import psycopg2
class CompanyDAO:
    global elist, empty_list, eid
    elist = []
    empty_list = []
    eid = 0
    # def __init__(self):
    #     connection_url = "dbname=%s Company=%s cname=%s" % ('dbname', 'Company', 'passwd')
    #     self.conn = psycopg2.connect(connection_url)

    def first_time(self):
        row = {}
        row[0] = len(elist)
        row[1] = 69
        row[2] = "Evil Corp."
        row[3] = "Evil Stuff"
        row[4] = "We're actually quite nice once you get to know us"
        elist.append(row)

    def insert(self, sid, cname, btype, description):
        # cursor = self.conn.cursor()
        # query = "insert into Company(sid, cname, btype, description, email, phone, address) values(%s, %s, %s, %s, %s, %s, %s) returning uid;"
        # cursor.execute(query, (sid, cname, btype, description, email, phone, address,))
        # uid = cursor.fetchone()
        # self.conn.commit()
        # return uid
        row = {}
        row[0] = len(elist)
        row[1] = sid
        row[2] = cname
        row[3] = btype
        row[4] = description
        elist.append(row)
        return row[0]

    def delete(self, cid):
        # cursor = self.conn.cursor()
        # query = "delete from Company where uid = %s;"
        # cursor.execute(query, (uid,))
        # self.conn.commit()
        # return uid
        for row in elist:
            if row[0] == cid:
                elist.remove(row)
                return cid

    def update(self, uid, sid, cname, btype, description):
        # cursor = self.conn.cursor()
        # query = "update Company set sid = %s, cname = %s, btype = %s, description = %s, email = %s, phone = %s, address = %s where uid = %s;"
        # cursor.execute(query, (sid, cname, btype, description, email, phone, address, uid,))
        # self.conn.commit()
        # return uid
        # entry = {}
        # entry[0] = uid
        # entry[1] = sid
        # entry[2] = cname
        # entry[3] = btype
        # entry[4] = description
        # entry[5] = email
        # entry[6] = phone
        # entry[7] = address
        for row in elist:
            if row[0] == uid:
                row[1] = sid
                row[2] = cname
                row[3] = btype
                row[4] = description
                return row

    def getAllCompanies(self):
        # cursor = self.conn.cursor()
        # query = "select * from Company;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        if len(elist)==0:
            self.first_time()
        return elist

    def getCompanyById(self, cid):
        # cursor = self.conn.cursor()
        # query = "select * from Company where uID = %s;"
        # cursor.execute(query, (uID,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[0] == cid:
                return row
        return empty_list


    def getCompanyBySid(self, sid):
        # cursor = self.conn.cursor()
        # query = "select * from Company where sid = %s;"
        # cursor.execute(query, (sid,))
        # result = cursor.fetchone()
        # return result
        for row in elist:
            if row[1] == sid:
                return row
        return empty_list

    def getCompanyByName(self, cname):
        # cursor = self.conn.cursor()
        # query = "select * from Company where btype = %s;"
        # cursor.execute(query, (btype,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in elist:
            if row[3] == cname:
                row_list.append(row)
        return row_list

    def getCompanyByCompanyType(self, type):
        # cursor = self.conn.cursor()
        # query = "select * from Company where description = %s;"
        # cursor.execute(query, (description,))
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result
        row_list = []
        for row in elist:
            if row[4] == type:
                row_list.append(row)
        return row_list