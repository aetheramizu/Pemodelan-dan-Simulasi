# ============================================================
# PROBLEM 5 - OPTIMASI PORTOFOLIO INVESTASI
# Monte Carlo Simulation
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Seed tetap agar hasil simulasi dapat direproduksi.
SEED = 20260922

# Jumlah portfolio acak yang akan dievaluasi.
N_PORTFOLIOS = 10_000

# Jumlah simulasi return satu tahun.
N_RETURN_SIMULATIONS = 100_000

# Tingkat bebas risiko untuk perhitungan Sharpe Ratio.
# Nilai ini merupakan asumsi akademik, bukan data pasar aktual.
RISK_FREE_RATE = 0.04

# Target return untuk kriteria "return minimal dengan risiko terendah".
TARGET_RETURN = 0.09

ASSETS = ["Saham A", "Saham B", "Obligasi", "Emas"]

# ============================================================
# DATA SINTETIS UNTUK TUJUAN AKADEMIK
# ============================================================
# Data berikut merupakan parameter contoh.
# Jangan menganggapnya sebagai data historis pasar aktual.
EXPECTED_RETURN = np.array([0.12, 0.09, 0.05, 0.07])
VOLATILITY = np.array([0.20, 0.15, 0.07, 0.12])

# Matriks korelasi antar aset.
CORRELATION = np.array([
    [1.00, 0.55, 0.10, 0.20],
    [0.55, 1.00, 0.05, 0.15],
    [0.10, 0.05, 1.00, 0.25],
    [0.20, 0.15, 0.25, 1.00],
])

# Covariance = volatility_i * volatility_j * correlation_ij
COVARIANCE = np.outer(VOLATILITY, VOLATILITY) * CORRELATION


def generate_random_weights(n_portfolios, n_assets, rng):
    """
    Membuat bobot portfolio secara acak.

    Distribusi Dirichlet digunakan karena:
    1. Semua bobot >= 0
    2. Jumlah bobot setiap portfolio = 1
    """
    return rng.dirichlet(
        np.ones(n_assets),
        size=n_portfolios
    )


def evaluate_portfolios(weights):
    """
    Menghitung return ekspektasian, volatilitas,
    dan Sharpe Ratio untuk seluruh portfolio.
    """

    # E(Rp) = w^T * mu
    portfolio_return = weights @ EXPECTED_RETURN

    # Var(Rp) = w^T * Sigma * w
    portfolio_variance = np.einsum(
        "ij,jk,ik->i",
        weights,
        COVARIANCE,
        weights
    )

    # Sigma_p = sqrt(Var(Rp))
    portfolio_volatility = np.sqrt(portfolio_variance)

    # Sharpe = (Rp - Rf) / Sigma_p
    sharpe_ratio = (
        portfolio_return - RISK_FREE_RATE
    ) / portfolio_volatility

    return (
        portfolio_return,
        portfolio_volatility,
        sharpe_ratio
    )


def simulate_one_year_returns(
    portfolio_weight,
    n_simulations,
    seed=SEED
):
    """
    Mensimulasikan return portfolio selama satu tahun.
    """
    rng = np.random.default_rng(seed)

    portfolio_mean = (
        portfolio_weight @ EXPECTED_RETURN
    )

    portfolio_variance = (
        portfolio_weight
        @ COVARIANCE
        @ portfolio_weight
    )

    portfolio_std = np.sqrt(portfolio_variance)

    return rng.normal(
        portfolio_mean,
        portfolio_std,
        n_simulations
    )


