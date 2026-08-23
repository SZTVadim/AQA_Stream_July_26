# 1. Создайте класс TestUser он должен иметь конструктор __init__, который принимает:
#    - username (обязательный)
#    - email (обязательный)
#    - password (обязательный)
#    - age (опциональный, по умолчанию None)
#    - is_active (опциональный, по умолчанию True


class TestUser:
    def __init__(self, username, email, password, age: int | None = None, is_active=True):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.is_active = is_active

    # 2. Добавьте метод validate_email(), который проверяет, что email содержит символ "@"
    #   и возвращает True/False

    def validate_email(self):
        return '@' in self.email

    # 3. Добавьте метод validate_password(), который проверяет, что пароль содержит минимум
    #   8 символов и возвращает True/False

    def validate_password(self):
        return len(self.password) >= 8

        # 4. Добавьте метод get_user_info(), который возвращает словарь со всеми данными пользователя

    def get_user_info(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "is_active": self.is_active
        }

    # 5. Добавьте метод is_adult(), который возвращает True, если возраст >= 18, иначе False
    #   (если возраст не указан, возвращает None)
    def is_adult(self):
        if self.age is None:
            return None
        return self.age >= 18


# user_1 = TestUser("golf", "el@gmail.ru", "Abcd123", "19", False)


#
# from pydantic import BaseModel, ConfigDict
#
#
# class TestUserModel(BaseModel):
#     model_config = ConfigDict(strict=True)
#     username: str
#     email: str
#     password: str
#     age: int | None = None
#     is_active: bool = True
#
#
# user_1 = TestUserModel(username="golf", password="Abcd123", age="19", is_active=False)


class TestLogger:
    def __init__(self):
        self.test_results = []
        self.passed = 0
        self.failed = 0

    def log_test(self, test_name, status):
        """Логирует результат выполнения теста"""
        if status not in ["passed", "failed"]:
            raise ValueError("Status must be 'passed' or 'failed'")

        self.test_results.append({
            "test_name": test_name,
            "status": status
        })

        if status == "passed":
            self.passed += 1
        else:
            self.failed += 1

    def get_statistics(self):
        """Возвращает статистику по тестам"""
        total = len(self.test_results)
        if total == 0:
            return {
                "total_tests": 0,
                "passed": 0,
                "failed": 0,
                "success_rate": 0.0
            }

        success_rate = round((self.passed / total) * 100, 2)
        return {
            "total_tests": total,
            "passed": self.passed,
            "failed": self.failed,
            "success_rate": success_rate
        }

    def get_failed_tests(self):
        """Возвращает список названий проваленных тестов"""
        return [result["test_name"] for result in self.test_results
                if result["status"] == "failed"]

    def clear(self):
        """Очищает все результаты и сбрасывает счётчики"""
        self.test_results = []
        self.passed = 0
        self.failed = 0


logger = TestLogger()
logger.log_test('Проверка авторизации', 'passed')
logger.log_test('Проверка регистрации', 'failed')
print(logger.get_statistics())

