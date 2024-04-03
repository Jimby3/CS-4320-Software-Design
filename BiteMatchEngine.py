from MethodSelection import select_restaurant_type, select_decision_type


class BiteMatchEngine:

    def __init__(self):
        print()

    def start_engine(self):

        print()

        restaurant_type = select_restaurant_type()

        decision_type = select_decision_type()

        if restaurant_type == 0:
            # they chose fast food
            print()
        else:
            # they chose sit-down
            print()

        if decision_type == 0:
            # single API call
            print()
        else:
            # pull restaurants into a
            print()

    def stop_engine(self):
        print()
