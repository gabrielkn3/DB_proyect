from flask import Flask, jsonify, request

from handler.BabyFoodHandler import BabyFoodHandler
from handler.DryFoodHandler import DryFoodHandler
from handler.IceHandler import IceHandler
from handler.MedicalDevicesHandler import MedicalDeviceHandler
from handler.MedicationHandler import MedicationHandler
from handler.ToolHandler import ToolHandler
from handler.resource_handler import ResourceHandler
from handler.supplier import SupplierHandler
from handler.CannedFoodHandler import CannedFoodHandler
from handler.user import userHandler
from handler.administrator import adminHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the Resource Manager DB App!'


@app.route('/ResourceApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return ResourceHandler().insertResourceJson(request.json)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/ResourceApp/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourcesById(rid)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(rid, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(rid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/<int:rid>/suppliers')
def getSuppliersByResourceId(rid):
    return ResourceHandler().getSuppliersByResourceId(rid)


@app.route ('/ResourceApp/suppliers', methods=['GET'])
def getAllSuppliers():
    if request.method == 'POST':
        # print("REQUEST: ", request.json)
        # return SupplierHandler().insertSupplier(request.json)
        pass
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            #return SupplierHandler().searchSuppliers(request.args)
            return jsonify(Error="Method not allowed"), 405


@app.route('/ResourceApp/suppliers/<int:sid>/',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(sid, request.form)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(sid)
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/ResourceApp/suppliers/<int:sid>/resources')
def getResourcesBySupplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)


#************************************************************MEDICAL DEVICES******************************************************************************
@app.route('/ResourceApp/resources/medicaldevices', methods=['GET', 'POST'])
def getAllMedicalDevices():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return MedicalDeviceHandler().insertMedicalDeviceJson(request.json)
    else:
        if not request.args:
            return MedicalDeviceHandler().getAllMedicalDevices()


