import psycopg2
import config.dbconfig
class MedicationDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select mid,rid,rname,mdosage,mdescription,rlocation from medications natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getMedicationById(self, rid):
        cursor = self.conn.cursor()
        query = "select mid,rid,rname,mdosage, mdescription,rlocation from medications natural inner join resource where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result



    def getMedicationByDosage(self, mdosage):
        cursor = self.conn.cursor()
        query = "select mid,rid,rname,mdosage,mdescription,rlocation from medications natural inner join resource where mdosage = %s;"
        cursor.execute(query, (mdosage,))
        result = []
        for row in cursor:
           result.append(row)

        return result

    def getMedicationByName(self, rname):
        cursor = self.conn.cursor()
        query = "select mid,rid,rname,mdosage, mdescription,rlocation from medications natural inner join resource where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
           result.append(row)

        return result

    def insert(self, mname, mdosage, mdescription,rid):
        cursor = self.conn.cursor()
        query = "insert into medications(mname, mdosage, mdescription, rid) values (%s, %s, %s, %s) returning mid;"
        cursor.execute(query, (mname, mdosage, mdescription, rid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()

        return mid

    def delete(self, mid):
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
        return mid

    def update(self, mid, mname, mdosage, mdescription):
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
        return mname

    def getResourceID(self,mid):
        cursor = self.conn.cursor()
        query = "select rid from medications natural inner join resource where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()

        return result

    def getCountByMedicationId(self):
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
