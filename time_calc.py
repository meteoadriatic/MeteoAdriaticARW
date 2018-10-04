from datetime import datetime, timedelta
from date_info import *

def calculate_init_time(yyyy_lbc, mm_lbc, dd_lbc, hh_lbc, init_delay):
    yyyy_lbc = int(yyyy_lbc)
    mm_lbc = int(mm_lbc)
    dd_lbc = int(dd_lbc)
    hh_lbc = int(hh_lbc)
    init_delay = int(init_delay)

    lbc_time = datetime(yyyy_lbc, mm_lbc, dd_lbc, hh_lbc)
    init_time = lbc_time + timedelta(hours=init_delay)
    return tuple([lbc_time, init_time])


def calculate_end_time(init_time, run_length):
    run_length = int(run_length)

    end_time = init_time + timedelta(hours=run_length)
    return end_time


gfs_run, wrf_init_time = calculate_init_time(YYYY_lbc, MM_lbc, DD_lbc, HH_lbc, init_delay)
wrf_end_time = calculate_end_time(wrf_init_time, run_length)