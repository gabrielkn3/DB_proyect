from flask import jsonify
from daos.requester import RequesterDAO
from handler.user import userHandler




class RequesterHandler:
    def build_requester_dict(self, row):
        result = {}
        result['reqid'] = row[0]
        result['uid'] = row[1]
        result['reqlocation'] = row[2]
        return result

    def build_resource_from_request(self, row):
        result = {}
        result['rtype'] = row[3]
        result['rquantity'] = row[6]
        result['reqid'] = row[2]
        return result

    def build_requester_attributes(self, reqid, reqlocation):
        result = {}
        result['reqid'] = reqid
        result['reqlocation'] = reqlocation
        return result

    def getAllRequesters(self):

        dao = RequesterDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getRequesterById(self, reqid):

        dao = RequesterDAO()

        row = dao.getRequesterById(reqid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            requester = self.build_requester_dict(row)
        return jsonify(Requester=requester)


    def searchRequesters(self, form):
        if len(form) > 1:
            return jsonify(Error = "Malformed search(REQUESTER) string."), 400
        else:
            reqlocation = form["reqlocation"]
            if reqlocation:
                dao = RequesterDAO()
                requester_list = dao.getRequestersByLocation(reqlocation)
                result_list = []
                for row in requester_list:
                    result = self.build_requester_dict(row)
                    result_list.append(result)
                return jsonify(Requester=result_list)
            else:
                return jsonify(Error="Malformed search(REQUESTER) string."), 400

    def getResourcesByRequesterId(self, reqid):
        dao = RequesterDAO()
        row = dao.getRequesterById(reqid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:  # supplier exists
            requests = dao.getResourcesByREQID(reqid)
            resources = self.build_resource_from_request(requests)
            return jsonify(Resources=resources)


    def updateRequester (self, reqid, form):
             dao = RequesterDAO()
             user_handler = userHandler()
             if not dao.getRequesterById(reqid):
                return jsonify(Error = "Supplier not found."), 404
             else:
                if len(form) > 1:
                    return user_handler.updateUser(form["uid"], form)
                else:
                    reqlocation = form['slocation']
                    if reqlocation:
                        dao.update(reqid, reqlocation)
                        result = self.build_supplier_attributes(reqid, reqlocation)
                        return jsonify(Requester=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update(REQUESTER) request"), 400


    def deleteRequester(self,reqid):
        dao = RequesterDAO()
        if not dao.getSupplierById(reqid):
            return jsonify(Error="Supplier not found."), 404
        else:
            status = dao.delete(reqid)
            if status:
                return jsonify(Result="Deleted REQUESTER with reqid: "+str(status))
            else:
                return jsonify(Error="Error deleting (REQUESTER) request"), 400

    # def insertRequester(self, form):
    #     if form and len(form) == 2:
    #         reqlocation = form['reqlocation']
    #         uid = form["uid"]
    #         if uid and reqlocation:
    #             dao = RequesterDAO()
    #             sid = dao.insert(uid, reqlocation)
    #             result = {}
    #             result["reqid"] = reqid
    #             result["uid"] = uid
    #             result["reqlocation"] = reqlocation
    #             return jsonify(Requester=result), 201
    #         else:
    #             return jsonify(Error="Malformed post(REQUESTER) request")
    #     else:
    #         return jsonify(Error="Malformed post(REQUESTER) request")