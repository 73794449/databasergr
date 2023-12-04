from prettytable import from_db_cursor


class View(object):
    @staticmethod
    def show_table_menu(tables):
        num = -1
        while not (list(tables)[0] <= num <= list(tables)[-1]):
            print("Select table:")
            for table in tables:
                print(str(table) + ") " + tables[table][1])

            num = int(input("Enter number: "))

        return num

    @staticmethod
    def show_msg(message):
        print(message)

    @staticmethod
    def show_menu():
        num = -1
        while not (num > 0 & num < 9):
            print("\n\n\n\n\nMenu: ")
            print("1) View table")
            print("2) View all tables")
            print("3) Add to table")
            print("4) Delete from table")
            print("5) Edit table")
            print("6) Randomize table")
            print("7) Search")
            print("8) Exit")
            num = int(input("Enter number: "))
        return num

    @staticmethod
    def show_table(table):
        print(from_db_cursor(table))

    @staticmethod
    def show_params_menu(params):
        print("\n Input params: ")
        entered_params = {}
        for param in params:
            print(str(param) + ") " + params[param])
            entered_params[param] = input("Input value: ")

        return entered_params

    @staticmethod
    def get_id():
        return int(input("Enter id: "))

    @staticmethod
    def show_params_menu_selection(params):
        print("\n Select param: ")
        num = -1
        while not (list(params)[0] <= num <= list(params)[-1]):
            for param in params:
                print(str(param) + ") " + params[param])
            num = int(input("Enter number: "))

        return num

    @staticmethod
    def get_param(param):
        return input("Input value for {}: ".format(param))

    @staticmethod
    def show_random_menu():
        return int(input("Input count of random elements: "))

    @staticmethod
    def show_execution_time(time):
        print("Execution time: {}".format(time))

    @staticmethod
    def show_sql_error(error):
        print("Got error:\n", error)

    @staticmethod
    def show_sanity_error():
        print("Entered value is not correct")

    @staticmethod
    def show_connection_error():
        print("Connection was not established")