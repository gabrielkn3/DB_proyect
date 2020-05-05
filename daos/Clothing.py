import config.dbconfig
import psycopg2
class ClothingDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select clid, rid, rname, clbrand, clsize, cldescription, rlocation from resource natural inner join clothing"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getClothingById(self, rid):
        cursor = self.conn.cursor()
        query = "select clid, rid, rname, clbrand, clsize, cldescription, rlocation from resource natural inner join clothing where rid = %s"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getClothingByBrand(self, clbrand):
        cursor = self.conn.cursor()
        query = "select clid, rid, rname, clbrand, clsize, cldescription, rlocation from resource natural inner join clothing where clbrand = %s"
        cursor.execute(query,(clbrand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingByName(self, rname):
        cursor = self.conn.cursor()
        query = "select clid, rid, rname, clbrand, clsize, cldescription, rlocation from resource natural inner join clothing where rname = %s"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingBySize(self, clsize):
        cursor = self.conn.cursor()
        query = "select clid, rid, rname, clbrand, clsize, cldescription, rlocation from resource natural inner join clothing where clsize = %s"
        cursor.execute(query, (clsize,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, clbrand, clname, clsize, cldescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'INSERTING:'
        row[1] = 'clothing'
        row[2] = 'insertname'
        row[3] = 'insertlocation'
        row[4] = 'Insertdescription'
        row[5] = 'DUMMYVAL'

        result.append(row)
        return rid

    def delete(self, clid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'DELETING:'
        row[1] = 'clothing'
        row[2] = 'deletename'
        row[3] = 'deletelocation'
        row[4] = 'deleteid'

        result.append(row)
        return clid

    def update(self, clid, clbrand, clname, clsize, cldescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'UPDATING:'
        row[1] = 'clothing'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return clname

    def getResourceID(self,clid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join clothing where clid = %s"
        cursor.execute(query, (clid,))
        result = cursor.fetchone()
        return result

    def getCountByClothingId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = '$3000 versace jacket'
        row[1] = '$500 sneakers'
        row[2] = '$900 tshirt'
        row[3] = 'clothing'
        row[4] = 'count'

        result.append(row)
        return row
