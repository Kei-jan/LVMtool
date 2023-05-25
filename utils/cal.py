import numpy as np


def cal_LVM(v):
    '''
    v: true volume (mm^3)
    LVM(g) = 1.05g/ml * v (mm^3)
    '''
    return np.around(1.05/1000 * v,4)


def cal_true_volume(label_array,nii_affine):
    '''
    label_array: np.array
    nii_affine: voxel physical size ([x,y,z])
    '''
    voxel_volume = np.abs(np.prod(np.diag(nii_affine)))
    label_volume = np.sum(label_array) * voxel_volume
    return label_volume

def select_voxel_value(v,val):
    label_array = np.where(v == val, 1, 0)
    return label_array