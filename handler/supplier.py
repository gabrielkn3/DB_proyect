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

    def build_resource_from_listing(self, row):
        result = {}
        result['rtype'] = row[3]
        result['rquantity'] = row[6]
        result['sid'] = row[2]
        return result

    def build_supplier_attributes(self, sid, slocation):
        result = {}
        result['sid'] = sid
        result['slocation'] = slocation
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


    def searchSuppliers(self, form):
        if len(form) > 1:
            return jsonify(Error = "Malformed search(SUPPLIER) string."), 400
        else:
            slocation = form["slocation"]
            if slocation:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByLocation(slocation)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(result)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def getResourcesBySupplierId(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:#supplier exists
            listings = dao.getResourcesBySID(sid)
            resources = self.build_resource_from_listing(listings)
            return jsonify(Resources=resources)




    def insertSupplier(self, form):#slocation is the only additional attribute from supplier that user does not have
        if len(form) == 8:
                s_dao = SupplierDAO()
                slocation = form['location']
                supplier = userHandler().insertUser(form)
                sid = s_dao.insert(supplier['uid'], slocation)
                supplier['sid'] = sid
                return jsonify(Supplier=supplier), 201

        else:
                return jsonify(Error="Malformed post(SUPPLIER) request")




    def updateSupplier (self, sid, form):
             dao = SupplierDAO()
             user_handler = userHandler()
             if not dao.getSupplierById(sid):
                return jsonify(Error = "Supplier not found."), 404
             else:
                if len(form) > 1:
                    return user_handler.updateUser(form["uid"], form)
                else:
                    slocation = form['slocation']
                    if slocation:
                        dao.update(sid, slocation)
                        result = self.build_supplier_attributes(sid, slocation)
                        return jsonify(Supplier=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update(SUPPLIER) request"), 400


    def deleteSupplier(self,sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            status = dao.delete(sid)
            if status:
                return jsonify(Result="Deleted Supplier with sid: "+str(status))
            else:
                return jsonify(Error="Error deleting (SUPPLIER) request"), 400

