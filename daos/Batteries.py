import config.dbconfig
import psycopg2
class BatteriesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select bid, rid, rname, bbrand, btype, blife, bdescription, rlocation from resource natural inner join batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getBatteriesById(self, rid):
        cursor = self.conn.cursor()
        query = "select bid, rid, rname, bbrand, btype, blife, bdescription, rlocation from resource natural inner join batteries where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getBatteriesByBrand(self, bbrand):
        cursor = self.conn.cursor()
        query = "select bid, rid, rname, bbrand, btype, blife, bdescription, rlocation from resource natural inner join batteries where bbrand = %s;"
        cursor.execute(query, (bbrand,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getBatteriesByType(self, btype):
        cursor = self.conn.cursor()
        query = "select bid, rid, rname, bbrand, btype, blife, bdescription, rlocation from resource natural inner join batteries where btype = %s;"
        cursor.execute(query, (btype,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getBatteriesByBatteryLife(self, blife):
        cursor = self.conn.cursor()
        query = "select bid, rid, rname, bbrand, btype, blife, bdescription, rlocation from resource natural inner join batteries where blife = %s;"
        cursor.execute(query, (blife,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def insert(self, bbrand, btype, blife, bdescription, rid):
        cursor = self.conn.cursor()
        query = "insert into batteries(bbrand,btype,blife,bdescription,rid) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (bbrand, btype, blife, bdescription,rid,))
        bid = cursor.fetchone()[0]
        self.conn.commit()
        return bid

    def delete(self, bid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'DELETING:'
        row[1] = 'Batteries'
        row[2] = 'deleteType'
        row[3] = 'deletelocation'
        row[4] = 'deleteid'

        result.append(row)
        return bid

    def update(self, bid, bbrand, btype, blife, bdescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pType = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pType, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'UPDATING:'
        row[1] = 'Batteries'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return btype

    def getResourceID(self,bid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join batteries where bid = %s;"
        cursor.execute(query, (bid,))
        result = cursor.fetchone()
        return result

    def getCountByBatteriesId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pType, sum(stock) from parts natural inner join supplies group by pid, pType order by pType;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = '#1 DURACELL BRAND'
        row[1] = 'PINK RABBIT'
        row[2] = 'DRUMS'
        row[3] = 'Batteries'
        row[4] = 'count'

        result.append(row)
        return row
