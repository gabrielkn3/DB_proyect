from flask import jsonify
from daos.stocks import stocksDAO

class stocksHandler:
    def build_stocks_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['pid'] = row[1]
        result['quantity'] = row[2]
        return result

    def insertStocks(self, form):
        if form and len(form) == 3:
            sid = form['sid']
            rid = form['rid']
            quantity = form['quantity']

            if sid and rid and quantity:
                dao = stocksDAO()
                stock = dao.insert(sid, rid, quantity)
                result = {}
                result['sid'] = int(stock[0])
                result['rid'] = int(stock[1])
                result['quantity'] = int(stock[2])
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
        return jsonify(Stocks=dao.getAllStocks())

    def getStocksBySupplierId(self, sid):
        dao = stocksDAO()
        return jsonify(Stocks=dao.getStocksBySupplierId(sid))

    def getStocksByResourceId(self, rid):
        dao = stocksDAO()
        return jsonify(Stocks=dao.getStocksByResourceId(rid))

    def getStocksByStockId(self, sid, rid):
        dao = stocksDAO()
        return jsonify(Stocks=dao.getStocksByStockId(sid, rid))

    def getStocksByQuantity(self, quantity):
        dao = stocksDAO()
        return jsonify(Stocks=dao.getStocksByQuantity(quantity))

    def getStocksByResourceIdAndQuantity(self, rid, quantity):
        dao = stocksDAO()
        return jsonify(Stocks=dao.getStocksByResourceIdAndQuantity(rid, quantity))
