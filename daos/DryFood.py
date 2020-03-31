#import psycopg2
class DryFoodDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllDryFood(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'dummydfid'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'DryFood'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getDryFoodById(self, dfid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '21'
       row[1] = 'get'
       row[2] = 'DryFood'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getDryFoodByName(self, dfname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'DryFood'
        row[3] = 'by'
        row[4] = 'Name'

        result.append(row)
        return result

    def getDryFoodByBrand(self, dfbrand):
        # cursor = self.conn.cursor()
        # query = "select * from parts where pcolor = %s;"
        # cursor.execute(query, (color,))
        # result = []
        # for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'DryFood'
        row[3] = 'By'
        row[4] = 'Brand'

        result.append(row)
        return result

    def insert(self, rid, dfbrand, dfname, dfdescription):
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

    def delete(self, dfid):
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
        return dfid

    def update(self, dfid, dfbrand, dfname, dfdescription):
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
        return dfbrand

    def getResourceID(self,dfid):
        rid = dfid+2;  #dummy code
        #select rid from DryFood where dfid = %s;
        return rid

    def getCountByDryFoodId(self):
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
