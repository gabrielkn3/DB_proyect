from flask import jsonify
from daos.supplier import SupplierDAO
from daos.company import CompanyDAO
from handler.user import userHandler





class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Email'] = row[3]
        result['City'] = row[4]
        result['Country'] = row[5]
        result['Address'] = row[6]
        result['Zip Code'] = row[7]
        return result

    def build_company_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['Company Name'] = row[1]
        result['Business Type'] = row[2]
        result['Description'] = row[3]
        result['sid'] = row[4]
        return result


    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
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

    def getResourcesBySupplierId(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:#supplier exists
            resources = dao.getResourcesBySID(sid)
            result_list = []
            for row in resources:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    def getSupplierByLocation(self, form):
        dao = SupplierDAO()
        slocation = form["slocation"]
        if not slocation:
            return jsonify(Error="Malformed request in [GET SUPPLIER BY LOCATION]")
        suppliers = dao.getSuppliersByLocation(slocation)
        result_list = []
        for row in suppliers:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)



    def insertSupplier(self, form):#slocation is the only additional attribute from supplier that user does not have
        if len(form) == 8:
                s_dao = SupplierDAO()
                slocation = form['location']
                supplier = userHandler().insertUser(form)
                sid = s_dao.insert(supplier['uid'], slocation)
                supplier['sid'] = sid
                return jsonify(Supplier=supplier), 201

        elif len(form) > 8:#if supplier wants to be a company
            comp = CompanyDAO()
            s_dao = SupplierDAO()
            slocation = form['location']
            compname = form['cname']
            btype = form['btype']
            description= form['description']
            supplier = userHandler().insertUser(form)
            sid = s_dao.insert(supplier['uid'], slocation)
            cid = comp.insert(sid, compname, btype, description)
            supplier['sid'] = sid
            company = supplier
            company['cid'] = cid
            return jsonify(Company=company), 201



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




  #--------------------------------------------------------------------COMPANIES--------------------------------------------------------------------------------------

    def getAllCompanies(self):
        dao = CompanyDAO()
        c_list = dao.getAllCompanies()
        result_list = []
        if not c_list:
            return jsonify(Result="No companies registered.")
        for row in c_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Companies=result_list)

    def getCompanyById(self, cid):

        dao = CompanyDAO()
        row = dao.getCompanyById(cid)
        if not row:
            return jsonify(Error="Company Not Found"), 404
        else:
            company = self.build_company_dict(row)
        return jsonify(Company=company)

    def getCompanyBySid(self, sid):
        dao = SupplierDAO()
        cdao = CompanyDAO()

        supplier = dao.getSupplierById(sid)
        if not supplier:
            return jsonify(Error="Company Not Found in Suppliers!!"), 404
        else:
            row = cdao.getCompanyBySid(sid)
            company = self.build_company_dict(row)
        return jsonify(Company=company)

    def getCompanyByName(self, form):
        dao = CompanyDAO()
        cname = form['cname']
        if not cname:
            return jsonify(Error="Company name must be provided."), 405
        c = dao.getCompanyByName(cname)
        if not c:
            return jsonify(Error="Company Not Found"), 404
        else:
            company = self.build_company_dict(c)
        return jsonify(Company=company)

    def getCompanyByType(self, form):
        dao = CompanyDAO()
        btype = form['btype']
        if not btype:
            return jsonify(Error="Company type must be provided."), 405
        c_list = dao.getCompanyByType(btype)
        result_list = []
        if not c_list:
            return jsonify(Error="Company Not Found"), 404
        else:
            for row in c_list:
                result = self.build_company_dict(row)
                result_list.append(result)
            return jsonify(Companies=result_list)









    def deleteCompany(self, cid):
        dao = CompanyDAO()

        row = dao.getCompanyById(cid)
        if not row:
            return jsonify(Error="Company Not Found"), 404
        else:
            status = dao.delete(cid)
            if status:
                return jsonify(Result="Deleted Company with sid: "+str(status))
            else:
                return jsonify(Error="Error deleting (COMPANY) request"), 400
