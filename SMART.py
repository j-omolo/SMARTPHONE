# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulated attribute
    
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")
    
    def display_info(self):
        return f"{self.brand} {self.model} - {self.__price}"

# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, refresh_rate):
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.refresh_rate = refresh_rate
    
    def display_info(self):  # Polymorphism
        return f"{self.brand} {self.model} (Gaming) - GPU: {self.gpu}, Refresh Rate: {self.refresh_rate}Hz"

# Derived class: CameraSmartphone
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
    
    def display_info(self):  # Polymorphism
        return f"{self.brand} {self.model} (Camera) - {self.camera_megapixels}MP Camera"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 999)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 1199, "Adreno 730", 144)
phone3 = CameraSmartphone("Apple", "iPhone 14 Pro", 1299, 48)

# Display information
print(phone1.display_info())
print(phone2.display_info())
print(phone3.display_info())
