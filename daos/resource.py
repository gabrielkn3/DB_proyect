import psycopg2
import config.dbconfig
class ResourceDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
           config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'], config.dbconfig.database_config['passwd'])
       self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource order by rname;"
        cursor.execute(query)
        result = [];
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resource where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()


        return result

    def getResourceByType(self, rtype):
        cursor = self.conn.cursor()
        query = "select * from resource where rtype = %s order by rtype;"
        cursor.execute(query, (rtype,))
        result = [];
        for row in cursor:
            result.append(row)

        return result

    def getResourceByName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)

        return result


    def getResourceByrequestID(self, requestID):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rname, rlocation from resource natural inner join request where requestID = %s;"
        cursor.execute(query, (requestID,))
        result = cursor.fetchone()

        return result

    def getResourceByTypeAndName(self, rtype, rname):
        cursor = self.conn.cursor()
        query = "select * from resource where rtype = %s and rname = %s;"
        cursor.execute(query, (rtype, rname))
        result = []
        for row in cursor:
           result.append(row)

        return result

    def getSuppliersByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select sid,slocation,rname from supplier natural inner join stocks natural inner join resource where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequestersByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select reqid,reqlocation from requester natural inner join request where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSuppliersByResourceType(self, rtype):
        cursor = self.conn.cursor()
        query = "select sid, slocation from supplier natural inner join listing natural inner join resource where rtype = %s;"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequestersByResourceType(self, rtype):
        cursor = self.conn.cursor()
        query = "select reqid,reqlocation from requester natural inner join request natural inner join resource where rtype = %s;"
        cursor.execute(query, (rtype,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getSuppliersByResourceName(self, rname):
        cursor = self.conn.cursor()
        query = "select sid, slocation from supplier natural inner join listing natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getRequestersByResourceName(self, rname):
        cursor = self.conn.cursor()
        query = "select reqid,reqlocation from requester natural inner join request natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def insert(self, rtype, rname, rlocation):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, rtype, rlocation) values (%s, %s, %s) returning pid;"
        cursor.execute(query, (rname,rtype,rlocation,))
        rid = cursor.fetchone()[0]
        self.conn.commit()

        return rid

    def delete(self, rid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'deleterid'
        row[1] = 'deletetype'
        row[2] = 'deletename'
        row[3] = 'deletelocation'

        result.append(row)
        return rid

    def update(self, rid, rname, rtype, rlocation):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        rid = 21 #dummy value
        row = {};
        result = [];
        row[0] = 'updaterid'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[3] = 'updatelocation'

        result.append(row)
        return rid

    def getCountByResourceId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'two number 9s'
        row[1] = 'a number 9 large'
        row[2] = 'a number 6 with extra dip'
        row[3] = 'a number 7'

        result.append(row)
        return row
