class TestCase:
    def __init__(self, steps=None, result=None):
        self.steps = dict(steps or {})
        self.result = result

    def set_step(self, step_number: int, step_text: str):
        self.steps[int(step_number)] = step_text

    def delete_step(self, step_number: int) -> bool:
        step_number = int(step_number)
        if step_number in self.steps:
            self.steps.pop(step_number)
            return True
        return False

    def set_result(self, result: str):
        self.result = result

    def get_test_case(self) -> dict:
        ordered = dict(sorted(self.steps.items()))
        return {'Шаги': ordered, 'Ожидаемый результат': self.result}



test_case_1 = TestCase({}, None)
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase({}, None)
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
