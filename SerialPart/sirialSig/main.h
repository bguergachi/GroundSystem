/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.h
 * Author: agsof
 *
 * Created on June 14, 2017, 11:29 PM
 */

#ifndef MAIN_H
#define MAIN_H
#include <stdio.h>
#include <stdlib.h>
#include <String.h>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <errno.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h> 


extern void setup();
extern void sendByte();
extern int getChar();


#ifdef __cplusplus
extern "C" {
#endif


#ifdef __cplusplus
}
#endif




#endif /* MAIN_H */

