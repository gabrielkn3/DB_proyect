import config.dbconfig
import psycopg2
class GeneratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGenerator(self):
        cursor = self.conn.cursor()
        query = "select gid, rid, rname, gbrand, gfueltype, gpowerOutput, gdescription, rlocation from resource natural inner join powerGenerators;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getGeneratorById(self, rid):
        cursor = self.conn.cursor()
        query = "select gid, rid, rname, gbrand, gfueltype, gpowerOutput, gdescription, rlocation from resource natural inner join powerGenerators where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getGeneratorByFuelType(self, gfueltype):
        cursor = self.conn.cursor()
        query = "select gid, rid, rname, gbrand, gfueltype, gpowerOutput, gdescription, rlocation from resource natural inner join powerGenerators where gfueltype = %s;"
        cursor.execute(query,(gfueltype,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getGeneratorByPowerOutput(self, gpoweroutput):
        cursor = self.conn.cursor()
        query = "select gid, rid, rname, gbrand, gfueltype, gpowerOutput, gdescription, rlocation from resource natural inner join powerGenerators where gpowerOutput = %s;"
        cursor.execute(query,(gpoweroutput,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def insert(self, gbrand, gfueltype, gpoweroutput, gdescription,rid):
        cursor = self.conn.cursor()
        query = "insert into powerGenerators values (%s, %s, %s, %s, %s) returning gid;"
        cursor.execute(query, (gbrand, gfueltype, gpoweroutput, gdescription, rid,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def delete(self, gid):
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
        row[5] = 'Dummyval'

        result.append(row)
        return gid

    def update(self, gid, gbrand, gfueltype, gpoweroutput, gdescription):
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
        return gbrand

    def getResourceID(self,gid):
        cursor = self.conn.cursor()
        query = "select rid from resource natural inner join powerGenerators where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getCountByGeneratorId(self):
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
