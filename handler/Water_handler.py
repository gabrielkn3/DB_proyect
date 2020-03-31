from flask import jsonify

from daos.Water import WaterDAO

from daos.resource import ResourceDAO


class WaterHandler:
    def build_Water_dict(self, row):
        result = {};
        result['wid'] = row[0]
        result['rid'] = row[1]
        result['wbrand'] = row[2]
        result['wsize'] = row[3]
        result['wdescription'] = row[4]
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

    def build_Water_attributes(self, wid, rid, wbrand, wsize, wdescription):
        result = {};
        result['wid'] = wid
        result['rid'] = rid
        result['wbrand'] = wbrand
        result['wsize'] = wsize
        result['wdescription'] = wdescription
        return result

    def getAllWater(self):
        dao = WaterDAO()
        Water_list = dao.getAllWater()
        result_list = []
        for row in Water_list:
            result = self.build_Water_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getWaterById(self, wid):
        dao = WaterDAO()
        row = dao.getWaterById(wid)
        if not row:
            return jsonify(Error = "Water Not Found"), 404
        else:
            Water = self.build_Water_dict(row)
            return jsonify(Water = Water)

    def getWaterBySize(self, wsize):
        dao = WaterDAO()
        Waterlist = dao.getWaterBySize(wsize)
        result_list = []
        if not Waterlist:
            return jsonify(Error = "No Water Found with the specified Size"), 404
        else:
            for row in Waterlist:
                result = self.build_Water_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)

    def getWaterByBrand(self, wbrand):    #Filter by Water category
        dao = WaterDAO()
        Waterlist = dao.getWaterByBrand(wbrand)
        result_list = []
        if not Waterlist:
            return jsonify(Error = "No Water Found with the Specified Brand"), 404
        else:
            for row in Waterlist:
                result = self.build_Water_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)

    def insertWater(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            wbrand = form['wbrand']
            wsize = form['rname']
            wdescription = form['wdescription']

            if rtype and rname and rlocation and sid and wbrand and wsize and wdescription:
                resourcedao = ResourceDAO()
                dao = WaterDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                wid = dao.insert(rid, wbrand, wsize, wdescription)
                result = self.build_Water_attributes(wid, rid, wbrand, wsize, wdescription)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertWaterJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        wbrand = json['wbrand']
        wsize = json['wsize']
        wdescription = json['wdescription']


        if rtype and rname and rlocation and sid and wbrand and wsize and wdescription:
            resourcedao = ResourceDAO()
            dao = WaterDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            wid = dao.insert(rid, wbrand, wsize, wdescription)
            result = self.build_Water_attributes(wid, rid, wbrand, wsize, wdescription)
            return jsonify(Water=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteWater(self, wid):
        dao = WaterDAO()
        resourceDAO = ResourceDAO()

        if not dao.getWaterById(wid):
            return jsonify(Error = "Water not found."), 404
        else:
            rid = dao.getResourceID(wid)
            dao.delete(wid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateWater(self, wid, form):
        resourceDAO = ResourceDAO()
        dao = WaterDAO()
        if not dao.getWaterById(wid):
            return jsonify(Error = "Water not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                wbrand = form['wbrand']
                wsize = form['wsize']
                wdescription = form['wdescription']

                rid = dao.getResourceID(wid)

                if rtype and rname and rlocation and sid and wbrand and wsize and wdescription:
                    dao.update(wid,wbrand, wsize, wdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_Water_attributes(wid, rid, wbrand, wsize,wdescription)
                    return jsonify(Water=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Water_counts(self, Water_counts):
        result = []
        #print(part_counts)
        for P in Water_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByWaterId(self):
        dao = WaterDAO()
        result = dao.getCountByWaterId()
        #print(self.build_part_counts(result))
        #return jsonify(WaterCounts = self.build_Water_counts(result)), 200
        return jsonify(WaterCounts=result), 200
