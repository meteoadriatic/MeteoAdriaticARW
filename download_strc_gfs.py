from time_calc import calculate_init_time, calculate_end_time
from strc import lbc_hours

# Defaults
YYYY_lbc = '2018'
MM_lbc = '10'
DD_lbc = '01'
HH_lbc = '00'
init_delay = '12'
run_length='120'
lbc_frequency='3'

strc_server=''
strc_path=''
strc_leftlon=''
strc_rightlon=''
strc_toplat=''
strc_bottomlat=''


gfs_run, wrf_init_time = calculate_init_time(YYYY_lbc, MM_lbc, DD_lbc, HH_lbc, init_delay)
wrf_end_time = calculate_end_time(wrf_init_time, run_length)

print('GFS RUN:', gfs_run)
print('WRF INIT:', wrf_init_time)
print('WRF END:', wrf_end_time)

# Build list of LBC's time stamps
lbc_hours = lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency)

# for lbc_time in lbc_hours:
#     print(lbc_time)




# function build_list_of_files() {
# strcdate=${ST_YYYY}${ST_MM}${ST_DD}${ST_HH}
# strcdate=`echo "$strcdate" | cut -c 3-`
# strcinit=${ST_HH}
# strcfilestring=""
# for ((i=$FIRSTFTIME;i<=$LASTFTIME;i+=$STEP)) ; do
#     FCST_TIME=`printf "%03d\n" "$i"`
#     strcfilestring+="file=${strcdate}.gfs.t${strcinit}z"
#     strcfilestring+=".${STRCRES}.pgrb2f${FCST_TIME}&"
# done
# }

# strccmd="${use_strc_server}/${STRCPATH}?${strcfilestring}"
# strccmd+="&leftlon=${LEFTLON}&rightlon=${RIGHTLON}"
# strccmd+="&toplat=${TOPLAT}&bottomlat=${BOTTOMLAT}&dset=${STRCDSET}"

