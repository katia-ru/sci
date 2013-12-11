# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 04:07:29 2013

@author: katia
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 03:02:40 2013

@author: katia
"""
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy

N_COM = (180)
R_CUT = float(6)
R_BOND_oo = 3.3
R_BOND_oh = 2.6
input_file = "/home/katia/Science/hemoglobin/ver2_1GZX/minimized_1GZX.pdb"
#input_file = "/home/katia/Science/hemoglobin/water_ball/water_ball_after_min.pdb"
pattern = "TIP3W"
#THRESHOLD = 5
#ширина окошка для радиальной функции
width = 0.1
N_COM = 1000

width_angle = 1

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
                h_2.append([float(q) for q in word[4:7]])
    return oo, h_1, h_2
    
def bonds():
    oo, h_1, h_2 = for_read()
    
    ow_x_coord, ow_y_coord, ow_z_coord = [i[0] for i in oo], [i[1] for i in oo], [i[2] for i in oo]
    hw1_x_coord, hw1_y_coord, hw1_z_coord = [i[0] for i in h_1], [i[1] for i in h_1], [i[2] for i in h_1]
    hw2_x_coord, hw2_y_coord, hw2_z_coord = [i[0] for i in h_2], [i[1] for i in h_2], [i[2] for i in h_2]    
    N_OX = len(oo)
    print N_OX
    angle = []    
    
    x_axis = []
    y_axis = []
    
    x_axis_angle = []
    y_axis_angle = []
    
    #width = 
    my_dict = {}
    my_dict_angle = {}
    oo_hist = 0
    g = [ [ 0 for j in xrange(N_OX) ] for i in xrange(N_OX) ]
    for ii in xrange(N_OX):
        for jj in xrange(N_OX):
            if ii != jj :
                dist1 = math.sqrt((ow_x_coord[ii] - hw1_x_coord[jj])**2 + \
                (ow_y_coord[ii]-hw1_y_coord[jj])**2 + (ow_z_coord[ii]-hw1_z_coord[jj])**2)
                
                dist2 = math.sqrt((ow_x_coord[ii] - hw2_x_coord[jj])**2 + \
                (ow_y_coord[ii]-hw2_y_coord[jj])**2 + (ow_z_coord[ii]-hw2_z_coord[jj])**2)
                
                dist_oo = math.sqrt((ow_x_coord[ii] - ow_x_coord[jj])**2 + \
                (ow_y_coord[ii] - ow_y_coord[jj])**2 + (ow_z_coord[ii] - ow_z_coord[jj])**2)
                
                dist_oo = int(dist_oo/width)*width
                if dist_oo < R_CUT:
                    if my_dict.has_key(dist_oo):
                        my_dict[dist_oo] += 1
                    else:
                        my_dict[dist_oo] = 1
                        
                #смотрим на углы:
                if (dist1 < R_BOND_oh and dist_oo < R_BOND_oo):        
                    vec_oh = [hw1_x_coord[jj] - ow_x_coord[ii], hw1_y_coord[jj] - ow_y_coord[ii], hw1_z_coord[jj] - ow_z_coord[ii] ]
                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
                    angle.append(math.acos(cosinus)/pi*180) 
                elif (dist2 < R_BOND_oh and dist_oo < R_BOND_oo):          
                    vec_oh = [hw2_x_coord[jj] - ow_x_coord[ii], hw2_y_coord[jj] - ow_y_coord[ii], hw2_z_coord[jj] - ow_z_coord[ii] ]
                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
                    angle.append(math.acos(cosinus)/pi*180)  
                
    for cur_angle in angle:
        cur_angle = int(cur_angle/width_angle)*width_angle
        if my_dict_angle.has_key(cur_angle):
            my_dict_angle[cur_angle] += 1
        else:
            my_dict_angle[cur_angle] = 1
        
    for ii in sorted(my_dict):
        if ii:
            my_dict[ii] /= 2
            my_dict[ii] = my_dict[ii]/(4*pi*ii**2/(R_CUT/N_COM))
            x_axis.append(ii)
            y_axis.append(my_dict[ii]) 
    
    x_axis_angle = sorted(my_dict_angle)
    y_axis_angle = [my_dict_angle[i] for i in x_axis_angle]
        
    #plt.bar(x_axis, y_axis,  width=x_axis[1]-x_axis[0])
#    
#    plt.bar(x_axis_angle, y_axis_angle,  width=x_axis_angle[1]-x_axis_angle[0])
#    #labels = [str(i/60) for i in x_axis]
#    #plt.xticks(x_axis, labels)
#    my_title = "Radial Distribution Function"
#    plt.title(my_title)
#    plt.savefig(my_title+".png")
    
    plt.subplot(2, 1, 1)
    plt.plot(x_axis, y_axis, 'yo-')
    plt.title('Radial Distribution Function')


    plt.subplot(2, 1, 2)
    plt.plot(x_axis_angle, y_axis_angle, 'r.-')
    plt.title("Angle Distribution Function")


    plt.show()

bonds()             
#                if (dist1 < R_BOND_oh and dist_oo < R_BOND_oo) : 
#                    print dist1, dist_oo
#                    list_numbers_new[ii].append(jj)
#                    list_o_x_coord[ii].append(ow_x_coord[jj])
#                    list_o_y_coord[ii].append(ow_y_coord[jj])
#                    list_o_z_coord[ii].append(ow_z_coord[jj])
#                    #print 'hydrogen bond exists!', ii, jj
#                    vec_oh = [hw1_x_coord[jj] - ow_x_coord[ii], hw1_y_coord[jj] - ow_y_coord[ii], hw1_z_coord[jj] - ow_z_coord[ii] ]
#                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
#                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
#                    angle.append(math.acos(cosinus)/pi*180)  
#                elif (dist2 < R_BOND_oh and dist_oo < R_BOND_oo) :          
#                    list_numbers_new[ii].append(jj)
#                    list_o_x_coord[ii].append(ow_x_coord[jj])
#                    list_o_y_coord[ii].append(ow_y_coord[jj])
#                    list_o_z_coord[ii].append(ow_z_coord[jj])
#                    #print 'hydrogen bond exists!', ii ,jj
#                    vec_oh = [hw2_x_coord[jj] - ow_x_coord[ii], hw2_y_coord[jj] - ow_y_coord[ii], hw2_z_coord[jj] - ow_z_coord[ii] ]
#                    vec_med = [(hw1_x_coord[jj] + hw2_x_coord[jj])/2, (hw1_y_coord[jj] + hw2_y_coord[jj])/2, (hw1_z_coord[jj] + hw2_z_coord[jj])/2]
#                    cosinus = (vec_oh[0]*vec_med[0]+vec_oh[1]*vec_med[1]+vec_oh[2]*vec_med[2])/math.sqrt(vec_oh[0]**2+vec_oh[1]**2+vec_oh[2]**2)/math.sqrt(vec_med[0]**2+vec_med[1]**2+vec_med[2]**2)
#                    angle.append(math.acos(cosinus)/pi*180)  
#                else:
#                    pass


