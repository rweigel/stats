"""Download and plot KIC 5812960 light curves from MAST.

Install the dependency with: python -m pip install lightkurve
Run with: python download_lc.py
"""

from pathlib import Path

import lightkurve as lk
import matplotlib.pyplot as plt


def main():
    target = "KIC 5812960"
    download_dir = Path(__file__).resolve().parent / "data" / "KIC_5812960"

    local_files = sorted(download_dir.rglob("kplr005812960-*_llc.fits"))
    if local_files:
        light_curves = [lk.read(filename, flux_column="pdcsap_flux") for filename in local_files]
    else:
        results = lk.search_lightcurve(
            target, mission="Kepler", author="Kepler", cadence="long"
        )
        if len(results) == 0:
            raise SystemExit(f"No Kepler long-cadence light curves found for {target}.")

        print(results)
        download_dir.mkdir(parents=True, exist_ok=True)
        light_curves = results.download_all(download_dir=str(download_dir))
        if light_curves is None or len(light_curves) != len(results):
            raise SystemExit("Some downloads failed. Run again to retry missing files.")

    figure, axis = plt.subplots(figsize=(12, 5))
    import numpy as np
    times = np.array([])
    data = np.array([])
    for light_curve in sorted(light_curves, key=lambda curve: curve.time[0].value):
        clean_curve = light_curve.remove_nans().normalize()
        time = clean_curve.time.value
        datum = clean_curve.flux.value
        times = np.concatenate((times, time))
        data = np.concatenate((data, datum))
        if True:
            # Compute and plot histogram of data
            # Compute and plot histogram of dt = np.diff(time)
            axis.scatter(
                clean_curve.time.value, clean_curve.flux.value,
                s=1, rasterized=True, label=f"Q{light_curve.meta['QUARTER']}",
            )
    plt.show()
    axis.scatter(times, data)
    # Compute and plot histogram of data
    # Compute and plot histogram of dt = np.diff(time)
    plt.show()
    axis.set(title=target, xlabel="Time (BKJD; BJD - 2454833)", ylabel="Normalized PDCSAP flux")
    axis.legend(ncol=9, fontsize=8, markerscale=4)
    figure.tight_layout()
    plot_path = download_dir / "KIC_5812960_light_curves.png"
    figure.savefig(plot_path, dpi=180)
    print(f"Plotted {len(light_curves)} light curves: {plot_path}")
    plt.show()


if __name__ == "__main__":
    main()