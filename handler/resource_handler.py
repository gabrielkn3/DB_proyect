from flask import jsonify

from daos.resource import ResourceDAO


class ResourceHandler:
    def build_resources_dict(self, row):
        result = {};
        result['rid'] = row[0]
        result['rnamme'] = row[1]
        result['rtype'] = row[2]
        result['rlocation'] = row[3]
        result['sid'] = row[4]
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

    def build_resources_attributes(self, rid, rname, rtype, rlocation, sid):
        result = {};
        result['rid'] = rid
        result['rname'] = rname
        result['rtype'] = rtype
        result['rlocation'] = rlocation
        result['sid'] = sid
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getResourcesById(self, rid):
        dao = ResourceDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource = resource)

    def getResourcesByName(self, rname):
        dao = ResourceDAO()
        row = dao.getResourceByName(rname)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource = resource)

    def getResourcesByType(self, rtype):    #Filter by resource category
        dao = ResourceDAO()
        row = dao.getResourceByType(rtype)
        if not row:
            return jsonify(Error = "No Resources Found in the Specified Category"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource = resource)

    # def searchResources(self, args):
    #     rname = args.get("rname")
    #     rtype = args.get("rtype")
    #
    #     dao = ResourceDAO()
    #     parts_list = []
    #     if (len(args) == 2) and rtype and rname:
    #         parts_list = dao.getResourceByTypeAndName(rtype, rname)
    #     elif (len(args) == 1) and rtype:
    #         parts_list = dao.getResourceByType(rtype)
    #     elif (len(args) == 1) and rname:
    #         parts_list = dao.getResourceByName(rname)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in parts_list:
    #         result = self.build_resources_dict(row)
    #         result_list.append(result)
    #     return jsonify(Parts=result_list)

    def getSuppliersByResourceId(self, rid):
        dao = ResourceDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceId(rid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getRequestersByResourceId(self, rid):
        dao = ResourceDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="Resource Not Found"), 404
        requester_list = dao.getRequestersByResourceId(rid)
        result_list = []
        for row in requester_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSuppliersByResourceName(self, rname):
        dao = ResourceDAO()
        if not dao.getResourceByName(rname):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceName(rname)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getRequestersByResourceName(self, rname):
        dao = ResourceDAO()
        if not dao.getResourceByName(rname):
            return jsonify(Error="Resource Not Found"), 404
        requester_list = dao.getRequestersByResourceName(rname)
        result_list = []
        for row in requester_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSuppliersByResourceType(self, rtype):
        dao = ResourceDAO()
        if not dao.getResourceByType(rtype):
            return jsonify(Error="Resource Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceType(rtype)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getRequestersByResourceType(self, rtype):
        dao = ResourceDAO()
        if not dao.getResourceByName(rtype):
            return jsonify(Error="Resource Not Found"), 404
        requester_list = dao.getRequestersByResourceType(rtype)
        result_list = []
        for row in requester_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    # def insertResource(self, form):
    #     print("form: ", form)
    #     if len(form) != 4:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         rtype = form['rtype']
    #         rname = form['rname']
    #         rlocation = form['rlocation']
    #         sid = form['sid']
    #         if rtype and rname and rlocation and sid:
    #             dao = ResourceDAO()
    #             rid = dao.insert(rtype,rname,rlocation,sid)
    #             result = self.build_resources_attributes(rid, rtype, rname, rlocation, sid)
    #             return jsonify(Resource=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def insertResourceJson(self, json):
    #     rtype = json['rtype']
    #     rname = json['rname']
    #     rlocation = json['rlocation']
    #     sid = json['sid']
    #     if rtype and rname and rlocation and sid:
    #         dao = ResourceDAO()
    #         rid = dao.insert(rtype, rname, rlocation, sid)
    #         result = self.build_resources_attributes(rid, rtype, rname, rlocation, sid)
    #         return jsonify(Resource=result), 201
    #
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def deleteResource(self, rid):
    #     dao = ResourceDAO()
    #     if not dao.getResourceById(rid):
    #         return jsonify(Error = "Resource not found."), 404
    #     else:
    #         dao.delete(rid)
    #         return jsonify(DeleteStatus = "OK"), 200
    #
    # def updateResource(self, rid, form):
    #     dao = ResourceDAO()
    #     if not dao.getResourceById(rid):
    #         return jsonify(Error = "Resource not found."), 404
    #     else:
    #         if len(form) != 4:
    #             return jsonify(Error="Malformed update request"), 400
    #         else:
    #             rtype = form['rtype']
    #             rname = form['rname']
    #             rlocation = form['rlocation']
    #             sid = form['sid']
    #             if rtype and rname and rlocation and sid:
    #                 dao.update(rid, rtype, rname, rlocation, sid)
    #                 result = self.build_part_attributes(rid, rtype, rname, rlocation, sid)
    #                 return jsonify(Resource=result), 200
    #             else:
    #                 return jsonify(Error="Unexpected attributes in update request"), 400

    def build_resource_counts(self, resource_counts):
        result = []
        #print(part_counts)
        for P in resource_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByResourceId(self):
        dao = ResourceDAO()
        result = dao.getCountByResourceId()
        #print(self.build_part_counts(result))
        #return jsonify(ResourceCounts = self.build_resource_counts(result)), 200
        return jsonify(ResourceCounts=result), 200
