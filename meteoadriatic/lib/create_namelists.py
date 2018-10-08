import sys
import fileinput
from shutil import copyfile


def create_namelist_wps(namelist_wps_static, namelist_wps_dynamic, wrf_init_time, wrf_end_time):
    copyfile(namelist_wps_static, namelist_wps_dynamic)

    for line in fileinput.input([namelist_wps_dynamic], inplace=True):
        if line.strip().startswith('start_date = '):
            line = "start_date = '" + str(wrf_init_time) + "'" + "\n"
        if line.strip().startswith('end_date = '):
            line = "start_date = '" + str(wrf_end_time) + "'" + "\n"
        sys.stdout.write(line)
