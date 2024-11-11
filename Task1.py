class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def new_user(self):
        name = input("Введіть ім'я користувача: ")
        self.users[self.next_id] = name
        print(f"Користувача додано: ID: {self.next_id}, Ім'я: {name}")
        self.next_id += 1

    def get_user_by_id(self, user_id):
        return self.users.get(user_id, "Користувач не знайдений")

    def get_users_by_name(self, name):
        found_users = {user_id: user_name for user_id, user_name in self.users.items() if user_name == name}
        return dict(sorted(found_users.items()))

    def get_all_users(self):
        return dict(sorted(self.users.items(), key=lambda x: x[1]))

    def delete_user_by_id(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"Користувач з ID {user_id} видалений")
        else:
            print("Користувач не знайдений")

    def delete_users_by_ids(self, ids):
        for user_id in ids:
            self.delete_user_by_id(user_id)

    def delete_users_in_range(self, start_id, end_id):
        for user_id in range(start_id, end_id + 1):
            self.delete_user_by_id(user_id)

class Application:
    def __init__(self):
        self.manager = UserManager()

    def show_help(self):
        print("new_user — додає користувача у програму.")
        print("user id — виводить інформацію про користувача із вказаним id")
        print("user name — виводить всіх користувачів із вказаним ім'ям у алфавітному порядку")
        print("all — виводить всіх користувачів, які були внесені у записник, в алфавітному порядку")
        print("del_user id — видаляє користувача із вказаним id")
        print("del_user id1,id2 — видаляє користувача із вказаними через кому id")
        print("del_user id1-id2 — видаляє користувачів з інтервалу id1-id2 включно")
        print("exit — вихід із програми")

    def run(self):
        print("Вітаю вас!")
        while True:
            print("* - допомога")
            num = input("Зробіть вибір: ")

            if num == "*":
                self.show_help()
            elif num == "new_user":
                self.manager.new_user()
            elif num.startswith("user "):
                _, arg = num.split(maxsplit=1)
                if arg.isdigit():
                    user = self.manager.get_user_by_id(int(arg))
                    print(user)
                else:
                    users_by_name = self.manager.get_users_by_name(arg)
                    for user_id, user_name in users_by_name.items():
                        print(f"ID: {user_id}, Name: {user_name}")
            elif num == "all":
                all_users = self.manager.get_all_users()
                for user_id, user_name in all_users.items():
                    print(f"ID: {user_id}, Name: {user_name}")
            elif num.startswith("del_user "):
                arg = num.split(maxsplit=1)[1]
                if '-' in arg:
                    start_id, end_id = map(int, arg.split('-'))
                    self.manager.delete_users_in_range(start_id, end_id)
                elif ',' in arg:
                    ids = map(int, arg.split(','))
                    self.manager.delete_users_by_ids(ids)
                elif arg.isdigit():
                    self.manager.delete_user_by_id(int(arg))
            elif num == "exit":
                print("Вихід із програми")
                break
            else:
                print("Невідома команда")

if __name__ == "__main__":
    app = Application()
    app.run()
