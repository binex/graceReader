#!/usr/bin/python
#coding=UTF-8


import os
import readGRACE


class ACCReader(readGRACE.GRACEReader):

    def __init__( self ):
        readGRACE.GRACEReader.__init__( self )

    def parseline( self, record_line ):
        if readGRACE.GRACEReader.parseline( self, record_line ) == False :
            data_item_record = self.split_body_line( record_line )
            data_item_record_dict = {}
            data_item_record_dict['gps_time'] = int( data_item_record[0] )
            data_item_record_dict['GRACE_id'] = data_item_record[1]
            data_item_record_dict['lin_accl_x'] = float( data_item_record[2] )
            data_item_record_dict['lin_accl_y'] = float( data_item_record[3] )
            data_item_record_dict['lin_accl_z'] = float( data_item_record[4] )
            data_item_record_dict['ang_accl_x'] = float( data_item_record[5] )
            data_item_record_dict['ang_accl_y'] = float( data_item_record[6] )
            data_item_record_dict['ang_accl_z'] = float( data_item_record[7] )
            data_item_record_dict['acl_x_res'] = float( data_item_record[8] )
            data_item_record_dict['acl_y_res'] = float( data_item_record[9] )
            data_item_record_dict['acl_z_res'] = float( data_item_record[10] )
            data_item_record_dict['qualflg'] = data_item_record[11]
            self.grace_body.append( data_item_record_dict )
            return True

