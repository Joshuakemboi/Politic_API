all_offices = [{
    "office_id": 2,
    "office_type": "Default_office_type",
    "office_name": "Default_office_name"
}]


class OfficeRecord:
    def __init__(self):
        self.all_offices = all_offices

    def create_office(self,office_type , office_name):
        new_office = {
            "office_id":len(self.all_offices),
            "office_type" : office_type,
            "office_name" : office_name
        }
        if new_office:
            self.all_offices.append(new_office)
        return new_office

    def get_all_offices(self):
        return self.all_offices

    def get_single_office(self,office_id):
        for office in self.all_offices:
            if office_id in office.values():
                return office

    def delete_single_office(self,office_id):
        for office in self.all_offices:
            if office_id in office.values():
                self.all_offices.remove(office)
                return self.all_offices