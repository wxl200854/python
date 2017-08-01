#! /usr/bin/env python

def get_ip(fp_src):
    line_src = fp_src.readline()
    slice_src = line_src.split('\t')
    src_ip = slice_src[0]
    return src_ip

def main():
    fp_src = open('123.txt','r')
    fp_dst = open('456.txt','r')
    fp_out = open('out.txt','w',buffering=0)
    while(fp_src.readline()):
        
        line_dst = fp_dst.readline()
        slice_dst = line_dst.split('\t')
        dst_ip = slice_dst[0]
        location_dst = slice_dst[1]
        if (get_ip(fp_src) == dst_ip):
            line_out = fp_src.readline() + location_dst
            fp_out.write(line_out)
           
   
        
    fp_dst.close()
    fp_src.close()
    fp_out.close()
    
   
if __name__ == "__main()__":
    main()
    
    
 


