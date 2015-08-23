import pytest
def f(x):
	return x+1


def test():
	assert f(1) == 2

test()