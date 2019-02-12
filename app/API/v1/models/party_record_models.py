all_parties = [{
    "party_id": 1000,
    "party_name": "taken_party",
    "party_headquarters_address": "taken_hq",
    "party_logo_url": "present_party_logo.png"
},{
    "party_id": 100,
    "party_name": "d-present_party2",
    "party_headquarters_address": "d-present_party_headquarters2",
    "party_logo_url": "d-present_party_logo.png"
}]




class PartyRecord:
    def __init__(self):
        self.all_parties = all_parties

    def create_party(self,party_name , party_headquarters_address , party_logo_url):
        new_party = {
            "party_id":len(self.all_parties),
            "party_name" : party_name,
            "party_headquarters_address" : party_headquarters_address,
            "party_logo_url":party_logo_url
        }
        if new_party:
            self.all_parties.append(new_party)
        return new_party
    def update_party(self,party_id , party_name , party_headquarters_address , party_logo_url):
        for party in self.all_parties:
            if party_id in party.values():
                def update(key_to_find, definition):
                    for key in party:
                        if key == key_to_find:
                            party[key] = definition
                update("party_id",party_id)
                update("party_name",party_name)
                update("party_headquarters_address",party_headquarters_address)
                update("party_logo_url",party_logo_url)
                return party



         




    def get_all_parties(self):
        return self.all_parties

    def get_single_party(self,party_id):
        for party in self.all_parties:
            if party_id in party.values():
                return party

    def delete_single_party(self,party_id):
        for party in self.all_parties:
            if party_id in party.values():
                self.all_parties.remove(party)
                return self.all_parties