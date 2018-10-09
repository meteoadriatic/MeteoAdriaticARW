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
max_dom = len(domains_definition)

start_date, end_date = calculate_nests_date(domains_definition, wrf_init_time)
start_date = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in start_date]
end_date = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in end_date]

interval_seconds = int(lbc_frequency) * 3600

create_namelist_wps(namelist_wps_static, namelist_wps_dynamic, start_date, end_date, max_dom, interval_seconds)



'''
Mistery:
In this file, relative link to runs/test_domain/static is
"../runs/test_domain"
however, in download_strc_py, which is at the same level, it is 
"runs/test_domain"

What's going on? A Pycharm joke?

'''