@app.route('/ResourceApp/resources/medicaldevices/<int:mdid>', methods=['GET', 'PUT', 'DELETE'])
def getMedicalDevicesById(mdid):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesById(mdid)
    elif request.method == 'PUT':
        return MedicalDeviceHandler().updateMedicalDevice(mdid, request.form)
    elif request.method == 'DELETE':
        return MedicalDeviceHandler().deleteMedicalDevice(mdid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/medicaldevices/Name/<string:mdname>', methods=['GET'])
def getMedicalDevicesByName(mdname):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesByName(mdname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medicaldevices/Brand/<string:mdbrand>', methods=['GET'])
def getMedicalDevicesByBrand(mdbrand):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesByBrand(mdbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************MEDICATION**********************************************************************

@app.route('/ResourceApp/resources/medication', methods=['GET', 'POST'])
def getAllMedication():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return MedicationHandler().insertMedicationJson(request.json)
    else:
        if not request.args:
            return MedicationHandler().getAllMedication()

@app.route('/ResourceApp/resources/medication/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMedicationById(mid):
    if request.method == 'GET':
        return MedicationHandler().getMedicationById(mid)
    elif request.method == 'PUT':
        return MedicationHandler().updateMedication(mid, request.form)
    elif request.method == 'DELETE':
        return MedicationHandler().deleteMedication(mid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medication/Name/<string:mname>', methods=['GET'])
def getMedicationByName(mname):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByName(mname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medication/Dosage/<string:mdosage>', methods=['GET'])
def getMedicationByDosage(mdosage):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByDosage(mdosage)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************BABY_FOOD**********************************************************************

@app.route('/ResourceApp/resources/babyfood', methods=['GET', 'POST'])
def getAllBabyFood():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return BabyFoodHandler().insertBabyFoodJson(request.json)
    else:
        if not request.args:
            return BabyFoodHandler().getAllBabyFood()

@app.route('/ResourceApp/resources/babyfood/<int:bfid>', methods=['GET', 'PUT', 'DELETE'])
def getBabyFoodById(bfid):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodById(bfid)
    elif request.method == 'PUT':
        return BabyFoodHandler().updateBabyFood(bfid, request.form)
    elif request.method == 'DELETE':
        return BabyFoodHandler().deleteBabyFood(bfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/babyfood/brand/<string:bfbrand>', methods=['GET'])
def getBabyFoodByBrand(bfbrand):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodByBrand(bfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/babyfood/flavor/<string:bfflavor>', methods=['GET'])
def getBabyFoodByFlavor(bfflavor):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodByFlavor(bfflavor)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************CANNED_FOOD**********************************************************************

@app.route('/ResourceApp/resources/cannedfood', methods=['GET', 'POST'])
def getAllCannedFood():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return CannedFoodHandler().insertCannedFoodJson(request.json)
    else:
        if not request.args:
            return CannedFoodHandler().getAllCannedFood()

@app.route('/ResourceApp/resources/cannedfood/<int:cfid>', methods=['GET', 'PUT', 'DELETE'])
def getCannedFoodById(cfid):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodById(cfid)
    elif request.method == 'PUT':
        return CannedFoodHandler().updateCannedFood(cfid, request.form)
    elif request.method == 'DELETE':
        return CannedFoodHandler().deleteCannedFood(cfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/cannedfood/brand/<string:cfbrand>', methods=['GET'])
def getCannedFoodByBrand(cfbrand):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodByBrand(cfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/cannedfood/name/<string:cfname>', methods=['GET'])
def getCannedFoodByFlavor(cfname):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodByName(cfname)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************DRY_FOOD**********************************************************************

@app.route('/ResourceApp/resources/dryfood', methods=['GET', 'POST'])
def getAllDryFood():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return DryFoodHandler().insertDryFoodJson(request.json)
    else:
        if not request.args:
            return DryFoodHandler().getAllDryFood()

@app.route('/ResourceApp/resources/dryfood/<int:dfid>', methods=['GET', 'PUT', 'DELETE'])
def getDryFoodById(dfid):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodById(dfid)
    elif request.method == 'PUT':
        return DryFoodHandler().updateDryFood(dfid, request.form)
    elif request.method == 'DELETE':
        return DryFoodHandler().deleteDryFood(dfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/dryfood/brand/<string:dfbrand>', methods=['GET'])
def getDryFoodByBrand(dfbrand):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodByBrand(dfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/dryfood/name/<string:dfname>', methods=['GET'])
def getDryFoodByFlavor(dfname):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodByName(dfname)
    else:
        return jsonify(Error="Method not allowed."), 405


##***********************************************ICE**********************************************************************

@app.route('/ResourceApp/resources/ice', methods=['GET', 'POST'])
def getAllIce():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return IceHandler().insertIceJson(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()

@app.route('/ResourceApp/resources/ice/<int:iid>', methods=['GET', 'PUT', 'DELETE'])
def getIceById(iid):
    if request.method == 'GET':
        return IceHandler().getIceById(iid)
    elif request.method == 'PUT':
        return IceHandler().updateIce(iid, request.form)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(iid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/ice/type/<string:itype>', methods=['GET'])
def getIceByType(itype):
    if request.method == 'GET':
        return IceHandler().getIceByType(itype)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/ice/weight/<string:iweight>', methods=['GET'])
def getIceByWeight(iweight):
    if request.method == 'GET':
        return IceHandler().getIceByWeight(iweight)
    else:
        return jsonify(Error="Method not allowed."), 405



##***********************************************TOOL**********************************************************************

@app.route('/ResourceApp/resources/tool', methods=['GET', 'POST'])
def getAllTool():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return ToolHandler().insertToolJson(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTool()

@app.route('/ResourceApp/resources/tool/<int:tid>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tid):
    if request.method == 'GET':
        return ToolHandler().getToolById(tid)
    elif request.method == 'PUT':
        return ToolHandler().updateTool(tid, request.form)
    elif request.method == 'DELETE':
        return ToolHandler().deleteTool(tid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/tool/brand/<string:tbrand>', methods=['GET'])
def getToolByBrand(tbrand):
    if request.method == 'GET':
        return ToolHandler().getToolByBrand(tbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/tool/name/<string:tname>', methods=['GET'])
def getToolByName(tname):
    if request.method == 'GET':
        return ToolHandler().getToolByName(tname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/countbyresourceid')
def getCountByResourceId():
    return ResourceHandler().getCountByResourceId()




#************************************************************ Users & Administrators ******************************************************************************

@app.route('/ResourceApp/user', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        return userHandler().insertUser(request.form)
    else:
        return userHandler().getAllUsers()

@app.route('/ResourceApp/user/administrator', methods=['GET', 'POST'])
def getAllAdmins():
    if request.method == 'POST':
        return adminHandler().insertAdmin(request.form)
    else:
        return adminHandler().getAllAdmins()

@app.route('/ResourceApp/user/id/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return userHandler().getUserById(uid)
    elif request.method == 'PUT':
        return userHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return userHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/administrator/adminId/<int:aid>', methods=['GET', 'PUT', 'DELETE'])
def getAdminByAid(aid):
    if request.method == 'GET':
        return adminHandler().getAdminByAdminId(aid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        return adminHandler().deleteAdmin(aid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/administrator/userId/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getAdminByUid(uid):
    if request.method == 'GET':
        return adminHandler().getAdminByUserId(uid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/username/<string:username>', methods=['GET'])
def getUserByUsername(username):
    if request.method == 'GET':
        return userHandler().getUserByUsername(username)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/firstname/<string:fname>', methods=['GET'])
def getUserByfame(fname):
    if request.method == 'GET':
        return userHandler().getUserByFirstName(fname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/lastname/<string:lname>', methods=['GET'])
def getUserBylname(lname):
    if request.method == 'GET':
        return userHandler().getUserByLastName(lname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/email/<string:email>', methods=['GET'])
def getUserByEmail(email):
    if request.method == 'GET':
        return userHandler().getUserByEmail(email)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/phone/<int:phone>', methods=['GET'])
def getUserByPhone(phone):
    if request.method == 'GET':
        return userHandler().getUserByPhoneNumber(phone)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/address/<string:address>', methods=['GET'])
def getUserByAddress(address):
    if request.method == 'GET':
        return userHandler().getUserByAddress(address)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run()