#!/usr/bin/python
#coding=UTF-8

import os
import readGRACE


class KBRReader(readGRACE.GRACEReader):

    def __init__( self ):
        readGRACE.GRACEReader.__init__( self )

    def parseline( self, record_line ):
        if readGRACE.GRACEReader.parseline( self, record_line ) == False:
            data_item_record = self.split_body_line( record_line )
            data_item_record_dict = {}
            data_item_record_dict['gps_time'] = int( data_item_record[0] )
            data_item_record_dict['biased_range'] = float( data_item_record[1] )
            data_item_record_dict['range_rate'] = float( data_item_record[2] )
            data_item_record_dict['range_accl'] = float( data_item_record[3] )
            data_item_record_dict['iono_corr'] = float( data_item_record[4] )
            data_item_record_dict['lighttime_corr'] = float( data_item_record[5] )
            data_item_record_dict['lighttime_rate'] = float( data_item_record[6] )
            data_item_record_dict['lighttime_accl'] = float( data_item_record[7] )
            data_item_record_dict['ant_centr_corr'] = float( data_item_record[8] )
            data_item_record_dict['ant_centr_rate'] = float( data_item_record[9] )
            data_item_record_dict['ant_centr_accl'] = float( data_item_record[10] )
            data_item_record_dict['K_A_SNR'] = int( data_item_record[11] )
            data_item_record_dict['Ka_A_SNR'] = int( data_item_record[12] )
            data_item_record_dict['K_B_SNR'] = int( data_item_record[13] )
            data_item_record_dict['Ka_B_SNR'] = int( data_item_record[14] )
            data_item_record_dict['qualflg'] = data_item_record[15]
            data_item_record_dict['corrected_biased_range'] = data_item_record_dict['biased_range'] +\
                    data_item_record_dict['lighttime_corr'] + data_item_record_dict['ant_centr_corr']
            data_item_record_dict['corrected_range_rate']   = data_item_record_dict['range_rate']   +\
                    data_item_record_dict['lighttime_rate'] + data_item_record_dict['ant_centr_rate']
            data_item_record_dict['corrected_range_accl']   = data_item_record_dict['range_accl']   +\
                    data_item_record_dict['lighttime_accl'] + data_item_record_dict['ant_centr_accl']
            self.grace_body.append( data_item_record_dict )
            return True

