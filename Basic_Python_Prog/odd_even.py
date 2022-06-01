#a=int(input("enter a number"))
#if a%2==0:
#    print(f"{a} is a even number")
#else:
#    print(f"{a} is an odd number")



from  check_pos_neg_number import ut
new_map={ 1: ['NRM6','NRM6.1'],
                2: ['NRM6.2']}
test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3},
             {'gfg' : 2}, {'best' : 3, 'gfg' : 4}]

ne_to_events_file = {
    1: {'FIVEGNODEB': {'low': {'CUCP': 'cell1',
                               'CUUP': 'cell2',
                               'CUDP': 'cell3',
                               'default': 'cell4', },

                       'high': {'CUCP': 'cell5',
                                'CUUP': 'cell6',
                                'CUDP': 'cell7',
                                'default': 'cell8',
                                }
                       },
        'GNODEBRADIO': {'low': {'CUCP': 'gecll9',
                                'CUUP': 'gcell10',
                                'CUDP': 'gcell11',
                                'default': 'gcell12', },

                        'high': {'CUCP': 'gcell13',
                                 'CUUP': 'gcell14',
                                 'CUDP': 'gcell15',
                                 'default': 'hello',
                                 }
                        }

        },
    2: {'GNODEBRADIO': {'low': {'CUCP': 'gecll9',
                                'CUUP': 'gcell10',
                                'CUDP': 'gcell11',
                                'default': 'gcell12', },

                        'high': {'CUCP': 'gcell13',
                                 'CUUP': 'gcell14',
                                 'CUDP': 'gcell15',
                                 'default': 'default',
                                 }
                        }

        }

}

dep_type='NRM6'
ne='GNODEBRADIO'
p='high'
#temp=''

for k,v in new_map.items():
    for i in v:
      if i==dep_type:
         temp=k
         print(temp)

#temp=2
#ne_to_events=ut.ne_to_events_file
if temp in ne_to_events_file:
   if ne in ne_to_events_file[temp]:
        if p in ne_to_events_file[temp][ne]:
            print(ne_to_events_file[temp][ne][p])

