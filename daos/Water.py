import psycopg2
import config.dbconfig
class WaterDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select wid, rid, rname, wbrand, wsize, wdescription, rlocation from resource natural inner join water;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getWaterById(self, rid):
        cursor = self.conn.cursor()
        query = "select wid, rid, rname, wbrand, wsize, wdescription, rlocation from resource natural inner join water where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getWaterBySize(self, wsize):
        cursor = self.conn.cursor()
        query = "select wid, rid, rname, wbrand, wsize, wdescription, rlocation from resource natural inner join water where wsize = %s;"
        cursor.execute(query,(wsize,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getWaterByBrand(self, wbrand):
        cursor = self.conn.cursor()
        query = "select wid, rid, rname, wbrand, wsize, wdescription, rlocation from resource natural inner join water where wbrand = %s;"
        cursor.execute(query,(wbrand,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def insert(self, wbrand, wsize, wdescription, rid):
        cursor = self.conn.cursor()
        query = "insert into water(wbrand, wsize, wdescription, rid) values (%s, %s, %s, %s) returning wid;"
        cursor.execute(query, (wbrand, wsize, wdescription, rid,))
        wid = cursor.fetchone()[0]
        self.conn.commit()
        return wid

    def delete(self, wid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'DELETING:'
        row[1] = 'WATER'
        row[2] = 'ID: 12345'

        result.append(row)
        return wid

    def update(self, wid, wbrand, wsize, wdescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'UPDATING:'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return wbrand

    def getResourceID(self,wid):
        cursor = self.conn.cursor()
        query = "select wid from resource natural inner join water where wid = %s;"
        cursor.execute(query, (wid,))
        result = cursor.fetchone()
        return result

    def getCountByWaterId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'A'
        row[1] = 'B'
        row[2] = 'C'
        row[3] = 'D'
        row[4] = 't98765'

        result.append(row)
        return row
