#!/usr/bin/python
#coding=UTF-8

import os


class GRACEReader(object):


    def __init__( self ):
        self.grace_header = { }
        self.grace_body   = []

    def open( self, grace_file_path ):
        try:
            ### Check the file exits
            if os.path.exists( grace_file_path ):
                grace_file = open( grace_file_path, 'r' )
                record_line = grace_file.readline()
                while record_line:
                    record_line = record_line.strip( '\n' )
                    self.parseline( record_line )
                    record_line = grace_file.readline()
                grace_file.close()
            else:
                print 'error: the file [%s] not exists!'%(grace_file_path)
        except:
            print 'error: something error in operator!'

    def parseline( self, record_line ):
        return self.parseheader( record_line )

    
    def split_body_line( self, record_line):
        data_record_item = record_line.split( ' ' )
        while '' in data_record_item:
            data_record_item.remove( '' )
        return data_record_item

    def parseheader( self, record_line ):
        if record_line.find( 'END OF HEADER' ) == -1:
            ### the header part
            if record_line.find( ':' ) != -1:
                pos = record_line.find( ':' )
                header_key = record_line[0:pos].strip()
                header_value = record_line[pos+1:len( record_line )].strip()
                #print [header_key, header_value]
                ### key 'PRODUCER AGENCY'
                if header_key.find( 'PRODUCER AGENCY' ) != -1 :
                    self.grace_header['producer_agency'] = header_value
                    return True
                ### key 'PRODUCER INSTITUTION'
                if header_key.find( 'PRODUCER INSTITUTION' ) != -1 :
                    self.grace_header['producer_institution'] = header_value
                    return True
                ### key 'FILE TYPE'
                if header_key.find( 'FILE TYPE' ) != -1 :
                    self.grace_header['file_type'] = int( header_value )
                    return True
                ### key 'FILE FORMAT'
                if header_key.find( 'FILE FORMAT' ) != -1 :
                    self.grace_header['file_format'] = int( header_value )
                    return True
                ### key 'SATELLITE NAME'
                if header_key.find( 'SATELLITE NAME' ) != -1 :
                    self.grace_header['satellite_name'] = header_value
                    return True
                ### key 'SENSOR NAME'
                if header_key.find( 'SENSOR NAME' ) != -1 :
                    self.grace_header['sensor_name'] = header_value
                    return True
                ### key 'TIME EPOCH'
                if header_key.find( 'TIME EPOCH' ) != -1 :
                    self.grace_header['time_epoch'] = header_value
                    return True
                ### key 'TIME FIRST OBS'
                if header_key.find( 'TIME FIRST OBS' ) != -1 :
                    blank_pos = header_value.find( ' ' )
                    second = header_value[0:blank_pos]
                    date_time = header_value[blank_pos+1:len(header_value)].strip('(').strip(')')
                    self.grace_header['time_first_obs'] = [second, date_time]
                    return True
                ### key 'TIME LAST OBS'
                if header_key.find( 'TIME LAST OBS' ) != -1 :
                    blank_pos = header_value.find( ' ' )
                    second = header_value[0:blank_pos]
                    date_time = header_value[blank_pos+1:len(header_value)].strip('(').strip(')')
                    self.grace_header['time_last_obs'] = [second, date_time]
                    return True
            else:
                return False
        else:
            return True


    def first_obs_time( self, index=0 ):
        if self.grace_header.has_key( 'time_first_obs' ):
            if index >= 0 and index <= 1 :
                return self.grace_header['time_first_obs'][index]
            else:
                print 'error: index out of range'
                return None
        else:
            return None

    def last_obs_time( self, index=0 ):
        if self.grace_header.has_key( 'time_last_obs' ):
            if index >= 0 and index <= 1 :
                return self.grace_header['time_last_obs'][index]
            else:
                print 'error: index out of range'
                return None
        else:
            return None

    def obs_interval( self ):
        if len( self.grace_body ) >= 2 :
            if self.grace_body[0].has_key( 'gps_time' ):
                now_gps_time = self.grace_body[0]['gps_time']
                next_gps_time = self.grace_body[1]['gps_time']
                return next_gps_time - now_gps_time
            else:
                print 'error: no attribute gps_time'
                return -2
        else:
            print 'error: length less than 2'
            return -1
