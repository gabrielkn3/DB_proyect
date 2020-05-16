from flask import jsonify
from daos.stocks import stocksDAO
from daos.supplier import SupplierDAO
from daos.resource import ResourceDAO

class stocksHandler:
    def build_stocks_dict(self, row):
        result = {}
        result['Amount stocked'] = row[0]
        result['Supplier ID'] = row[1]
        result['Resource ID'] = row[2]
        return result

    def insertStocks(self, form):
        if form and len(form) == 3:
            sid = form['sid']
            rid = form['rid']
            quantity = form['squantity']

            if not SupplierDAO().validateID(sid):
                return jsonify(Error="Supplier doest not exist."), 404
            if not ResourceDAO().validateID(rid):
                return jsonify(Error="Resource doest not exist."), 404

            if sid and rid and quantity:
                dao = stocksDAO()
                dao.insert(sid, rid, quantity)
                result = {}
                result['sid'] = sid
                result['rid'] = rid
                result['squantity'] = quantity
                return jsonify(Stocks=result), 201
            else:
                return jsonify(Error="Malformed post request."), 400
        else:
            return jsonify(Error="Malformed post request."), 400

    def deleteStocks(self, sid, rid):
        dao = stocksDAO()
        if not dao.getStocksByStockId(sid, rid):
            return jsonify(Error="Relationship not found."), 404
        else:
            dao.delete(sid, rid)
            return jsonify(DeleteStatus="Relationship deleted successfully")

    def updateStocks(self, sid, rid, form):
        dao = stocksDAO
        if not dao.getStocksByStockId(sid, rid):
            return jsonify(Error="Relationship not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed post request."), 400
            else:
                quantity = form['quantity']
                if sid and rid and quantity:
                    dao.update(sid, rid, quantity)
                    result = {}
                    result['sid'] = sid
                    result['rid'] = rid
                    result['quantity'] = quantity
                    return jsonify(Stocks=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request."), 400

    def getAllStocks(self):
        dao = stocksDAO()
        list = dao.getAllStocks()
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)

    def getStocksBySupplierId(self, sid):
        dao = stocksDAO()
        list = dao.getStocksBySupplierId(sid)
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)

    def getStocksByResourceId(self, rid):
        dao = stocksDAO()
        list = dao.getStocksByResourceId(rid)
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)

    def getStocksByStockId(self, sid, rid):
        dao = stocksDAO()
        list = dao.getStocksByStockId(sid, rid)
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)

    def getStocksByQuantity(self, quantity):
        dao = stocksDAO()
        list = dao.getStocksByQuantity(quantity)
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)

    def getStocksByResourceIdAndQuantity(self, rid, quantity):
        dao = stocksDAO()
        list = dao.getStocksByResourceIdAndQuantity(rid, quantity)
        result = []

        if not list:
            return jsonify(Error="No stocks found"), 404

        for row in list:
            result.append(self.build_stocks_dict(row))
        return jsonify(Stocks=result)
