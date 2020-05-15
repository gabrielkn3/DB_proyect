import psycopg2
import config.dbconfig
class CannedFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCannedFood(self):
        cursor = self.conn.cursor()
        query = "select cfid, rid, rname, cfbrand, cfdescription, rlocation from resource natural inner join cannedfood;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getCannedFoodById(self, rid):
        cursor = self.conn.cursor()
        query = "select cfid, rid, rname, cfbrand, cfdescription, rlocation from resource natural inner join cannedfood where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()

        return result

    def getCannedFoodByName(self, cfname):
        cursor = self.conn.cursor()
        query = "select cfid, rid, rname, cfbrand, cfdescription, rlocation from resource natural inner join cannedfood where cfname = %s;"
        cursor.execute(query,(cfname,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getCannedFoodByBrand(self, cfbrand):
        cursor = self.conn.cursor()
        query = "select cfid, rid, rname, cfbrand, cfdescription, rlocation from resource natural inner join cannedfood where cfbrand = %s;"
        cursor.execute(query,(cfbrand,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def insert(self, cfbrand, cfname, cfdescription, rid):
        cursor = self.conn.cursor()
        query = "insert into cannedfood(cfbrand, cfname, cfdescription, rid) values (%s, %s, %s, %s) returning cfid;"
        cursor.execute(query, (cfbrand, cfname, cfdescription,rid,))
        cfid = cursor.fetchone()[0]
        self.conn.commit()
        return cfid

    def delete(self, cfid):
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
        return cfid

    def update(self, cfid, cfbrand, cfname, cfdescription):
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
        return cfbrand

    def getResourceID(self,cfid):
        cursor = self.conn.cursor()
        query = "select cfid, rid, rname, cfbrand, cfdescription, rlocation from resource natural inner join cannedfood where cfid = %s;"
        cursor.execute(query, (cfid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCountByCannedFoodId(self):
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
