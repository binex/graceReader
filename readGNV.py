#!/bin/usr/python
#coding=UTF-8


import os
import readGRACE

class GNVReader(readGRACE.GRACEReader):

    def __init__( self ):
        readGRACE.GRACEReader.__init__( self )

    def parseline( self, record_line ):
        if readGRACE.GRACEReader.parseline( self, record_line ) == False:
            ### the body part
            data_item_record = self.split_body_line( record_line )
            data_item_record_dict = { }
            data_item_record_dict['gps_time'] = int( data_item_record[0] )
            data_item_record_dict['GRACE_id'] = data_item_record[1]
            data_item_record_dict['coord_ref'] = data_item_record[2]
            data_item_record_dict['xpos'] = float( data_item_record[3] )
            data_item_record_dict['ypos'] = float( data_item_record[4] )
            data_item_record_dict['zpos'] = float( data_item_record[5] )
            data_item_record_dict['xpos_err'] = float( data_item_record[6] )
            data_item_record_dict['ypos_err'] = float( data_item_record[7] )
            data_item_record_dict['zpos_err'] = float( data_item_record[8] )
            data_item_record_dict['xvel'] = float( data_item_record[9] )
            data_item_record_dict['yvel'] = float( data_item_record[10] )
            data_item_record_dict['zvel'] = float( data_item_record[11] )
            data_item_record_dict['xvel_err'] = float( data_item_record[12] )
            data_item_record_dict['yvel_err'] = float( data_item_record[13] )
            data_item_record_dict['zvel_err'] = float( data_item_record[14] )
            data_item_record_dict['qualflg'] = data_item_record[15]
            self.grace_body.append( data_item_record_dict )
            return True
