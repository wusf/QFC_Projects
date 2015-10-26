#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: checking data quality
  Created: 2015/10/23
"""

from abc import ABCMeta
from ConfigParser import ConfigParser

########################################################################
class DataCheck(object):
    """"""
    __metaclass__ = ABCMeta

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    
    #----------------------------------------------------------------------
    def LoadConfig(self, stkUniv, table2BCheck):
        """"""
        conf = ConfigParser()
        conf.read(stkUniv)
        securityType = conf.sections()
        self.security = {}
        for tp in securityType:
            self.security[tp] = {}
            data = conf.items(tp)
            for sec in data:
                symbol = sec[0]
                name = sec[1]
                self.security[tp][symbol] = name
             
    
    #----------------------------------------------------------------------
    def Connect2Wind(self):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def IntegrityCheck(self, dateBeg, dateEnd):
        """"""
        pass
    
    #----------------------------------------------------------------------
    def GetDatabaseUpdateTime(self):
        """"""
        pass

    #----------------------------------------------------------------------
    def IfDataUpdated(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    def AnyImportantChange(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    def Report(self):
        """"""
        pass
        
        
        
    
    