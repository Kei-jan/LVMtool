import numpy as np


def cal_LVM(v):
    '''
    v: true volume (mm^3)
    LVM(g) = 1.05g/ml * v (mm^3)
    '''
    return 1.05/1000 * v


def cal_true_volume(v,inter):
    '''
    v: voxel volume (int number)
    inter: voxel physical size ([x,y,z])
    '''
