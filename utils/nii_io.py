import nibabel as nib
import numpy as np

def read_nii(nii_path):
    nii_data = nib.load(nii_path)
    nii_array = np.array(nii_data.get_fdata())
    nii_affine = nii_data.affine
    return nii_array, nii_affine