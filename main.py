from flask import Flask, jsonify, request
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

@app.route('/PartApp/suppliers/<int:sid>',
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


@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

@app.route('/PartApp/parts/countbypartid')
def getCountByResourceId():
    return ResourceHandler().getCountByPartId()

if __name__ == '__main__':
    app.run()