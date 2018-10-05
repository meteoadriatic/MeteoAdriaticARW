from lib.time_calc import gfs_run, wrf_init_time, wrf_end_time
from lib import strc
import urllib.request
from date_info import *

# Defaults
strc_server = 'http://ems1.comet.ucar.edu'
strc_path = 'cgi-bin/PTmaster.pl'
strc_leftlon = '6'
strc_rightlon = '25'
strc_toplat = '51'
strc_bottomlat = '39'
strc_gfs_grid = '0p25'
strc_dataset = 'gfsp25'

download_dir = 'download'


print('GFS RUN:', gfs_run)
print('WRF INIT:', wrf_init_time)
print('WRF END:', wrf_end_time)

# Clean input directory
strc.clean_inputdir(download_dir)

# Build strc request cgi command
lbc_hours = strc.lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency)
ptiles_string = strc.ptiles_string(gfs_run, lbc_hours, strc_gfs_grid)
cgi = strc.build_cgi(strc_server, strc_path, ptiles_string, strc_leftlon,
                     strc_rightlon, strc_toplat, strc_bottomlat, strc_dataset)

# Request ptiles
req = urllib.request.Request(cgi)
resp = urllib.request.urlopen(req)
strc_response = resp.read()

# Download ptiles
strc.download_ptiles(strc_response.decode("utf-8"), download_dir)
