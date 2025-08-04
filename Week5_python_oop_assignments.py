class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.is_powered_on = False

    def power_on(self):
        if not self.is_powered_on:
            self.is_powered_on = True
            return f"{self.brand} {self.model} is now on!"
        return "Phone is already on!"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, gpu):
        super().__init__(brand, model, storage_gb)
        self.gpu = gpu
        self.gaming_mode = False

    def toggle_gaming_mode(self):
        self.gaming_mode = not self.gaming_mode
        return f"Gaming mode {"enabled" if self.gaming_mode else "disabled"}"

# Activity 2: Polymorphism
class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "Running on four legs!"

class Bird(Animal):
    def move(self):
        return "Flying in the sky!"

class Fish(Animal):
    def move(self):
        return "Swimming in water!"

# Demonstration
if __name__ == "__main__":
    print("=== Smartphone Demo ===")
    my_phone = GamingPhone("GamerX", "Pro 5", 512, "RTX 4090")
    print(my_phone.power_on())
    print(my_phone.toggle_gaming_mode())
    
    print("\n=== Animal Polymorphism Demo ===")
    animals = [Dog("Buddy"), Bird("Tweety"), Fish("Nemo")]
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.move()}")
