from time_calc import calculate_init_time, calculate_end_time
from strc import lbc_hours, strc_ptiles_string, strc_cgi, strc_download, clean_inputdir
import urllib.request


# Defaults
YYYY_lbc = '2018'
MM_lbc = '10'
DD_lbc = '03'
HH_lbc = '12'
init_delay = '06'
run_length='06'
lbc_frequency='3'

strc_server='http://ems1.comet.ucar.edu'
strc_path='cgi-bin/PTmaster.pl'
strc_leftlon='6'
strc_rightlon='25'
strc_toplat='51'
strc_bottomlat='39'
strc_gfs_grid='0p25'
strc_dataset='gfsp25'

download_dir='download'


gfs_run, wrf_init_time = calculate_init_time(YYYY_lbc, MM_lbc, DD_lbc, HH_lbc, init_delay)
wrf_end_time = calculate_end_time(wrf_init_time, run_length)

print('GFS RUN:', gfs_run)
print('WRF INIT:', wrf_init_time)
print('WRF END:', wrf_end_time)

# Clean input directory
clean_inputdir(download_dir)

# Build strc request cgi command
lbc_hours = lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency)
strc_ptiles_string = strc_ptiles_string(gfs_run, lbc_hours, strc_gfs_grid)
strc_cgi = strc_cgi(strc_server, strc_path, strc_ptiles_string, strc_leftlon,
                            strc_rightlon, strc_toplat, strc_bottomlat, strc_dataset)

# Request ptiles
req = urllib.request.Request(strc_cgi)
resp = urllib.request.urlopen(req)
strc_response = resp.read()

# Download ptiles
strc_download(strc_response.decode("utf-8"), download_dir)
