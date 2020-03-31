from flask import jsonify

from daos.Tool import ToolDAO

from daos.resource import ResourceDAO


class ToolHandler:
    def build_Tool_dict(self, row):
        result = {};
        result['tid'] = row[0]
        result['rid'] = row[1]
        result['tbrand'] = row[2]
        result['tname'] = row[3]
        result['tdescription'] = row[4]
        return result

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

    def build_requester_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ReqID'] = row[1]
        result['rfirstname'] = row[2]
        result['rlastname'] = row[3]
        result['remail'] = row[4]
        result['rphone'] = row[5]
        result['raddress'] = row[6]
        result['rlocation'] = row[6]
        return result

    def build_Tool_attributes(self, tid, rid, tbrand, tname, tdescription):
        result = {};
        result['tid'] = tid
        result['rid'] = rid
        result['tbrand'] = tbrand
        result['tname'] = tname
        result['tdescription'] = tdescription
        return result

    def getAllTool(self):
        dao = ToolDAO()
        Tool_list = dao.getAllTool()
        result_list = []
        for row in Tool_list:
            result = self.build_Tool_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getToolById(self, tid):
        dao = ToolDAO()
        row = dao.getToolById(tid)
        if not row:
            return jsonify(Error = "Tool Not Found"), 404
        else:
            Tool = self.build_Tool_dict(row)
            return jsonify(Tool = Tool)

    def getToolByName(self, tname):
        dao = ToolDAO()
        Toollist = dao.getToolByName(tname)
        result_list = []
        if not Toollist:
            return jsonify(Error = "No Tool Found with the specified flavor"), 404
        else:
            for row in Toollist:
                result = self.build_Tool_dict(row)
                result_list.append(result)
            return jsonify(Tool = result_list)

    def getToolByBrand(self, tbrand):    #Filter by Tool category
        dao = ToolDAO()
        Toollist = dao.getToolByBrand(tbrand)
        result_list = []
        if not Toollist:
            return jsonify(Error = "No Tool Found with the Specified Brand"), 404
        else:
            for row in Toollist:
                result = self.build_Tool_dict(row)
                result_list.append(result)
            return jsonify(Tool = result_list)

    def insertTool(self, form):
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            tbrand = form['tbrand']
            tname = form['tname']
            tdescription = form['tdescription']

            if rtype and rname and rlocation and sid and tbrand and tname and tdescription:
                resourcedao = ResourceDAO()
                dao = ToolDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                tid = dao.insert(rid, tbrand, tname, tdescription)
                result = self.build_Tool_attributes(tid, rid, tbrand, tname, tdescription)
                return jsonify(Tool=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertToolJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']
        tbrand = json['tbrand']
        tname = json['tname']
        tdescription = json['tdescription']


        if rtype and rname and rlocation and sid and tbrand and tname and tdescription:
            resourcedao = ResourceDAO()
            dao = ToolDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            tid = dao.insert(rid, tbrand, tname, tdescription)
            result = self.build_Tool_attributes(tid, rid, tbrand, tname, tdescription)
            return jsonify(Tool=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteTool(self, tid):
        dao = ToolDAO()
        resourceDAO = ResourceDAO()

        if not dao.getToolById(tid):
            return jsonify(Error = "Tool not found."), 404
        else:
            rid = dao.getResourceID(tid)
            dao.delete(tid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateTool(self, tid, form):
        resourceDAO = ResourceDAO()
        dao = ToolDAO()
        if not dao.getToolById(tid):
            return jsonify(Error = "Tool not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                tbrand = form['tbrand']
                tname = form['tname']
                tdescription = form['tdescription']

                rid = dao.getResourceID(tid)

                if rtype and rname and rlocation and sid and tbrand and tname and tdescription:
                    dao.update(tid, tbrand, tname, tdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_Tool_attributes(tid, rid, tbrand, tname,tdescription)
                    return jsonify(Tool=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Tool_counts(self, Tool_counts):
        result = []
        #print(part_counts)
        for P in Tool_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByToolId(self):
        dao = ToolDAO()
        result = dao.getCountByToolId()
        #print(self.build_part_counts(result))
        #return jsonify(ToolCounts = self.build_Tool_counts(result)), 200
        return jsonify(ToolCounts=result), 200
