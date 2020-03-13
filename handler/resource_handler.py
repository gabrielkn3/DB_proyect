

class ResourceHandler:
    def build_resource_dict(self, row):
        result = {};
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rdescription'] = row[2]
        result['rlocation'] = row[3]
        result['rstock'] = row[4]
        result['sid'] = row[5]
        return result

    def build_part_attributes(self, rid, rtype, rdescription, rlocation, rstock, sid):
        result = {};
        result['rid'] = rid
        result['rtype'] = rtype
        result['rdescription'] = rdescription
        result['rlocation'] = rlocation
        result['rstock'] = rstock
        result['sid'] = sid
        return result