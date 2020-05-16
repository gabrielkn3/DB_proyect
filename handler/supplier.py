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



    def insertSupplier(self, form):
        #insert supplier from scratch
        if len(form) == 11:
                if not self.verifySupplierForm(form):
                    return jsonify(Error="Info given for inserting Supplier ->Incomplete"), 400
                slocation = form['location']
                s_dao = SupplierDAO()
                user = userHandler().insertUser(form)
                sid = s_dao.insert(slocation, user['uid'])
                row = s_dao.getSupplierById(sid)
                if not row:
                    return jsonify(Error="Supplier was NOT Inserted Correctly"), 404
                else:
                    supplier = self.build_supplier_dict(row)
                    supplier['Phone No.'] = user['phone']
                    return jsonify(NewSupplier=supplier), 201
        else:
                return jsonify(Error="Malformed POST(SUPPLIER) request")





#NOT SUPPORTED
    def updateSupplier (self, sid, form):
             return jsonify(Error="Update (SUPPLIER) not supported"), 400
             # user_handler = userHandler()
             # if not dao.getSupplierById(sid):
             #    return jsonify(Error = "Supplier not found."), 404
             # else:
             #    if len(form) > 1:
             #        return user_handler.updateUser(form["uid"], form)
             #    else:
             #        slocation = form['slocation']
             #        if slocation:
             #            dao.update(sid, slocation)
             #            result = self.build_supplier_attributes(sid, slocation)
             #            return jsonify(Supplier=result), 200
             #        else:
             #            return jsonify(Error="Unexpected attributes in update(SUPPLIER) request"), 400

    def deleteSupplier(self, sid):
            return jsonify(Error="Delete (SUPPLIER) not supported"), 400
            # if not dao.getSupplierById(sid):
            #     return jsonify(Error="Supplier not found."), 404
            # else:
            #     status = dao.delete(sid)
            #     if status:
            #         return jsonify(Result="Deleted Supplier with sid: "+str(status))
            #     else:
            #         return jsonify(Error="Error deleting (SUPPLIER) request"), 400




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




    def insertCompany(self, form):
        #from scratch, need to insert in user, supplier and company
        if len(form) == 14:
            if not self.verifyCompanyForm(form):
                return jsonify(Error="Info given for inserting Company ->Incomplete"), 400
            s_dao = SupplierDAO()
            c_dao = CompanyDAO()
            slocation = form['location']
            cname = form['cname']
            btype = form['btype']
            cdescription = form['description']
            user = userHandler().insertUser(form)
            sid = s_dao.insert(slocation, user['uid'])
            row1 = s_dao.getSupplierById(sid)
            if not row1:
                return jsonify(Error="Supplier was NOT Inserted Correctly"), 404
            else:
                supplier = self.build_supplier_dict(row1)
                cid = c_dao.insert(cname, btype, cdescription, sid)
                row2 = c_dao.getCompanyById(cid)
                if not row2:
                    return jsonify(Error="Company was NOT Inserted Correctly"), 404
                supplier['Phone No.'] = user['phone']
                supplier['Company Name'] = cname
                supplier['Business Type'] = btype
                supplier['Description'] = cdescription
                supplier['cid'] = cid
                return jsonify(New_Company=supplier), 201

        elif len(form) == 4: #not from scratch, Only insert in company ==> EXISTING Supplier
            if not self.verifySmallForm(form):
                return jsonify(Error="Info given for inserting Company ->Incomplete"), 400
            sid = form['sid']
            cname = form['cname']
            btype = form['btype']
            cdescription = form['description']
            s_dao = SupplierDAO()
            c_dao = CompanyDAO()
            row = s_dao.getSupplierById(sid)
            if not row:
                return jsonify(Error="Supplier does not exist -> Cannot register Company with this info, must register as supṕlier first."), 400
            cid = c_dao.insert(cname, btype, cdescription, sid)
            row2 = c_dao.getCompanyById(cid)
            if not row2:
                return jsonify(Error="Company was NOT Inserted Correctly"), 404
            company = self.build_company_dict(row2)
            return jsonify(Upgraded_to_Company=company), 201
        else:
            return jsonify(Error="Malformed POST request (COMPANY)"), 400




    def deleteCompany(self, cid):
        return jsonify(Error="Delete (COMPANY) not supported"), 400
        # row = dao.getCompanyById(cid)
        # if not row:
        #     return jsonify(Error="Company Not Found"), 404
        # else:
        #     status = dao.delete(cid)
        #     if status:
        #         return jsonify(Result="Deleted Company with sid: "+str(status))
        #     else:
        #         return jsonify(Error="Error deleting (COMPANY) request"), 400

#For Registering as Supplier
    def verifySupplierForm(self, form):
        username = form['username']
        password = form['password']
        fname = form['firstname']
        lname = form['lastname']
        email = form['email']
        country = form['country']
        city = form['city']
        address = form['address']
        zip = form['zip']
        slocation = form['location']
        phone = form['phone']
        return (username and password and fname and lname and email and country and city and address and zip and slocation and phone)

  #For registering a user as Supplier->Company
    def verifyCompanyForm(self, form):
        username = form['username']
        password = form['password']
        fname = form['firstname']
        lname = form['lastname']
        email = form['email']
        country = form['country']
        city = form['city']
        address = form['address']
        zip = form['zip']
        slocation = form['location']
        phone = form['phone']
        cname = form['cname']
        btype = form['btype']
        cdescription = form['description']
        return (username and password and fname and lname and email and country and city and address and zip and slocation and phone and cname and btype and cdescription)

#For registering a Supplier as Company
    def verifySmallForm(self, form):
        sid = form['sid']
        cname = form['cname']
        btype = form['btype']
        cdescription = form['description']
        return (sid and cname and btype and cdescription)