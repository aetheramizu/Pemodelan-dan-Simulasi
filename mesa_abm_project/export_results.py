"""
Run SugarscapeG1mt (seed=42) and the Session 20 batch run, then inject the
recorded output into index.html (replaces the `const DATA = ...;` line).

Usage: python export_results.py
"""
import json
import re
from pathlib import Path

import numpy as np
import mesa

from sugarscape_g1mt import SugarscapeG1mt, Trader

HERE = Path(__file__).parent
SEED = 42
STEPS = 1000
FRAME_STEPS = [0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]


def r(x, n=4):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), n)


def single_run():
    model = SugarscapeG1mt(seed=SEED)
    frames = []

    def snap(step):
        pos = [list(a.pos) for a in model.schedule.agents_by_type[Trader].values()]
        frames.append({"step": step, "pos": pos})

    snap(0)
    for s in range(1, STEPS + 1):
        model.step()
        if s in FRAME_STEPS:
            snap(s)

    df = model.datacollector.get_model_vars_dataframe()
    trader = [int(v) for v in df["Trader"]]
    volume = [int(v) for v in df["Trade Volume"]]
    price = [r(v) for v in df["Price"]]
    final = trader[-1]
    stable_from = next(i + 1 for i in range(len(trader)) if all(t == final for t in trader[i:]))
    p = df["Price"]
    meta = {
        "seed": SEED, "steps": STEPS, "initial_traders": model.initial_population,
        "final_traders": final, "stable_from": stable_from,
        "vol_step1": volume[0], "vol_late_mean": r(np.mean(volume[800:]), 1),
        "price_mean": r(p.dropna().mean()),
        "price_std_early": r(p.iloc[:100].std(ddof=0)),
        "price_std_late": r(p.iloc[800:].std(ddof=0)),
    }
    return {"meta": meta, "frames": frames,
            "series": {"trader": trader, "volume": volume, "price": price}}


def batch():
    params = {"width": 50, "height": 50, "vision_min": range(1, 3),
              "metabolism_max": [3, 5], "seed": SEED}
    import pandas as pd
    res = pd.DataFrame(mesa.batch_run(SugarscapeG1mt, parameters=params, iterations=1,
                                      number_processes=1, data_collection_period=1,
                                      display_progress=False))
    rows = []
    for _, g in res.groupby("RunId"):
        # agent reporters make batch_run emit one row per agent per step; keep one per step
        g = g.sort_values("Step").drop_duplicates("Step", keep="last")
        rows.append({"vision_min": int(g["vision_min"].iloc[0]),
                     "metabolism_max": int(g["metabolism_max"].iloc[0]),
                     "final_traders": int(g["Trader"].iloc[-1]),
                     "price_mean": r(g["Price"].dropna().mean()),
                     "total_volume": int(g["Trade Volume"].sum())})
    return rows


if __name__ == "__main__":
    sugar = np.genfromtxt(HERE / "sugar-map.txt").astype(int).tolist()
    data = {"sugar": sugar, **single_run(), "batch": batch()}
    html_path = HERE / "index.html"
    html = html_path.read_text(encoding="utf-8")
    blob = json.dumps(data, separators=(",", ":"))
    html, n = re.subn(r"^const DATA = .*;$", lambda m: "const DATA = " + blob + ";", html,
                      count=1, flags=re.M)
    assert n == 1, "DATA line not found in index.html"
    html_path.write_text(html, encoding="utf-8")
    print(json.dumps(data["meta"], indent=1))
    print(json.dumps(data["batch"], indent=1))
