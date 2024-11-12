from abc import ABC, abstractmethod
#The builder pattern organizes object construction into a set of steps
# To create an object, we need to execute a series of the steps on a builder object.

# 1. Builder: The builder interface defines the contract for constructing the object.
class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, seats):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer):
        pass

    @abstractmethod
    def set_gps(self, gps):
        pass

# 2. Concrete Builder: A concrete builder class implements the builder interface and provides specific implementations for each building step.
class CarBuilder(Builder):
    def __init__(self):
        # self.car = Car()
        self.reset()
        # self.set_seats = None
        # self.set_engine = None
        # self.set_trip_computer = None
        # self.set_gps = None

    def reset(self):
        self.car = Car()
        print("Creating a new car...")
  
    def set_seats(self, seats):
        self.car.seats = seats
        print("Adding seats...", seats)
    
    def set_engine(self, engine):
        self.car.engine = engine
        print("Adding engine...", engine)
    
    def set_trip_computer(self, trip_computer):
        self.car.trip_computer = trip_computer
        print("Adding trip computer...", trip_computer)
    
    def set_gps(self, gps):
        self.car.gps = gps
        print("Adding GPS...", gps)
    
    def get_result(self):
        return self.car

# Product: The product class represents the final result of the building process.
class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return f"Car(seats={self.seats}, engine={self.engine}, trip_computer={self.trip_computer}, gps={self.gps})"

class CarManualBuilder(Builder):
    def __init__(self):
        # self.manual = Manual()
        self.reset()
        # self.set_seats()
        # self.set_engine = []
        # self.set_trip_computer = None
        # self.set_gps = None

    def reset(self):
        self.manual = Manual()
        print("Creating a new car manual...")
  
    def set_seats(self, seats):
        self.manual.seats = seats
        print("Adding seats...", seats)
    
    def set_engine(self, engine):
        self.manual.engine = engine
        print("Adding engine...", engine)
    
    def set_trip_computer(self, trip_computer):
        self.manual.trip_computer = trip_computer
        print("Adding trip computer...", trip_computer)
    
    def set_gps(self, gps):
        self.manual.gps = gps
        print("Adding GPS...", gps)
    
    def get_result(self):
        return self.manual

# Product: The product class represents the final result of the building process.
class Manual:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return f"Manual(seats={self.seats}, engine={self.engine}, trip_computer={self.trip_computer}, gps={self.gps})"
# 3. Director: The director class defines the order in which to execute the building steps
# It may encapsulate various ways to construct a product using the same builder object.
class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct(self):
        self.builder.reset()
        self.builder.set_seats(2)
        self.builder.set_engine("V8")
        self.builder.set_trip_computer(True)
        self.builder.set_gps(True)

# 4. Client Code: The client code creates both the builder and the director objects. Before construction starts, the client must pass a builder object to the director.
builder = CarBuilder()
car_director = Director(builder)
car_director.construct()

car = builder.get_result()

manual = CarManualBuilder()
director = Director(manual)
director.construct()

car_manual = manual.get_result()
print(car)
print(car_manual)
