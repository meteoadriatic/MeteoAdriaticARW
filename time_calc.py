from datetime import datetime, timedelta


def calculate_init_time(yyyy_lbc: str, mm_lbc: str, dd_lbc: str, hh_lbc: str, init_delay: str) -> object:
    yyyy_lbc = int(yyyy_lbc)
    mm_lbc = int(mm_lbc)
    dd_lbc = int(dd_lbc)
    hh_lbc = int(hh_lbc)
    init_delay = int(init_delay)

    lbc_time = datetime(yyyy_lbc, mm_lbc, dd_lbc, hh_lbc)
    init_time = lbc_time + timedelta(hours=init_delay)
    return tuple([lbc_time, init_time])


lbc_time, init_time = calculate_init_time('2000', '01', '01', '00', '30')
