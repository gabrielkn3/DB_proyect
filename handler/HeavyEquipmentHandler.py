from flask import jsonify

from daos.HeavyEquipment import HeavyEquipmentDAO

from daos.resource import ResourceDAO


class HeavyEquipmentHandler:
    def build_HeavyEquipment_dict(self, row):
        result = {};
        result['hid'] = row[0]
        result['rid'] = row[1]
        result['hbrand'] = row[2]
        result['hname'] = row[3]
        result['hdescription'] = row[4]
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

    def build_HeavyEquipment_attributes(self, hid, rid, hbrand, hname, hdescription):
        result = {};
        result['hid'] = hid
        result['rid'] = rid
        result['hbrand'] = hbrand
        result['hname'] = hname
        result['hdescription'] = hdescription
        return result

    def getAllHeavyEquipment(self):
        dao = HeavyEquipmentDAO()
        HeavyEquipment_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HeavyEquipment_list:
            result = self.build_HeavyEquipment_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getHeavyEquipmentById(self, hid):
        dao = HeavyEquipmentDAO()
        row = dao.getHeavyEquipmentById(hid)
        if not row:
            return jsonify(Error = "HeavyEquipment Not Found"), 404
        else:
            HeavyEquipment = self.build_HeavyEquipment_dict(row)
            return jsonify(HeavyEquipment = HeavyEquipment)

    def getHeavyEquipmentByName(self, hname):
        dao = HeavyEquipmentDAO()
        HeavyEquipmentlist = dao.getHeavyEquipmentByName(hname)
        result_list = []
        if not HeavyEquipmentlist:
            return jsonify(Error = "No HeavyEquipment Found with the specified Name"), 404
        else:
            for row in HeavyEquipmentlist:
                result = self.build_HeavyEquipment_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquipment = result_list)

    def getHeavyEquipmentByBrand(self, hbrand):    #Filter by HeavyEquipment category
        dao = HeavyEquipmentDAO()
        HeavyEquipmentlist = dao.getHeavyEquipmentByBrand(hbrand)
        result_list = []
        if not HeavyEquipmentlist:
            return jsonify(Error = "No HeavyEquipment Found with the Specified Brand"), 404
        else:
            for row in HeavyEquipmentlist:
                result = self.build_HeavyEquipment_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquipment = result_list)

    def insertHeavyEquipment(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            hbrand = form['hbrand']
            hname = form['hname']
            hdescription = form['hdescription']

            if rtype and rname and rlocation and sid and hbrand and hname and hdescription:
                resourcedao = ResourceDAO()
                dao = HeavyEquipmentDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                hid = dao.insert(rid, hbrand, hname, hdescription)
                result = self.build_HeavyEquipment_attributes(hid, rid, hbrand, hname, hdescription)
                return jsonify(HeavyEquipment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertHeavyEquipmentJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        hbrand = json['hbrand']
        hname = json['hname']
        hdescription = json['hdescription']


        if rtype and rname and rlocation and sid and hbrand and hname and hdescription:
            resourcedao = ResourceDAO()
            dao = HeavyEquipmentDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            hid = dao.insert(rid, hbrand, hname, hdescription)
            result = self.build_HeavyEquipment_attributes(hid, rid, hbrand, hname, hdescription)
            return jsonify(HeavyEquipment=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteHeavyEquipment(self, hid):
        dao = HeavyEquipmentDAO()
        resourceDAO = ResourceDAO()

        if not dao.getHeavyEquipmentById(hid):
            return jsonify(Error = "HeavyEquipment not found."), 404
        else:
            rid = dao.getResourceID(hid)
            dao.delete(hid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateHeavyEquipment(self, hid, form):
        resourceDAO = ResourceDAO()
        dao = HeavyEquipmentDAO()
        if not dao.getHeavyEquipmentById(hid):
            return jsonify(Error = "HeavyEquipment not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                hbrand = form['hbrand']
                hname = form['hname']
                hdescription = form['hdescription']

                rid = dao.getResourceID(hid)

                if rtype and rname and rlocation and sid and hbrand and hname and hdescription:
                    dao.update(hid, hbrand, hname, hdescription)
                    resourceDAO.update(rid, rname,rtype,rlocation)
                    result = self.build_HeavyEquipment_attributes(hid, rid, hbrand, hname,hdescription)
                    return jsonify(HeavyEquipment=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_HeavyEquipment_counts(self, HeavyEquipment_counts):
        result = []
        #print(part_counts)
        for P in HeavyEquipment_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByHeavyEquipmentId(self):
        dao = HeavyEquipmentDAO()
        result = dao.getCountByHeavyEquipmentId()
        #print(self.build_part_counts(result))
        #return jsonify(HeavyEquipmentCounts = self.build_HeavyEquipment_counts(result)), 200
        return jsonify(HeavyEquipmentCounts=result), 200
