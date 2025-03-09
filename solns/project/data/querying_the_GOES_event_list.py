# Modified version of code from (on 2025-03-08):
# https://docs.sunpy.org/en/stable/generated/gallery/acquiring_data/querying_the_GOES_event_list.html

"""
==================================
Querying the GOES flare event list
==================================

How to retrieve the GOES flare event list, sort and save the results.
"""
from sunpy.net import Fido
from sunpy.net import attrs as a

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

    fname = f"querying_the_GOES_event_list.{year}"
    print(f"Writing {fname}." + "{csv, pkl}")
    df.to_csv("{fname}.csv", index=False)
    df.to_pickle(f"{fname}.pkl")
