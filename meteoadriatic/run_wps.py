from lib.time_calc import wrf_init_time, wrf_end_time
from lib.create_namelists import create_namelist_wps

namelist_wps_static = "../runs/test_domain/static/namelist.wps"
namelist_wps_dynamic = "../runs/test_domain/wpsprd/namelist.wps"

'''
This file prepares prerequisites required to run WPS suite (ungrib.exe and metgrid.exe) and then executes it.

Step 1. Use namelist_wps_static template to create dynamic version with correct start and end datetime.
We need to edit "start_date = ..." and "end_date = ..." lines

'''

create_namelist_wps(namelist_wps_static, namelist_wps_dynamic, wrf_init_time, wrf_end_time)


'''
Above construction works but only for parent domain entry.
TODO: construct a loop that will also add entries for nests.

'''


'''
Mistery:
In this file, relative link to runs/test_domain/static is
"../runs/test_domain"
however, in download_strc_py, which is at the same level, it is 
"runs/test_domain"

What's going on? A Pycharm joke?

'''