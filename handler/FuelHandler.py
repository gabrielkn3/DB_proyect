from flask import jsonify

from daos.Fuel import FuelDAO

from daos.resource import ResourceDAO


class FuelHandler:
    def build_Fuel_dict(self, row):
        result = {};
        result['fid'] = row[0]
        result['rid'] = row[1]
        result['ftype'] = row[2]
        result['fquantity'] = row[3]
        result['fdescription'] = row[4]
        result['octane'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['stype'] = row[1]
        result['stype'] = row[2]
        result['semail'] = row[3]
        result['sphone'] = row[4]
        result['saddress'] = row[5]
        result['sfinance'] = row[6]
        return result

    def build_requester_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ReqID'] = row[1]
        result['rfirsttype'] = row[2]
        result['rlasttype'] = row[3]
        result['remail'] = row[4]
        result['rphone'] = row[5]
        result['raddress'] = row[6]
        result['rlocation'] = row[6]
        return result

    def build_Fuel_attributes(self, fid, rid, ftype, fquantity, fdescription):
        result = {};
        result['fid'] = fid
        result['rid'] = rid
        result['ftype'] = ftype
        result['fquantity'] = fquantity
        result['fdescription'] = fdescription
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        Fuel_list = dao.getAllFuel()
        result_list = []
        for row in Fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getFuelById(self, fid):
        dao = FuelDAO()
        row = dao.getFuelById(fid)
        if not row:
            return jsonify(Error = "Fuel Not Found"), 404
        else:
            Fuel = self.build_Fuel_dict(row)
            return jsonify(Fuel = Fuel)

    def getFuelByQuantity(self, fquantity):
        dao = FuelDAO()
        Fuellist = dao.getFuelByQuantity(fquantity)
        result_list = []
        if not Fuellist:
            return jsonify(Error = "No Fuel Found with the specified Quantity"), 404
        else:
            for row in Fuellist:
                result = self.build_Fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)

    def getFuelBytype(self, ftype):    #Filter by Fuel category
        dao = FuelDAO()
        Fuellist = dao.getFuelBytype(ftype)
        result_list = []
        if not Fuellist:
            return jsonify(Error = "No Fuel Found with the Specified type"), 404
        else:
            for row in Fuellist:
                result = self.build_Fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)

    def getFuelByOctane(self, octane):
        dao = FuelDAO()
        Fuellist = dao.getFuelByOctane(octane)
        result_list = []
        if not Fuellist:
            return jsonify(Error = "No Fuel Found with the specified Octane"), 404
        else:
            for row in Fuellist:
                result = self.build_Fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)

    def insertFuel(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rtype = form['rtype']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            ftype = form['ftype']
            fquantity = form['fquantity']
            fdescription = form['fdescription']

            if rtype and rtype and rlocation and sid and ftype and fquantity and fdescription:
                resourcedao = ResourceDAO()
                dao = FuelDAO()
                rid = resourcedao.insert(rtype,rtype,rlocation,sid)
                fid = dao.insert(rid, ftype, fquantity, fdescription)
                result = self.build_Fuel_attributes(fid, rid, ftype, fquantity, fdescription)
                return jsonify(Fuel=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertFuelJson(self, json):

        rtype = json['rtype']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        ftype = json['ftype']
        fquantity = json['fquantity']
        fdescription = json['fdescription']


        if rtype and rtype and rlocation and sid and ftype and fquantity and fdescription:
            resourcedao = ResourceDAO()
            dao = FuelDAO()
            rid = resourcedao.insert(rtype, rtype, rlocation, sid)
            fid = dao.insert(rid, ftype, fquantity, fdescription)
            result = self.build_Fuel_attributes(fid, rid, ftype, fquantity, fdescription)
            return jsonify(Fuel=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFuel(self, fid):
        dao = FuelDAO()
        resourceDAO = ResourceDAO()

        if not dao.getFuelById(fid):
            return jsonify(Error = "Fuel not found."), 404
        else:
            rid = dao.getResourceID(fid)
            dao.delete(fid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateFuel(self, fid, form):
        resourceDAO = ResourceDAO()
        dao = FuelDAO()
        if not dao.getFuelById(fid):
            return jsonify(Error = "Fuel not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rtype = form['rtype']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                ftype = form['ftype']
                fquantity = form['fquantity']
                fdescription = form['fdescription']
                octane = form['octane']

                rid = dao.getResourceID(fid)

                if rtype and rtype and rlocation and sid and ftype and fquantity and octane and fdescription:
                    dao.update(fid, ftype, fquantity, fdescription, octane)
                    resourceDAO.update(rid, rtype,rtype,rlocation, octane)
                    result = self.build_Fuel_attributes(fid, rid, ftype, fquantity,fdescription, octane)
                    return jsonify(Fuel=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Fuel_counts(self, Fuel_counts):
        result = []
        #print(part_counts)
        for P in Fuel_counts:
            D = {}
            D['id'] = P[0]
            D['type'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByFuelId(self):
        dao = FuelDAO()
        result = dao.getCountByFuelId()
        #print(self.build_part_counts(result))
        #return jsonify(FuelCounts = self.build_Fuel_counts(result)), 200
        return jsonify(FuelCounts=result), 200
