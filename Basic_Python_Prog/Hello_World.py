#print ('Hello World')
#ls=[1,2,2,3]
#ls="hello"
#for i in range(len(ls)):
#    print(ls[i],end="")
ne_to_events_file={
    'OLD_NRM':{'FIVEGNODEB':{'low':{'CUCP':'cell1',
                                        'CUUP':'cell2',
                                        'CUDP':'cell3',
                                        'default':'cell4',},

                                'high':{'CUCP':'cell5',
                                        'CUUP':'cell6',
                                        'CUDP':'cell7',
                                        'default':'cell8',
                                        }
                                 },
            'GNODEBRADIO': {'low': {'CUCP': 'gecll9',
                                          'CUUP': 'gcell10',
                                          'CUDP': 'gcell11',
                                          'default': 'gcell12', },

                                  'high': {'CUCP': 'gcell13',
                                           'CUUP': 'gcell14',
                                           'CUDP': 'gcell15',
                                           'default': 'gcell16',
                                           }
                                  }

                   },
  'NRM6.2':{'GNODEBRADIO': {'low': {'CUCP': 'gecll9',
                                          'CUUP': 'gcell10',
                                          'CUDP': 'gcell11',
                                          'default': 'gcell12', },

                                  'high': {'CUCP': 'gcell13',
                                           'CUUP': 'gcell14',
                                           'CUDP': 'gcell15',
                                           'default': 'gcell16',
                                           }
                                  }

                   }


    }



#for p_id, p_info in people.items():
#    print("\nPerson ID:", p_id)

#    for key in p_info:
#        print(key + ':', p_info[key])

dep='NRM4'
ne='GNODEBRADIO'
p='high'
OLD_NRM=['NRM6','NRM6.1']
#for n in ne_to_events_file:
#    if(n==dep):
#        print("hello")
if  dep in ne_to_events_file:
   if ne in ne_to_events_file[dep]:
       if p in ne_to_events_file[dep][ne]:
          print(ne_to_events_file[dep][ne][p])
       else:
            print("no")
else:
    if dep in OLD_NRM:
      dep='OLD_NRM'
    if dep in ne_to_events_file:
        if ne in ne_to_events_file[dep]:
            if p in ne_to_events_file[dep][ne]:
                print(ne_to_events_file[dep][ne][p])
            else:
                print("no")

#print(ne_to_events_file['OLD_NRM']['FIVEGNODEB'][p])
#print(ne_to_events_file['NRM6.2']['GNODEBRADIO'])

#for a in people:
#    if a==1:
#        print("congrats")
#        break
#    else:
#        print("unsuccessful")