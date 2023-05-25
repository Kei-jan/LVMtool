import argparse

def get_parser():

    parser = argparse.ArgumentParser(description='LVMtool')
    
    parser.add_argument('-nii_path', dest='nii_path', default='', type=str)
    parser.add_argument('-label_val', dest='label_val', default=1, type=int)

    return parser

if __name__ =="__main__":

    parser = get_parser()
    args_dict = parser.parse_args()