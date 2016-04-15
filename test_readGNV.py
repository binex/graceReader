#!/usr/bin/python
#coding=UTF-8


import readGNV
import readACC
import readSCA
import readKBR


def testReadGNV():
    reader = readGNV.GNVReader()
    reader.open( 'data/GNV1B_2013-02-01_A_02.asc' )
    print 'record len = %d'%( len( reader.grace_body ) )
    print reader.grace_body[0]

def testReadACC():
    reader = readACC.ACCReader()
    reader.open( 'data/ACC1B_2003-09-14_B_00.asc' )
    print 'record len = %d'%( len( reader.grace_body ) )
    print reader.grace_body[0]


def testReadSCA():
    reader = readSCA.SCAReader()
    reader.open( 'data/SCA1B_2003-09-14_A_00.asc' )
    print 'record len = %d'%( len( reader.grace_body ) )
    print reader.first_obs_time()
    print reader.grace_body[0]

def testReadKBR():
    reader = readKBR.KBRReader()
    reader.open( 'data/KBR1B_2003-09-14_X_00.asc' )
    print 'record len = %d'%( len( reader.grace_body ) )
    print reader.first_obs_time()
    print reader.grace_body[0]

if __name__ == '__main__':
    #testReadGNV()
    #testReadACC()
    #testReadSCA()
    testReadKBR()


