# Modified version of code from (on 2025-03-08):
# https://docs.sunpy.org/en/stable/generated/gallery/acquiring_data/querying_the_GOES_event_list.html
from sunpy.net import Fido
from sunpy.net import attrs as a

import logging
log = logging.getLogger('sunpy')
log.setLevel('DEBUG')

event_type = "FL"
observatory = "GOES"

for year in range(2000, 2024):
    tstart = f"{year}/01/01"
    tend = f"{year}/12/31"

    print(f"Querying the HEK for year {year}")
    result = Fido.search(a.Time(tstart, tend),
                         a.hek.EventType(event_type),
                         a.hek.OBS.Observatory == observatory)

    hek_results = result["hek"]

    filtered_results = hek_results["event_starttime",
                                   "event_peaktime",
                                   "event_endtime",
                                   "fl_goescls",
                                   "ar_noaanum"]

    df = filtered_results.to_pandas()

    fname = f"download.{year}"
    print(f"Writing {fname}." + "{csv, pkl}")
    df.to_csv(f"{fname}.csv", index=False)
    df.to_pickle(f"{fname}.pkl")
