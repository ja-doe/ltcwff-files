#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:30:16 2022

@author: jan
"""

#### Lists and Dicts

my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

# my_roster_list_upper = ['', '', '']
# i=0
# for player in my_roster_list:
#     my_roster_list_upper[i]= player.title()
#     i=i+1
    
# my_roster_list_upper = []
# for player in my_roster_list:
#     my_roster_list_upper.append(player.title())

my_roster_dict = {'qb': 'tom brady',
                  'rb1': 'adrian peterson',
                  'wr1': 'antonio brown'}

my_roster_dict['k'] = 'mason crosby'

# for x in my_roster_dict:
#     print(f"position: {x}")
    
# for x in my_roster_dict:
#     print(f"position: {x}")
#     print(f"player: {my_roster_dict[x]}")
    
# for x in my_roster_dict:
#     print(f"{x}: {my_roster_dict[x]}")

# for x,y in my_roster_dict.items():
#     print(f"{x}: {y}")


#### Comprehrensions

my_roster_list_proper = [x.title() for x in my_roster_list]

my_roster_last_names = [full_name.split(' ')[1]
                        for full_name in my_roster_list]

my_roster_first_names = [full_name.split(' ')[0]
                        for full_name in my_roster_list]

my_roster_a_only = [x for x in my_roster_list if x.startswith('a')]

my_roster_a_only_title = [x.title() for x in my_roster_list if x.startswith('a')]


#### Dict Comprehension

pts_per_player = {'tom brady': 20.7,
                  'adrian peterson': 10.1,
                  'antonio brown': 18.5}

pts_x2_per_upper_player = {
    name.upper(): pts*2 for name, pts in pts_per_player.items()}

# Dict to List and then passed to sum function
print(sum([pts for _, pts in pts_per_player.items()]))






































