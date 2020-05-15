import psycopg2
import config.dbconfig
class DryFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllDryFood(self):
        cursor = self.conn.cursor()
        query = "select dfid, rid, dfbrand, rname, cdfescription, rlocation from resource natural inner join dryfood;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getDryFoodById(self, rid):
        cursor = self.conn.cursor()
        query = "select dfid, rid, dfbrand, rname, cdfescription, rlocation from resource natural inner join dryfood where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getDryFoodByName(self, rname):
        cursor = self.conn.cursor()
        query = "select dfid, rid, dfbrand, rname, cdfescription, rlocation from resource natural inner join dryfood where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getDryFoodByBrand(self, dfbrand):
        cursor = self.conn.cursor()
        query = "select dfid, rid, dfbrand, rname, cdfescription, rlocation from resource natural inner join dryfood where dfbrand = %s;"
        cursor.execute(query, (dfbrand,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def insert(self, dfbrand, dfname, dfdescription,rid):
        cursor = self.conn.cursor()
        query = "insert into dryfood(dfbrand, dfname, cdfescription, rid) values (%s,%s,%s,%s) returning dfid;"
        cursor.execute(query, (dfbrand,dfname,dfdescription,rid,))
        dfid = cursor.fetchone()[0]
        self.conn.commit()
        return dfid

    def delete(self, dfid):
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
        return dfid

    def update(self, dfid, dfbrand, dfname, dfdescription):
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
        return dfbrand

    def getResourceID(self,dfid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join dryfood where dfid = %s;"
        cursor.execute(query, (dfid,))
        result = cursor.fetchone()
        return result

    def getCountByDryFoodId(self):
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
