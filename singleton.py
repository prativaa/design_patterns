from abc import ABC, abstractmethod
# Abstract class Transport
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Both the concrete classes Truck and Ship extends Transport class and implement deliver method
class Truck(Transport):
    def deliver(self):
        return "Deliver by land in a box"
    
class Ship(Transport):
    def deliver(self):
        return "Deliver by sea in a container"

# 1. Define and Create a singleton class (Logistics)
class Logistics:
    # 2. We use a class varibale to track the singleton instance
    _instance = None
    # the class variable _instance holds the single instance of Logistics
    def __new__(cls):
        # 3. To ensure it is singleton, we will override the __new__ method
        if cls._instance is None:
            # if no instance exists, create a single new instance and assign it to _instance
            # if instance already exists, __new__ returns it ensuring only one instance is created
            cls._instance = super(Logistics, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def create_transport(transport_type):
        # static method create_transport takes a string and returns an instance of the corresponding transport class
        if transport_type == "Truck":
            return Truck()
        elif transport_type == "Ship":
            return Ship()
        else:
            raise ValueError(f"Invalid transport type: {transport_type}")

# Client code
factory = Logistics() #it will get the singleton instance
another_factory = Logistics() # it will also get the same singleton instance

print(factory == another_factory) #Output: True
# Output is true since both references point to the same instance

#use both factory and another_factory instance to create transport
truck = factory.create_transport("Truck")
ship = another_factory.create_transport("Ship")

print(truck.deliver())  # Output: Deliver by land in a box
print(ship.deliver()) # Output: Deliver by sea in a container
