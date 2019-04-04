from scipy import signal
from scipy import misc
import numpy as np
import skimage.measure


def test_svert(one, two):
	return signal.convolve2d(one, two, boundary='symm', mode='same')


def test_max_pool(arr):
	return skimage.measure.block_reduce(np.array(arr), (3,3), np.max)


