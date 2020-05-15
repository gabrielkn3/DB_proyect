from flask import jsonify
from daos.Payment import paymentDAO
from daos.requester import RequesterDAO
from daos.supplier import SupplierDAO

class paymentHandler:
    def build_payment_dict(self, row):
        result = {}
        result['payment id'] = row[0]
        result['amount'] = row[1]
        result['payment type'] = row[2]
        result['payment details'] = row[3]
        result['requestor id'] = row[4]
        result['supplier id'] = row[5]
        return result

    def insertPayment(self, form):
        if form and len(form) == 5:
            reqid = form['reqid']
            sid = form['sid']
            price = form['pamount']
            paymentType = form['paymenttype']
            acDetail = form['paymentdetails']

            if not RequesterDAO().validateID(reqid):
                return jsonify(Error="Requester does not exist."), 404
            if not SupplierDAO().validateID(sid):
                return jsonify(Error="Supplier doest not exist."), 404
            if reqid and sid and price and paymentType and acDetail:
                dao = paymentDAO()
                pid = dao.insert(reqid, sid, price, paymentType, acDetail)
                result = {}
                result['pid'] = pid
                result['reqid'] = reqid
                result['sid'] = sid
                result['pamount'] = price
                result['paymenttype'] = paymentType
                result['paymentdetails'] = acDetail
                return jsonify(Payment=result), 201
            else:
                return jsonify(Error="Malformed post request."), 400
        else:
            return jsonify(Error="Malformed post request."), 400

    def deletePayment(self, pid):
        dao = paymentDAO()
        if not dao.getPaymentByPaymentId(pid):
            return jsonify(Error="Payment not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus="Payment deleted successfully."), 200

    def updatePayment(self, pid, form):
        dao = paymentDAO()
        if not dao.getPaymentByPaymentId(pid):
            return jsonify(Error="Payment not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed post request."), 400
            else:
                reqid = form['reqid']
                sid = form['sid']
                price = form['price']
                paymentType = form['paymentType']
                acDetail = form['acDetail']
                if reqid and sid and price and paymentType and acDetail:
                    dao.update(pid, reqid, sid, price, paymentType, acDetail)
                    result = {}
                    result['pid'] = pid
                    result['reqid'] = reqid
                    result['sid'] = sid
                    result['price'] = price
                    result['paymentType'] = paymentType
                    result['acDetails'] = acDetail
                    return jsonify(Payment=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request."), 400


    def getAllPayments(self):
        dao = paymentDAO()
        payment_list = dao.getAllPayments()
        result_list = []

        if not payment_list:
            return jsonify(Error="No payments found"), 404

        for row in payment_list:
            result_list.append(self.build_payment_dict(row))
        return jsonify(Payments=result_list)

    def getPaymentByPaymentId(self, pid):
        dao = paymentDAO()
        payment = dao.getPaymentByPaymentId(pid)
        if not payment:
            return jsonify(Error="Payment not found."), 404
        else:
            result = self.build_payment_dict(payment)
            return jsonify(Payment=result)

    def getPaymentByRequestorId(self, reqid):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByRequestorId(reqid)
        result_list = []

        if not payment_list:
            return jsonify(Error="No payments found"), 404

        for row in payment_list:
            result_list.append(self.build_payment_dict(row))
        return jsonify(Payments=result_list)

    def getPaymentBySupplierId(self, sid):
        dao = paymentDAO()
        payment_list = dao.getPaymentsBySupplierId(sid)
        result_list = []

        if not payment_list:
            return jsonify(Error="No payments found"), 404

        for row in payment_list:
            result_list.append(self.build_payment_dict(row))
        return jsonify(Payments=result_list)

    def getPaymentByPrice(self, price):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByPrice(price)
        result_list = []

        if not payment_list:
            return jsonify(Error="No payments found"), 404

        for row in payment_list:
            result_list.append(self.build_payment_dict(row))
        return jsonify(Payments=result_list)

    def getPaymentByType(self, paymentType):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByType(paymentType)
        result_list = []

        if not payment_list:
            return jsonify(Error="No payments found"), 404

        for row in payment_list:
            result_list.append(self.build_payment_dict(row))
        return jsonify(Payments=result_list)

