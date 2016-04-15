#!/usr/bin/python
#coding=UTF-8

import os
import readGRACE

class SCAReader(readGRACE.GRACEReader):

    def __init__( self ):
        readGRACE.GRACEReader.__init__( self )

    def parseline( self, record_line ):
        if readGRACE.GRACEReader.parseline( self, record_line ) == False:
            data_item_record = self.split_body_line( record_line  )
            data_item_record_dict = {}
            data_item_record_dict['gps_id'] = int( data_item_record[0] )
            data_item_record_dict['GRACE_id'] = data_item_record[1]
            data_item_record_dict['sca_id'] = data_item_record[2]
            data_item_record_dict['quatangle'] = float( data_item_record[3] )
            data_item_record_dict['quaticoeff'] = float( data_item_record[4] )
            data_item_record_dict['quatjcoeff'] = float( data_item_record[5] )
            data_item_record_dict['quatkcoeff'] = float( data_item_record[6] )
            data_item_record_dict['qual_rss'] = float( data_item_record[7] )
            data_item_record_dict['qualflg'] = data_item_record[8]
            self.grace_body.append( data_item_record_dict )
            return True

