/* Replace "dll.h" with the name of your header */
#include "dll.h"
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__declspec( dllexport ) void Credit ()
{
    MessageBox (0, "Jiaqi Huang @ KrappLab\n2014-11-13\n", "Credit", MB_ICONINFORMATION);
}

__declspec( dllexport ) int Hexagonization(double* ptr, int row, int col, int e)
{
    int x, y;
    
    //int e = 15;
    int h, w;
    h = round(e/2);
    w = round(e*sqrt(3)/2);
    


    int u,v;

    
    u=0;v=0;
    double omma_data, omma_sum, omma_len;
    
    for (u=0; u< round(480/6/h); u++)
    {
        for(v=0; v< round(640/2/w); v++)
        {
    //================================================== odd_scan
    omma_sum = 0;
    omma_len = 0;
    for( x= u*6*h+h; x<=u*6*h+3*h; x++)
    {
        for( y= v*2*w; y<= v*2*w+2*w; y++)
        {   
            omma_sum += ptr[x*col+y];
            omma_len ++; 
        }
    }
    omma_data = omma_sum / omma_len;
    
    for( x= u*6*h; x<u*6*h+4*h; x++)
    {
        for( y= v*2*w; y< v*2*w+2*w; y++)
        {   
            if (x>=u*6*h+h && x<=u*6*h+3*h && y>= v*2*w && y<= v*2*w+2*w)
            {
                ptr[x*col+y] = omma_data ;
            }
            
            if( x <= u*6*h+2*h && y <= v*2*w+w && (x%h)*w +(y%w)*h >= (w*h-(w+h)/2) )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x <= u*6*h+2*h && y >= v*2*w+w && (x%h)*w >= (y%w)*h )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x >= u*6*h+2*h && y <= v*2*w+w && (x%h)*w < (y%w)*h )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x >= u*6*h+2*h && y >= v*2*w+w && (x%h)*w + (y%w)*h < (w*h-(w+h)/2) )
            {
                ptr[x*col+y] = omma_data ;
            }
            
        }
    }
    
    //================================================== even_scan
    omma_sum = 0;
    omma_len = 0;
    for( x= u*6*h+4*h; x<=u*6*h+6*h; x++)
    {
        for( y= v*2*w+w; y<= v*2*w+3*w; y++)
        {   
            omma_sum += ptr[x*col+y];
            omma_len ++; 
        }
    }
    omma_data = omma_sum / omma_len;
    
    for( x= u*6*h+3*h; x<u*6*h+7*h; x++)
    {
        for( y= v*2*w+w; y< v*2*w+3*w; y++)
        {   
            if (x>=u*6*h+4*h && x<=u*6*h+6*h && y>= v*2*w+w && y<= v*2*w+3*w)
            {
                ptr[x*col+y] = omma_data ;
            }
            
            if( x <= u*6*h+5*h && y <= v*2*w+2*w && (x%h)*w +(y%w)*h >= (w*h-(w+h)/2) )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x <= u*6*h+5*h && y >= v*2*w+2*w && (x%h)*w >= (y%w)*h )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x >= u*6*h+5*h && y <= v*2*w+2*w && (x%h)*w < (y%w)*h )
            {
                ptr[x*col+y] = omma_data ;
            }
            if( x >= u*6*h+5*h && y >= v*2*w+2*w && (x%h)*w + (y%w)*h < (w*h-(w+h)/2) )
            {
                ptr[x*col+y] = omma_data ;
            }
            
        }
    }
    //================================================== end_of_scan
        }
    }
    
    
    return 0;
}
