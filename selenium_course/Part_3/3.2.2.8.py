import sys
def test_input_text(expected_result, actual_result):
    assert expected_result  == actual_result, \
        f"expected {expected_result}, got {actual_result}"
    expected_result = 8,
    actual_result = 11



#second variant
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    if expected_result !=  actual_result:
        print("expected " + expected_result + ',' + " got " + actual_result)
