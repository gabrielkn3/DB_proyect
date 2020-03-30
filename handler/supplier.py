from flask import jsonify
from daos.supplier import SupplierDAO


class SupplierHandler:
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

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        result['rlocation'] = row[3]
        result['sid'] = row[4]
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

    def getResourceBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        resource_list = dao.getResourceBySupplierId(sid)
        result_list = []
        for row in resource_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(ResourceSupplied=result_list)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            address = args.get("address")
            if address:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByCity(address)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(row)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, form):
        if form and len(form) == 3:
            stype = form['stype']
            sname = form['sname']
            semail = form['semail']
            sphone = form['sphone']
            saddress = form['saddress']
            sfinance = form['sfinance']

            if stype and sname and semail and sphone and saddress and sfinance:
                dao = SupplierDAO()
                sid = dao.insert(stype, sname, semail, sphone, saddress, sfinance)
                result = {}
                result["sid"] = sid
                result["stype"] = stype
                result["sname"] = sname
                result["semail"] = semail
                result["sphone"] = sphone
                result["saddress"] = saddress
                result["sfinance"] = sfinance

                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")