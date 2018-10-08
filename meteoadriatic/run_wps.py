from lib.time_calc import wrf_init_time
from lib.create_namelists import calculate_nests_date, create_namelist_wps
from date_info import *

namelist_wps_static = "../runs/test_domain/static/namelist.wps"
namelist_wps_dynamic = "../runs/test_domain/wpsprd/namelist.wps"

'''
This file prepares prerequisites required to run WPS suite (ungrib.exe and metgrid.exe) and then executes it.

Step 1. Use namelist_wps_static template to create dynamic version with correct start and end datetime.
We need to edit "start_date = ..." and "end_date = ..." lines

'''

nests_definition = nests.split(",")
domains_definition = ['0:0:0'] + nests_definition

domains_start, domains_end = calculate_nests_date(domains_definition, wrf_init_time)
domains_start = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in domains_start]
domains_end = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in domains_end]
print(domains_start)
print(domains_end)

create_namelist_wps(namelist_wps_static, namelist_wps_dynamic, domains_start, domains_end)



'''
Mistery:
In this file, relative link to runs/test_domain/static is
"../runs/test_domain"
however, in download_strc_py, which is at the same level, it is 
"runs/test_domain"

What's going on? A Pycharm joke?

'''