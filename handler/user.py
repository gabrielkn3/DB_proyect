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

    def insertUser(self, form):
        if form and len(form) == 7:
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
                address = form['address']
                if username and password and fname and lname and email and phone and address:
                    dao.update(username, password, fname, lname, email, phone, address, uid)
                    result = {}
                    result['uid'] = uid
                    result['username'] = username
                    result['password'] = password
                    result['fname'] = fname
                    result['lname'] = lname
                    result['email'] = email
                    result['phone'] = phone
                    result['address'] = address
                    return jsonify(User=result), 200
                else:
                    return  jsonify(Error="Unexpected attributes in update request."), 400

    def getAllUsers(self):
        dao = userDAO()
        # users_list = dao.getAllUsers()
        # result_list = []
        # for row in users_list:
        #     result_list.append(self.build_user_dict(row))
        # return jsonify(Users=result_list)
        return jsonify(Result=dao.getAllUsers())

    def getUserById(self, id):
        dao = userDAO()
        # user = dao.getUserById(id)
        # if not user:
        #     return jsonify(Error="User not found"), 404
        # else:
        #     result = self.build_user_dict(user)
        #     return jsonify(User=result)
        return jsonify(Result=dao.getUserById(id))

    def getUserByUsername(self, username):
        dao = userDAO()
        # user = dao.getUserById(username)
        # if not user:
        #     return jsonify(Error="User not found"), 404
        # else:
        #     result = self.build_user_dict(user)
        #     return jsonify(User=result)

        return jsonify(Result=dao.getUserByUsername(username))

    def getUserByFirstName(self, fname):
        dao = userDAO()
        # user_list = dao.getUserByFirstName(fname)
        # result_list = []
        # if not user_list:
        #     return jsonify(Error="Users not found"), 404
        # else:
        #     for row in user_list:
        #         result = self.build_user_dict(row)
        #         result_list.append(result)
        #     return jsonify(Users=result_list)
        return jsonify(Result=dao.getUserByFirstName(fname))

    def getUserByLastName(self, lname):
        dao = userDAO()
        # user_list = dao.getUserByFirstName(lname)
        # result_list = []
        # if not user_list:
        #     return jsonify(Error="Users not found"), 404
        # else:
        #     for row in user_list:
        #         result = self.build_user_dict(row)
        #         result_list.append(result)
        #     return jsonify(Users=result_list)
        return jsonify(Result=dao.getUserByLastName(lname))

    def getUserByEmail(self, email):
        dao = userDAO()
        # user = dao.getUserByEmail(email)
        # if not user:
        #     return jsonify(Error="User not found"), 404
        # else:
        #     result = self.build_user_dict(user)
        #     return jsonify(User=result)
        return jsonify(Result=dao.getUserByEmail(email))

    def getUserByPhoneNumber(self, phone):
        dao = userDAO()
        # user = dao.getUserById(phone)
        # if not user:
        #     return jsonify(Error="User not found"), 404
        # else:
        #     result = self.build_user_dict(user)
        #     return jsonify(User=result)
        return jsonify(Result=dao.getUserByPhoneNumber(phone))

    def getUserByAddress(self, address):
        dao = userDAO()
        # user_list = dao.getUserByAddress(address)
        # result_list = []
        # if not user_list:
        #     return jsonify(Error="Users not found"), 404
        # else:
        #     for row in user_list:
        #         result = self.build_user_dict(row)
        #         result_list.append(result)
        #     return jsonify(Users=result_list)
        return jsonify(Result=dao.getUserByAddress(address))

