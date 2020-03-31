from flask import Flask, jsonify, request

from handler.MedicalDevicesHandler import MedicalDeviceHandler
from handler.MedicationHandler import MedicationHandler
from handler.resource_handler import ResourceHandler
from handler.supplier import SupplierHandler
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

@app.route('/ResourceApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/ResourceApp/suppliers/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/ResourceApp/suppliers/<int:sid>/resources')
def getResourcesBySupplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

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

@app.route('/ResourceApp/resources/Medication/Name/<string:mname>', methods=['GET'])
def getMedicationByName(mname):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByName(mname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/Medication/Brand/<string:mdosage>', methods=['GET'])
def getMedicationByDosage(mdosage):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByBrand(mdosage)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/countbyresourceid')
def getCountByResourceId():
    return ResourceHandler().getCountByResourceId()

if __name__ == '__main__':
    app.run()