class Phone:
    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        storage_gb: int,
        is_in_stock: bool
    ) -> None:
        self.brand: str = brand
        self.model: str = model
        self.price: float = price
        self.color: str = color
        self.storage_gb: int = storage_gb
        self.is_in_stock: bool = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if not (0 <= discount_percent <= 100):
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.price *= (1 - discount_percent / 100)

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        return (
            f"{self.get_full_name()} | Цена: {self.price:.2f} ₽ | "
            f"Цвет: {self.color} | Память: {self.storage_gb}GB | "
            f"{self.check_availability()}"
        )


# ===== Демонстрация =====
if __name__ == "__main__":
    phone1 = Phone("Apple", "iPhone 14", 90000, "Black", 128, True)
    phone2 = Phone("Samsung", "Galaxy S23", 80000, "White", 256, False)
    phone3 = Phone("Xiaomi", "Redmi Note 12", 25000, "Blue", 128, True)
    phone4 = Phone("OnePlus", "Nord 3", 35000, "Gray", 256, True)

    phones = [phone1, phone2, phone3, phone4]

    for phone in phones:
        print(phone)
        print("Полное имя:", phone.get_full_name())
        print("Наличие:", phone.check_availability())
        phone.apply_discount(10)
        print("Цена после скидки 10%:", phone.price)
        print("-" * 50)
