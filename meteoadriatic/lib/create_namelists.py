import sys
import fileinput
from shutil import copyfile
from datetime import timedelta


def calculate_nests_date(domains_definition, wrf_init_time):
    nests_start = list()
    nests_end = list()
    for item in domains_definition:
        id, delay, length = item.split(":")
        nest_start = wrf_init_time + timedelta(hours=int(delay))
        nest_end = wrf_init_time + timedelta(hours=int(delay)) + timedelta(hours=int(length))
        nests_start.append(nest_start)
        nests_end.append(nest_end)
    return nests_start, nests_end


def create_namelist_wps(namelist_wps_static, namelist_wps_dynamic, start_date, end_date, max_dom, interval_seconds):
    copyfile(namelist_wps_static, namelist_wps_dynamic)
    for line in fileinput.input([namelist_wps_dynamic], inplace=True):
        if line.strip().startswith('max_dom = '):
            line = " max_dom = " + str(max_dom) + ",\n"
        if line.strip().startswith('start_date = '):
            insert_string = "', ".join(start_date)
            line = " start_date = '" + insert_string + "'" + ",\n"
        if line.strip().startswith('end_date = '):
            insert_string = "', ".join(end_date)
            line = " end_date = '" + insert_string + "'" + ",\n"
        if line.strip().startswith('interval_seconds = '):
            insert_string = "', ".join(end_date)
            line = " interval_seconds = " + str(interval_seconds) + "\n"
        sys.stdout.write(line)
