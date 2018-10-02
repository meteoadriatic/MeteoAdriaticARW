from time_calc import calculate_init_time

# Defaults
YYYY_lbc = '2018'
MM_lbc = '10'
DD_lbc = '01'
HH_lbc = '00'
init_delay = '30'

gfs_run, wrf_init_time = calculate_init_time(YYYY_lbc, MM_lbc, DD_lbc, HH_lbc, init_delay)

print(gfs_run)
print(wrf_init_time)
