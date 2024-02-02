import unittest
from binomial_coefficient import binomial_coefficient
import math


class TestEuclideanAlgorithm(unittest.TestCase):
	def test_1(self):
		self.assertEqual(binomial_coefficient(10, 5), 252)

	def test_2(self):
		for n in range(100 + 1):
			for k in range(n + 1):
				self.assertEqual(binomial_coefficient(n, k), math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))

	def test_3(self):
		self.assertEqual(binomial_coefficient(654, 321), 2088624953383760971488243926215983314668007079040575840458852317553835286687166542234979310586620807550210480099247071146340471456463666098110787162439679333032277411632733692493464039370070191000)

	def test_4(self):
		self.assertEqual(binomial_coefficient(1000, 500), 270288240945436569515614693625975275496152008446548287007392875106625428705522193898612483924502370165362606085021546104802209750050679917549894219699518475423665484263751733356162464079737887344364574161119497604571044985756287880514600994219426752366915856603136862602484428109296905863799821216320)


if __name__ == '__main__':
	unittest.main()