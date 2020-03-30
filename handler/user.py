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
        result['phone'] = row[6]
        result['address'] = row[7]
        return result

    def getAllUsers(self):
        dao = userDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result_list.append(self.build_user_dict(row))
        return jsonify(Users=result_list)

    def insertUser(self, form):
        if form and len(form) == 3:
            username = form['username']
            password = form['password']
            fname = form['fname']
            lname = form['lname']
            email = form['email']
            phone = form['phone']
            address = form['address']

            if username and password and fname and lname and email and phone and address:
                dao = userDAO()
                uid = dao.insert(username, password, fname, lname, email, phone, address)
                result = {}
                result['uid'] = uid
                result['username'] = username
                result['password'] = password
                result['fname'] = fname
                result['lname'] = lname
                result['email'] = email
                result['phone'] = phone
                result['address'] = address
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def getUserById(self, id):
        dao = userDAO()
        if not dao.getUserById(id):
            return jsonify(Error="User not found"), 404
        else:
            user = self.getUserById(id)
            return jsonify(User=user)

    def getUserByUsername(self, username):
        dao = userDAO()
        if not dao.getUserById(username):
            return jsonify(Error="User not found"), 404
        else:
            user = self.getUserByUsername(username)
            return jsonify(User=user)

    def getUserByFirstName(self, fname):
        dao = userDAO()
        if not dao.getUserById(fname):
            return jsonify(Error="Users not found"), 404
        else:
            user_list = self.getUserByUsername(fname)
            return jsonify(Users=user_list)

    def getUserByLastName(self, lname):
        dao = userDAO()
        if not dao.getUserById(lname):
            return jsonify(Error="Users not found"), 404
        else:
            user_list = self.getUserByUsername(lname)
            return jsonify(Users=user_list)

    def getUserByEmail(self, email):
        dao = userDAO()
        if not dao.getUserById(email):
            return jsonify(Error="User not found"), 404
        else:
            user = self.getUserByUsername(email)
            return jsonify(User=user)

    def getUserByPhoneNumber(self, phone):
        dao = userDAO()
        if not dao.getUserById(phone):
            return jsonify(Error="User not found"), 404
        else:
            user = self.getUserByUsername(phone)
            return jsonify(User=user)

    def getUserByAddress(self, address):
        dao = userDAO()
        if not dao.getUserById(address):
            return jsonify(Error="Users not found"), 404
        else:
            user_list = self.getUserByUsername(address)
            return jsonify(Users=user_list)

