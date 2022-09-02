import calculator
def test_add():
    ret = calculator.add(114, 514)
    assert(ret == 628)
def test_minus():
    ret = calculator.minus(114, 514)
    assert(ret == -400)
