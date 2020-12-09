#Import required package
import argparse
#define arg_parse function
def arg_parse():
    #include argparse and verbosity   
    parser = argparse.ArgumentParser()
    parser.add_argument("help",  type=int, help="Insert a value equal or smaller than 20")
    parser.add_argument("--verbosity", help="The output will have a maximum of 20 lines",action="store_true")
    args = parser.parse_args()
arg_pars()  





