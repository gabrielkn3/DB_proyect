from flask import jsonify

from daos.MedicalDevice import MedicalDeviceDAO

from daos.resource import ResourceDAO


class MedicalDeviceHandler:
    def build_MedicalDevices_dict(self, row):
        result = {};
        result['mdid'] = row[0]
        result['rid'] = row[1]
        result['mdbrand'] = row[2]
        result['mdname'] = row[3]
        result['mddescription'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['sid'] = row[1]
        result['sfirstname'] = row[2]
        result['slastname'] = row[3]
        result['semail'] = row[4]
        result['sphone'] = row[5]
        result['saddress'] = row[6]
        result['slocation'] = row[7]
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

    def build_MedicalDevices_attributes(self, mdid, rid, mdbrand, mdname, mddescription):
        result = {};
        result['mdid'] = mdid
        result['rid'] = rid
        result['mdbrand'] = mdbrand
        result['mdname'] = mdname
        result['mddescription'] = mddescription
        return result

    def getAllMedicalDevices(self):
        dao = MedicalDeviceDAO()
        MedicalDevices_list = dao.getAllMedicalDevices()
        result_list = []
        for row in MedicalDevices_list:
            result = self.build_MedicalDevices_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getMedicalDevicesById(self, mdid):
        dao = MedicalDeviceDAO()
        row = dao.getMedicalDevicesById(mdid)
        if not row:
            return jsonify(Error = "Medical Device Not Found"), 404
        else:
            MedicalDevice = self.build_MedicalDevices_dict(row)
            return jsonify(MedicalDevice = MedicalDevice)

    def getMedicalDevicesByName(self, mdname):
        dao = MedicalDeviceDAO()
        MedicalDevices_list = dao.getMedicalDevicesByName(mdname)
        result_list = []
        if not MedicalDevices_list:
            return jsonify(Error = "No Medical Devices Found with the Specified Name."), 404
        else:
            for row in MedicalDevices_list:
                result = self.build_MedicalDevices_dict(row)
                result_list.append(result)
            return jsonify(Results= result_list)

    def getMedicalDevicesByBrand(self, mdbrand):    #Filter by MedicalDevice category
        dao = MedicalDeviceDAO()
        MedicalDevices_list = dao.getMedicalDevicesByBrand(mdbrand)
        result_list = []
        if not MedicalDevices_list:
            return jsonify(Error = "No Medical Devices Found with the Specified Brand."), 404
        else:
            for row in MedicalDevices_list:
                result = self.build_MedicalDevices_dict(row)
                result_list.append(result)
            return jsonify(Results = result_list)

    def insertMedicalDevice(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            mdbrand = form['mdbrand']
            mdname = form['rname']
            mddescription = form['mddescription']

            if rtype and rname and rlocation and sid and mdbrand and mdname and mddescription:
                resourcedao = ResourceDAO()
                dao = MedicalDeviceDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                mdid = dao.insert(rid, mdbrand, mdname, mddescription)
                result = self.build_MedicalDevices_attributes(mdid, rid, mdbrand, mdname, mddescription)
                return jsonify(MedicalDevice=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMedicalDeviceJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        mdbrand = json['mdbrand']
        mdname = json['rname']
        mddescription = json['mddescription']


        if rtype and rname and rlocation and sid and mdbrand and mdname and mddescription:
            resourcedao = ResourceDAO()
            dao = MedicalDeviceDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            mdid = dao.insert(rid, mdbrand, mdname, mddescription)
            result = self.build_MedicalDevices_attributes(mdid, rid, mdbrand, mdname, mddescription)
            return jsonify(MedicalDevice=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMedicalDevice(self, mdid):
        dao = MedicalDeviceDAO()
        resourceDAO = ResourceDAO()

        if not dao.getMedicalDevicesById(mdid):
            return jsonify(Error = "MedicalDevice not found."), 404
        else:
            rid = dao.getResourceID(mdid)
            dao.delete(mdid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMedicalDevice(self, mdid, form):
        resourceDAO = ResourceDAO()
        dao = MedicalDeviceDAO()
        if not dao.getMedicalDevicesById(mdid):
            return jsonify(Error = "MedicalDevice not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                mdbrand = form['mdbrand']
                mdname = form['mdname']
                mddescription = form['mddescription']

                rid = dao.getResourceID(mdid)
                sid = 42  ##MEGADUMMYVALUE

                if rtype and rname and rlocation and sid and mdbrand and mdname and mddescription:
                    dao.update(mdbrand, mdname, mddescription)
                    resourceDAO.update(rid,rname,rtype,rlocation,sid)
                    result = self.build_MedicalDevices_attributes(mdid, rid, mdbrand, mdname,mddescription)
                    return jsonify(MedicalDevice=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_MedicalDevice_counts(self, MedicalDevice_counts):
        result = []
        #print(part_counts)
        for P in MedicalDevice_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByMedicalDeviceId(self):
        dao = MedicalDeviceDAO()
        result = dao.getCountByMedicalDeviceId()
        #print(self.build_part_counts(result))
        #return jsonify(MedicalDeviceCounts = self.build_MedicalDevice_counts(result)), 200
        return jsonify(MedicalDeviceCounts=result), 200
