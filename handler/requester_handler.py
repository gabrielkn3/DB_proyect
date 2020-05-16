from flask import jsonify
from daos.requester import RequesterDAO
from handler.user import userHandler


class RequesterHandler:
    def build_requester_dict(self, row):
        result = {}
        result['reqid'] = row[0]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Email'] = row[3]
        result['City'] = row[4]
        result['Country'] = row[5]
        result['Address'] = row[6]
        result['Zip Code'] = row[7]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rtype'] = row[2]
        return result

    def build_requester_attributes(self, reqid, reqlocation):
        result = {}
        result['reqid'] = reqid
        result['reqlocation'] = reqlocation
        return result

    def getAllRequesters(self):

        dao = RequesterDAO()
        requesters_list = dao.getAllRequesters()
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters=result_list)

    def getRequesterById(self, reqid):

        dao = RequesterDAO()
        row = dao.getRequesterById(reqid)
        if not row:
            return jsonify(Error="Requester Not Found"), 404
        else:
            requester = self.build_requester_dict(row)
        return jsonify(Requester=requester)


    def getResourcesByRequesterId(self, reqid):

        dao = RequesterDAO()
        requester = dao.getRequesterById(reqid)
        result_list = []
        if not requester:
            return jsonify(Error="Requester Not Found"), 404
        else:  # Requester exists
            resource_list = dao.getResourcesByREQID(reqid)
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    def insertRequester(self, form):
        # insert requester from scratch
        if len(form) == 11:
            if not self.verifyRequesterForm(form):
                return jsonify(Error="Info given for inserting Requester ->Incomplete"), 400
            r_dao = RequesterDAO()
            reqlocation = form['location']
            user = userHandler().insertUser(form)
            reqid = r_dao.insert(reqlocation, user['uid'])
            row = r_dao.getRequesterById(reqid)
            if not row:
                return jsonify(Error="Requester was NOT Inserted Correctly"), 404
            else:
                requester = self.build_requester_dict(row)
                requester['Phone No.'] = user['phone']
                return jsonify(New_Requester=requester), 201
        else:
                return jsonify(Error="Malformed POST(REQUESTER) request")







    #Only filters by location... cheking more requirements later
    def searchRequesters(self, form):
        if len(form) > 1:
            return jsonify(Error="Malformed search(REQUESTER) string."), 400
        else:
            reqlocation = form["reqlocation"]
            if reqlocation:
                dao = RequesterDAO()
                requester_list = dao.getRequestersByLocation(reqlocation)
                result_list = []
                for row in requester_list:
                    result = self.build_requester_dict(row)
                    result_list.append(result)
                return jsonify(Requesters=result_list)
            else:
                return jsonify(Error="Malformed search(REQUESTER) string."), 400





   #------------------------------------------------------------------------------------------------------------------------------------------

    def updateRequester (self, reqid, form):
        return jsonify(Error="Update (REQUESTER) not supported"), 400

             # dao = RequesterDAO()
             # user_handler = userHandler()
             # if not dao.getRequesterById(reqid):
             #    return jsonify(Error = "Requester not found."), 404
             # else:
             #    if len(form) > 1:
             #        return user_handler.updateUser(form["uid"], form)
             #    else:
             #        reqlocation = form['reqlocation']
             #        if reqlocation:
             #            dao.update(reqid, reqlocation)
             #            result = self.build_requester_attributes(reqid, reqlocation)
             #            return jsonify(Requester=result), 200
             #        else:
             #            return jsonify(Error="Unexpected attributes in update(REQUESTER) request"), 400


    def deleteRequester(self,reqid):
        return jsonify(Error="Delete (REQUESTER) not supported"), 400
        # if not dao.getRequesterById(reqid):
        #     return jsonify(Error="Requester not found."), 404
        # else:
        #     status = dao.delete(reqid)
        #     if status:
        #         return jsonify(Result="Deleted REQUESTER with reqid: "+str(status))
        #     else:
        #         return jsonify(Error="Error deleting (REQUESTER) request"), 400



#For Registering as Requester
    def verifyRequesterForm(self, form):
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