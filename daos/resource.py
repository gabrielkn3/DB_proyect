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
        row[5] = 'dummyprice'

        result.append(row)
        #for row in cursor:
        #    result.append(row)
        return result

    def getResourcesById(self, rid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
       row = {};
       result = {};
       row[0] = 'dummyrid'
       row[1] = 'Get'
       row[2] = 'Resources'
       row[3] = 'By'
       row[4] = 'ID Values'
       row[5] = 'dummyprice'

       result[0] = row
       return result

    def getResourceByType(self, rtype):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pcolor = %s;"
        #cursor.execute(query, (color,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Resource'
        row[3] = 'By'
        row[4] = 'Type'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getResourceByName(self, rname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'resource'
        row[3] = 'by'
        row[4] = 'Name'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getResourceByTypeAndName(self, rtype, rname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s and pcolor = %s;"
        #cursor.execute(query, (material,color))
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Resource'
        row[3] = 'By'
        row[4] = 'TypeAndName'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getSuppliersByResourceId(self, rid):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Suppliers'
        row[3] = 'by'
        row[4] = 'ResourceID'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getRequestersByResourceId(self, rid):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'requesters'
        row[3] = 'By'
        row[4] = 'ResourceID'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getSuppliersByResourceType(self, rtype):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'suppliers'
        row[3] = 'By'
        row[4] = 'ResourceType'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getRequestersByResourceType(self, rtype):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'get'
        row[2] = 'requesters'
        row[3] = 'by'
        row[4] = 'ResourceType'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getSuppliersByResourceName(self, rname):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'Suppliers'
        row[3] = 'By'
        row[4] = 'Resource Name'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def getRequestersByResourceName(self, rname):
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'Get'
        row[2] = 'supplies'
        row[3] = 'By'
        row[4] = 'ResourceName'
        row[5] = 'dummyprice'

        result[0] = row
        return result

    def insert(self, rtype, rname, rdescription, rlocation, sid):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        row = {};
        result = {};
        row[0] = 'dummyrid'
        row[1] = 'inserttype'
        row[2] = 'insertname'
        row[3] = 'insertlocation'
        row[4] = 'Insertdescription'
        row[5] = 'dummysid'

        result[0] = row
        return sid

    def delete(self, rid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = {};
        row[0] = 'deleterid'
        row[1] = 'deletetype'
        row[2] = 'deletename'
        row[3] = 'deletelocation'
        row[4] = 'deletedescription'
        row[5] = 'deletesid'

        result[0] = row
        return rid

    def update(self, rid, rtype, rname, rdescription, rlocation, sid):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = {};
        row[0] = 'updaterid'
        row[1] = 'updatetype'
        row[2] = 'updatename'
        row[3] = 'updatedescription'
        row[4] = 'updatelocation'
        row[5] = 'updatesid'

        result[0] = row
        return rid

    def getCountByResourceID(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        row = {};
        result = {};
        row[0] = 'two number 9s'
        row[1] = 'a number 9 large'
        row[2] = 'a number 6 with extra dip'
        row[3] = 'a number 7'
        row[4] = 'two number 45s, one with cheese'
        row[5] = 'and a large soda'

        result[0] = row
        return result
