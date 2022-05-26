# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:38:25 2021

@author: Domagoj
"""
from gurobipy import *
import pandas as pd
import time
import matplotlib.pyplot as plt 
import datetime
import numpy as np
from math import *
import cmath
import random

UP_need=[0,5,0,0,0,7,9,0,12,0,0,4,1,0,0,0,6,0,2,0,0,0,1,0]
DOWN_need=[2,0,0,4,0,0,0,0,0,4,0,0,0,0,7,0,0,0,0,7,0,0,0,0]

DA_char={}
DA_dischar={}

ID_char={}
ID_dischar={}

FLEXup={}
FLEXdown={}

chargo={}
dischargo={}
netto={}

blnc_up={}
blnc_dwn={}

objValues={}


DA_char_hour={}
DA_dis_hour={}

ID_char_hour={}
ID_dis_hour={}


FLEX_char_hour={}
FLEX_dis_hour={}


BM_char_hour={}
BM_dis_hour={}

tempori={}

for BUDG in range (0,24): 
        model=Model("stoha_robust_balanc")
        
        
        
        
        
        #06.04.2021. 
        #CROPEX DA
        DA_prices_0={0:22.75, 1:39.5, 2:19.03, 3:23.95, 4:39.93, 5:39.5, 6:60.33, 7:67.00, 8:75.7, 9:72.62, 10:69.58, 11:67.89, 12:65.65, 13:63.91, 14:63.6, 15:63.43, 16:62.59, 17:61.24, 18:63.46, 19:70.05, 20:71.44, 21:62.41,22:62.97, 23:60.72 }
        #CROPEX AVG ID
        ID_avg_0={0:31.70, 1:28.16, 2:24.79, 3:24.00, 4:27.00, 5:45.00, 6:63.76, 7:77.96, 8:81.00, 9:88.91, 10:105.93, 11:80.33, 12:90.92, 13:80.45, 14:56.99, 15:64.15, 16:61.46, 17:63.45, 18:84.04, 19:83.67, 20:89.63, 21:70.65, 22:69.79, 23:67.16}
        #CROPEX MIN ID
        ID_min_0={0:29.32, 1:28.16, 2:24.70, 3:24.00, 4:27.00, 5:45.00, 6:61.29, 7:71.80, 8:71.00, 9:68.99, 10:65.89, 11:59.90, 12:59.90, 13:59.60, 14: 56.00, 15: 54.95, 16:55.00, 17:60.00, 18:75.00, 19:80.13, 20: 87.01, 21:62.00, 22:66.00, 23:64.00}
        #CROPEX MAX ID
        ID_max_0={0:37.00, 1:28.16, 2:24.80, 3:24.00, 4:27.00, 5:45.00, 6:64.99, 7:88.00, 8:85.00, 9: 103.20, 10:111.0, 11:92.10, 12:110.0, 13:90.00, 14: 59.96, 15:85.00, 16:90.00, 17:89.00, 18:90.00, 19:90.00, 20:95.30, 21:80.00, 22:74.99, 23:69.97 }
        
        
        #30.03.2021
        #CROPEX DA
        DA_prices_1={0:47.08, 1:46.46, 2:44.65, 3:45.59, 4:46.27, 5:53.22, 6:65.09, 7:78.22, 8:76.73, 9:64.63, 10:62.12, 11:55.16, 12:49.70, 13:45.92, 14:43.04, 15:43.08, 16:52.76, 17:59.52, 18:64.03, 19:82.37, 20:77.01, 21:67.04, 22:65.69, 23:60.00 }
        #CROPEX AVG ID
        ID_avg_1={0:48.85, 1:49.93, 2:47.3, 3:47.59, 4:48.23, 5:51.67, 6:64.03, 7:76.23, 8:78.22, 9:71.06, 10:64.44, 11:54.10, 12:49.66, 13:42.32, 14:42.76, 15:44.59, 16:48.74, 17:53.22, 18:59.43, 19:69.28, 20:69.68, 21:68.20, 22:65.74, 23:60.32}
        #CROPEX MIN ID
        ID_min_1={0:47.90, 1:48.54, 2:47.18, 3:47.48, 4:48.09, 5:51.60, 6:61.70, 7:75.77, 8:78.10, 9:66.12, 10:61.00, 11:52.00, 12:48.00, 13:41.59, 14:42.00, 15:43.98, 16:47.00, 17:51.59, 18:58.70, 19:67.57, 20:69.68, 21:64.23, 22:62.22, 23:57.62}
        #CROPEX MAX ID
        ID_max_1={0:52.00, 1:50.00, 2:47.47, 3:48.01, 4:48.90, 5:51.99, 6:64.30, 7:76.69, 8:78.32, 9:74.00, 10:67.00, 11:59.00, 12:54.18, 13:51.48, 14:51.01, 15:46.95, 16:51.20, 17:54.85, 18:63.00, 19:75.20, 20:69.68, 21:69.00, 22:66.00, 23:60.50}
        
        
        DA_scens={}
        DA_prob={}
        ID_avg={}
        ID_min={}
        ID_max={}
        
        FLEX_up_price={}
        FLEX_down_price={}
        
        
        
        
        for s_f in range(0,2):
            ID_avg[0,s_f]=ID_avg_0
            ID_avg[1,s_f]=ID_avg_1
            ID_min[0,s_f]=ID_min_0
            ID_min[1,s_f]=ID_min_1
            ID_max[0,s_f]=ID_max_0
            ID_max[1,s_f]=ID_max_1
        DA_scens[0]=DA_prices_0
        DA_scens[1]=DA_prices_1
        DA_prob[0]=0.5
        DA_prob[1]=0.5
        
        flex_price_prob={}
        for s in range (2):
            if s==0:
                flex_price_prob[s,0]=0.8
                flex_price_prob[s,1]=0.2
            if s==1:
                flex_price_prob[s,0]=0.2
                flex_price_prob[s,1]=0.8
        
        #FLEXIBILITY PRICES
        for t in range(0,24):
            for s in range (0,2):
                for s_f in range (0,2):
                    FLEX_up_price[s,s_f,t]=DA_scens[s_f][t]*1.3
                    FLEX_down_price[s,s_f,t]=DA_scens[s_f][t]*0.8
        
        #FLEXIBILITY NEED
        
        
        
        #BALACNING
        bm_up={}
        bm_down={}
        
        
        bm_up_0={0:13.71, 1:55.54, 2:11.47, 3:14.43, 4:24.06, 5:23.80, 6:36.36, 7:46.65, 8:53.03, 9:102.12, 10:93.03, 11:40.91, 12:92.31, 13:89.87, 14:89.43, 15:89.19, 16:82.84, 17:79.96, 18:89.23, 19:95.39, 20:93.70, 21:37.61, 22:37.95, 23:36.59}
        bm_down_0={0:13.71, 1:55.54, 2:11.47, 3:14.43, 4:24.06, 5:23.80, 6:36.36, 7:46.65, 8:53.03, 9:102.12, 10:93.03, 11:40.91, 12:92.31, 13:89.87, 14:89.43, 15:89.19, 16:82.84, 17:79.96, 18:89.23, 19:95.39, 20:93.70, 21:37.61, 22:37.95, 23:36.59}
        
        bm_up_1={0:61.5, 1:61.53, 2:58.81, 3:61.11, 4:60.76, 5:69.67, 6:87.70, 7:105.67, 8:101.58, 9:650.01, 10:81.30, 11:72.58, 12:65.19, 13:60.59, 14:57.00, 15:60.58, 16:71.75, 17:78.55,  18:84.03, 19:115.83, 20:106.69, 21:90.28, 22:87.18, 23:81.13}
        bm_down_1={0:61.5, 1:61.53, 2:58.81, 3:61.11, 4:60.76, 5:69.67, 6:87.70, 7:105.67, 8:101.58, 9:650.01, 10:81.30, 11:72.58, 12:65.19, 13:60.59, 14:57.00, 15:60.58, 16:71.75, 17:78.55,  18:84.03, 19:115.83, 20:106.69, 21:90.28, 22:87.18, 23:81.13}
        
        for t in range(0,24):
            for s_f in range (0,2):
                bm_up[0,s_f,t]=bm_up_0[t]
                bm_down[0,s_f,t]=bm_down_0[t]
                bm_up[1,s_f,t]=bm_up_1[t]
                bm_down[1,s_f,t]=bm_down_1[t]
            
        
            
        
        # =============================================================================
        # p=0.5 #između 0 i 1
        # for s in range (0,2):
        #     for t in range(0,24):
        #         bm_up[s,t]=DA_scens[s][t]*(1+p)
        #         bm_down[s,t]=DA_scens[s][t]*(1-p)
        # 
        # =============================================================================
        
        delta_ID_down={}
        delta_ID_up={}
        delta_avg={}
        for s in range (0,2):
            for s_f in range (0,2):
                for t in range (0,24):
                    delta_ID_down[s,s_f,t]=ID_avg[s,s_f][t]-ID_min[s,s_f][t]
                    delta_ID_up[s,s_f,t]=ID_max[s,s_f][t]-ID_avg[s,s_f][t]
                    delta_avg[s,s_f,t]=(delta_ID_down[s,s_f,t]+delta_ID_up[s,s_f,t])
        
        
        #PARAMS
        eff=0.81
        batt_cap=5
        P_ch=5
        P_dis=5
        
        
        DA_dis={}
        DA_ch={}
        x_DA={}
        soe={}
        for s in range (0,2):
            for s_f in range (0,2):
                soe[s,s_f,-1]=5
        SOE_ccCV=0.555
        
        
        
        
        R={0:0, 1:0.23, 2:0.947, 3:1}
        F={0:0.823,1:0.658,2:0.046, 3:0}
        
        delta_soe={}
        soe_i={}
        
        #ID VARS
        ID_ch={}
        ID_dis={}
        x_ID={}
        
        #BM VARS
        dev_ch={}
        dev_dis={}
        
        #FLEXI VARS
        flex_up={} 
        flex_down={}
        
        #aux vars
        g={} #netto punjenje-pražnjejne
        c={} #fizikalno punjenje baterije u trenutku t
        d={} #fizikalno pražnjenje baterije u trenutku t
        
        for t in range (0,24):
            for s in range (0,2):
                for s_f in range (0,2):
                    g[s,s_f,t]=model.addVar(lb=-GRB.INFINITY, name="netto ch_dis in the hour: %d, s: %d, s_f: %d"%(t,s,s_f))
                    c[s,s_f,t]=model.addVar( name="physical battery charging in the hour: %d, s: %d, s_f: %d"%(t,s,s_f))
                    d[s,s_f,t]=model.addVar( name="physical battery discharging in the hour: %d, s: %d, s_f: %d"%(t,s,s_f))
        
        
        ###BINARY FOR THE TIME OF DELIVERY
        x={}
        
        for t in range (0,24):
            DA_dis[t]=model.addVar(lb=0,  name="DA discharge in the hour: %d"%t)
            DA_ch[t]=model.addVar(lb=0,  name="DA charge in the hour: %d"%t)
            x_DA[t]=model.addVar(lb=0, vtype=GRB.BINARY, name="Charging switch on/off in the hour %d"%t)
            for s in range (0,2):
                for s_f in range (0,2):
                    #dis[t,s]=model.addVar(lb=0, name="Discharge in the hour: %d"%t)
                    #ch[t,s]=model.addVar(lb=0,  name="Charge in the hour: %d"%t)
                    #bin_ch[t,s]=model.addVar(lb=0, vtype=GRB.BINARY, name="Charging switch on/off in the hour %d"%t)
                    #bin_dis[t,s]=model.addVar(lb=0, vtype=GRB.BINARY, name="Discharging switch on/off in the hour %d"%t)
                    ID_ch[s,s_f,t]=model.addVar(lb=0, name="ID charge in the hour: %d, scenario:%d,%d"%(t,s,s_f))
                    ID_dis[s,s_f,t]=model.addVar(lb=0, name="ID discharge in the hour: %d, scenario:%d,%d"%(t,s,s_f))
                    x_ID[s,s_f,t]=model.addVar(lb=0, vtype=GRB.BINARY, name="ID discharging switch on/off in the hour %d, scenario: %d,%d"%(t,s,s_f))
        
                    x[s,s_f,t]=model.addVar(lb=0, vtype=GRB.BINARY, name="Delivery time charging on/off in the hour: %d, scenario: %d,%d"%(t,s,s_f))
                    
                    dev_ch[s,s_f,t]=model.addVar(lb=0, name="Charging deviation in hour %d, scenario %d,%d"%(t,s,s_f))
                    dev_dis[s,s_f,t]=model.addVar(lb=0, name="Discharging deviation in hour %d, scenario %d,%d"%(t,s,s_f))
                    soe[s,s_f,t]=model.addVar(lb=0, name="SOE in the hour: %d, scenario %d,%d"%(t,s,s_f))
                    delta_soe[s,s_f,t]=model.addVar(lb=0, name="delta SOE in the hour %d, scenario: %d, %d"%(t,s,s_f))
                    for i in range (3):
                        soe_i[t,i,s,s_f]=model.addVar(lb=0, name="SOE segment %d in the hour %d"%(i,t))
        
                    
        for t in range(0,24):
            for s in range (0,2):
                flex_up[s,t]=model.addVar(lb=0, name="Flex up in scenario %d in hour %d"%(s,t))
                flex_down[s,t]=model.addVar(lb=0, name="Flex down in scenario %d in hour %d"%(s,t))
             
        
        for t in range (0,24):
            for s in range (2):
                for s_f in range (2):
                    model.addConstr(DA_ch[t]-dev_ch[s,s_f,t]<=P_ch*x_DA[t])
                    model.addConstr(DA_dis[t]-dev_dis[s,s_f,t]<=P_dis*(1-x_DA[t]))
        
        for t in range(0,24):
            for s in range(0,2):
                model.addConstr(flex_up[s,t]<=UP_need[t])
                model.addConstr(flex_down[s,t]<=DOWN_need[t])
        
        
        
        ###
        for t in range (0,24):
            for s in range (0,2):
                for s_f in range (0,2):
                    model.addConstr(ID_ch[s,s_f,t]<=P_ch*x_ID[s,s_f,t])
                    model.addConstr(ID_dis[s,s_f,t]<=P_dis*(1-x_ID[s,s_f,t]))
        
        
        for t in range (0,24):
            for s in range (0,2):
                for s_f in range (0,2):
                    #model.addConstr(ch[t]<=P_ch/eff*bin_ch[t])
                    model.addConstr(flex_up[s,t]<=P_dis+DA_ch[t]-dev_ch[s,s_f,t]+ID_ch[s,s_f,t]-DA_dis[t]+dev_dis[s,s_f,t]-ID_dis[s,s_f,t])
                    model.addConstr(flex_down[s,t]<=P_ch+DA_dis[t]-dev_dis[s,s_f,t]+ID_dis[s,s_f,t]-DA_ch[t]+dev_ch[s,s_f,t]-ID_ch[s,s_f,t])
                    model.addConstr(g[s,s_f,t]==DA_ch[t] - dev_ch[s,s_f,t] + ID_ch[s,s_f,t] + flex_down[s,t] - DA_dis[t] + dev_ch[s,s_f,t] - ID_dis[s,s_f,t] - flex_up[s,t])
                    model.addConstr(g[s,s_f,t]==c[s,s_f,t]-d[s,s_f,t])
                    model.addConstr(c[s,s_f,t] <= P_ch*x[s,s_f,t])
                    model.addConstr(d[s,s_f,t] <= P_dis*(1-x[s,s_f,t])) 
                    
                    model.addConstr(soe[s,s_f,t]==soe[s,s_f,t-1]+c[s,s_f,t]*eff-d[s,s_f,t])
                    model.addConstr(soe[s,s_f,t]<=batt_cap) 
            
            #model.addConstr(ch[t]<=P_ch/eff*((batt_cap-soe[t])/(batt_cap-batt_cap*SOE_ccCV)))
        for s in range (0,2):
            for s_f in range (0,2):
                model.addConstr(soe[s,s_f,23]>=soe[s,s_f,-1])
            
        #
        
        #ENERGY CHARGING MODEL
          
        for i in range (3):
            for s in range (2):
                for s_f in range (2):
                    soe_i[-1,i,s,s_f]=model.addVar(lb=0, name="SOE segment %d in the hour %d, scenario %d"%(i,t,s)) 
        for s in range (2):
            for s_f in range (2):        
                model.addConstr(soe[s,s_f,-1]==quicksum(soe_i[-1,i,s,s_f] for i in range (3)))
        
        
        for t in range (24):
            for s in range (2):
                for s_f in range (2):
                    model.addConstr(soe[s,s_f,t]==quicksum(soe_i[t,i,s,s_f] for i in range (3)))
                    model.addConstr(soe_i[t,i,s,s_f] <= batt_cap*(R[i+1]-R[i]))
                    model.addConstr(delta_soe[s,s_f,t]==F[0]*batt_cap + quicksum ( (F[i+1]-F[i])/(R[i+1]-R[i])*soe_i[t-1,i,s,s_f] for i in range (3))  )
                    model.addConstr(c[s,s_f,t]<=delta_soe[s,s_f,t]/eff)
        
        
            
        model.update()
        
        #UNCERTAINTY BUDGET
        #BUDG=0
        
        
        #DUAL OD ROBUSNOG DIJELA
        z={}
        omega={}
        y={}
        for s in range(0,2):
            for s_f in range (0,2):
                z[s,s_f]=model.addVar(lb=0, name="Sensitivity of the model to changing budget of uncertainty, scenario %d"%s)
                for t in range (0,24):
                    omega[s,s_f,t]=model.addVar(lb=0, name="value greater than 0 when b from primal is greater than 0")
                    y[s,s_f,t]=model.addVar(lb=-GRB.INFINITY)
                
        for s in range(0,2):
            for s_f in range (2):
                for t in range(0,24):
                    model.addConstr(-DA_prob[s]*flex_price_prob[s,s_f]*y[s,s_f,t]*delta_avg[s,s_f,t]+z[s,s_f]+omega[s,s_f,t]>=0)
                    model.addConstr(y[s,s_f,t]>=ID_ch[s,s_f,t]-ID_dis[s,s_f,t])
                    model.addConstr(y[s,s_f,t]>=-(ID_ch[s,s_f,t]-ID_dis[s,s_f,t]))
        
                
        
        
        model.update()
        
        
        def cost():
            temp=0
            for t in range(0,24):
                for s in range(0,2):
                    temp+=DA_prob[s]*DA_scens[s][t]*(DA_dis[t]-DA_ch[t])
                    for s_f in range(0,2):
                        temp+=flex_price_prob[s,s_f]*DA_prob[s]*(flex_up[s,t]*FLEX_up_price[s,s_f,t] -flex_down[s,t]*FLEX_down_price[s,s_f,t])
                        temp+=flex_price_prob[s,s_f]*DA_prob[s]*(-dev_ch[s,s_f,t]*bm_down[s,s_f,t]-dev_dis[s,s_f,t]*bm_up[s,s_f,t])
                        temp+=flex_price_prob[s,s_f]*DA_prob[s]*ID_avg[s,s_f][t]*(ID_dis[s,s_f,t]-ID_ch[s,s_f,t])
                        temp+=-omega[s,s_f,t]
            for s in range(2):
                for s_f in range (2):
                    temp+=-flex_price_prob[s,s_f]*DA_prob[s]*z[s,s_f]*BUDG
            return temp
        
        # =============================================================================
        # def cost1():
        #     temp=0
        #     for t in range(0,24):
        #         temp+=quicksum(DA_scens[i][t]*DA_prob[i] for i in range (0,2))*(DA_dis[t]-DA_ch[t])
        #         for s in range(0,2):
        #             temp+=DA_prob[s]*ID_avg[s][t]*(ID_dis[t,s]-ID_ch[t,s])
        #             temp+=DA_prob[s]*-dev_ch[s,t]*bm_down[s,t]-DA_prob[s]*dev_dis[s,t]*bm_up[s,t]
        #             temp+=DA_prob[s]*flex_up[s,t]*FLEX_up_price[s,t]-DA_prob[s]*flex_down[s,t]*FLEX_down_price[s,t]
        #     for s in range(0,2):
        #         temp+=-DA_prob[s]*z[s]*BUDG-quicksum(omega[s,t] for t in range (0,24))
        #     return temp
        # =============================================================================
                
        model.setObjective(cost(), GRB.MAXIMIZE)
        
        model.optimize()
        objValues[BUDG]=model.objVal
        temp=0
        for t in range (0,24):
            temp+=DA_ch[t].x
        DA_char[BUDG]=temp
       
        #DA_char[BUDG]=quicksum(DA_ch[t].x for t in range (0,24))   
        temp=0
        for t in range (0,24):
            temp+=DA_dis[t].x
        DA_dischar[BUDG]=temp
        
        #DA_dischar[BUDG]=quicksum(DA_dis[t].x for t in range (0,24))
        temp=0
        for t in range (0,24):
            for s in range (0,2):
                    for s_f in range (0,2):
                        temp+=flex_price_prob[s,s_f]*DA_prob[s]*ID_ch[s,s_f,t].x
        ID_char[BUDG]=temp
        #ID_char[BUDG]=quicksum(ID_ch[t,s].x for t in range (0,24) for s in range(0,2))
        temp=0
        for t in range (0,24):
            for s in range(0,2):
                for s_f in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*ID_dis[s,s_f,t].x
        ID_dischar[BUDG]=temp    
        #ID_dischar[BUDG]=quicksum(ID_dis[t,s].x for t in range (0,24) for s in range(0,2))
        temp=0
        for t in range (0,24):
            for s in range (0,2):
                temp+=flex_price_prob[s,s_f]*DA_prob[s]*flex_up[s,t].x
        FLEXup[BUDG]=temp
        
        temp=0
        for t in range (0,24):
            for s in range(0,2):
                temp+=flex_price_prob[s,s_f]*DA_prob[s]*flex_down[s,t].x
        FLEXdown[BUDG]=temp
        
        temp=0
        for t in range (0,24):
            for s_f in range (0,2):
                for s in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*c[s_f,s,t].x
        chargo[BUDG]=temp
        
        temp=0
        for t in range (0,24):
            for s_f in range (0,2):
                for s in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*d[s_f,s,t].x
        dischargo[BUDG]=temp
        
        temp=0
        for t in range (0,24):
            for s_f in range (0,2):
                for s in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*g[s_f,s,t].x
        netto[BUDG]=temp
        
        
        temp=0
        for t in range (0,24):
            for s_f in range (0,2):
                for s in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*dev_dis[s_f,s,t].x
        blnc_up[BUDG]=temp
        
        temp=0
        for t in range (0,24):
            for s_f in range (0,2):
                for s in range (0,2):
                    temp+=flex_price_prob[s,s_f]*DA_prob[s]*dev_ch[s_f,s,t].x
        blnc_dwn[BUDG]=temp
    
        for t in range (24):
            tempori[t,BUDG]=DA_ch[t].x
            DA_char_hour[t,BUDG]=tempori[t,BUDG]
        for t in range (24):
            tempori[t,BUDG]=DA_dis[t].x
            DA_dis_hour[t,BUDG]=tempori[t,BUDG]
            
        for t in range (24):
            temp=0
            for s in range(2):
                for s_f in range (2):
                    tempu=flex_price_prob[s,s_f]*DA_prob[s]*ID_ch[s,s_f,t].x
                    temp+=tempu
            tempori[t,BUDG]=temp
            ID_char_hour[t,BUDG]=tempori[t,BUDG]
        for t in range (24):
            temp=0
            for s in range(2):
                for s_f in range(2):
                    tempu=flex_price_prob[s,s_f]*DA_prob[s]*ID_dis[s,s_f,t].x
                    temp+=tempu
            tempori[t,BUDG]=temp
            ID_dis_hour[t,BUDG]=tempori[t,BUDG]
            
        for t in range (24):
            temp=0
            for s in range(2):
                tempu=flex_down[s,t].x
                temp+=tempu
            tempori[t,BUDG]=temp
            FLEX_char_hour[t,BUDG]=tempori[t,BUDG]
        for t in range (24):
            temp=0
            for s in range(2):
                tempu=flex_up[s,t].x
                temp+=tempu
            tempori[t,BUDG]=temp
            FLEX_dis_hour[t,BUDG]=tempori[t,BUDG]
            
        for t in range (24):
            temp=0
            for s in range(2):
                for s_f in range (2):
                    tempu=dev_ch[s,s_f,t].x
                    temp+=tempu
            tempori[t,BUDG]=temp
            BM_char_hour[t,BUDG]=tempori[t,BUDG]
        for t in range (24):
            temp=0
            for s in range(2):
                for s_f in range(2):
                    tempu=dev_dis[s,s_f,t].x
                    temp+=tempu
            tempori[t,BUDG]=temp
            BM_dis_hour[t,BUDG]=tempori[t,BUDG]
                
                
# =============================================================================
# for t in range (24):
#     for b in range (24):
#         z_ID_dis.append(ID_dis_hour[t,b])
#         z_ID_char.append(ID_char_hour[t,b])
#         
# z_rez['Discharging']=z_flex_dis
# 
# z_rez['Charging']=z_flex_char
# 
# fig = plt.figure()
# 
# ax = fig.add_subplot(111, projection='3d')
# labels = ["Charging", "Discharging"]
# 
# for l in labels:
# 
#     ax.scatter(x, y, z_rez[l], label=l)
# 
# ax.set_title("FLEX activity")
# 
# ax.set_xlabel("Hour")
# 
# ax.set_ylabel("Uncertainty budget")
# 
# ax.set_zlabel("Quantity")
# 
# ax.legend(loc="best")
# 
# plt.show()
# =============================================================================





#ISPISI

def ispis_param (a,x_title,y_title,Title):
    temp=[]
    x=list(range(0,24))
    for i in range (0,24):
        temp.append(a[i])
    print(temp)
    fig = plt.figure()
    fig.set_size_inches(12, 8)
    plt.step(x,temp)
    fig.suptitle(Title, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel(x_title, fontsize=18)
    plt.ylabel(y_title, fontsize=18)
    
def ispis (a):
    temp=[]
    x=list(range(0,24))
    for i in range (0,24):
        temp.append(a[0,0,i].x)
    plt.step(x,temp)
    
def multispis (a,b,ime1,ime2):
    temp1=[]
    temp2=[]
    for i in range (0,24):
        temp1.append(a[i].x)
    for i in range (0,24):
        temp2.append(b[0,0,i].x)
    plt.step(temp1,'r',temp2,'b--')
    plt.legend([ime1, ime2])

def multispis_param (a,b,ime1,ime2,x_title,y_title,Title):
    temp1=[]
    temp2=[]
    for i in range (0,24):
        temp1.append(a[i])
    for i in range (0,24):
        temp2.append(b[i])
    fig = plt.figure()
    plt.step(temp1,'r',temp2,'b--')
    plt.legend([ime1, ime2], fontsize='xx-large') 
    fig.set_size_inches(12, 8)
    fig.suptitle(Title, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel(x_title, fontsize=18)
    plt.ylabel(y_title, fontsize=18)   
    
def multispis_mix (param,var,ime1,ime2):
    temp1=[]
    temp2=[]
    for i in range (0,24):
        temp1.append(param[i])
    for i in range (0,24):
        temp2.append(var[i].x)
    plt.step(temp1,'r',temp2,'b--')
    plt.legend([ime1, ime2])    
    
def multispis_mix3 (param,var1,var2,ime1,ime2, ime3,naslov):
    temp1=[]
    temp2=[]
    temp3=[]
    for i in range (0,24):
        temp1.append(param[i])
    for i in range (0,24):
        temp2.append(var1[i].x)
    for i in range (0,24):
        temp3.append(var2[i].x)
    plt.step(temp1,'r',temp2,'b--',temp3,'g')
    plt.legend([ime1, ime2, ime3])
    plt.title(naslov)
    
def multispis_param4 (param1,param2,param3,param4,ime1,ime2, ime3,ime4,Title,x_title,y_title):
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    for i in range (0,24):
        temp1.append(param1[i])
    for i in range (0,24):
        temp2.append(-param2[i])
    for i in range (0,24):
        temp3.append(param3[i])
    for i in range (0,24):
        temp4.append(-param4[i])
    fig = plt.figure()
    fig.set_size_inches(12, 8)
    fig.suptitle(Title, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel(x_title, fontsize=18)
    plt.ylabel(y_title, fontsize=18)
    plt.step(temp1,'r',temp2,'b--',temp3,'g',temp4,'y')
    plt.legend([ime1, ime2, ime3,ime4],fontsize='xx-large')
    
#pd.Series(DA_proba_hour).rename_axis(['Hour', 'Budg']).reset_index(name='DA_ch')    
#grupa=data.groupby(["Hour","DayOfWeek"])
# 
# for d in range (7):
#     for h in range (24):
#         dani.append(d)
#         sati.append(h)
#         cijene.append(grupa.take([d*24+h]).values.tolist()[0][0])
#         print(grupa.take([d*24+h]))
# 
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# 
# ax.plot_trisurf(dani, sati, cijene, linewidth=0.2, antialiased=True)
# 
# plt.show()
    


    


    
