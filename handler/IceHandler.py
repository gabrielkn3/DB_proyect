from flask import jsonify

from daos.Ice import IceDAO

from daos.resource import ResourceDAO


class IceHandler:
    def build_Ice_dict(self, row):
        result = {};
        result['iid'] = row[0]
        result['rid'] = row[1]
        result['itype'] = row[2]
        result['iweight'] = row[3]
        result['idescription'] = row[4]
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

    def build_Ice_attributes(self, iid, rid, itype, iweight, idescription):
        result = {};
        result['iid'] = iid
        result['rid'] = rid
        result['itype'] = itype
        result['iweight'] = iweight
        result['idescription'] = idescription
        return result

    def getAllIce(self):
        dao = IceDAO()
        Ice_list = dao.getAllIce()
        result_list = []
        for row in Ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getIceById(self, iid):
        dao = IceDAO()
        row = dao.getIceById(iid)
        if not row:
            return jsonify(Error = "Ice Not Found"), 404
        else:
            Ice = self.build_Ice_dict(row)
            return jsonify(Ice = Ice)

    def getIceByWeight(self, iweight):
        dao = IceDAO()
        Icelist = dao.getIceByWeight(iweight)
        result_list = []
        if not Icelist:
            return jsonify(Error = "No Ice Found with the specified flavor"), 404
        else:
            for row in Icelist:
                result = self.build_Ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)

    def getIceByType(self, itype):    #Filter by Ice category
        dao = IceDAO()
        Icelist = dao.getIceByType(itype)
        result_list = []
        if not Icelist:
            return jsonify(Error = "No Ice Found with the Specified Type"), 404
        else:
            for row in Icelist:
                result = self.build_Ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)

    def insertIce(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            itype = form['itype']
            iweight = form['iweight']
            idescription = form['idescription']

            if rtype and rname and rlocation and sid and itype and iweight and idescription:
                resourcedao = ResourceDAO()
                dao = IceDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                iid = dao.insert(rid, itype, iweight, idescription)
                result = self.build_Ice_attributes(iid, rid, itype, iweight, idescription)
                return jsonify(Ice=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertIceJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        itype = json['itype']
        iweight = json['iweight']
        idescription = json['idescription']


        if rtype and rname and rlocation and sid and itype and iweight and idescription:
            resourcedao = ResourceDAO()
            dao = IceDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            iid = dao.insert(rid, itype, iweight, idescription)
            result = self.build_Ice_attributes(iid, rid, itype, iweight, idescription)
            return jsonify(Ice=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteIce(self, iid):
        dao = IceDAO()
        resourceDAO = ResourceDAO()

        if not dao.getIceById(iid):
            return jsonify(Error = "Ice not found."), 404
        else:
            rid = dao.getResourceID(iid)
            dao.delete(iid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateIce(self, iid, form):
        resourceDAO = ResourceDAO()
        dao = IceDAO()
        if not dao.getIceById(iid):
            return jsonify(Error = "Ice not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                itype = form['itype']
                iweight = form['iweight']
                idescription = form['idescription']

                rid = dao.getResourceID(iid)

                if rtype and rname and rlocation and sid and itype and iweight and idescription:
                    dao.update(iid, itype, iweight, idescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_Ice_attributes(iid, rid, itype, iweight,idescription)
                    return jsonify(Ice=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Ice_counts(self, Ice_counts):
        result = []
        #print(part_counts)
        for P in Ice_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByIceId(self):
        dao = IceDAO()
        result = dao.getCountByIceId()
        #print(self.build_part_counts(result))
        #return jsonify(IceCounts = self.build_Ice_counts(result)), 200
        return jsonify(IceCounts=result), 200
