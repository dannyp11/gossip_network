import sys, math

# ****************   Main program  *********************************************
def main():
    #   File IO ###############################################
    
    N = int(raw_input())
    n = 2 * N       
    
    a = [[0 for x in range(1)] for y in range(n)] 
    
    # print >> sys.stderr, a
    print >> sys.stderr, "N=", N
     
    for line in range (0, N):
        x , y = [int(j) for j in raw_input().split()]
         
        # print >> sys.stderr, '%d %d' % (x, y)    
            
        m, n = sortTwo(x, y)
        
        a[m].append(n)
        a[n].append(m)
        a[m][0] += 1
        a[n][0] += 1
        
         
    print >> sys.stderr, "Done file IO \n \n"    
    ##############################################################