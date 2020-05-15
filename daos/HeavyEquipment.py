import psycopg2
import config.dbconfig
class HeavyEquipmentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquipment(self):
        cursor = self.conn.cursor()
        query = "select hid, rid, rname, hbrand, hdescription, rlocation from resource natural inner join heavyequipment;"
        cursor.execute(query)
        result = [];
        for row in cursor:
           result.append(row)
        return result

    def getHeavyEquipmentById(self, rid):
        cursor = self.conn.cursor()
        query = "select hid, rid, rname, hbrand, hdescription, rlocation from resource natural inner join heavyequipment where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()

        return result

    def getHeavyEquipmentByName(self, rname):
        cursor = self.conn.cursor()
        query = "select hid, rid, rname, hbrand, hdescription, rlocation from resource natural inner join heavyequipment where rname = %s;"
        cursor.execute(query, (rname,))
        result = [];
        for row in cursor:
           result.append(row)
        return result

    def getHeavyEquipmentByBrand(self, hbrand):
        cursor = self.conn.cursor()
        query = "select hid, rid, rname, hbrand, hdescription, rlocation from resource natural inner join heavyequipment where hbrand = %s;"
        cursor.execute(query, (hbrand,))
        result = [];
        for row in cursor:
           result.append(row)
        return result

    def insert(self, hbrand, hname, hdescription,rid):
        cursor = self.conn.cursor()
        query = "insert into heavyEquipment values (%s, %s, %s, %s) returning hid;"
        cursor.execute(query, (hbrand,hname,hdescription, rid,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def delete(self, hid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'DELETING:'
        row[1] = 'deletetype'
        row[2] = 'deletename'
        row[3] = 'deletelocation'
        row[4] = 'deleteid'

        result.append(row)
        return hid

    def update(self, hid, hbrand, hname, hdescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'UPDATE:'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return hbrand

    def getResourceID(self,hid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join heavyequipment where hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()

        return result

    def getCountByHeavyEquipmentId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'ABC'
        row[1] = 'DEF'
        row[2] = 'GHI'
        row[3] = 'JKL'
        row[4] = 'MNO'

        result.append(row)
        return row
