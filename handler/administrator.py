from flask import jsonify
from daos.administrator import adminDAO

class adminHandler:
    def build_admin_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['uid'] = row[1]
        return result

    def insertAdmin(self, form):
        if form and len(form) == 1:
            ##aid = form['aid']
            uid = form['uid']

            if uid:
                dao = adminDAO()
                aid = dao.insert(uid)
                result = {}
                result['aid'] = aid
                result['uid'] = uid
                return jsonify(Admin=result), 201
            else:
                return jsonify(Error="Malformed post request")

        else:
            return jsonify(Error="Malformed post request")

    def deleteAdmin(self, aid):
        dao = adminDAO()
        if not dao.getAdminByAdminId(aid):
            return jsonify(Error="Admin not found."), 404
        else:
            dao.delete(aid)
            return jsonify(DeleteStatus="Admin deleted successfully."), 200

    #update not necessary

    def getAllAdmins(self):
        dao = adminDAO()
        admin_list = dao.getAllAdmins()
        result_list = []

        if not admin_list:
            return jsonify(Error="No admins found"), 404

        for row in admin_list:
            result_list.append(self.build_admin_dict(row))
        return jsonify(Admins=result_list)


    def getAdminByAdminId(self, aid):
        dao = adminDAO()
        admin = dao.getAdminByAdminId(aid)
        if not admin:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_admin_dict(admin)
        return jsonify(Admin=result)

    def getAdminByUserId(self, uid):
        dao = adminDAO()
        admin = dao.getAdminByUserId(uid)
        if not admin:
            return jsonify(Error="User not found"), 404
        else:
            result = self.build_admin_dict(admin)
            return jsonify(Admin=result)