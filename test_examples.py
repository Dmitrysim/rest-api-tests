import requests

class TestExample:

    def test_check_math(self):
        a = 5
        b = 9
        assert a+b == 14

    def test_check_mult(self):
        a = 5
        b = 9
        assert a*b == 45

    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Vitalii"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "It's not true"
