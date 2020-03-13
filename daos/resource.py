import psycopg2
class ResourceDAO:
    def __init__(self):

       connection_url = "dbname=%s user=%s password=%s" % ('dbname',
                                                    'user',
                                                          'passwd')
       self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        result = 'Returns List of Resources'
        #for row in cursor:
        #    result.append(row)
        return result

    def getResourcesById(self, rid):
       # cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
        result = 'Returns Resources by ID ' + str(rid)
        return result

    def getResourceByType(self, rtype):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pcolor = %s;"
        #cursor.execute(query, (color,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        result = 'Returns Resources by Type/Category: '  + str(rtype)
        return result

    def getResourceByName(self, rname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s;"
        #cursor.execute(query, (material,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        result = 'Returns Resources by Name: ' + str(rname)
        return result

    def getResourceByTypeAndName(self, rtype, rname):
        #cursor = self.conn.cursor()
        #query = "select * from parts where pmaterial = %s and pcolor = %s;"
        #cursor.execute(query, (material,color))
        #result = []
        #for row in cursor:
        #    result.append(row)
        result = 'Returns Resources by Type and Name: ' + str(rtype) + ', ' + str(rname)
        return result

    def getSuppliersByResourceId(self, rid):
        result = 'Returns Suppliers by Resource ID ' + str(rid)
        return result

    def getRequestersByResourceId(self, rid):
        result = 'Returns Requesters by Resource ID ' + str(rid)
        return result

    def getSuppliersByResourceType(self, rtype):
        result = 'Returns Suppliers by Resource Type ' + str(rtype)
        return result

    def getRequestersByResourceType(self, rtype):
        result = 'Returns Requesters by Resource Type ' + str(rtype)
        return result

    def getSuppliersByResourceName(self, rname):
        result = 'Returns Suppliers by Resource Name ' + str(rname)
        return result

    def getRequestersByResourceName(self, rname):
        result = 'Returns Requesters by Resource Name ' + str(rname)
        return result

    def insert(self, rtype, rname, rdescription, rlocation, sid):
        #cursor = self.conn.cursor()
        #query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        #pid = cursor.fetchone()[0]
        #self.conn.commit()
        rid = 'Inserts Resource into db and returns resource id'
        return rid

    def delete(self, rid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        result = 'Erases entry and returns' + str(rid)
        return rid

    def update(self, rid, rtype, rname, rdescription, rlocation, sid):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        result = 'Updates Entry ' + str(rid)
        return rid

    def getCountByResourceID(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        result = 'Returns # of Resources Available'
        return result
