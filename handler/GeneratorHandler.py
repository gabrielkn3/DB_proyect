from flask import jsonify

from daos.Generator import GeneratorDAO

from daos.resource import ResourceDAO


class GeneratorHandler:
    def build_Generator_dict(self, row):
        result = {};
        result['gid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['gbrand'] = row[3]
        result['gfueltype'] = row[4]
        result['gpoweroutput'] = row[5]
        result['gdescription'] = row[6]
        result['rlocation'] = row[7]
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

    def build_Generator_attributes(self, gid, rid, gbrand, gfueltype, gpoweroutput, gdescription):
        result = {};
        result['gid'] = gid
        result['rid'] = rid
        result['gbrand'] = gbrand
        result['gfueltype'] = gfueltype
        result['gpoweroutput'] = gpoweroutput
        result['gdescription'] = gdescription
        return result

    def getAllGenerator(self):
        dao = GeneratorDAO()
        Generator_list = dao.getAllGenerator()
        result_list = []
        for row in Generator_list:
            result = self.build_Generator_dict(row)
            result_list.append(result)
        return jsonify(Results=result_list)

    def getGeneratorById(self, gid):
        dao = GeneratorDAO()
        row = dao.getGeneratorById(gid)
        if not row:
            return jsonify(Error = "Generator Not Found"), 404
        else:
            Generator = self.build_Generator_dict(row)
            return jsonify(Generator = Generator)

    def getGeneratorByFuelType(self, gfueltype):
        dao = GeneratorDAO()
        Generatorlist = dao.getGeneratorByFuelType(gfueltype)
        result_list = []
        if not Generatorlist:
            return jsonify(Error = "No Generator Found with the specified Fuel Type"), 404
        else:
            for row in Generatorlist:
                result = self.build_Generator_dict(row)
                result_list.append(result)
            return jsonify(Generator = result_list)

    def getGeneratorByPowerOutput(self, gpoweroutput):    #Filter by Generator category
        dao = GeneratorDAO()
        Generatorlist = dao.getGeneratorByPowerOutput(gpoweroutput)
        result_list = []
        if not Generatorlist:
            return jsonify(Error = "No Generator Found with the Specified Power Output"), 404
        else:
            for row in Generatorlist:
                result = self.build_Generator_dict(row)
                result_list.append(result)
            return jsonify(Generator = result_list)

    def insertGenerator(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            rtype = form['rtype']
            rlocation = form['rlocation']
            sid = form['sid']

            gbrand = form['gbrand']
            gfueltype = form['gfueltype']
            gpoweroutput = form['gpoweroutput']
            gdescription = form['gdescription']

            if rtype and rname and rlocation and sid and gbrand and gfueltype and gpoweroutput and gdescription:
                resourcedao = ResourceDAO()
                dao = GeneratorDAO()
                rid = resourcedao.insert(rtype,rname,rlocation,sid)
                gid = dao.insert(rid, gbrand, gfueltype, gpoweroutput, gdescription)
                result = self.build_Generator_attributes(gid, rid, gbrand, gfueltype, gpoweroutput, gdescription)
                return jsonify(Generator=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertGeneratorJson(self, json):

        rname = json['rname']
        rtype = json['rtype']
        rlocation = json['rlocation']
        sid = json['sid']

        gbrand = json['gbrand']
        gfueltype = json['gfueltype']
        gpoweroutput = json['gpoweroutput']
        gdescription = json['gdescription']

        if rtype and rname and rlocation and sid and gbrand and gfueltype and gpoweroutput and gdescription:
            resourcedao = ResourceDAO()
            dao = GeneratorDAO()
            rid = resourcedao.insert(rtype, rname, rlocation, sid)
            gid = dao.insert(rid, gbrand, gfueltype, gpoweroutput, gdescription)
            result = self.build_Generator_attributes(gid, rid, gbrand, gfueltype, gpoweroutput, gdescription)
            return jsonify(Generator=result), 201

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteGenerator(self, gid):
        dao = GeneratorDAO()
        resourceDAO = ResourceDAO()

        if not dao.getGeneratorById(gid):
            return jsonify(Error = "Generator not found."), 404
        else:
            rid = dao.getResourceID(gid)
            dao.delete(gid)
            resourceDAO.delete(rid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateGenerator(self, gid, form):
        resourceDAO = ResourceDAO()
        dao = GeneratorDAO()
        if not dao.getGeneratorById(gid):
            return jsonify(Error = "Generator not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                rtype = form['rtype']
                rlocation = form['rlocation']
                sid = form['sid']

                gbrand = form['gbrand']
                gfueltype = form['gfueltype']
                gpoweroutput = form['gpoweroutput']
                gdescription = form['gdescription']

                rid = dao.getResourceID(gid)

                if rtype and rname and rlocation and sid and gbrand and gfueltype and gpoweroutput and gdescription:
                    dao.update(gid, gbrand, gfueltype, gpoweroutput, gdescription)
                    resourceDAO.update(rid,rname,rtype,rlocation)
                    result = self.build_Generator_attributes(gid, rid, gbrand, gfueltype, gpoweroutput, gdescription)
                    return jsonify(Generator=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_Generator_counts(self, Generator_counts):
        result = []
        #print(part_counts)
        for P in Generator_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByGeneratorId(self):
        dao = GeneratorDAO()
        result = dao.getCountByGeneratorId()
        #print(self.build_part_counts(result))
        #return jsonify(GeneratorCounts = self.build_Generator_counts(result)), 200
        return jsonify(GeneratorCounts=result), 200
