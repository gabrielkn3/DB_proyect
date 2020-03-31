#import psycopg2
class ClothingDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)x
        row={};
        result = [];
        row[0] = 'ALL'
        row[1] = 'CLOTHING'
        row[2] = 'GET'
        row[3] = 'TEST'
        row[4] = 'SUCCESSFUL'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getClothingById(self, cid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = 'CID 9810'
       row[1] = 'get'
       row[2] = 'Clothing'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getClothingByBrand(self, cbrand):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'SUPREME'
        row[1] = 'Get'
        row[2] = 'Clothing'
        row[3] = 'by'
        row[4] = 'Brand'

        result.append(row)
        return result

    def getClothingByName(self, cname):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'SUPREME T-SHIRT'
        row[1] = 'Get'
        row[2] = 'Clothing'
        row[3] = 'By'
        row[4] = 'Name'


        result.append(row)
        return result

    def getClothingBySize(self, csize):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'XXL'
        row[1] = 'Get'
        row[2] = 'Clothing'
        row[3] = 'By'
        row[4] = 'Size'

        result.append(row)
        return result

    def insert(self, rid, cname, cbrand, cdescription):
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

        result.append(row)
        return rid

    def delete(self, cid):
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
        return cid

    def update(self, cid, cname, cbrand, cdescription):
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
        return cname

    def getResourceID(self,cid):
        rid = cid+2;  #dummy code
        #select rid from Clothing where cid = %s;
        return rid

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