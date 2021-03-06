# -*- coding: utf-8 -*-
# (c) 2016 - Ilya Prokin - isprokin@gmail.com - https://iprokin.github.io
# INRIA Rhone-Alpes
# STDP model : variables' names and initial values
import numpy as np

ST_vars_and_ic = \
    { 'h_caL13' : 0.99182137906713796
    , 'm_caL13' : 0.0036977671871038817

    , 'o_AMPA'  : 0.0
    , 'd_AMPA'  : 0.0

    , 'o_NMDA'  : 0.0

    , 'h_CICR'  : 0.82466766689469506
    , 'Ca_cyt'  : 0.12132718966407073
    , 'Ca_ER'   : 63.348087686853646
    , 'IP3'     : 0.057291400446753571
    , 'DAG'     : 0.005734867663641929
    , 'DAGLP'   : 4.1969621599776083e-07
    , 'twoAG'   : 3.2085896623941232e-06
    , 'AEA'     : 0.0061033848099783438
    , 'fpre'    : 1.0

    , 'I1P'     : 0.042380592866431144
    , 'PP1'     : 0.00093939509311232795

    , 'V'       : -69.999016204528218

    , 'o_CB1R'  : 3.4373437854140236e-07
    , 'd_CB1R'  : 0.002994487796947427
    }

CaMKII_ic=np.array(
    [ 0.23316029213700182
    , 0.0034298074889746086
    , 0.00028889779878196254
    , 0.00013756133483052541
    , 3.6365976788029681e-05
    , 4.1274017451676494e-06
    , 4.2498580055485264e-06
    , 1.2513942987290664e-07
    , 3.2696082960591099e-07
    , 4.5484170099234244e-08
    , 3.078127923587743e-08
    , 2.7970211543431621e-09
    , 1.3221817318283754e-11
    ])

lCaMKII = len(CaMKII_ic)
NEQ = len(ST_vars_and_ic) + lCaMKII

si = lambda x, SK=ST_vars_and_ic.keys(): lCaMKII + SK.index(x)
