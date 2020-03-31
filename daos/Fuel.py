#import psycopg2
class FuelDAO:
    def __init__(self):

       connection_url = "dbType=%s user=%s password=%s" % ('dbType',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pType, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'FID 12345'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'Fuel'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getFuelById(self, fid):
       # cursor = self.conn.cursor()
        #query = "select pid, pType, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '2211'
       row[1] = 'get'
       row[2] = 'Fuel'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getFuelByQuantity(self, fquantity):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = '30GAL'
        row[1] = 'Get'
        row[2] = 'Fuel'
        row[3] = 'by'
        row[4] = 'Quantity'

        result.append(row)
        return result

    def getFuelByType(self, ftype):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'DIESEL'
        row[1] = 'Get'
        row[2] = 'Fuel'
        row[3] = 'by'
        row[4] = 'Type'

        result.append(row)
        return result

    def getFuelByOctane(self, octane):
       # cursor = self.conn.cursor()
        #query = "select pid, pType, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '86octane'
       row[1] = 'get'
       row[2] = 'Fuel'
       row[3] = 'by'
       row[4] = 'octane'

       return row

    def insert(self, rid, ftype, fquantity, fdescription):
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

    def update(self, fid, ftype, fquantity, fdescription):
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
        rid = fid+2;  #dummy code
        #select rid from Fuel where fid = %s;
        return rid

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
