#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:42:40 2017

@author: 3502264
"""

TRANSPOSE = d.transpose
SYMETRIE = d.symetrie
COMPOSITION_BASE = d.compositionBase

import definitions as d


def transposeSet(S):
    return S.keys()

def symetrieSet(S):
    return S.keys()

def compose(r1, r2):
    if (r1, r2) in COMPOSITION_BASE.keys():
        return COMPOSITION_BASE[(r1, r2)]
    else:
        if '>' in (r1, r2):
            return {'>'}
        else:
            if 'd' in (r1, r2):
                return {'d'}
    
print(compose('ot', 'm'))