class Location:
    def __init__(self, city: str, postoffise: int):
        self.city = city
        self.postoffise = postoffise

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Vehicle:
    def __init__(self, vehicleNo: int, isAvailable: bool):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

class Order:
    def __init__(self, orderId: int, user_name: str, location: Location, items: list, vehicle: None):
        self.orderId = orderId
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    def calculateAmount(self):
        amount = 0
        for i in range(0, len(self.items)):
            amount += self.items[i].price
        return amount

    def assignVehicle(self, vehicle: list):
        if type(vehicles) == list:
            vehicles.remove(vehicles[0])
        return vehicles

class LogisticSystem:
    def __init__(self, orders: list, vehicles: list):
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        return location.city

    def trackOrder(self, orderId: int):
        if vehicles == None:
            return 'There is no available vehicle to deliver an order.'
        else:
            return f'Your order #{orderId} is sent to {logSystem.placeOrder(my_order)}. Total price: {Order.calculateAmount(my_order)} UAH.'


# if __name__ == "__main__":
#     vehicles = None
#     my_items = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
#     location =  Location(city = 'Kharkiv', postoffise = 17)
#     my_order = Order(orderId = None, user_name = 'Olesya', location = location, items = my_items, vehicle = None)
#     logSystem = LogisticSystem(orders = [my_order], vehicles = vehicles)
#     logSystem.placeOrder(my_order)
#     print(logSystem.trackOrder(234976475))

# if __name__ == "__main__":
#     vehicles = [Vehicle(1, True), Vehicle(2, True)]
#     my_items = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
#     location =  Location(city = 'Odessa', postoffise = 3)
#     my_order = Order(orderId = None, user_name = 'Andrii', location = location, items = my_items, vehicle = None)
#     logSystem = LogisticSystem(orders = [my_order], vehicles = vehicles)
#     logSystem.placeOrder(my_order)
#     print(logSystem.trackOrder(234976475))