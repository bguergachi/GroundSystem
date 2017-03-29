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
#include <string.h>
#include <errno.h>

#include <wiringPi.h>
#include <wiringSerial.h>

int main() {
    int fd;
    int count;
    unsigned int nextTime;

    if ((fd = serialOpen("/dev/ttyAMA0", 115200)) < 0) {
        fprintf(stderr, "Unable to open serial device: %s\n", strerror(errno));
        return 1;
    }

    if (wiringPiSetup() == -1) {
        fprintf(stdout, "Unable to start wiringPi: %s\n", strerror(errno));
        return 1;
    }

    serialPutchar(fd,5);
    
    printf("%d",serialGetchar(fd));

    printf("\n");
    return 0;
}

