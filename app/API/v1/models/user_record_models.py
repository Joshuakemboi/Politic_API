all_users = [{

        "first_name" : "first_name",
        "second_name" :"second_name",
        "other_name" : "other_name",
        "email": "taken_email@gmail.com",
        "phone_number": "0720000000",
        "passport_url": "url",
        "password": "Joshu455s*",
        "repeat_password": "Joshu455s*"
    }]

admins = [{
        "first_name" : "Josh",
        "second_name" :"kemboi",
        "other_name" : "rop",
        "email": "josh@gmail.com",
        "phone_number": "0702983637",
        "passport_url": "url",
        "password": "Joshu455s*",
        "repeat_password": "Joshu455s*"
    }]


class UserRecord:
    def __init__(self):
        self.all_users = all_users
        self.admins = admins

    def create_user(self,first_name ,second_name,other_name, email , phone_number,passport_url , password , repeat_password):
        def is_admin():
            for admin in self.admins:
                if email in admin.values():
                    return True
                if phone_number in admin.values():
                    return True
                else:
                    return False
        new_user = {
            "id":len(self.all_users)-1,
            "first_name" : first_name,
            "second_name" : second_name,
            "other_name" : other_name,
            "email": email,
            "phone_number": phone_number,
            "is_admin":is_admin(),
            "passport_url":passport_url,
            "password": password,
            "repeat_password": repeat_password,
        }
        if new_user:
            self.all_users.append(new_user)
        return new_user

    def get_all_users(self):
        return self.all_users

    def get_single_user(self, username):
        usr = [usr for usr in all_users if usr[username] == username]
        if usr:
            return usr
        return None
