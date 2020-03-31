from flask import jsonify

from daos.Medication import MedicationDAO

from daos.resource import ResourceDAO


class MedicationHandler:
    def build_Medication_dict(self, row):
        result = {};
        result['mid'] = row[0]
        result['rid'] = row[1]
        result['mname'] = row[2]
        result['mdosage'] = row[3]
        result['mdescription'] = row[4]
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

    def build_Medication_attributes(self, mid, rid, mname, mdosage, mdescription):
        result = {};
        result['mid'] = mid
        result['rid'] = rid
        result['mname'] = mname
        result['mdosage'] = mdosage
        result['mdescription'] = mdescription
        return result

    def getAllMedication(self):
        dao = MedicationDAO()
        Medication_list = dao.getAllMedication()
        result_list = []
        for row in Medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getMedicationById(self, mid):
        dao = MedicationDAO()
        row = dao.getMedicationById(mid)
        if not row:
            return jsonify(Error = "Medication Not Found"), 404
        else:
            Medication = self.build_Medication_dict(row)
            return jsonify(Medication = Medication)

    def getMedicationByDosage(self, mdosage):
        dao = MedicationDAO()
        medicationlist = dao.getMedicationByDosage(mdosage)
        result_list = []
        if not medicationlist:
            return jsonify(Error = "No Medication Found with the specified Dosage"), 404
        else:
            for row in medicationlist:
                result = self.build_Medication_dict(row)
                result_list.append(result)
            return jsonify(Medication = result_list)

    def getMedicationByName(self, mname):    #Filter by Medication category
        dao = MedicationDAO()
        medicationlist = dao.getMedicationByName(mname)
        result_list = []
        if not medicationlist:
            return jsonify(Error = "No Medication Found with the Specified Name"), 404
        else:
            for row in medicationlist:
                result = self.build_Medication_dict(row)
                result_list.append(result)
            return jsonify(Medication = result_list)

    def insertMedication(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            mname = form['mname']
            mdosage = form['mdosage']
            mdescription = form['mdescription']

            if rtype and rname and rlocation and sid and mname and mdosage and mdescription:
                resourcedao = ResourceDAO()
                dao = MedicationDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                mid = dao.insert(rid, mname, mdosage, mdescription)
                result = self.build_Medication_attributes(mid, rid, mname, mdosage, mdescription)
                return jsonify(Medication=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMedicationJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        mname = json['mname']
        mdosage = json['mdosage']
        mdescription = json['mdescription']


        if rtype and rname and rlocation and sid and mname and mdosage and mdescription:
            resourcedao = ResourceDAO()
            dao = MedicationDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            mid = dao.insert(rid, mname, mdosage, mdescription)
            result = self.build_Medication_attributes(mid, rid, mname, mdosage, mdescription)
            return jsonify(Medication=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMedication(self, mid):
        dao = MedicationDAO()
        resourceDAO = ResourceDAO()

        if not dao.getMedicationById(mid):
            return jsonify(Error = "Medication not found."), 404
        else:
            rid = dao.getResourceID(mid)
            dao.delete(mid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMedication(self, mid, form):
        resourceDAO = ResourceDAO()
        dao = MedicationDAO()
        if not dao.getMedicationById(mid):
            return jsonify(Error = "Medication not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                mname = form['mname']
                mdosage = form['mdosage']
                mdescription = form['mdescription']

                rid = dao.getResourceID(mid)

                if rtype and rname and rlocation and sid and mname and mdosage and mdescription:
                    dao.update(mid, mname, mdosage, mdescription)
                    resourceDAO.update(rid, rname,rtype,rlocation)
                    result = self.build_Medication_attributes(mid, rid, mname, mdosage,mdescription)
                    return jsonify(Medication=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Medication_counts(self, Medication_counts):
        result = []
        #print(part_counts)
        for P in Medication_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByMedicationId(self):
        dao = MedicationDAO()
        result = dao.getCountByMedicationId()
        #print(self.build_part_counts(result))
        #return jsonify(MedicationCounts = self.build_Medication_counts(result)), 200
        return jsonify(MedicationCounts=result), 200
