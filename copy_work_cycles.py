# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 03:02:40 2013

@author: katia
"""
N_COM = (180)
R_CUT = float(5)
R_BOND_oo = 3.3
R_BOND_oh = 2.6
input_file = "/home/katia/Science/hemoglobin/ver2_1MBN/qwe.pdb"
pattern = "TIP3W"

def for_read():
    in_file = open(input_file, "r")
    oo = []
    h_1 = []
    h_2 = [] 
    for ii in in_file:
        word = ii.split()
        if pattern in ii:
            if "OH2" in ii:
                #пишем все координаты
                oo.append([float(q) for q in word[4:7]])
            elif "H1" in ii:
                h_1.append([float(q) for q in word[4:7]])
            elif "H2" in ii:
                print word[4:7]
                h_2.append([float(q) for q in word[4:7]])
    print oo
    return oo, h_1, h_2
    
def bonds():
    oo, h_1, h_2 = for_read()
    ow_x_coord, ow_y_coord, ow_z_coord = [i[0] for i in oo], [i[1] for i in oo], [i[2] for i in oo]
    hw1_x_coord, hw1_y_coord, hw1_z_coord = [i[0] for i in h_1], [i[1] for i in h_1], [i[2] for i in h_1]
    hw2_x_coord, hw2_y_coord, hw2_z_coord = [i[0] for i in h_2], [i[1] for i in h_2], [i[2] for i in h_2]    
    N_OX = len(oo)
    angle = []    
    list_numbers_new = []
    list_o_x_coord = []
    list_o_y_coord = []
    list_o_z_coord = []
    for ii in range(N_OX) :
        list_numbers_new.append([])
        list_o_x_coord.append([])
        list_o_y_coord.append([])
        list_o_z_coord.append([])
        for jj in range(N_OX):
            if ii != jj :
                dist1 = math.sqrt((ow_x_coord[ii] - hw1_x_coord[jj])**2 + \
                (ow_y_coord[ii]-hw1_y_coord[jj])**2 + (ow_z_coord[ii]-hw1_z_coord[jj])**2)
                
                dist2 = math.sqrt((ow_x_coord[ii] - hw2_x_coord[jj])**2 + \
                (ow_y_coord[ii]-hw2_y_coord[jj])**2 + (ow_z_coord[ii]-hw2_z_coord[jj])**2)
                
                dist_oo = math.sqrt((ow_x_coord[ii] - ow_x_coord[jj])**2 + \
                (ow_y_coord[ii] - ow_y_coord[jj])**2 + (ow_z_coord[ii] - ow_z_coord[jj])**2)
                
                if (dist1 < R_BOND_oh and dist_oo < R_BOND_oo) : 
                    print dist1, dist_oo
                    list_numbers_new[ii].append(jj)
                    list_o_x_coord[ii].append(ow_x_coord[jj])
                    list_o_y_coord[ii].append(ow_y_coord[jj])
                    list_o_z_coord[ii].append(ow_z_coord[jj])
                    #print 'hydrogen bond exists!', ii, jj
                    vec_oh = [hw1_x_coord[jj] - ow_x_coord[ii], hw1_y_coord[jj] - ow_y_coord[ii], hw1_z_coord[jj] - ow_z_coord[ii] ]
                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
                    angle.append(math.acos(cosinus)/pi*180)  
                elif (dist2 < R_BOND_oh and dist_oo < R_BOND_oo) :          
                    list_numbers_new[ii].append(jj)
                    list_o_x_coord[ii].append(ow_x_coord[jj])
                    list_o_y_coord[ii].append(ow_y_coord[jj])
                    list_o_z_coord[ii].append(ow_z_coord[jj])
                    #print 'hydrogen bond exists!', ii ,jj
                    vec_oh = [hw2_x_coord[jj] - ow_x_coord[ii], hw2_y_coord[jj] - ow_y_coord[ii], hw2_z_coord[jj] - ow_z_coord[ii] ]
                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
                    angle.append(math.acos(cosinus)/pi*180)  
                else:
                    pass

            
bonds()
