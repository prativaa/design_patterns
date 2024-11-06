from abc import ABC, abstractmethod

# 1. Abstract class Transport which is base class for all type of transport.
class Transport(ABC):
    @abstractmethod
    # abstract class has abstract method create which must be implemented by each subclass
    def deliver(self):
        pass

# 2. Both the concrete classes Truck and Ship extends Transport class and implement deliver method
class Truck(Transport):
    def deliver(self):
        return "Deliver by land in a box"

class Ship(Transport):
    def deliver(self):
        return "Deliver by sea in a container"

# 3. Factory class (Logistics) is defined in order to create objects based on given inputs
class Logistics:
    @staticmethod
    def create_transport(transport_type):
        # static method create_transport takes a string and returns an instance of the corresponding transport class
        if transport_type == "Truck":
            return Truck()
        elif transport_type == "Ship":
            return Ship()
        else:
            raise ValueError(f"Invalid transport type: {transport_type}")

# 4. Client code
factory = Logistics()
# client code calls the factory method create_transport and it do not need to know about the specific class implementation details
truck = factory.create_transport("Truck")
ship = factory.create_transport("Ship")

print(truck.deliver())  # Output: Deliver by land in a box
print(ship.deliver()) # Output: Deliver by sea in a container
