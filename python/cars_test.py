from unittest.mock import Mock, MagicMock, patch
import unittest

from source_code.cars import CarShop, Car


class TestDemoModule(unittest.TestCase):
    # Example of basic unit test
    def test_get_bill(self):
        expected_result = 3
        shop = CarShop()

        actual_result = shop.get_bill(1, 2)

        assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"

    # Example of unit test where a self-written class is mocked
    @patch("source_code.cars.CarColors.get_color")
    def test_get_car_color(self, MockGetColor):
        MockGetColor.return_value = "red"
        expected_result = "Your car is red"
        shop = CarShop()

        actual_result = shop.get_car_color()

        assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"
        # Verify that DemoModule used the expected method in its dependent class
        MockGetColor.assert_called()

    # Example of verifying behavior on another class acted upon by this class
    def test_fix_car(self):
        car = Car()
        car_spy = Mock(wraps=car)
        shop = CarShop()

        shop.fix_car(car_spy)

        assert not car.broken, f"Expected: False, Actual: {car.broken}"
        # Verify the expected function was called on the car
        car_spy.fix.assert_called()

    # The next two examples demonstrate testing out branching code (if/else conditional)
    def test_get_sell_price_broken_car(self):
        expected_result = 1
        car = Car()
        shop = CarShop()
        shop = CarShop()

        actual_result = shop.get_car_sell_price(car)

        assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"

    def test_get_sell_price_fixed_car(self):
        expected_result = 10000
        car = Car()
        car.fix()
        shop = CarShop()

        actual_result = shop.get_car_sell_price(car)

        assert expected_result == actual_result, f"Expected: {expected_result}, Actual: {actual_result}"


if __name__ == "__main__":
    unittest.main()
