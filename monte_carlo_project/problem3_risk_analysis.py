# ============================================================
# PROBLEM 3 - ANALISIS RISIKO PROYEK
# Monte Carlo Simulation
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Seed dibuat tetap agar hasil simulasi dapat direproduksi.
SEED = 20260922

# Batas waktu proyek dalam hari kerja.
DEADLINE = 45

# Parameter setiap aktivitas proyek.
# Mean = estimasi durasi rata-rata
# StdDev = ketidakpastian durasi
TASKS = pd.DataFrame({
    "Tugas": [
        "Analisis Kebutuhan",
        "Desain UI/UX",
        "Pengembangan Frontend",
        "Pengembangan Backend",
        "Integrasi & Pengujian",
        "Deployment"
    ],
    "Mean": [5, 6, 12, 10, 6, 2],
    "StdDev": [1.0, 1.2, 2.0, 2.0, 1.5, 0.5],
})


def sample_truncated_normal(mean, std, size, rng):
    """
    Menghasilkan sampel dari distribusi normal yang dibatasi
    agar durasi tidak pernah bernilai negatif.
    """
    lower = (0 - mean) / std

    return truncnorm.rvs(
        lower,
        np.inf,
        loc=mean,
        scale=std,
        size=size,
        random_state=rng
    )


def simulate_project(n_trials, seed=SEED):
    """
    Menjalankan simulasi Monte Carlo untuk total durasi proyek.

    Setiap trial menghasilkan satu durasi untuk setiap tugas,
    kemudian seluruh durasi tugas dijumlahkan.
    """
    rng = np.random.default_rng(seed)

    # Sampling seluruh tugas secara vectorized.
    task_samples = np.column_stack([
        sample_truncated_normal(
            row.Mean,
            row.StdDev,
            n_trials,
            rng
        )
        for row in TASKS.itertuples(index=False)
    ])

    # Total durasi = jumlah seluruh tugas.
    total_duration = task_samples.sum(axis=1)

    return total_duration


def summarize(total_duration, deadline=DEADLINE):
    """
    Menghitung statistik deskriptif dan probabilitas deadline.
    """
    s = pd.Series(total_duration)

    probability_on_time = (s <= deadline).mean()
    probability_overrun = 1 - probability_on_time

    return {
        "Rata-rata": s.mean(),
        "Median": s.median(),
        "Standar Deviasi": s.std(ddof=1),
        "Minimum": s.min(),
        "Maksimum": s.max(),
        "P5": s.quantile(0.05),
        "P50": s.quantile(0.50),
        "P90": s.quantile(0.90),
        "P95": s.quantile(0.95),
        "P(On Time)": probability_on_time,
        "P(Overrun)": probability_overrun
    }


def main():
    # Jumlah trial yang dibandingkan sesuai kebutuhan tugas.
    trial_counts = [10_000, 100_000, 1_000_000]

    results = []
    final_totals = None

    for n in trial_counts:
        totals = simulate_project(n)

        statistics = summarize(totals)

        results.append({
            "Jumlah Simulasi": n,
            **statistics
        })

        # Simulasi 1 juta trial digunakan sebagai hasil akhir.
        if n == 1_000_000:
            final_totals = totals

    results_df = pd.DataFrame(results)

    print("\n=== HASIL PERBANDINGAN JUMLAH SIMULASI ===")
    print(results_df.to_string(index=False))

    # --------------------------------------------------------
    # Visualisasi 1: Histogram Durasi Proyek
    # --------------------------------------------------------
    plt.figure(figsize=(10, 6))

    plt.hist(
        final_totals,
        bins=60,
        density=True,
        alpha=0.75
    )

    plt.axvline(
        DEADLINE,
        linestyle="--",
        linewidth=2,
        label=f"Batas waktu = {DEADLINE} hari"
    )

    plt.title("Distribusi Total Durasi Proyek")
    plt.xlabel("Total Durasi Proyek (hari kerja)")
    plt.ylabel("Kepadatan Probabilitas")
    plt.legend()
    plt.tight_layout()

    plt.savefig("problem3_histogram.png", dpi=200)
    plt.show()

    # --------------------------------------------------------
    # Visualisasi 2: Empirical CDF
    # --------------------------------------------------------
    sorted_duration = np.sort(final_totals)
    cumulative_probability = (
        np.arange(1, len(sorted_duration) + 1)
        / len(sorted_duration)
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        sorted_duration,
        cumulative_probability
    )

    plt.axvline(
        DEADLINE,
        linestyle="--",
        linewidth=2,
        label=f"Batas waktu = {DEADLINE} hari"
    )

    plt.title("CDF Empiris Total Durasi Proyek")
    plt.xlabel("Total Durasi Proyek (hari kerja)")
    plt.ylabel("Probabilitas Kumulatif")
    plt.legend()
    plt.tight_layout()

    plt.savefig("problem3_cdf.png", dpi=200)
    plt.show()

    # --------------------------------------------------------
    # Visualisasi 3: Pengaruh Jumlah Trial
    # --------------------------------------------------------
    plt.figure(figsize=(10, 6))

    plt.plot(
        results_df["Jumlah Simulasi"],
        results_df["Rata-rata"],
        marker="o",
        label="Rata-rata durasi"
    )

    plt.plot(
        results_df["Jumlah Simulasi"],
        results_df["P95"],
        marker="o",
        label="P95"
    )

    plt.axhline(
        DEADLINE,
        linestyle="--",
        linewidth=2,
        label=f"Batas waktu = {DEADLINE} hari"
    )

    plt.xscale("log")
    plt.title("Pengaruh Jumlah Simulasi terhadap Hasil")
    plt.xlabel("Jumlah Simulasi (skala logaritmik)")
    plt.ylabel("Durasi (hari kerja)")
    plt.legend()
    plt.tight_layout()

    plt.savefig("problem3_trial_comparison.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
