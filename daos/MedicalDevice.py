import psycopg2
import config.dbconfig
class MedicalDeviceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host = 'localhost' password=%s" % (
            config.dbconfig.database_config['dbname'], config.dbconfig.database_config['user'],
            config.dbconfig.database_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select * from MedicalDevices;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getMedicalDevicesById(self, mdid):
        cursor = self.conn.cursor()
        query = "select * from Medical Devices where mdid = %s;"
        cursor.execute(query, (mdid,))
        result = cursor.fetchone()


        return result

    def getMedicalDevicesByName(self, mdname):
        cursor = self.conn.cursor()
        query = "select * from MedicalDevices where mdname = %s;"
        cursor.execute(query, (mdname,))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getMedicalDevicesByBrand(self, mdbrand):
        cursor = self.conn.cursor()
        query = "select * from MedicalDevices where mdbrand = %s;"
        cursor.execute(query, (mdbrand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, mdbrand, mdname, mdescription):
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

    def delete(self, mdid):
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
        return mdid

    def update(self, mdid, mdbrand, mdname, mddescription):
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
        return mdbrand

    def getResourceID(self,mdid):
        rid = mdid;  #dummy code
        #select rid from MedicalDevices where mdid = %s;
        return rid

    def getCountByMedicalDevicesId(self):
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
