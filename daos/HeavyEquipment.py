#import psycopg2
class MedicationDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllMedication(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'HID 12345'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'Heavy Equipment'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getMedicationById(self, hid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '21'
       row[1] = 'get'
       row[2] = 'Heavy Equipment'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getMedicationByName(self, hname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'POWER DRILL'
        row[1] = 'Get'
        row[2] = 'Heavy Equipment'
        row[3] = 'by'
        row[4] = 'Name'

        result.append(row)
        return result

    def getMedicationByBrand(self, hbrand):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'HOME DEPOT'
        row[1] = 'Get'
        row[2] = 'Heavy Equipment'
        row[3] = 'By'
        row[4] = 'Brand'

        result.append(row)
        return result

    def insert(self, rid, hbrand, hname, hdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
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
        rid = hid+2;  #dummy code
        #select rid from Medication where hid = %s;
        return rid

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
