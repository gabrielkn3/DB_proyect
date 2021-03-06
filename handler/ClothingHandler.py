from flask import jsonify

from daos.Clothing import ClothingDAO

from daos.resource import ResourceDAO


class ClothingHandler:
    def build_Clothing_dict(self, row):
        result = {};
        result['clid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['clbrand'] = row[3]
        result['clsize'] = row[4]
        result['cldescription'] = row[5]
        result['rlocation'] = row[6]

        return result

    def build_Clothing_attributes(self, clid, rid, rname, clbrand, clname, clsize, cldescription, rlocation):
        result = {};
        result['clid'] = clid
        result['rid'] = rid
        result['rname'] = rname
        result['clbrand'] = clbrand
        result['clname'] = clname
        result['clsize'] = clsize
        result['cldescription'] = cldescription
        result['rlocation'] = rlocation
        return result

    def getAllClothing(self):
        dao = ClothingDAO()
        Clothing_list = dao.getAllClothing()
        result_list = []
        for row in Clothing_list:
            result = self.build_Clothing_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getClothingById(self, clid):
        dao = ClothingDAO()
        row = dao.getClothingById(clid)
        if not row:
            return jsonify(Error = "Clothing Not Found"), 404
        else:
            Clothing = self.build_Clothing_dict(row)
            return jsonify(Clothing = Clothing)

    def getClothingByBrand(self, clbrand):
        dao = ClothingDAO()
        Clothinglist = dao.getClothingByBrand(clbrand)
        result_list = []
        if not Clothinglist:
            return jsonify(Error = "No Clothing Found with the specified Brand"), 404
        else:
            for row in Clothinglist:
                result = self.build_Clothing_dict(row)
                result_list.append(result)
            return jsonify(Clothing = result_list)

    def getClothingByName(self, clname):    #Filter by Clothing category
        dao = ClothingDAO()
        Clothinglist = dao.getClothingByName(clname)
        result_list = []
        if not Clothinglist:
            return jsonify(Error = "No Clothing Found with the Specified Name"), 404
        else:
            for row in Clothinglist:
                result = self.build_Clothing_dict(row)
                result_list.append(result)
            return jsonify(Clothing = result_list)

    def getClothingBySize(self, clsize):
        dao = ClothingDAO()
        Clothinglist = dao.getClothingBySize(clsize)
        result_list = []
        if not Clothinglist:
            return jsonify(Error="No Clothing Found with the specified Size"), 404
        else:
            for row in Clothinglist:
                result = self.build_Clothing_dict(row)
                result_list.append(result)
            return jsonify(Clothing=result_list)

    def insertClothing(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            clname = form['clname']
            clbrand = form['clbrand']
            cldescription = form['cldescription']
            clsize = form['clsize']

            if rtype and rname and rlocation and sid and clname and clbrand and clsize and cldescription:
                resourcedao = ResourceDAO()
                dao = ClothingDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                clid = dao.insert(rid, clname, clbrand, cldescription, clsize)
                result = self.build_Clothing_attributes(clid, rid, clname, clbrand, cldescription, clsize)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertClothingJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        clname = json['rname']
        clbrand = json['clbrand']
        cldescription = json['cldescription']
        clsize = json['clsize']


        if rtype and rname and rlocation and clname and clbrand and cldescription and clsize:
            resourcedao = ResourceDAO()
            dao = ClothingDAO()
            rid = resourcedao.insert(rtype, rname, rlocation)
            clid = dao.insert(clbrand, clname, clsize, cldescription, rid)
            result = self.build_Clothing_attributes(clid, rid, rname, clname, clbrand, cldescription,clsize, rlocation)
            return jsonify(Clothing=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteClothing(self, clid):
        dao = ClothingDAO()
        resourceDAO = ResourceDAO()

        if not dao.getClothingById(clid):
            return jsonify(Error = "Clothing not found."), 404
        else:
            rid = dao.getResourceID(clid)
            dao.delete(clid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateClothing(self, clid, form):
        resourceDAO = ResourceDAO()
        dao = ClothingDAO()
        if not dao.getClothingById(clid):
            return jsonify(Error = "Clothing not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                clname = form['clname']
                clbrand = form['clbrand']
                cldescription = form['cldescription']
                clsize = form['clsize']

                rid = dao.getResourceID(clid)

                if rtype and rname and rlocation and sid and clname and clbrand and cldescription and clsize:
                    dao.update(clid, clname, clbrand, cldescription, clsize)
                    resourceDAO.update(rid, rname,rtype,rlocation)
                    result = self.build_Clothing_attributes(clid, rid, clname, clbrand,cldescription, clsize)
                    return jsonify(Clothing=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Clothing_counts(self, Clothing_counts):
        result = []
        #print(part_counts)
        for P in Clothing_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByClothingId(self):
        dao = ClothingDAO()
        result = dao.getCountByClothingId()
        #print(self.build_part_counts(result))
        #return jsonify(ClothingCounts = self.build_Clothing_counts(result)), 200
        return jsonify(ClothingCounts=result), 200
