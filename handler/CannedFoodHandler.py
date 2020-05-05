from flask import jsonify

from daos.CannedFood import CannedFoodDAO

from daos.resource import ResourceDAO


class CannedFoodHandler:
    def build_CannedFood_dict(self, row):
        result = {};
        result['cfid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['cfbrand'] = row[3]
        result['cfdescription'] = row[4]
        result['rlocation'] = row[5]
        return result

    def build_CannedFood_attributes(self, cfid, rid, cfbrand, cfname, cfdescription):
        result = {};
        result['cfid'] = cfid
        result['rid'] = rid
        result['cfbrand'] = cfbrand
        result['cfname'] = cfname
        result['cfdescription'] = cfdescription
        return result

    def getAllCannedFood(self):
        dao = CannedFoodDAO()
        CannedFood_list = dao.getAllCannedFood()
        result_list = []
        for row in CannedFood_list:
            result = self.build_CannedFood_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getCannedFoodById(self, cfid):
        dao = CannedFoodDAO()
        row = dao.getCannedFoodById(cfid)
        if not row:
            return jsonify(Error = "CannedFood Not Found"), 404
        else:
            CannedFood = self.build_CannedFood_dict(row)
            return jsonify(CannedFood = CannedFood)

    def getCannedFoodByName(self, cfname):
        dao = CannedFoodDAO()
        CannedFoodlist = dao.getCannedFoodByName(cfname)
        result_list = []
        if not CannedFoodlist:
            return jsonify(Error = "No CannedFood Found with the specified flavor"), 404
        else:
            for row in CannedFoodlist:
                result = self.build_CannedFood_dict(row)
                result_list.append(result)
            return jsonify(CannedFood = result_list)

    def getCannedFoodByBrand(self, cfbrand):    #Filter by CannedFood category
        dao = CannedFoodDAO()
        CannedFoodlist = dao.getCannedFoodByBrand(cfbrand)
        result_list = []
        if not CannedFoodlist:
            return jsonify(Error = "No CannedFood Found with the Specified Brand"), 404
        else:
            for row in CannedFoodlist:
                result = self.build_CannedFood_dict(row)
                result_list.append(result)
            return jsonify(CannedFood = result_list)

    def insertCannedFood(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            cfbrand = form['cfbrand']
            cfname = form['cfname']
            cfdescription = form['cfdescription']

            if rtype and rname and rlocation and sid and cfbrand and cfname and cfdescription:
                resourcedao = ResourceDAO()
                dao = CannedFoodDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                cfid = dao.insert(rid, cfbrand, cfname, cfdescription)
                result = self.build_CannedFood_attributes(cfid, rid, cfbrand, cfname, cfdescription)
                return jsonify(CannedFood=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertCannedFoodJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        cfbrand = json['cfbrand']
        cfname = json['cfname']
        cfdescription = json['cfdescription']


        if rtype and rname and rlocation and sid and cfbrand and cfname and cfdescription:
            resourcedao = ResourceDAO()
            dao = CannedFoodDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            cfid = dao.insert(rid, cfbrand, cfname, cfdescription)
            result = self.build_CannedFood_attributes(cfid, rid, cfbrand, cfname, cfdescription)
            return jsonify(CannedFood=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteCannedFood(self, cfid):
        dao = CannedFoodDAO()
        resourceDAO = ResourceDAO()

        if not dao.getCannedFoodById(cfid):
            return jsonify(Error = "CannedFood not found."), 404
        else:
            rid = dao.getResourceID(cfid)
            dao.delete(cfid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateCannedFood(self, cfid, form):
        resourceDAO = ResourceDAO()
        dao = CannedFoodDAO()
        if not dao.getCannedFoodById(cfid):
            return jsonify(Error = "CannedFood not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                cfbrand = form['cfbrand']
                cfname = form['cfname']
                cfdescription = form['cfdescription']

                rid = dao.getResourceID(cfid)

                if rtype and rname and rlocation and sid and cfbrand and cfname and cfdescription:
                    dao.update(cfid, cfbrand, cfname, cfdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_CannedFood_attributes(cfid, rid, cfbrand, cfname,cfdescription)
                    return jsonify(CannedFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_CannedFood_counts(self, CannedFood_counts):
        result = []
        #print(part_counts)
        for P in CannedFood_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByCannedFoodId(self):
        dao = CannedFoodDAO()
        result = dao.getCountByCannedFoodId()
        #print(self.build_part_counts(result))
        #return jsonify(CannedFoodCounts = self.build_CannedFood_counts(result)), 200
        return jsonify(CannedFoodCounts=result), 200
