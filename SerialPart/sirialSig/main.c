/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: agsof
 *
 * Created on June 14, 2017, 6:52 PM
 */

#include "main.h"

struct Altimeter{
    
    long temperature;
    long pressure;
    
};

struct GPS{
    
    long latitude;
    long longitude;
    long altitude;
    long time;
};


/*
 * 
 */
int main(int argc, char** argv) {
    
    setup();
    int fd = getFB();
    FILE *dataLog = fopen("../dataLog.txt","w+");
    int counter = 0;
    char currentByte = 0;
    
    struct Altimeter altimeter;
    while(true){
        
        currentByte = getChar();
        switch (currentByte){
            case 'p':
                altimeter.temperature = getChar() << 8 | getChar();
                altimeter.pressure = getChar() << 16
                break;
               
            case 'a':
                break;
                
            case 'g':
                break; 
                
            default:
                break;
        }
        
        
        if(counter == 2000){
            sendByte();
            counter = 0;
        }
        counter++;
    }
    
    fclose(dataLog);
    return (EXIT_SUCCESS);
}