def main():
    rng = np.random.default_rng(SEED)

    # --------------------------------------------------------
    # 1. Generate 10.000 portfolio acak
    # --------------------------------------------------------
    weights = generate_random_weights(
        N_PORTFOLIOS,
        len(ASSETS),
        rng
    )

    # --------------------------------------------------------
    # 2. Evaluasi seluruh portfolio
    # --------------------------------------------------------
    returns, risks, sharpes = evaluate_portfolios(weights)

    # --------------------------------------------------------
    # 3. Tentukan portfolio berdasarkan kriteria matematis
    # --------------------------------------------------------

    # Kriteria 1: Sharpe Ratio maksimum
    index_max_sharpe = np.argmax(sharpes)

    # Kriteria 2: Volatilitas minimum
    index_min_volatility = np.argmin(risks)

    # Kriteria 3: Return >= target dengan risiko minimum
    feasible = np.where(
        returns >= TARGET_RETURN
    )[0]

    index_target = feasible[
        np.argmin(risks[feasible])
    ]

    print("\n=== PORTOFOLIO SHARPE MAKSIMUM ===")
    print(
        dict(
            zip(
                ASSETS,
                weights[index_max_sharpe]
            )
        )
    )

    print(
        "Expected Return:",
        f"{returns[index_max_sharpe]:.2%}"
    )

    print(
        "Volatilitas:",
        f"{risks[index_max_sharpe]:.2%}"
    )

    print(
        "Sharpe Ratio:",
        f"{sharpes[index_max_sharpe]:.4f}"
    )

    # --------------------------------------------------------
    # Visualisasi 1: Risk-Return Scatter
    # --------------------------------------------------------
    plt.figure(figsize=(10, 6))

    plt.scatter(
        risks,
        returns,
        c=sharpes,
        s=10,
        alpha=0.35
    )

    plt.scatter(
        risks[index_max_sharpe],
        returns[index_max_sharpe],
        s=100,
        marker="*",
        label="Sharpe Ratio Maksimum"
    )

    plt.scatter(
        risks[index_min_volatility],
        returns[index_min_volatility],
        s=80,
        marker="X",
        label="Volatilitas Minimum"
    )

    plt.scatter(
        risks[index_target],
        returns[index_target],
        s=80,
        marker="D",
        label="Target Return / Risiko Minimum"
    )

    plt.xlabel("Volatilitas Tahunan (Risiko)")
    plt.ylabel("Expected Return Tahunan")
    plt.title("Ruang Risk-Return Portfolio")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "problem5_risk_return.png",
        dpi=200
    )
    plt.show()

    # --------------------------------------------------------
    # Visualisasi 2: Approximate Efficient Frontier
    # --------------------------------------------------------
    bins = np.linspace(
        returns.min(),
        returns.max(),
        30
    )

    frontier = []

    for lower, upper in zip(
        bins[:-1],
        bins[1:]
    ):
        index = np.where(
            (returns >= lower)
            & (returns < upper)
        )[0]

        if len(index):
            selected = index[
                np.argmin(risks[index])
            ]

            frontier.append(
                (
                    returns[selected],
                    risks[selected]
                )
            )

    frontier = np.array(frontier)

    plt.figure(figsize=(10, 6))

    plt.scatter(
        risks,
        returns,
        s=8,
        alpha=0.15,
        label="Portfolio Acak"
    )

    plt.plot(
        frontier[:, 1],
        frontier[:, 0],
        linewidth=2,
        label="Efficient Frontier Aproksimasi"
    )

    plt.scatter(
        risks[index_max_sharpe],
        returns[index_max_sharpe],
        s=100,
        marker="*",
        label="Sharpe Ratio Maksimum"
    )

    plt.xlabel("Volatilitas Tahunan (Risiko)")
    plt.ylabel("Expected Return Tahunan")
    plt.title("Efficient Frontier Aproksimasi")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "problem5_efficient_frontier.png",
        dpi=200
    )
    plt.show()

    # --------------------------------------------------------
    # 4. Simulasi return satu tahun
    # --------------------------------------------------------
    selected_weight = weights[index_max_sharpe]

    simulated_returns = simulate_one_year_returns(
        selected_weight,
        N_RETURN_SIMULATIONS
    )

    # --------------------------------------------------------
    # Visualisasi 3: Distribusi Return
    # --------------------------------------------------------
    plt.figure(figsize=(10, 6))

    plt.hist(
        simulated_returns,
        bins=70,
        density=True,
        alpha=0.75
    )

    plt.axvline(
        0,
        linestyle="--",
        label="Return 0%"
    )

    plt.axvline(
        simulated_returns.mean(),
        linestyle=":",
        linewidth=2,
        label=(
            f"Rata-rata simulasi = "
            f"{simulated_returns.mean():.2%}"
        )
    )

    plt.xlabel("Return Portfolio Satu Tahun")
    plt.ylabel("Kepadatan Probabilitas")
    plt.title(
        "Distribusi Return Satu Tahun "
        "Portfolio Sharpe Maksimum"
    )
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "problem5_return_distribution.png",
        dpi=200
    )
    plt.show()

    # --------------------------------------------------------
    # Visualisasi 4: Komposisi Portfolio
    # --------------------------------------------------------
    plt.figure(figsize=(9, 5))

    plt.bar(
        ASSETS,
        selected_weight
    )

    plt.xlabel("Aset")
    plt.ylabel("Bobot Portfolio")
    plt.title(
        "Alokasi Portfolio dengan Sharpe Ratio Maksimum"
    )

    plt.tight_layout()

    plt.savefig(
        "problem5_allocation.png",
        dpi=200
    )
    plt.show()


if __name__ == "__main__":
    main()
