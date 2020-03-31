#import psycopg2
class GeneratorDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllGenerator(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'dummygid'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'Generator'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getGeneratorById(self, gid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '21'
       row[1] = 'get'
       row[2] = 'Generator'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getGeneratorByFuelType(self, gfueltype):
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
        row[2] = 'Generator'
        row[3] = 'by'
        row[4] = 'Fuel Type'

        result.append(row)
        return result

    def getGeneratorByPowerOutput(self, gpoweroutput):
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
        row[2] = 'Generator'
        row[3] = 'By'
        row[4] = 'Power Output'

        result.append(row)
        return result

    def insert(self, rid, gbrand, gfueltype, gpoweroutput, gdescription):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'inserttype'
        row[2] = 'insergfueltype'
        row[3] = 'insertlocation'
        row[4] = 'Insergdescription'

        result.append(row)
        return rid

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
        rid = gid+2;  #dummy code
        #select rid from Generator where gid = %s;
        return rid

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
