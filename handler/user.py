from flask import jsonify
from daos.user import userDAO

class userHandler:

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Email'] = row[3]
        result['City'] = row[4]
        result['Country'] = row[5]
        result['Address'] = row[6]
        result['Zip Code'] = row[7]
        return result


    def build_phone_dict(self,row):
        result = {}
        result['uid'] = row[0]
        result['Phone No.'] = row[1]
        result['First Name'] = row[2]
        result['Last Name'] = row[3]
        result['Email'] = row[4]
        return result

    def insertUser(self, form):
        if form and len(form) == 10:
            username = form['username']
            password = form['password']
            fname = form['fname']
            lname = form['lname']
            email = form['email']
            phone = form['phone']
            country = form['country']
            city = form['city']
            saddress = form['saddress']
            zipcode = form['zip']

            if username and password and fname and lname and email and phone and\
                    country and city and saddress and zipcode:
                dao = userDAO()
                uid = dao.insert(username, password, fname, lname, email, phone, country, city, saddress, zipcode)
                result = {}
                result['uid'] = uid
                result['username'] = username
                result['password'] = password
                result['fname'] = fname
                result['lname'] = lname
                result['email'] = email
                result['phone'] = int(phone)
                result['country'] = country
                result['city'] = city
                result['saddress'] = saddress
                result['zip'] = zipcode
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed post request")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif form and len(form) == 11: #*********************************REQUESTER OR SUPPLIER*********************************
            username = form['username']
            password = form['password']
            fname = form['firstname']
            lname = form['lastname']
            email = form['email']
            phone = form['phone']
            country = form['country']
            city = form['city']
            saddress = form['address']
            zipcode = form['zip']
            location = form['location']


            if username and password and fname and lname and email and phone and \
                    country and city and saddress and zipcode and location:
                dao = userDAO()
                uid = dao.insert(username, password, fname, lname, email, phone,
                                 country, city, saddress, zipcode)
                #attributes that supplier doesn't have
                result = {}
                result['uid'] = uid
                result['phone'] = phone
                return result
            else:
                return jsonify(Error="Malformed post request")

        else:
            return jsonify(Error="Malformed post request")

    def deleteUser(self, uid):
        dao = userDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found"), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus="User deleted successfully."), 200

    def updateUser(self, uid, form):
        dao = userDAO()
        if not dao.getUserById(uid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request."), 400
            else:
                username = form['username']
                password = form['password']
                fname = form['fname']
                lname = form['lname']
                email = form['email']
                phone = form['phone']
                state = form['state']
                city = form['city']
                neighborhood = form['neighborhood']
                street = form['street']
                housenumber = form['housenumber']
                zipcode = form['zipcode']
                if username and password and fname and lname and email and phone and \
                        state and city and neighborhood and street and housenumber and zipcode:
                    dao.update(uid, username, password, fname, lname, email, phone,
                               state, city, neighborhood, street, housenumber, zipcode)
                    result = {}
                    result['uid'] = uid
                    result['username'] = username
                    result['password'] = password
                    result['fname'] = fname
                    result['lname'] = lname
                    result['email'] = email
                    result['phone'] = phone
                    result['state'] = state
                    result['city'] = city
                    result['neighborhood'] = neighborhood
                    result['street'] = street
                    result['housenumber'] = housenumber
                    result['zipcode'] = zipcode
                    return jsonify(User=result), 200
                else:
                    return  jsonify(Error="Unexpected attributes in update request."), 400

    def getAllUsers(self):
        dao = userDAO()
        users_list = dao.getAllUsers()
        result_list = []

        if not users_list:
            return jsonify(Error="Users not found"), 404

        for row in users_list:
            result_list.append(self.build_user_dict(row))
        return jsonify(Users=result_list)

    def getUserById(self, id):
        dao = userDAO()
        user = dao.getUserById(id)
        if not user:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_user_dict(user)
            return jsonify(User=result)

    def getUserByUsername(self, username):
        dao = userDAO()
        user = dao.getUserByUsername(username)
        if not user:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_user_dict(user)
            return jsonify(User=result)

    def getUserByFirstName(self, fname):
        dao = userDAO()
        user_list = dao.getUserByFirstName(fname)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByLastName(self, lname):
        dao = userDAO()
        user_list = dao.getUserByLastName(lname)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByEmail(self, email):
        dao = userDAO()
        user = dao.getUserByEmail(email)
        if not user:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_user_dict(user)
            return jsonify(User=result)

    # def getUserByPhoneNumber(self, phone):
    def getUserPhoneNumbers(self, uid):
        dao = userDAO()
        phone_list = dao.getUserPhoneNumber(uid)
        result_list = []
        if not phone_list:
            return jsonify(Error="User not found"), 404
        else:
            for row in phone_list:
                result = self.build_phone_dict(row)
                result_list.append(result)
            return jsonify(PhoneNumbers=result_list)

    def getUserByCountry(self, country):
        dao = userDAO()
        user_list = dao.getUserByCountry(country)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByCity(self, city):
        dao = userDAO()
        user_list = dao.getUserByCity(city)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByAddress(self, address):
        dao = userDAO()
        user_list = dao.getUserByAddress(address)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByZipcode(self, zipcode):
        dao = userDAO()
        user_list = dao.getUserByZipcode(zipcode)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserByCountryAndCity(self, country, city):
        dao = userDAO()
        user_list = dao.getUserByCountryAndCity(country, city)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getAllPhoneNumbers(self):
        dao = userDAO()
        phone_list = dao.getAllPhones()
        result_list = []

        if not phone_list:
            return jsonify(Error="Users not found"), 404
        for row in phone_list:
            result_list.append(self.build_phone_dict(row))
        return jsonify(PhoneNumbers=result_list)

    def test(self, uid):
        dao = userDAO()
        userID = dao.test(uid)
        if not userID:
            return jsonify(Error="User not found"), 404
        else:
            print("Handler = " + str(userID))
            return str(userID)
