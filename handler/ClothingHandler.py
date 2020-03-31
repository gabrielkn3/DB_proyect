from flask import jsonify

from daos.Clothing import ClothingDAO

from daos.resource import ResourceDAO


class ClothingHandler:
    def build_Clothing_dict(self, row):
        result = {};
        result['cid'] = row[0]
        result['rid'] = row[1]
        result['cname'] = row[2]
        result['cbrand'] = row[3]
        result['cdescription'] = row[4]
        result['csize'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['stype'] = row[1]
        result['sname'] = row[2]
        result['semail'] = row[3]
        result['sphone'] = row[4]
        result['saddress'] = row[5]
        result['sfinance'] = row[6]
        return result

    def build_requester_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ReqID'] = row[1]
        result['rfirstname'] = row[2]
        result['rlastname'] = row[3]
        result['remail'] = row[4]
        result['rphone'] = row[5]
        result['raddress'] = row[6]
        result['rlocation'] = row[6]
        return result

    def build_clothing_attributes(self, cid, rid, cname, cbrand, cdescription, csize):
        result = {};
        result['cid'] = cid
        result['rid'] = rid
        result['cname'] = cname
        result['cbrand'] = cbrand
        result['cdescription'] = cdescription
        result['csize'] = csize
        return result

    def getAllClothing(self):
        dao = ClothingDAO()
        Clothing_list = dao.getAllClothing()
        result_list = []
        for row in Clothing_list:
            result = self.build_Clothing_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getClothingById(self, cid):
        dao = ClothingDAO()
        row = dao.getClothingById(cid)
        if not row:
            return jsonify(Error = "Clothing Not Found"), 404
        else:
            Clothing = self.build_Clothing_dict(row)
            return jsonify(Clothing = Clothing)

    def getClothingByBrand(self, cbrand):
        dao = ClothingDAO()
        Clothinglist = dao.getClothingByBrand(cbrand)
        result_list = []
        if not Clothinglist:
            return jsonify(Error = "No Clothing Found with the specified Brand"), 404
        else:
            for row in Clothinglist:
                result = self.build_Clothing_dict(row)
                result_list.append(result)
            return jsonify(Clothing = result_list)

    def getClothingByName(self, cname):    #Filter by Clothing category
        dao = ClothingDAO()
        Clothinglist = dao.getClothingByName(cname)
        result_list = []
        if not Clothinglist:
            return jsonify(Error = "No Clothing Found with the Specified Name"), 404
        else:
            for row in Clothinglist:
                result = self.build_Clothing_dict(row)
                result_list.append(result)
            return jsonify(Clothing = result_list)

    def getClothingBySize(self, csize):
        dao = ClothingDAO()
        Clothinglist = dao.getClothingBySize(csize)
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
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            cname = form['cname']
            cbrand = form['cbrand']
            cdescription = form['cdescription']
            csize = form['csize']

            if rtype and rname and rlocation and sid and cname and cbrand and csize and cdescription:
                resourcedao = ResourceDAO()
                dao = ClothingDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                cid = dao.insert(rid, cname, cbrand, cdescription, csize)
                result = self.build_Clothing_attributes(cid, rid, cname, cbrand, cdescription, csize)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertClothingJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        cname = json['cname']
        cbrand = json['cbrand']
        cdescription = json['cdescription']
        csize = json['csize']


        if rtype and rname and rlocation and sid and cname and cbrand and cdescription and csize:
            resourcedao = ResourceDAO()
            dao = ClothingDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            cid = dao.insert(rid, cname, cbrand, cdescription,csize)
            result = self.build_Clothing_attributes(cid, rid, cname, cbrand, cdescription,csize)
            return jsonify(Clothing=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteClothing(self, cid):
        dao = ClothingDAO()
        resourceDAO = ResourceDAO()

        if not dao.getClothingById(cid):
            return jsonify(Error = "Clothing not found."), 404
        else:
            rid = dao.getResourceID(cid)
            dao.delete(cid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateClothing(self, cid, form):
        resourceDAO = ResourceDAO()
        dao = ClothingDAO()
        if not dao.getClothingById(cid):
            return jsonify(Error = "Clothing not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                cname = form['cname']
                cbrand = form['cbrand']
                cdescription = form['cdescription']
                csize = form['csize']

                rid = dao.getResourceID(cid)

                if rtype and rname and rlocation and sid and cname and cbrand and cdescription and csize:
                    dao.update(cid, cname, cbrand, cdescription, csize)
                    resourceDAO.update(rid, rname,rtype,rlocation)
                    result = self.build_Clothing_attributes(cid, rid, cname, cbrand,cdescription, csize)
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
