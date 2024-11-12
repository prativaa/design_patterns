from abc import ABC, abstractmethod

#first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table)
# 1. Abstract class Chair which is base class for all type of chairs.
class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass
 
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def has_legs(self):
        pass
    
    @abstractmethod
    def sit_on(self):
        pass
    
class CoffeeTable(ABC):
    @abstractmethod
    def has_legs(self):
        pass
    
    @abstractmethod
    def sit_on(self):
        pass

# then we can make all variants of products follow those interfaces.
# for example, all chair variants can implement the Chair interface, and so on
# 2. Concrete chair classes
class VictorianChair(Chair):
    def has_legs(self):
        return "Victorian Chair has beautiful aesthetics and strong built legs"
    
    def sit_on(self):
        return "Sit like royalties on Victorian Chair"

class ModernChair(Chair):
    def has_legs(self):
        return "Modern chair has modern style legs"
    
    def sit_on(self):
        return "Modern chair has ergonomic seats"

# Concrete sofa classes
class VictorianSofa(Sofa):
    def has_legs(self):
        return "Victorian Sofa has beautiful aesthetics and strong built legs"
    
    def sit_on(self):
        return "Sit like royalties on Victorian Sofa"

class ModernSofa(Sofa):
    def has_legs(self):
        return "Modern Sofa has modern style legs"
    
    def sit_on(self):
        return "Modern Sofa has ergonomic seats"
    
# Concrete coffee table classes
class VictorianCoffeeTable(CoffeeTable):
    def has_legs(self):
        return "Victorian Coffee Table has beautiful aesthetics and strong built legs"
    
    def sit_on(self):
        return "Sit like royalties on Victorian Coffee Table"

class ModernCoffeeTable(CoffeeTable):
    def has_legs(self):
        return "Modern coffee table has modern style legs"
    
    def sit_on(self):
        return "Modern Coffee table are not very comfortable to seat longer."

# declare the abstract factory- an interface with a list of creation methods for each of the abstract products
#eg, create_chair, create_sofa, create_coffee_table
# 3. Abstract factory class
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
    
    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

# 4. Concrete Factories implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()
    
    def create_coffee_table(self):
        return VictorianCoffeeTable()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self):
        return ModernSofa()
    
    def create_coffee_table(self):
        return ModernCoffeeTable()
    
# 4. Client code
# client code calls the factory method furniture factory and it do not need to know about the specific class implementation details
def client_code(factory: FurnitureFactory):
    print("\n=== Furniture type: Chair ===")
    chair = factory.create_chair()
    print(chair.has_legs())
    print(chair.sit_on())

    print("\n=== Furniture type: Sofa ===")
    sofa = factory.create_sofa()
    print(sofa.has_legs())
    print(sofa.sit_on())

    print("\n=== Furniture type: Coffee Table ===")
    coffee_table = factory.create_coffee_table()
    print(coffee_table.has_legs())
    print(coffee_table.sit_on())

# the client can workk with any concrete factory/product variant, as long as it communicates
# with their objects via abstract interfaces
print("*** Victorian Furnuitures ***")
victorian_factory = VictorianFurnitureFactory()
client_code(victorian_factory)

print("\n*** Modern Furnuitures ***")
modern_factory = ModernFurnitureFactory()
client_code(modern_factory)
