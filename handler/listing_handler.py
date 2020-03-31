from flask import jsonify
from daos.listing import ListingDAO

class ListingHandler:
    def build_listing_dict(self, row):
        result = {}
        result['lid'] = row[0]
        result['rid'] = row[1]
        result['uid'] = row[2]
        result['rtype'] = row[3]
        result['postDate'] = row[4]
        result['lprice'] = row[5]
        result['amount'] = row[6]
        result['rlocation'] = row[7]
        return result

    def build_listing_attributes(self, lid, rid, rtype, postDate, uid, lprice, amount, rlocation):
        result = {}
        result['lid'] = lid
        result['rid'] = rtype
        result['uid'] = uid
        result['rtype'] = rtype
        result['postDate'] = postDate
        result['lprice'] = lprice
        result['amount'] = amount
        result['rlocation'] = rlocation
        return result

  #Only show listings where status = open OR just delete when closed #
    def getAllListings(self):
        dao = ListingDAO()
        listings_list = dao.getAllListings()
        result_list = []
        for row in listings_list:
            result = self.build_listing_dict(row)
            result_list.append(result)
        return jsonify(Listing=result_list)

    def getListingById(self, lid):
        dao = ListingDAO()
        row = dao.getListingById(lid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            listing = self.build_listing_dict(row)
            return jsonify(Listing=listing)

    def searchListings(self, args):

        rtype = args.get("rtype")
        lprice = args.get("lprice")
        rid = args.get("rid")
        sid = args.get("sid")

        dao = ListingDAO()
        listings_list = []
        if (len(args) == 1) and rtype:
            listings_list = dao.getListingsByType(rtype)
        elif (len(args) == 1) and lprice:
            listings_list = dao.getListingsByPrice(lprice)
        elif (len(args) == 1) and sid:
            listings_list = dao.getListingsBySupplierID(sid)
        elif (len(args) == 1) and rid:
            listings_list = dao.getListingsByRID(rid)
        elif (len(args) == 2) and rtype and lprice:
            listings_list = dao.getListingsByTypeAndPrice(rtype, lprice)
        elif (len(args) == 2) and rid and lprice:
            listings_list = dao.getListingsByRIDAndPrice(rid, lprice)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in listings_list:
            result = self.build_listing_dict(row)
            result_list.append(result)
        return jsonify(Listings=result_list)

    def getSuppliersByListingId(self, lid):
        dao = ListingDAO()
        if not dao.getListingById(lid):
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = dao.getSuppliersByListingId(lid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)
    # Verificar si Supplier se paso properly con el import #

    def insertListing(self, form):
        print("form: ", form)
        if len(form) != 8:
            return jsonify(Error="Malformed post request"), 400
        else:
            lid = form['lid']
            rid = form['rid']
            rtype = form['rtype']
            postDate = form['postDate']
            uid = form['uid']
            lprice = form['lprice']
            amount = form['amount']
            rlocation = form['rlocation']

            if lid and rid and rtype and postDate and uid and lprice and amount and rlocation:
                dao = ListingDAO()
                lid = dao.insert(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
                result = self.build_listing_attributes(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
                return jsonify(Listing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertListingJson(self, json):
        lid = json['lid']
        rid = json['rid']
        rtype = json['rtype']
        postDate = json['postDate']
        uid = json['uid']
        lprice = json['lprice']
        amount = json['amount']
        rlocation = json['rlocation']
        if lid and rid and rtype and postDate and uid and lprice and amount and rlocation:
            dao = ListingDAO()
            lid = dao.insert(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
            result = self.build_listing_attributes(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
            return jsonify(Listing=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteListing(self, lid):
        dao = ListingDAO()
        if not dao.getListingById(lid):
            return jsonify(Error="Part not found."), 404
        else:
            dao.delete(lid)
            return jsonify(DeleteStatus="OK"), 200

    def updateListing(self, lid, form):
        dao = ListingDAO()
        if not dao.getListingById(lid):
            return jsonify(Error="Part not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                lid = form['lid']
                rid = form['rid']
                rtype = form['rtype']
                postDate = form['postDate']
                uid = form['uid']
                lprice = form['lprice']
                amount = form['amount']
                rlocation = form['rlocation']
                if lid and rid and rtype and postDate and uid and lprice and amount and rlocation:
                    dao.update(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
                    result = self.build_listing_attributes(lid, rid, rtype, postDate, uid, lprice, amount, rlocation)
                    return jsonify(Listing=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_listing_counts(self, listing_counts):
        result = []
        # print(part_counts)
        for P in listing_counts:
            D = {}
            D['lid'] = P[0]
            D['rid'] = P[1]
            D['uid'] = P[2]
            D['rtype'] = P[3]
            D['postDate'] = P[4]
            D['lprice'] = P[5]
            D['amount'] = P[6]
            D['rlocation'] = P[7]
            result.append(D)
        return result

    def getCountByListingId(self):
        dao = ListingDAO()
        result = dao.getCountByListingId()
        # print(self.build_listing_counts(result))
        return jsonify(ListingCounts=self.build_listing_counts(result)), 200



