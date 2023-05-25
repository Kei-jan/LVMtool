import os

from utils.args import get_parser
from utils.nii_io import read_nii
from utils.cal import select_voxel_value,cal_true_volume,cal_LVM

def main_cal(args):
    nii_array, nii_affine = read_nii(args.nii_path)
    label_array = select_voxel_value(nii_array,args.label_val)
    v = cal_true_volume(label_array,nii_affine)
    lvm = cal_LVM(v)
    print(f'LVM: {lvm} (g)')

if __name__ == '__main__':

    parser = get_parser()
    args_dict = parser.parse_args()
    main_cal(args_dict)