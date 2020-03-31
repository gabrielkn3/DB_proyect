#import psycopg2
class BatteriesDAO:
    def __init__(self):

       connection_url = "dbType=%s user=%s password=%s" % ('dbType',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pType, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)x
        row={};
        result = [];
        row[0] = 'ALL'
        row[1] = 'Batteries'
        row[2] = 'GET'
        row[3] = 'TEST'
        row[4] = 'SUCCESSFUL'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getBatteriesById(self, bid):
       # cursor = self.conn.cursor()
        #query = "select pid, pType, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = 'bid 9810'
       row[1] = 'get'
       row[2] = 'Batteries'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getBatteriesByBrand(self, bbrand):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'DURACELL'
        row[1] = 'Get'
        row[2] = 'Batteries'
        row[3] = 'by'
        row[4] = 'Brand'

        result.append(row)
        return result

    def getBatteriesByType(self, btype):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'AAA'
        row[1] = 'Get'
        row[2] = 'Batteries'
        row[3] = 'By'
        row[4] = 'Type'


        result.append(row)
        return result

    def getBatteriesByBatteryLife(self, batteryLife):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = '10 Hours'
        row[1] = 'Get'
        row[2] = 'Batteries'
        row[3] = 'By'
        row[4] = 'BatteryLife'

        result.append(row)
        return result

    def insert(self, rid, btype, bbrand, bdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pType, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pType, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'INSERTING:'
        row[1] = 'Batteries'
        row[2] = 'insertType'
        row[3] = 'insertlocation'
        row[4] = 'Insertdescription'

        result.append(row)
        return rid

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

    def update(self, bid, btype, bbrand, bdescription):
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
        rid = bid+2;  #dummy code
        #select rid from Batteries where bid = %s;
        return rid

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
