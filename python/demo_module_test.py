from . import demo_module.DemoModule

# Example of basic unit test
def test_add_nums():
    expected_result = 3
    demo = DemoModule()

    actual_result = demo.add_nums(1, 2)

    assert expected_result == actual_result, "1 + 2 = 3"
