/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   newmain.c
 * Author: agsof
 *
 * Created on March 29, 2017, 1:52 AM
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>




struct data{
    
    int alt;
    int temp;
    
};


int main ()
{
  int fd ;
  int count ;
  unsigned int nextTime ;

  
  struct data stuff;
  
  stuff.alt = 5;
  stuff.temp =2;
  


 
    

      printf ("\nOut: %3d: ", count) ;
      fflush (stdout) ;
      


    delay (1000) ;

    

  printf ("\n") ;
  return 0 ;
}




