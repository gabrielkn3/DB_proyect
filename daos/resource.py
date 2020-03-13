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
        row[0] = str(69)
        row[1] = 'agua'
        row[2] = 'Fiji'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = str(420)

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
       row[0] = '69'
       row[1] = 'Fiji'
       row[2] = 'agua'
       row[3] = 'agua come-mierda'
       row[4] = 'Mall of San Juan'
       row[5] = '420'

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
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

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
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

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
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getSuppliersByResourceId(self, rid):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getRequestersByResourceId(self, rid):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getSuppliersByResourceType(self, rtype):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getRequestersByResourceType(self, rtype):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getSuppliersByResourceName(self, rname):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result

    def getRequestersByResourceName(self, rname):
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

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
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return sid

    def delete(self, rid):
        #cursor = self.conn.cursor()
        #query = "delete from parts where pid = %s;"
        #cursor.execute(query, (pid,))
        #self.conn.commit()
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return rid

    def update(self, rid, rtype, rname, rdescription, rlocation, sid):
        #cursor = self.conn.cursor()
        #query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        #cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        #self.conn.commit()
        row = {};
        result = {};
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

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
        row[0] = '69'
        row[1] = 'Fiji'
        row[2] = 'agua'
        row[3] = 'agua come-mierda'
        row[4] = 'Mall of San Juan'
        row[5] = '420'

        result[0] = row
        return result
