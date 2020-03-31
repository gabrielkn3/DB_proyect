from flask import jsonify
from daos.supplier import SupplierDAO
from handler.user import userHandler


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['uid'] = row[1]
        result['slocation'] = row[2]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        result['rlocation'] = row[3]
        result['sid'] = row[4]
        return result

    def build_supplier_attributes(self, sid, uid, slocation):
        result = {};
        result['sid'] = sid
        result['slocation'] = slocation
        result['uid'] = uid
        return result

    def getAllSuppliers(self):

        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):

        dao = SupplierDAO()

        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
        return jsonify(Supplier=supplier)


    # def searchSuppliers(self, args):
    #     if len(args) > 1:
    #         return jsonify(Error = "Malformed search string."), 400
    #     else:
    #         address = args.get("address")
    #         if address:
    #             dao = SupplierDAO()
    #             supplier_list = dao.getSuppliersByCity(address)
    #             result_list = []
    #             for row in supplier_list:
    #                 result = self.build_supplier_dict(row)
    #                 result_list.append(row)
    #             return jsonify(Suppliers=result_list)
    #         else:
    #             return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, uid, form):
        if form and len(form) == 1:
            slocation = form['slocation']

            if uid and slocation:
                dao = SupplierDAO()
                sid = dao.insert(uid, slocation)
                result = {}
                result["sid"] = sid
                result["uid"] = uid
                result["slocation"] = slocation
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post(SUPPLIER) request")
        else:
            return jsonify(Error="Malformed post(SUPPLIER) request")


    def updateSupplier(self, sid, uid, form):
             dao = SupplierDAO()
             user_handler = userHandler()
             if not dao.getSupplierById(sid):
                return jsonify(Error = "Supplier not found."), 404
             else:
                if len(form) != 1:
                    return user_handler.updateUser(uid, form)
                else:
                    slocation = form['slocation']
                    if slocation:
                        dao.update(slocation)
                        result = self.build_supplier_attributes(sid, uid, slocation)
                        return jsonify(Supplier=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update(SUPPLIER) request"), 400