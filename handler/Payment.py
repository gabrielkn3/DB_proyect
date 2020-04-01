from flask import jsonify
from daos.Payment import paymentDAO

class paymentHandler:
    def build_payment_dict(self,row):
        result = {}
        result['pid'] = row[0]
        result['reqid'] = row[1]
        result['sid'] = row[2]
        result['price'] = row[3]
        result['paymentType'] = row[4]
        result['acDetails'] = row[5]
        return result

    def insertPayment(self, form):
        if form and len(form) == 5:
            reqid = form['reqid']
            sid = form['sid']
            price = form['price']
            paymentType = form['paymentType']
            acDetail = form['acDetail']

            if reqid and sid and price and paymentType and acDetail:
                dao = paymentDAO()
                pid = dao.insert(reqid, sid, paymentType, paymentType, acDetail)
                result = {}
                result['pid'] = pid
                result['reqid'] = reqid
                result['sid'] = sid
                result['price'] = price
                result['paymentType'] = paymentType
                result['acDetails'] = acDetail
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
            return jsonify(DeleteStatus="Payment deleted succesfully."), 200

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
                    dao.update(reqid, sid, price, paymentType, acDetail, pid)
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
        # payment_list = dao.getAllPayments()
        # result_list = []
        # for row in payment_list:
        #     result_list.append(self.build_payment_dict(row))
        # return jsonify(Payments=result_list)
        return jsonify(Payment=dao.getAllPayments())

    def getPaymentByPaymentId(self, pid):
        dao = paymentDAO()
        payment = dao.getPaymentByPaymentId(pid)
        # if not payment:
        #     return jsonify(Error="Payment not found."), 404
        # else:
        #     result = self.build_payment_dict(payment)
        #     return jsonify(Payment=result)
        return jsonify(Payment=payment)

    def getPaymentByRequestorId(self, reqid):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByRequestorId(reqid)
        # result_list = []
        # for row in payment_list:
        #     result_list.append(self.build_payment_dict(row))
        # return jsonify(Payments=result_list)
        return jsonify(Payment=payment_list)

    def getPaymentBySupplierId(self, sid):
        dao = paymentDAO()
        payment_list = dao.getPaymentsBySupplierId(sid)
        # result_list = []
        # for row in payment_list:
        #     result_list.append(self.build_payment_dict(row))
        # return jsonify(Payments=result_list)
        return jsonify(Payment=payment_list)

    def getPaymentByPrice(self, price):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByPrice(price)
        # result_list = []
        # for row in payment_list:
        #     result_list.append(self.build_payment_dict(row))
        # return jsonify(Payments=result_list)
        return jsonify(Payment=payment_list)

    def getPaymentByType(self, paymentType):
        dao = paymentDAO()
        payment_list = dao.getPaymentsByType(paymentType)
        # result_list = []
        # for row in payment_list:
        #     result_list.append(self.build_payment_dict(row))
        # return jsonify(Payments=result_list)
        return jsonify(Payment=payment_list)

