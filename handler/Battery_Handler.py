from flask import jsonify

from daos.Batteries import BatteriesDAO

from daos.resource import ResourceDAO


class BatteriesHandler:
    def build_Batteries_dict(self, row):
        result = {};
        result['bid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['bbrand'] = row[3]
        result['btype'] = row[4]
        result['blife'] = row[5]
        result['bdescription'] = row[6]
        result['rlocation'] = row[7]

        return result

    def build_Batteries_attributes(self, bid, rid, rname, bbrand, btype, blife, bdescription, rlocation):
        result = {};
        result['bid'] = bid
        result['rid'] = rid
        result['rname'] = rname
        result['bbrand'] = bbrand
        result['btype'] = btype
        result['blife'] = blife
        result['bdescription'] = bdescription
        result['rlocation'] = rlocation
        return result

    def getAllBatteries(self):
        dao = BatteriesDAO()
        Batteries_list = dao.getAllBatteries()
        result_list = []
        for row in Batteries_list:
            result = self.build_Batteries_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getBatteriesById(self, bid):
        dao = BatteriesDAO()
        row = dao.getBatteriesById(bid)
        if not row:
            return jsonify(Error = "Batteries Not Found"), 404
        else:
            Batteries = self.build_Batteries_dict(row)
            return jsonify(Batteries = Batteries)

    def getBatteriesByBrand(self, bbrand):
        dao = BatteriesDAO()
        Batterieslist = dao.getBatteriesByBrand(bbrand)
        result_list = []
        if not Batterieslist:
            return jsonify(Error = "No Batteries Found with the specified Brand"), 404
        else:
            for row in Batterieslist:
                result = self.build_Batteries_dict(row)
                result_list.append(result)
            return jsonify(Batteries = result_list)

    def getBatteriesByType(self, btype):    #Filter by Batteries category
        dao = BatteriesDAO()
        Batterieslist = dao.getBatteriesByType(btype)
        result_list = []
        if not Batterieslist:
            return jsonify(Error = "No Batteries Found with the Specified Type"), 404
        else:
            for row in Batterieslist:
                result = self.build_Batteries_dict(row)
                result_list.append(result)
            return jsonify(Batteries = result_list)

    def getBatteriesByLife(self, blife):
        dao = BatteriesDAO()
        Batterieslist = dao.getBatteriesByBatteryLife(blife)
        result_list = []
        if not Batterieslist:
            return jsonify(Error="No Batteries Found with the specified Battery Life"), 404
        else:
            for row in Batterieslist:
                result = self.build_Batteries_dict(row)
                result_list.append(result)
            return jsonify(Batteries=result_list)

    def insertBatteries(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            btype = form['btype']
            bbrand = form['bbrand']
            bdescription = form['bdescription']
            blife = form['blife']

            if rtype and rname and rlocation and sid and btype and bbrand and blife and bdescription:
                resourcedao = ResourceDAO()
                dao = BatteriesDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                bid = dao.insert(rid, bbrand, btype, blife, bdescription)
                result = self.build_Batteries_attributes(bid, rid, bbrand, btype, blife, bdescription)
                return jsonify(Batteries=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertBatteriesJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        bbrand = json['bbrand']
        btype = json['btype']
        blife = json['blife']
        bdescription = json['bdescription']



        if rtype and rname and rlocation and btype and bbrand and bdescription and blife:
            resourcedao = ResourceDAO()
            dao = BatteriesDAO()
            rid = resourcedao.insert(rtype, rname, rlocation)
            bid = dao.insert(bbrand, btype, blife, bdescription,rid)
            result = self.build_Batteries_attributes(bid, rid, rname, bbrand, btype, blife,bdescription, rlocation)
            return jsonify(Batteries=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteBatteries(self, bid):
        dao = BatteriesDAO()
        resourceDAO = ResourceDAO()

        if not dao.getBatteriesById(bid):
            return jsonify(Error = "Batteries not found."), 404
        else:
            rid = dao.getResourceID(bid)
            dao.delete(bid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateBatteries(self, bid, form):
        resourceDAO = ResourceDAO()
        dao = BatteriesDAO()
        if not dao.getBatteriesById(bid):
            return jsonify(Error = "Batteries not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                btype = form['btype']
                bbrand = form['bbrand']
                bdescription = form['bdescription']
                blife = form['blife']

                rid = dao.getResourceID(bid)

                if rtype and rname and rlocation and sid and btype and bbrand and bdescription and blife:
                    dao.update(bid, bbrand, btype, blife, bdescription)
                    resourceDAO.update(rid, rname,rtype,rlocation)
                    result = self.build_Batteries_attributes(bid, rid, bbrand, btype, blife, bdescription)
                    return jsonify(Batteries=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Batteries_counts(self, Batteries_counts):
        result = []
        #print(part_counts)
        for P in Batteries_counts:
            D = {}
            D['id'] = P[0]
            D['Type'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByBatteriesId(self):
        dao = BatteriesDAO()
        result = dao.getCountByBatteriesId()
        #print(self.build_part_counts(result))
        #return jsonify(BatteriesCounts = self.build_Batteries_counts(result)), 200
        return jsonify(BatteriesCounts=result), 200
