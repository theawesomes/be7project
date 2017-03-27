from tester import *
def wrapper(net):
	for i in range(26):
		net.predict1(test_data[i])
		
