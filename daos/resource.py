#import psycopg2
class ResourceDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       #self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        row={};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'All'
        row[3] = 'Resources'
        row[4] = 'Test'


        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getResourceById(self, rid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       row[0] = '21'
       row[1] = 'get'
       row[2] = 'resources'
       row[3] = 'by'
       row[4] = 'iD Values'


       return row

    def getResourceByType(self, rtype):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pcolor = %s;"
        #cursor.execute(query, (color,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Resource'
        row[3] = 'By'
        row[4] = 'Type'

        result.append(row)
        return result

    def getResourceByName(self, rname):
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
        row[2] = 'resource'
        row[3] = 'by'
        row[4] = 'Name'

        result.append(row)
        return result

    def getResourceByTypeAndName(self, rtype, rname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s and pcolor = %s;"
        #cursor.execute(query, (material,color))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Resource'
        row[3] = 'By'
        row[4] = 'TypeAndName'

        result.append(row)
        return result

    def getSuppliersByResourceId(self, rid):
        row = {};
        result = [];
        row[0] = 'dummysid'
        row[1] = 'Get'
        row[2] = 'Suppliers'
        row[3] = 'by'
        row[4] = 'ResourceID'
        row[5] = 'dummyval'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def getRequestersByResourceId(self, rid):
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'requesters'
        row[3] = 'By'
        row[4] = 'ResourceID'
        row[5] = 'dummyprice'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def getSuppliersByResourceType(self, rtype):
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'suppliers'
        row[3] = 'By'
        row[4] = 'ResourceType'
        row[5] = 'dummyprice'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def getRequestersByResourceType(self, rtype):
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'requesters'
        row[3] = 'by'
        row[4] = 'ResourceType'
        row[5] = 'dummyprice'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def getSuppliersByResourceName(self, rname):
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Suppliers'
        row[3] = 'By'
        row[4] = 'Resource Name'
        row[5] = 'dummyprice'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def getRequestersByResourceName(self, rname):
        row = {};
        result = [];
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'supplies'
        row[3] = 'By'
        row[4] = 'ResourceName'
        row[5] = 'dummyprice'
        row[6] = 'dummyval2'

        result.append(row)
        return result

    def insert(self, rname, rtype, rlocation, sid):
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
        return sid

    def delete(self, rid):
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
        return rid

    def update(self, rname, rtype, rlocation):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        rid = 21 #dummy value
        row = {};
        result = [];
        row[0] = 'updaterid'
        row[1] = 'updatename'
        row[2] = 'updatetype'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result.append(row)
        return rid

    def getCountByResourceId(self):
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
