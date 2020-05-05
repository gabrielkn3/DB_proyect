from flask import jsonify

from daos.DryFood import DryFoodDAO

from daos.resource import ResourceDAO


class DryFoodHandler:
    def build_DryFood_dict(self, row):
        result = {};
        result['dfid'] = row[0]
        result['rid'] = row[1]
        result['dfbrand'] = row[2]
        result['rname'] = row[3]
        result['dfdescription'] = row[4]
        result['rlocation'] = row[5]
        return result

    def build_DryFood_attributes(self, dfid, rid, dfbrand, dfname, dfdescription):
        result = {};
        result['dfid'] = dfid
        result['rid'] = rid
        result['dfbrand'] = dfbrand
        result['dfname'] = dfname
        result['dfdescription'] = dfdescription
        return result

    def getAllDryFood(self):
        dao = DryFoodDAO()
        DryFood_list = dao.getAllDryFood()
        result_list = []
        for row in DryFood_list:
            result = self.build_DryFood_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getDryFoodById(self, dfid):
        dao = DryFoodDAO()
        row = dao.getDryFoodById(dfid)
        if not row:
            return jsonify(Error = "DryFood Not Found"), 404
        else:
            DryFood = self.build_DryFood_dict(row)
            return jsonify(DryFood = DryFood)

    def getDryFoodByName(self, dfname):
        dao = DryFoodDAO()
        DryFoodlist = dao.getDryFoodByName(dfname)
        result_list = []
        if not DryFoodlist:
            return jsonify(Error = "No DryFood Found with the specified flavor"), 404
        else:
            for row in DryFoodlist:
                result = self.build_DryFood_dict(row)
                result_list.append(result)
            return jsonify(DryFood = result_list)

    def getDryFoodByBrand(self, dfbrand):    #Filter by DryFood category
        dao = DryFoodDAO()
        DryFoodlist = dao.getDryFoodByBrand(dfbrand)
        result_list = []
        if not DryFoodlist:
            return jsonify(Error = "No DryFood Found with the Specified Brand"), 404
        else:
            for row in DryFoodlist:
                result = self.build_DryFood_dict(row)
                result_list.append(result)
            return jsonify(DryFood = result_list)

    def insertDryFood(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            dfbrand = form['dfbrand']
            dfname = form['dfname']
            dfdescription = form['dfdescription']

            if rtype and rname and rlocation and sid and dfbrand and dfname and dfdescription:
                resourcedao = ResourceDAO()
                dao = DryFoodDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                dfid = dao.insert(rid, dfbrand, dfname, dfdescription)
                result = self.build_DryFood_attributes(dfid, rid, dfbrand, dfname, dfdescription)
                return jsonify(DryFood=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertDryFoodJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        dfbrand = json['dfbrand']
        dfname = json['dfname']
        dfdescription = json['dfdescription']


        if rtype and rname and rlocation and sid and dfbrand and dfname and dfdescription:
            resourcedao = ResourceDAO()
            dao = DryFoodDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            dfid = dao.insert(rid, dfbrand, dfname, dfdescription)
            result = self.build_DryFood_attributes(dfid, rid, dfbrand, dfname, dfdescription)
            return jsonify(DryFood=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteDryFood(self, dfid):
        dao = DryFoodDAO()
        resourceDAO = ResourceDAO()

        if not dao.getDryFoodById(dfid):
            return jsonify(Error = "DryFood not found."), 404
        else:
            rid = dao.getResourceID(dfid)
            dao.delete(dfid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateDryFood(self, dfid, form):
        resourceDAO = ResourceDAO()
        dao = DryFoodDAO()
        if not dao.getDryFoodById(dfid):
            return jsonify(Error = "DryFood not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                dfbrand = form['dfbrand']
                dfname = form['dfname']
                dfdescription = form['dfdescription']

                rid = dao.getResourceID(dfid)

                if rtype and rname and rlocation and sid and dfbrand and dfname and dfdescription:
                    dao.update(dfid, dfbrand, dfname, dfdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_DryFood_attributes(dfid, rid, dfbrand, dfname,dfdescription)
                    return jsonify(DryFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_DryFood_counts(self, DryFood_counts):
        result = []
        #print(part_counts)
        for P in DryFood_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByDryFoodId(self):
        dao = DryFoodDAO()
        result = dao.getCountByDryFoodId()
        #print(self.build_part_counts(result))
        #return jsonify(DryFoodCounts = self.build_DryFood_counts(result)), 200
        return jsonify(DryFoodCounts=result), 200
