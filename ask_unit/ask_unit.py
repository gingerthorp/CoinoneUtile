import decimal


def ask_unit(recent_price: list):
    """

    최근 봉 시고저종 가격 기반의 호가 단위 산출 알고리즘.
    :param recent_price: [시가, 고가, 저가, 종가]
    :return: 적용 가능한 호가 단위.
    """
    # 코인원 호가 기준

    fixed_unit_rule = [
        {"min": 0, "max": 1, "unit": 0.0001},
        {"min": 1, "max": 10, "unit": 0.001},
        {"min": 10, "max": 100, "unit": 0.01},
        {"min": 100, "max": 1000, "unit": 0.1},
        {"min": 1000, "max": 5000, "unit": 1},
        {"min": 5000, "max": 10000, "unit": 5},
        {"min": 10000, "max": 50000, "unit": 10},
        {"min": 50000, "max": 100000, "unit": 50},
        {"min": 100000, "max": 500000, "unit": 100},
        {"min": 500000, "max": 1000000, "unit": 500},
        {"min": 1000000, "max": 10 ** 10, "unit": 1000}
    ]

    # 종가 가격의 코인원 호가 단위
    fixed_unit = 0
    close_price = recent_price[3]

    for check in fixed_unit_rule:
        if check["min"] <= close_price < check["max"]:
            fixed_unit = check["unit"]
            break

    # 시가, 고가, 저가, 종가 가격 숫자 기반의 호가 단위.
    # 10010원 -> 10원, 50070원 -> 10원, 500100원 -> 100원, 500500원 -> 500원, 50050원 -> 50원, 50090원 -> 10원
    # 0.123원 -> 0.001원, 0.1234원 -> 0.0001원 ..
    recent_unit = []
    decimal_min = 0
    for price in recent_price:
        real_port = (decimal.Decimal(str(price)) - decimal.Decimal(str(int(price))))  # 소수부 산출.
        decimal_len = len(str(real_port))  # 소수부 길이 유추.

        if decimal_len > 2:  # 소수부 인 경우 최수 3자리, ex) 0.1 -> 3자리.
            decimal_min = 10 ** (-(decimal_len - 2))  # 소수부에 대한 최솟값 산출.

        else:
            # 정수부 호가 구하기(자연수인 경우)
            for i in range(1, 5):
                division = 10 ** i  # 최대 100000
                rest = price % division  # 남은 10000 단위.(현재는 1000 단위)

                if rest > 0:  # 나머지 발생.
                    unit = 10 ** (i - 1)  # 정수부의 최소단위.

                    # 5 단위 경우
                    five_unit = unit * 5
                    if five_unit == rest:
                        unit = five_unit

                    decimal_min = unit
                    break
        recent_unit.append(decimal_min)

    # 시, 고, 저, 종 가격 숫자 기반의 호가 단위 중 최솟값.
    min_recent_unit = min(recent_unit)

    # 가격 스케일에 따른 코인원 호가 단위과 숫자 기반 호가 단위 중 최대값.
    # 최대값(가격 스케일 코인원 호가, 숫자 기반 호가)
    result = max(min_recent_unit, fixed_unit)

    print(f"recent price -> recent unit -> min(recent_unit)")
    print(f"{recent_price} -> {recent_unit} -> {min_recent_unit}\n")

    print(f"close price -> close fixed unit")
    print(f"{close_price} -> {fixed_unit}\n")

    print(f"max(min recent unit, close fixed unit) -> result unit")
    print(f"max({min_recent_unit}, {fixed_unit}) -> {result}")

    print("-" * 50)

    return result


if __name__ == '__main__':

    print("-" * 50)
    test_case = [
        [38850, 39800, 40250, 38670],
        [0.763, 0.77, 0.785, 0.747],
        [3735, 3735, 3735, 3735],
        [3010, 3010, 3010, 3010],
        [116.2, 116.8, 117, 116.2],
        [3369, 3495, 3495, 3369],
        [3450, 3450, 3450, 3450],
        [35.2, 35.2, 35.2, 35.2],
        [36.88, 36.88, 36.88, 36.87],
        [708.4, 727, 727, 700.1],
        [578, 571, 588, 565]

    ]

    for recent_price in test_case:
        unit = ask_unit(recent_price)
