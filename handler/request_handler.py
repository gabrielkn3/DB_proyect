from flask import jsonify
from daos.request import RequestDAO
from daos.resource import ResourceDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['RequestID'] = row[0]
        result['requestStatus'] = row[1]
        result['requestQuantity'] = row[2]
        result['requestDate'] = row[3]
        result['rid'] = row[4]
        result['reqID'] = row[5]

        return result

    def build_request_attributes(self, RequestID, status, rid, reqID, requantity, date):
        result = {}
        result['RequestID'] = RequestID
        result['requestStatus'] = status
        result['requestQuantity'] = rid
        result['requestDate'] = reqID
        result['rid'] = requantity
        result['reqID'] = date
        return result

    def getAllRequests(self):
        dao = RequestDAO()
        requests_list = dao.getAllRequests()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request = result_list)

    def getRequestByID(self, RequestID):
        dao = RequestDAO()
        row = dao.getRequestByID(RequestID)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            req = self.build_request_dict(row)
        return jsonify(Request=req)



    def getRequestByreqID(self, reqID):
        dao = RequestDAO()
        result = dao.getRequestByreqID(reqID)
        out = []
        if not result:
            return jsonify(Error="No Requests found"), 404
        else:
            for row in result:
                entry = self.build_request_dict(row)
                out.append(entry)
        return jsonify(Request=out)

    def getRequestByrname(self, rname):
        dao = RequestDAO()
        result = dao.getRequestByrname(rname)
        out = []
        if not result:
            return jsonify(Error="No Requests found"), 404
        else:
            for row in result:
                entry =  self.build_request_dict(row)
                out.append(entry)
        return jsonify(Request=out)

    def getRequestsByRID(self, rid):
        dao = RequestDAO()
        row = dao.getRequestByRID(rid)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            req = self.build_request_dict(row)
        return jsonify(Request=req)

    def getRequestsByResourceName(self, rname):
        resourcedao = ResourceDAO()
        dao = RequestDAO()
        row = resourcedao.getResourceByName(rname)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            req = self.build_request_dict(row)
        return jsonify(Request=req)

    def searchRequests(self, args):

        rid = args.get("rid")
        status = args.get("status")
        quantity = args.get("quantity")

        dao = RequestDAO()
        request_list = []
        if (len(args) == 1) and status:
            request_list = dao.getRequestByStatus(status)
        elif (len(args) == 1) and quantity:
            request_list = dao.getRequestsByQuantity(quantity)
        elif (len(args) == 2) and rid and status:
            request_list = dao.getRequestByRIDAndStatus(rid, status)
        elif (len(args) == 2) and rid and quantity:
            request_list = dao.getRequestByRIDAndQuantity(rid, quantity)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def insertRequest(self, form):
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            requestStatus = json['requestStatus']
            requestQuantity = json['requestQuantity']
            requestDate = json['requestDate']
            rid = json['rid']
            reqID = json['reqID']

            if status and rid and reqID and requantity and date:
                dao = RequestDAO()
                RequestID = dao.insert(status, rid, reqID, requantity, date)
                result = self.build_request_attributes(RequestID, status, rid, reqID, requantity, date)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertRequestJson(self, json):
        requestStatus = json['requestStatus']
        requestQuantity = json['requestQuantity']
        requestDate = json['requestDate']
        rid = json['rid']
        reqID = json['reqID']

        if requestStatus and requestQuantity and requestDate and rid and reqID:
            dao = RequestDAO()
            RequestID = dao.insert(requestStatus, requestQuantity, requestDate, rid, reqID)
            result = self.build_request_attributes(RequestID, requestStatus, requestQuantity, requestDate, rid, reqID)
            return jsonify(Request=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteRequest(self, RequestID):
        dao = RequestDAO()
        if not dao.getRequestByID(RequestID):
            return jsonify(Error="Part not found."), 404
        else:
            dao.delete(RequestID)
            return jsonify(DeleteStatus="OK"), 200

    def updateRequest(self, RequestID, form):
        dao = RequestDAO()
        if not dao.getRequestByID(RequestID):
            return jsonify(Error="Part not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                status = form['status']
                rid = form['status']
                reqID = form['reqID']
                requantity = form['requantity']
                date = form['date']
                if status and rid and reqID and requantity and date:
                    dao.update(RequestID, status, rid, reqID, requantity, date)
                    result = self.build_request_attributes(RequestID, status, rid, reqID, requantity, date)
                    return jsonify(Request=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_request_counts(self, request_counts):
        result = []
        for P in request_counts:
            D = {}
            D['RequestID'] = P[0]
            D['status'] = P[1]
            D['rid'] = P[2]
            D['reqID'] = P[4]
            D['requantity'] = P[6]
            D['date'] = P[7]
            result.append(D)
        return result

    # def getCountByRequestId(self):
    #     dao = RequestDAO()
    #     result = dao.getCountByRequestId()
    #     # print(self.build_listing_counts(result))
    #     return jsonify(RequestCounts=self.build_listing_counts(result)), 200
    #



