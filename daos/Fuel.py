import config.dbconfig
import psycopg2
class FuelDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select fid, rid, rname, ftype, fquantity, foctane, fdescription, rlocation from resource natural inner join fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getFuelById(self, rid):
        cursor = self.conn.cursor()
        query = "select fid, rid, rname, ftype, fquantity, foctane, fdescription, rlocation from resource natural inner join fuel where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()

        return result

    def getFuelByQuantity(self, fquantity):
        cursor = self.conn.cursor()
        query = "select fid, rid, rname, ftype, fquantity, foctane, fdescription, rlocation from resource natural inner join fuel where fquantity = %s;"
        cursor.execute(query,(fquantity,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getFuelByType(self, ftype):
        cursor = self.conn.cursor()
        query = "select fid, rid, rname, ftype, fquantity, foctane, fdescription, rlocation from resource natural inner join fuel where ftype = %s;"
        cursor.execute(query,(ftype,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getFuelByOctane(self, foctane):
        cursor = self.conn.cursor()
        query = "select fid, rid, rname, ftype, fquantity, foctane, fdescription, rlocation from resource natural inner join fuel where foctane = %s;"
        cursor.execute(query, (foctane,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def insert(self, rid, ftype, fquantity, octane, fdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pType, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pType, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'INSERTING:'
        row[1] = 'inserttype'
        row[2] = 'insertname'
        row[3] = 'insertlocation'
        row[4] = 'Insertdescription'


        result.append(row)
        return rid

    def delete(self, fid):
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
        return fid

    def update(self, fid, ftype, fquantity, octane, fdescription):
        #cursor = self.conn.cursor()
        #query = "update parts set pType = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pType, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'UPDATE:'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return ftype

    def getResourceID(self,fid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join fuel where fid = %s;"
        cursor.execute(query, (fid,))
        result = cursor.fetchone()

        return result

    def getCountByFuelId(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pType, sum(stock) from parts natural inner join supplies group by pid, pType order by pType;"
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
