class UI:
    def __init__(self, controller):
        self.controller = controller
    
    @staticmethod
    def printMenu():
        print("1. Simulate a new day")
        print("2. Display persons")
        print("3. Vaccinate a person")
        print("4. Exit")
    
    def start(self):
        while True:
            try:
                UI.printMenu()
                choice = int(input())
                if choice == 1:
                    self.controller.simulateDay()
                elif choice == 2:
                    UI.printList(self.controller.repo.data)
                elif choice == 3:
                    ID = int(input("Enter the ID of the person you want to vaccinate:\n"))
                    self.controller.vaccinate(ID)
                elif choice == 4:
                    return
                else:
                    raise ValueError("Invalid option")
            except ValueError as e:
                print(e)
    
    @staticmethod
    def printList(l):
        for i in l:
            print(i)