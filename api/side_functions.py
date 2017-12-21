# This file contains large functions required in views.py
from scipy.optimize import linprog
import numpy as np

class SectorStock:
	def __init__(self,branche,perc):
		self.branche = branche
		self.perc = perc
	def set_perc(self,perc):
		self.perc = perc


def lin_op(branche_list,effect_list,perc_list):
	stock_dist = []
	for branche in branche_list:
		sector_stock = SectorStock(branche,0) 
		stock_dist.append(sector_stock)
	max_inv = 0.50
	A = np.identity(len(branche_list))
	Asum = np.ones([1,len(branche_list)])
	b = max_inv*np.ones(len(branche_list))
	bsum = [sum(perc_list)/100]
	sum_list = [1+sum(effect_list[i][:])/100 for i in range(0,len(effect_list)) ]
	c = list(-1*np.array(sum_list))	
	res = linprog(c, A_ub=A, b_ub=b, A_eq=Asum, b_eq=bsum)
	opt_dist_list = list(100*res.x)

	return opt_dist_list