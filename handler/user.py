from flask import jsonify
from daos.user import userDAO


class userHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['username'] = row[1]
        result['password'] = row[2]
        result['fname'] = row[3]
        result['lname'] = row[4]
        result['email'] = row[5]
        result['state'] = row[6]
        result['city'] = row[7]
        result['neighborhood'] = row[8]
        result['street'] = row[9]
        result['housenumber'] = row[10]
        result['zipcode'] = row[11]
        return result

    def build_phones_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['phone'] = row[1]
        return result

    def insertUser(self, form):
        if form and len(form) == 7:
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

            if username and password and fname and lname and email and phone and\
                    state and city and neighborhood and street and housenumber and zipcode:
                dao = userDAO()
                uid = dao.insert(username, password, fname, lname, email, phone,
                                 state, city, neighborhood, street, housenumber, zipcode)
                result = {}
                result['uid'] = uid
                result['username'] = username
                result['password'] = password
                result['fname'] = fname
                result['lname'] = lname
                result['email'] = email
                result['phone'] = int(phone)
                result['state'] = state
                result['city'] = city
                result['neighborhood'] = neighborhood
                result['street'] = street
                result['housenumber'] = housenumber
                result['zipcode'] = zipcode
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed post request")

        elif form and len(form) == 8: #*********************************REQUESTER OR SUPPLIER*********************************
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
            location = form['location']

            if username and password and fname and lname and email and phone and \
                    state and city and neighborhood and street and housenumber and zipcode and location:
                dao = userDAO()
                uid = dao.insert(username, password, fname, lname, email, phone,
                                 state, city, neighborhood, street, housenumber, zipcode)
                result = {}
                result['uid'] = uid
                result['username'] = username
                result['password'] = password
                result['fname'] = fname
                result['lname'] = lname
                result['email'] = email
                result['phone'] = int(phone)
                result['state'] = state
                result['city'] = city
                result['neighborhood'] = neighborhood
                result['street'] = street
                result['housenumber'] = housenumber
                result['zipcode'] = zipcode
                result['location'] = location
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
        user = dao.getUserById(username)
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
        user_list = dao.getUserByFirstName(lname)
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
        phones = dao.getUserPhoneNumber(uid)
        if not phones:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_phones_dict(phones)
            return jsonify(User=result)

    def getUserByState(self, state):
        dao = userDAO()
        user_list = dao.getUserByState(state)
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

    def getUserByNeighborhood(self, neighborhood):
        dao = userDAO()
        user_list = dao.getUserByneighborhood(neighborhood)
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

    def getUserByStateAndCity(self, state, city):
        dao = userDAO()
        user_list = dao.getUserByStateAndCity(state, city)
        result_list = []
        if not user_list:
            return jsonify(Error="Users not found"), 404
        else:
            for row in user_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

