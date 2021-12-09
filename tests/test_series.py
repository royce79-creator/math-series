from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci():
  expected = 34
  actual = fibonacci(9)
  assert expected == actual

def test_fibonacci2():
  expected = 6765
  actual = fibonacci(20)
  assert expected == actual

def test_lucas():
  expected = 123
  actual = lucas(10)
  assert expected == actual

def test_lucas2():
  expected = 47
  actual = lucas(8)
  assert expected == actual

def test_sum_series_fibonacci():
  expected = 13
  actual = sum_series(7, 0, 1)
  assert expected == actual

def test_sum_series_fibonacci2():
  expected = 
  actual = sum_series(15, 0, 1)
  asser expected == actual

def test_sum_series_lucas():
  expected = 123
  actual = sum_series(10, 2, 1)
  assert expected == actual

def test_sum_series_lucas2():
  expected = 
  actual = sum_series(13, 2, 1)
  assert expected == actual



