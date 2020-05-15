from flask import jsonify
from daos.receipt import ReceiptDAO

class receiptHandler:
    def build_receipt_dict(self, row):
        result = {}
        result['oid'] = row[0]
        result['ostatus'] = row[1]
        result['reqid'] = row[2]
        result['sid'] = row[3]
        result['pid'] = row[4]
        return result

    def build_receipt_attributes(self, oid, ReqID, sid, pid, rid, quantity, status):
        result = {}
        result['oid'] = oid
        result['ReqID'] = ReqID
        result['sid'] = sid
        result['pid'] = pid
        result['rid'] = rid
        result['quantity'] = quantity
        result['status'] = status
        return result

    def getAllReceipts(self):
        dao = ReceiptDAO()
        receipts_list = dao.getAllReceipts()
        result_list = []
        for row in receipts_list:
            result = self.build_receipt_dict(row)
            result_list.append(result)
        return jsonify(Receipt=result_list)

    def getReceiptByID(self, oid):
        dao = ReceiptDAO()
        row = dao.getReceiptByID(oid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            receipt = self.build_receipt_dict(row)
            return jsonify(Receipt=receipt)

    def getReceiptByRequestorID(self, ReqID):
        dao = ReceiptDAO()
        result = dao.getReceiptByRequestorID(ReqID)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)

    def getReceiptByRID(self, rid):
        dao = ReceiptDAO()
        result = dao.getReceiptByRID(rid)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)

    def getReceiptBySupplierID(self, sid):
        dao = ReceiptDAO()
        result = dao.getReceiptBySupplierID(sid)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(sid)
        return jsonify(Receipt=result_list)


    def getReceiptByQuantity(self, quantity):
        dao = ReceiptDAO()
        result = dao.getReceiptByQuantity(quantity)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)
    
    def getReceiptByStatus(self, status):
        dao = ReceiptDAO()
        result = dao.getReceiptByStatus(status)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)

    def getReceiptByRIDAndStatus(self, status, rid):
        dao = ReceiptDAO()
        result = dao.getReceiptByRIDAndStatus(status, rid)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)

    def getReceiptByRIDAndQuantity(self, quantity, rid):
        dao = ReceiptDAO()
        result = dao.getReceiptByRIDAndQuantity(quantity, rid)
        result_list = []
        if not result:
            return jsonify(Error="Receipt Not Found"), 404
        else:
            for row in result:
                req = self.build_receipt_dict(row)
                result_list.append(req)
        return jsonify(Receipt=result_list)


    def searchReceipts(self, args):

        rid = args.get("rid")
        quantity = args.get("quantity")
        status = args.get("status")

        dao = ReceiptDAO()
        receipts_list = []
        if (len(args) == 1) and rid:
            receipts_list = dao.getReceiptByRID(rid)
        elif (len(args) == 1) and quantity:
            receipts_list = dao.getReceiptByQuantity(quantity)
        elif (len(args) == 1) and status:
            receipts_list = dao.getReceiptByStatus(status)
        elif (len(args) == 2) and rid and quantity:
            receipts_list = dao.getReceiptByRIDAndQuantity(rid, quantity)
        elif (len(args) == 2) and rid and status:
            receipts_list = dao.getReceiptByRIDAndStatus(rid, status)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in receipts_list:
            result = self.build_receipt_dict(row)
            result_list.append(result)
        return jsonify(Receipts=result_list)

    def insertReceipt(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error="Malformed post Receipt"), 400
        else:
            oid = form['oid']
            ReqID = form['ReqID']
            sid = form['sid']
            pid = form['pid']
            rid = form['rid']
            quantity = form['quantity']
            status = form['status']

            if oid and ReqID and sid and pid and rid and quantity and status:
                dao = ReceiptDAO()
                lid = dao.insert(oid, ReqID, sid, pid, rid, quantity, status)
                result = self.build_receipt_attributes(oid, ReqID, sid, pid, rid, quantity, status)
                return jsonify(Receipts=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post Receipt"), 400

    def insertReceiptJson(self, json):
        oid = json['oid']
        ReqID = json['ReqID']
        sid = json['sid']
        pid = json['pid']
        rid = json['rid']
        quantity = json['quantity']
        status = json['status']
        if oid and ReqID and sid and pid and rid and quantity and status:
            dao = ReceiptDAO()
            oid = dao.insert(oid, ReqID, sid, pid, rid, quantity, status)
            result = self.build_receipt_attributes(oid, ReqID, sid, pid, rid, quantity, status)
            return jsonify(receipt=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post Receipt"), 400

    def deleteReceipt(self, oid):
        dao = ReceiptDAO()
        if not dao.getreceiptById(oid):
            return jsonify(Error="Part not found."), 404
        else:
            dao.delete(oid)
            return jsonify(DeleteStatus="OK"), 200

    def updateReceipt(self, oid, form):
        dao = ReceiptDAO()
        if not dao.getreceiptById(oid):
            return jsonify(Error="Part not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update Receipt"), 400
            else:
                oid = form['oid']
                ReqID = form['ReqID']
                sid = form['sid']
                pid = form['pid']
                rid = form['rid']
                quantity = form['quantity']
                status = form['status']
                if oid and ReqID and sid and pid and rid and quantity and status:
                    dao.update(oid, ReqID, sid, pid, rid, quantity, status)
                    result = self.build_receipt_attributes(oid, ReqID, sid, pid, rid, quantity, status)
                    return jsonify(Receipt=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update Receipt"), 400
