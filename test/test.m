clc;
clear all;

POSITION = struct('null',zeros(3,1),'ex',zeros(3,1),'ey',zeros(3,1),'ez',zeros(3,1))
BGs = struct('info',struct,'BG_FEM',cell(1),'BG_MOR',cell(1))
BGs.info = struct('bg_n',0)

    BG_FEM = struct('info',struct,'sys_mat_thm',struct,'mat_param',struct,'PIN',cell(1),'POSITION',POSITION)
    BG_FEM.info = struct('name','','pin_n',0,'node_n',0,'convection_index', 0)

