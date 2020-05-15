from flask import jsonify

from daos.BabyFood import BabyFoodDAO

from daos.resource import ResourceDAO


class BabyFoodHandler:
    def build_BabyFood_dict(self, row):
        result = {};
        result['bfid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['bfbrand'] = row[3]
        result['bfflavor'] = row[4]
        result['bfdescription'] = row[5]
        result['rlocation'] = row[6]
        return result

    def build_BabyFood_attributes(self, bfid, rid, rname, bfbrand, bfflavor, bfdescription, rlocation):
        result = {};
        result['bfid'] = bfid
        result['rid'] = rid
        result['rname'] = rname
        result['bfbrand'] = bfbrand
        result['bfflavor'] = bfflavor
        result['bfdescription'] = bfdescription
        result['rlocation'] = rlocation
        return result

    def getAllBabyFood(self):
        dao = BabyFoodDAO()
        BabyFood_list = dao.getAllBabyFood()
        result_list = []
        for row in BabyFood_list:
            result = self.build_BabyFood_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getBabyFoodById(self, bfid):
        dao = BabyFoodDAO()
        row = dao.getBabyFoodById(bfid)
        if not row:
            return jsonify(Error = "BabyFood Not Found"), 404
        else:
            BabyFood = self.build_BabyFood_dict(row)
            return jsonify(BabyFood = BabyFood)

    def getBabyFoodByFlavor(self, bfflavor):
        dao = BabyFoodDAO()
        BabyFoodlist = dao.getBabyFoodByFlavor(bfflavor)
        result_list = []
        if not BabyFoodlist:
            return jsonify(Error = "No BabyFood Found with the specified flavor"), 404
        else:
            for row in BabyFoodlist:
                result = self.build_BabyFood_dict(row)
                result_list.append(result)
            return jsonify(BabyFood = result_list)

    def getBabyFoodByBrand(self, bfbrand):    #Filter by BabyFood category
        dao = BabyFoodDAO()
        BabyFoodlist = dao.getBabyFoodByBrand(bfbrand)
        result_list = []
        if not BabyFoodlist:
            return jsonify(Error = "No BabyFood Found with the Specified Brand"), 404
        else:
            for row in BabyFoodlist:
                result = self.build_BabyFood_dict(row)
                result_list.append(result)
            return jsonify(BabyFood = result_list)

    # def insertBabyFood(self, form):
    #     print("form: ", form)
    #     if len(form) != 7:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         rname = form['rname']
    #         rtype = form['rtype']
    #         rlocation = form['rlocation']
    #         sid = form['sid']
    #
    #         bfbrand = form['bfbrand']
    #         bfflavor = form['bfflavor']
    #         bfdescription = form['bfdescription']
    #
    #         if rtype and rname and rlocation and sid and bfbrand and bfflavor and bfdescription:
    #             resourcedao = ResourceDAO()
    #             dao = BabyFoodDAO()
    #             rid = resourcedao.insert(rtype,rname,rlocation,sid)
    #             bfid = dao.insert(rid, bfbrand, bfflavor, bfdescription)
    #             result = self.build_BabyFood_attributes(bfid, rid, bfbrand, bfflavor, bfdescription)
    #             return jsonify(BabyFood=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400

    def insertBabyFoodJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        bfbrand = json['bfbrand']
        bfflavor = json['bfflavor']
        bfdescription = json['bfdescription']


        if rtype and rname and rlocation and bfbrand and bfflavor and bfdescription:
            resourcedao = ResourceDAO()
            dao = BabyFoodDAO()
            rid = resourcedao.insert(rname,rtype,rlocation)
            bfid = dao.insert(bfbrand, bfflavor, bfdescription, rid)
            result = self.build_BabyFood_attributes(bfid, rid, rname, bfbrand, bfflavor, bfdescription, rlocation)
            return jsonify(BabyFood=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteBabyFood(self, bfid):
        dao = BabyFoodDAO()
        resourceDAO = ResourceDAO()

        if not dao.getBabyFoodById(bfid):
            return jsonify(Error = "BabyFood not found."), 404
        else:
            rid = dao.getResourceID(bfid)
            dao.delete(bfid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateBabyFood(self, bfid, form):
        resourceDAO = ResourceDAO()
        dao = BabyFoodDAO()
        if not dao.getBabyFoodById(bfid):
            return jsonify(Error = "BabyFood not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                bfbrand = form['bfbrand']
                bfflavor = form['bfflavor']
                bfdescription = form['bfdescription']

                rid = dao.getResourceID(bfid)

                if rtype and rname and rlocation and sid and bfbrand and bfflavor and bfdescription:
                    dao.update(bfid, bfbrand, bfflavor, bfdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_BabyFood_attributes(bfid, rid, bfbrand, bfflavor,bfdescription)
                    return jsonify(BabyFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_BabyFood_counts(self, BabyFood_counts):
        result = []
        #print(part_counts)
        for P in BabyFood_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByBabyFoodId(self):
        dao = BabyFoodDAO()
        result = dao.getCountByBabyFoodId()
        #print(self.build_part_counts(result))
        #return jsonify(BabyFoodCounts = self.build_BabyFood_counts(result)), 200
        return jsonify(BabyFoodCounts=result), 200
