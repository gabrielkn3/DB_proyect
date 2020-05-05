import psycopg2
import config.dbconfig
class ToolDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTool(self):
        cursor = self.conn.cursor()
        query = "select tid,rid,rname, tbrand, tdescription, rlocation from resource natural inner join tools;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getToolById(self, rid):
        cursor = self.conn.cursor()
        query = "select tid,rid,rname, tbrand, tdescription, rlocation from resource natural inner join tools where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getToolByName(self, rname):
        cursor = self.conn.cursor()
        query = "select tid,rid,rname, tbrand, tdescription, rlocation from resource natural inner join tools where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolByBrand(self, tbrand):
        def getToolByName(self, tbrand):
            cursor = self.conn.cursor()
            query = "select tid,rid,rname, tbrand, tdescription, rlocation from resource natural inner join tools where tbrand = %s;"
            cursor.execute(query, (tbrand,))
            result = []
            for row in cursor:
                result.append(row)
            return result


    def insert(self, rid, tbrand, tname, tdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'inserttype'
        row[2] = 'insertname'
        row[3] = 'insertlocation'
        row[4] = 'Insertdescription'

        result.append(row)
        return rid

    def delete(self, tid):
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
        row[4] = 'deleteid'

        result.append(row)
        return tid

    def update(self, tid, tbrand, tname, tdescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'updaterid'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return tbrand

    def getResourceID(self,tid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join tools where tid = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result

    def getCountByToolId(self):
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
        row[4] = 'two number 45s, one with cheese and a large soda'

        result.append(row)
        return row
