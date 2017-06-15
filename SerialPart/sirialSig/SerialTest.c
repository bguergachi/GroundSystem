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
#include <errno.h>
#include <unistd.h>

#include <wiringPi.h>
#include <wiringSerial.h>

struct data{
    
    int alt;
    int temp;
    
};


int main ()
{
  int fd ;
  int count ;
  unsigned int nextTime ;

  if ((fd = serialOpen ("/dev/ttyS0", 115200)) < 0)
  {
    fprintf (stderr, "Unable to open serial device: %s\n", strerror (errno)) ;
    return 1 ;
  }

  if (wiringPiSetupGpio () == -1)
  {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror (errno)) ;
    return 1 ;
  }
  
  struct data stuff;
  
  stuff.alt = 5;
  stuff.temp =2;
  


 
    

      printf ("\nOut: %3d: ", count) ;
      fflush (stdout) ;
      serialPutchar (fd, stuff) ;


    delay (1000) ;

    while (serialDataAvail (fd))
    {
      
      printf (" -> %3d", serialGetchar (fd)) ;
      fflush (stdout) ;
    }

  printf ("\n") ;
  return 0 ;
}




