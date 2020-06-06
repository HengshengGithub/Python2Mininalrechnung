import numpy as np

global Maschine

Maschine = {'info':{}, 'BGs':{}, 'CONTROL': {}}
Maschine['info'] = {'name':''}

Position = {'null':np.zeros((3,1)),'ex':np.zeros((3,1)),\
            'ey':np.zeros((3,1)), 'ez':np.zeros((3,1))}



BGs = {'info':{}, 'BG_FEM':np.empty(1), 'BG_MOR': np.empty(1)}
BGs['info'] = {'bg_n':0}

BG_FEM = {'info':{}, 'sys_mat_thm':{}, 'mat_param':{},\
          'PIN':np.empty(1), 'POSITION':Position}
BG_FEM['info'] = {'name':'', 'pin_n':0, 'node_n':0, 'convection_index':0}


Maschine['BGs'] = BGs