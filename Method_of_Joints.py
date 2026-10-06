#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:37:32 2021

@author: kendrick shepherd
"""

import sys

import Geometry_Operations as geom

# Determine the unknown bars next to this node
def UnknownBars(node):
    bars_next_to_this_node = node.bars
    unknown_bars = []
    for bar in bars_next_to_this_node:
        if not bar.is_computed:
            unknown_bars.append(bar)
    return unknown_bars

# Determine if a node if "viable" or not
def NodeIsViable(node):
    unk_bars = UnknownBars(node)
    if 0 < len(unk_bars) <= 2:
        return True
    else:
        return False
    
# Compute unknown force in bar due to sum of the
# forces in the x direction
def SumOfForcesInLocalX(node, local_x_bar):
    local_x_vector = geom.BarNodeToVector(node, local_x_bar)
    
    global_x_force = node.GetNetXForce()
    global_y_force = node.GetNetYForce()
    
    x_direction = [1,0]
    y_direction = [0,1]
    
    sum = 0
    
    sum +=  global_x_force * geom.CosineVectors(local_x_vector,x_direction)
    sum += global_y_force * geom.CosineVectors(local_x_vector,y_direction)
    
    for bar in node:
        if bar 
    
    
    
   
    
    
    return

# Compute unknown force in bar due to sum of the 
# forces in the y direction
def SumOfForcesInLocalY(node, unknown_bars):
    
    return
    
# Perform the method of joints on the structure
def IterateUsingMethodOfJoints(nodes,bars):
    return