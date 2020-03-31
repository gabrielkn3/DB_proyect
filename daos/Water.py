#import psycopg2
class WaterDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'Test'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'Water'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getWaterById(self, wid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '12345'
       row[1] = 'Get'
       row[2] = 'Water'
       row[3] = 'by'
       row[4] = 'ID'


       return row

    def getWaterBySize(self, wsize):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = '1 Gallon'
        row[1] = 'Get'
        row[2] = 'Water'
        row[3] = 'by'
        row[4] = 'Size'

        result.append(row)
        return result

    def getWaterByBrand(self, wbrand):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'FIJI'
        row[1] = 'Get'
        row[2] = 'Water'
        row[3] = 'By'
        row[4] = 'Brand'

        result.append(row)
        return result

    def insert(self, rid, wbrand, wsize, wdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'Inserting:'
        row[1] = 'RID'
        row[2] = 'BRAND'
        row[3] = 'SIZE'
        row[4] = 'DESCRIPTION'

        result.append(row)
        return rid

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

    def update(self, wbrand, wsize, wdescription):
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
        rid = wid+2;  #dummy code
        #select rid from Water where wid = %s;
        return rid

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
