from lib.time_calc import wrf_init_time
from lib import namelists
from date_info import *
from conf import vtables
import shutil
import configparser
import os




'''
Read configuration files
references:
https://wiki.python.org/moin/ConfigParserExamples
'''

Config = configparser.ConfigParser()
defaults = Config.read("../config/defaults.ini")

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


input_dataset = ConfigSectionMap("dataset")['input_dataset']
wps_version = ConfigSectionMap("model")['wps_version']


# Set file paths
wps_prdir = "../runs/test_domain/wpsprd/"
static_dir = "../runs/test_domain/static/"
namelist_wps_static = static_dir + "namelist.wps"
namelist_wps_dynamic = wps_prdir + "namelist.wps"
tables_dir = "../tables/" + wps_version + "/WPS/"


# Clean wps_prdir
if os.path.isdir(wps_prdir):
    shutil.rmtree(wps_prdir)
os.mkdir(wps_prdir)


'''
This module prepares prerequisites required to run WPS suite (ungrib.exe and metgrid.exe) and then executes it.

Requirements: acquired input (LBC) files in runs/<domainname>/input
Module output: prepared metgrid_* files in runs/<domainname>/wpsprd 
'''


'''
----------------------------------------
--------------- Step 1. ----------------
------------- namelist.wps -------------
----------------------------------------
 
Use namelist_wps_static template to create dynamic version with correct start and end datetime.
We take namelist.wps template from domain static directory and according to particular run variables, edit lines:

"start_date = ..."         (nested)
"end_date = ..."           (nested)
"max_dom = ..."            (single)
"interval_seconds = ..."   (single)

'''


'''
Determine domains definition from config/user input. We need to know number of configured domains
For each of them we need to get start delay time (hours after MOAD) and run length. Information about
nests should be given in form of list with each entry in format 'x:y:z' where x is nest ID, y is
start delay and z is run length for that nest. MOAD (mother of all domains) always has definition '0:0:0'
and is not included in user configuration entries, but added in domains definition in code below.  
'''
nests_definition = nests.split(",")
domains_definition = ['0:0:0'] + nests_definition
max_dom = len(domains_definition)


'''
Here we calculate start_date and end_date and interval_seconds 
namelist.wps entries for all requested domains. Proper format handling is also done here. 
'''
start_date, end_date = namelists.calculate_nests_date(domains_definition, wrf_init_time)
start_date = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in start_date]
end_date = [dt.strftime("%Y-%m-%d_%H:%M:%S") for dt in end_date]

interval_seconds = int(lbc_frequency) * 3600

shutil.copyfile(namelist_wps_static, namelist_wps_dynamic)
namelists.create_namelist_wps(namelist_wps_dynamic, start_date, end_date, max_dom, interval_seconds)


'''
----------------------------------------
--------------- Step 2. ----------------
--------------- linking ----------------
----------------------------------------

All tables and executables has to be linked into WPS process directory.

'''

# 2A: link Vtable according to input data source
vtable = vtables.Vtables.get(input_dataset)

print("Selected Vtable:", vtable)
os.symlink(tables_dir + vtable, wps_prdir + "Vtable")