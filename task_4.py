class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, quantity):
        if quantity.hours is None:
            return (7 - quantity.rest_days) * 8
        else:
            return quantity.hours
            
    @classmethod
    def get_email(cls, quantity):
        if quantity.email is None:
            return f"{quantity.name}@email.com" 
        else:
            return quantity.email
    Collapse commentComment on lines R19 to R32AlexKitIt commented on May 16, 2026 AlexKitIton May 16, 2026More actionsНужно исправить: эти методы принимают класс и все атрибуты и если конкретный None - выполняют его вычисление и вернут класс со всеми атрибутамиReactWrite a replyResolve comment
    @classmethod
    def set_hourly_payment(cls, new_value):
        cls.hourly_payment = new_value

    def salary(self):
        worked_hours = self.get_hours(self)
        return worked_hours * self.hourly_payment
