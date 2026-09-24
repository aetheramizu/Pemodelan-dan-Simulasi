# LAPORAN PROYEK MONTE CARLO SIMULATION

## Mata Kuliah: Pemodelan dan Simulasi

---

# 1. PENDAHULUAN

## 1.1 Latar Belakang

Monte Carlo Simulation merupakan metode komputasi yang menggunakan proses pengambilan sampel secara acak dan dilakukan berulang kali untuk mempelajari perilaku suatu sistem yang memiliki ketidakpastian. Metode ini sesuai digunakan ketika sebuah permasalahan tidak cukup direpresentasikan oleh satu nilai pasti, tetapi lebih tepat dijelaskan melalui sekumpulan kemungkinan hasil.

Berdasarkan modul tugas, proyek Monte Carlo bertujuan menerapkan simulasi Monte Carlo untuk menyelesaikan permasalahan nyata serta mengeksplorasi konsep randomness, probability, dan statistical analysis melalui coding dan teknik komputasi. Modul juga mensyaratkan adanya kode dan laporan yang memuat problem statement, methodology, results termasuk visualisasi, analysis/discussion, dan conclusion. fileciteturn0file1L2-L15

Pada proyek ini dibahas dua problem yang diberikan dalam konteks tugas:

1. **Problem 3 — Risk Analysis for Project Management**
2. **Problem 5 — Monte Carlo Simulation for Investment Portfolio Optimization**

Kedua permasalahan tersebut memiliki unsur ketidakpastian. Pada manajemen proyek, ketidakpastian berasal dari variasi durasi aktivitas. Pada portfolio, ketidakpastian berasal dari return dan risiko aset.

## 1.2 Tujuan

Tujuan umum proyek adalah menerapkan Monte Carlo Simulation pada dua skenario yang berbeda dan menganalisis hasilnya secara statistik.

Tujuan Problem 3:

- membangun model probabilistik untuk durasi aktivitas proyek;
- menjalankan simulasi dengan 10.000, 100.000, dan 1.000.000 trial;
- memperoleh distribusi total durasi proyek;
- menghitung mean, median, standard deviation, dan percentile;
- menghitung peluang proyek selesai sebelum deadline;
- menganalisis risiko schedule overrun.

Tujuan Problem 5:

- membangun portfolio yang terdiri dari beberapa kelas aset;
- mendefinisikan expected return, volatility, dan correlation;
- menghasilkan banyak kemungkinan alokasi portfolio;
- menghitung expected return dan risiko menggunakan covariance matrix;
- menghitung Sharpe Ratio;
- memilih portfolio berdasarkan kriteria matematis;
- mensimulasikan kemungkinan return portfolio selama satu tahun.

---

# 2. PROBLEM 3 — RISK ANALYSIS FOR PROJECT MANAGEMENT

## 2.1 Problem Statement

Dalam proyek pengembangan perangkat lunak, durasi setiap aktivitas tidak dapat diketahui secara pasti. Estimasi dapat berbeda dari realisasi karena kompleksitas pekerjaan, revisi, kendala teknis, dan faktor lainnya.

Skenario proyek terdiri atas enam aktivitas:

1. Analisis Kebutuhan
2. Desain UI/UX
3. Pengembangan Frontend
4. Pengembangan Backend
5. Integrasi & Pengujian
6. Deployment

Monte Carlo Simulation digunakan untuk menghasilkan banyak kemungkinan durasi proyek dan memperkirakan peluang proyek selesai sebelum deadline.

Deadline proyek ditetapkan sebesar **45 hari kerja**.

Requirement resmi Problem 3 meminta model distribusi probabilitas untuk setiap task, simulasi dengan jumlah trial berbeda, serta visualisasi distribusi total durasi dan probabilitas memenuhi deadline. fileciteturn0file1L34-L44

## 2.2 Tujuan Simulasi

Simulasi bertujuan:

1. mengetahui distribusi total durasi proyek;
2. mengetahui durasi rata-rata dan median;
3. mengukur variasi durasi;
4. mengetahui P5, P50, P90, dan P95;
5. menghitung probabilitas on-time;
6. menghitung probabilitas schedule overrun;
7. membandingkan kestabilan hasil pada jumlah trial yang berbeda.

## 2.3 Asumsi Model

Asumsi yang digunakan:

- seluruh aktivitas dianggap berjalan secara berurutan;
- durasi antaraktivitas dianggap independen;
- parameter mean dan standard deviation merupakan asumsi akademik;
- durasi mengikuti normal distribution yang dibatasi pada nol;
- tidak ada scope change;
- tidak ada rework;
- tidak ada resource constraint;
- tidak ada dependency tambahan di luar urutan task.

Asumsi ini diperlukan karena modul hanya memberikan bentuk umum model dan tidak memberikan dataset proyek aktual.

## 2.4 Dataset / Input Data

| Aktivitas | Mean (hari) | SD (hari) | Distribusi |
|---|---:|---:|---|
| Analisis Kebutuhan | 5 | 1.0 | Normal truncated |
| Desain UI/UX | 6 | 1.2 | Normal truncated |
| Pengembangan Frontend | 12 | 2.0 | Normal truncated |
| Pengembangan Backend | 10 | 2.0 | Normal truncated |
| Integrasi & Pengujian | 6 | 1.5 | Normal truncated |
| Deployment | 2 | 0.5 | Normal truncated |

### Alasan pemilihan distribusi

Modul memperbolehkan penggunaan probability distribution seperti normal distribution dengan mean dan standard deviation. fileciteturn0file1L39-L40

Normal distribution dipilih karena sesuai untuk model sederhana yang berpusat pada nilai estimasi dengan variasi tertentu.

Namun, normal distribution standar memungkinkan nilai negatif. Karena durasi pekerjaan tidak mungkin negatif, digunakan **truncated normal distribution dengan batas bawah 0**. Dengan demikian, setiap sampel tetap memiliki karakteristik berbasis normal tetapi tidak menghasilkan durasi negatif.

## 2.5 Metodologi Monte Carlo

Pada setiap trial:

1. Durasi Analisis Kebutuhan diambil secara acak.
2. Durasi Desain UI/UX diambil secara acak.
3. Durasi Frontend diambil secara acak.
4. Durasi Backend diambil secara acak.
5. Durasi Integrasi & Pengujian diambil secara acak.
6. Durasi Deployment diambil secara acak.
7. Seluruh durasi dijumlahkan.

Model total durasi:

**T = T₁ + T₂ + T₃ + T₄ + T₅ + T₆**

Proses tersebut dilakukan untuk:

- 10.000 simulasi;
- 100.000 simulasi;
- 1.000.000 simulasi.

## 2.6 Rumus

Probabilitas selesai tepat waktu:

**P(On Time) ≈ jumlah simulasi dengan T ≤ deadline / jumlah seluruh simulasi**

Probabilitas overrun:

**P(Overrun) = 1 − P(On Time)**

Oleh karena itu:

**P(On Time) + P(Overrun) ≈ 1**

Percentile digunakan untuk melihat bagian tertentu dari distribusi durasi. P90, misalnya, menunjukkan nilai durasi yang mencakup sekitar 90% hasil simulasi di bawah atau sama dengan nilai tersebut.

## 2.7 Implementasi

Implementasi menggunakan:

- **NumPy** untuk operasi numerik dan vectorization;
- **Pandas** untuk pengolahan data dan statistik;
- **Matplotlib** untuk grafik;
- **SciPy** untuk truncated normal distribution.

Kode dibagi ke dalam beberapa function sehingga lebih mudah dibaca dan diuji. Simulasi juga dibuat vectorized agar 1.000.000 trial dapat diproses secara efisien.

## 2.8 Hasil Simulasi

| Jumlah Trial | Mean | Median | SD | Minimum | Maximum | P5 | P50 | P90 | P95 | P(On Time) | P(Overrun) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10,000 | 41.021 | 41.018 | 3.617 | 24.075 | 54.444 | 35.060 | 41.018 | 45.621 | 46.972 | 86.41% | 13.59% |
| 100,000 | 40.988 | 40.968 | 3.600 | 24.866 | 57.882 | 35.076 | 40.968 | 45.595 | 46.905 | 86.71% | 13.29% |
| 1,000,000 | 40.999 | 41.000 | 3.599 | 21.113 | 57.921 | 35.078 | 41.000 | 45.613 | 46.913 | 86.67% | 13.33% |

Hasil final menggunakan **1.000.000 simulasi**:

- Mean = **40.999 hari**
- Median = **41.000 hari**
- Standard deviation = **3.599 hari**
- Minimum = **21.113 hari**
- Maximum = **57.921 hari**
- P5 = **35.078 hari**
- P50 = **41.000 hari**
- P90 = **45.613 hari**
- P95 = **46.913 hari**
- P(On Time) = **86.67%**
- P(Overrun) = **13.33%**

Validasi probabilitas:

**0.8667 + 0.1333 = 1.0000**

Hasil tersebut konsisten dengan total probabilitas 1.

## 2.9 Analisis Histogram

Histogram memperlihatkan distribusi kemungkinan total durasi proyek.

Sebagian besar hasil simulasi terkonsentrasi di sekitar 41 hari. Akan tetapi, terdapat bagian distribusi yang melewati deadline 45 hari.

Garis deadline pada histogram membantu menunjukkan bahwa proyek dengan durasi rata-rata sekitar 41 hari tetap mempunyai kemungkinan mengalami keterlambatan.

Dengan demikian, mean tidak cukup untuk menggambarkan seluruh risiko jadwal.

## 2.10 Analisis CDF

Empirical CDF menggambarkan probabilitas kumulatif:

**P(T ≤ t)**

Pada titik 45 hari, nilai CDF memberikan estimasi probabilitas proyek selesai sebelum atau tepat pada deadline.

CDF juga membantu menentukan durasi yang diperlukan untuk tingkat probabilitas tertentu. Ini menjadikan CDF relevan untuk schedule risk analysis.

## 2.11 Analisis Percentile

P90 hasil simulasi adalah sekitar **45.61 hari**.

Artinya, sekitar 90% hasil simulasi memiliki durasi tidak lebih dari nilai tersebut, sedangkan sekitar 10% hasil memiliki durasi lebih besar.

P95 adalah sekitar **46.91 hari**, yang memberikan gambaran lebih konservatif terhadap schedule risk.

Karena P90 dan P95 berada di sekitar atau di atas deadline 45 hari, penggunaan mean saja dapat membuat risiko tail distribution terlihat lebih kecil daripada kondisi yang ditunjukkan oleh simulasi.

## 2.12 Analisis Jumlah Trial

Perbandingan 10.000, 100.000, dan 1.000.000 trial menghasilkan statistik yang relatif stabil.

Hal ini menunjukkan bahwa estimasi Monte Carlo mengalami convergence ketika jumlah trial bertambah.

Namun, trial yang lebih besar membutuhkan lebih banyak sumber daya komputasi. Karena itu, penggunaan NumPy vectorization menjadi penting untuk menjaga efisiensi.

## 2.13 Discussion

Berdasarkan hasil simulasi, estimasi rata-rata durasi proyek adalah sekitar 41 hari, sedangkan deadline ditetapkan 45 hari.

Meskipun mean berada di bawah deadline, probabilitas schedule overrun tetap sebesar **13.33%**.

Hal tersebut memperlihatkan manfaat Monte Carlo dibandingkan estimasi deterministik. Estimasi deterministik hanya memberikan satu angka, sedangkan Monte Carlo menghasilkan distribusi kemungkinan dan probabilitas.

## 2.14 Limitations

Beberapa keterbatasan model:

1. Task dianggap independen.
2. Task dianggap sequential.
3. Tidak ada resource constraint.
4. Tidak ada rework.
5. Tidak ada perubahan scope.
6. Parameter bukan berasal dari proyek nyata.
7. Truncated normal merupakan pilihan pemodelan, bukan satu-satunya distribusi yang mungkin digunakan.

Dalam proyek nyata, distribusi PERT/beta, lognormal, triangular, atau distribusi empiris dapat dipertimbangkan apabila tersedia data historis yang memadai.

## 2.15 Potential Improvement / Extension

Sebagai extension untuk aspek creativity, simulasi dapat dikembangkan menjadi **deadline sensitivity analysis**.

Beberapa deadline dapat diuji, misalnya:

- 40 hari;
- 42 hari;
- 45 hari;
- 47 hari;
- 50 hari.

Kemudian probabilitas on-time dibandingkan untuk setiap deadline. Dengan demikian, hasil dapat ditampilkan sebagai schedule-risk curve.

## 2.16 Kesimpulan Problem 3

Monte Carlo Simulation berhasil digunakan untuk memodelkan ketidakpastian durasi proyek.

Hasil 1.000.000 trial menunjukkan mean sekitar **41 hari** dan probability schedule overrun sekitar **13.33%** terhadap deadline 45 hari.

P90 dan P95 memberikan informasi tambahan mengenai upper-tail risk. Dengan demikian, Monte Carlo dapat memberikan gambaran risiko jadwal yang lebih lengkap dibandingkan hanya menggunakan estimasi rata-rata.

---

# 3. PROBLEM 5 — MONTE CARLO SIMULATION UNTUK OPTIMASI PORTOFOLIO INVESTASI

## 3.1 Problem Statement

Sebuah portfolio terdiri dari beberapa jenis aset. Setiap aset memiliki expected return, volatility, dan hubungan korelasi dengan aset lainnya.

Tujuan simulasi adalah menghasilkan banyak kemungkinan portfolio allocation, menghitung return dan risiko masing-masing, kemudian membandingkannya berdasarkan kriteria matematis.

Modul Problem 5 secara khusus meminta portfolio dengan beberapa aset, parameter mean return, volatility, dan correlation, simulasi future return, distribusi portfolio return, serta visualisasi risk-return trade-off. fileciteturn0file1L54-L65

## 3.2 Tujuan Simulasi

Simulasi bertujuan:

1. membuat 10.000 portfolio acak;
2. memastikan bobot setiap portfolio berjumlah 100%;
3. menghitung expected return;
4. menghitung covariance-based risk;
5. menghitung Sharpe Ratio;
6. mencari portfolio dengan Sharpe Ratio maksimum;
7. mencari portfolio dengan volatilitas minimum;
8. mencari portfolio dengan target return minimal 9% dan risiko minimum;
9. mensimulasikan 100.000 kemungkinan return satu tahun.

## 3.3 Dataset / Parameter

Data yang digunakan adalah **data sintetis untuk tujuan akademik**.

Data tersebut **bukan data historis aktual**.

| Aset | Expected Return | Volatility |
|---|---:|---:|
| Saham A | 12% | 20% |
| Saham B | 9% | 15% |
| Obligasi | 5% | 7% |
| Emas | 7% | 12% |

Correlation matrix:

| | Saham A | Saham B | Obligasi | Emas |
|---|---:|---:|---:|---:|
| Saham A | 1.00 | 0.55 | 0.10 | 0.20 |
| Saham B | 0.55 | 1.00 | 0.05 | 0.15 |
| Obligasi | 0.10 | 0.05 | 1.00 | 0.25 |
| Emas | 0.20 | 0.15 | 0.25 | 1.00 |

## 3.4 Alasan Menggunakan Data Sintetis

Modul menyebutkan historical data sebagai salah satu input Problem 5. Namun, pada proyek ini tidak dilakukan pengambilan dataset pasar historis dari sumber eksternal.

Oleh karena itu, parameter ditetapkan sebagai **synthetic academic data**.

Hal ini penting agar hasil tidak secara keliru disebut sebagai historical market result.

Jika penelitian dilanjutkan, parameter dapat diganti dengan data historis yang benar-benar diperoleh dari sumber valid, disertai sumber, periode, metode return calculation, volatility, correlation, dan covariance.

## 3.5 Asumsi

Model menggunakan asumsi:

- portfolio bersifat long-only;
- tidak ada short selling;
- seluruh bobot non-negatif;
- jumlah bobot = 1;
- expected return tahunan konstan;
- volatility tahunan konstan;
- correlation konstan;
- tidak ada biaya transaksi;
- tidak ada pajak;
- tidak ada liquidity constraint;
- return satu tahun dimodelkan menggunakan normal distribution;
- model hanya digunakan untuk tujuan akademik.

## 3.6 Covariance Matrix

Covariance antara aset i dan j dihitung dengan:

**Σᵢⱼ = σᵢ × σⱼ × ρᵢⱼ**

dengan:

- σ = volatility;
- ρ = correlation;
- Σ = covariance matrix.

Penggunaan covariance matrix sangat penting karena risiko portfolio dipengaruhi oleh hubungan antar aset.

## 3.7 Random Portfolio Allocation

Sebanyak **10.000 portfolio** dibuat menggunakan Dirichlet distribution.

Keuntungan metode ini:

- setiap bobot bernilai ≥ 0;
- total bobot = 1;
- seluruh portfolio memenuhi constraint long-only.

## 3.8 Expected Portfolio Return

Rumus:

**E(Rp) = wᵀμ**

dengan:

- w = vector bobot;
- μ = vector expected return.

## 3.9 Portfolio Volatility

Rumus portfolio variance:

**σp² = wᵀΣw**

Kemudian:

**σp = √(wᵀΣw)**

Formula ini memenuhi requirement bahwa portfolio risk harus dihitung menggunakan covariance matrix dan bukan weighted-average volatility.

## 3.10 Sharpe Ratio

Sharpe Ratio:

**Sharpe = (E(Rp) − Rf) / σp**

Risk-free rate yang digunakan adalah **4% per tahun** sebagai asumsi akademik.

## 3.11 Kriteria Optimasi

Tiga kriteria digunakan:

### A. Maximum Sharpe Ratio

Portfolio dengan nilai Sharpe Ratio terbesar dari 10.000 portfolio.

### B. Minimum Volatility

Portfolio dengan volatility paling rendah.

### C. Target Return dengan Risiko Minimum

Di antara portfolio dengan expected return minimal 9%, dipilih portfolio dengan volatility paling rendah.

Kriteria ini membuat proses pemilihan portfolio dapat dijelaskan secara matematis.

## 3.12 Hasil Simulasi Portfolio

| Kriteria | Expected Return | Volatilitas | Sharpe | Saham A | Saham B | Obligasi | Emas |
|---|---:|---:|---:|---:|---:|---:|---:|
| Maximum Sharpe | 8.52% | 9.85% | 0.4590 | 30.58% | 21.29% | 21.66% | 26.47% |
| Minimum Volatility | 5.80% | 6.25% | 0.2873 | 0.30% | 11.93% | 72.89% | 14.88% |
| Target Return / Min Risk | 9.00% | 10.97% | 0.4561 | 31.24% | 28.64% | 6.71% | 33.42% |

Untuk portfolio Maximum Sharpe:

- Expected Return = **8.52%**
- Volatility = **9.85%**
- Sharpe Ratio = **0.4590**

Total bobot portfolio:

**1.000000**

Nilai tersebut menunjukkan constraint 100% terpenuhi.

## 3.13 Simulasi Return Satu Tahun

Portfolio Maximum Sharpe digunakan untuk simulasi future performance selama satu tahun sebanyak **100.000 trial**.

Hasil:

- Mean return = **8.49%**
- Median = **8.51%**
- Standard deviation = **9.85%**
- P5 = **-7.74%**
- P95 = **24.68%**
- Probabilitas return negatif = **19.49%**

Distribusi ini memperlihatkan bahwa expected return positif tidak berarti seluruh kemungkinan outcome akan positif.

## 3.14 Analisis Risk-Return Scatter

Scatter plot menampilkan 10.000 portfolio.

- Sumbu X = volatility sebagai ukuran risiko.
- Sumbu Y = expected return.
- Warna merepresentasikan Sharpe Ratio.

Portfolio yang berada lebih tinggi memiliki expected return yang lebih besar, sedangkan portfolio yang berada lebih kanan memiliki volatility lebih tinggi.

Maximum Sharpe portfolio ditandai sebagai portfolio yang memiliki return relatif terhadap risiko paling tinggi berdasarkan kriteria Sharpe yang digunakan.

## 3.15 Approximate Efficient Frontier

Efficient frontier dibuat secara aproksimasi.

Rentang expected return dibagi menjadi beberapa interval. Pada setiap interval dipilih portfolio dengan volatility paling rendah.

Hasil tersebut kemudian dihubungkan untuk menghasilkan approximate efficient frontier.

Karena portfolio dihasilkan secara random, frontier ini bukan solusi optimasi analitis eksak. Ia merupakan frontier berdasarkan sample portfolio yang berhasil dihasilkan oleh Monte Carlo.

## 3.16 Analisis Alokasi

Portfolio hasil simulasi menunjukkan bahwa kombinasi beberapa aset dapat menghasilkan karakteristik risiko-return yang berbeda.

Diversifikasi menjadi penting karena correlation antar aset tidak semuanya sama dengan 1.

Ketika aset mempunyai correlation yang lebih rendah, perubahan salah satu aset tidak selalu diikuti perubahan yang sama besar pada aset lainnya. Hal tersebut dapat membantu mengurangi portfolio risk dibandingkan pendekatan yang hanya menggunakan satu aset.

## 3.17 Discussion

Monte Carlo Simulation memungkinkan eksplorasi ruang portfolio secara efisien.

Daripada menghitung satu allocation saja, 10.000 allocation dievaluasi. Setiap allocation kemudian dibandingkan berdasarkan expected return, covariance-based volatility, dan Sharpe Ratio.

Dengan pendekatan ini, istilah "optimal" tidak digunakan secara subjektif. Portfolio Maximum Sharpe dipilih berdasarkan kriteria matematis yang eksplisit.

## 3.18 Limitations

Model memiliki beberapa keterbatasan:

1. Data bersifat sintetis.
2. Tidak menggunakan historical market data.
3. Expected return dianggap konstan.
4. Volatility dianggap konstan.
5. Correlation dianggap konstan.
6. Normal distribution mungkin tidak menggambarkan seluruh karakteristik return nyata.
7. Return pasar dapat memiliki skewness dan fat tails.
8. Hanya 10.000 allocation yang dicoba.
9. Maximum Sharpe merupakan hasil terbaik dari sample, bukan jaminan global optimum.
10. Transaction cost, tax, liquidity, drawdown, dan rebalancing belum dimodelkan.

## 3.19 Potential Improvement / Extension

Beberapa extension yang dapat dikembangkan:

### A. Perbandingan Strategi

Bandingkan:

- Equal Weight;
- Minimum Volatility;
- Maximum Sharpe;
- Target Return Portfolio.

### B. Sensitivity Analysis

Ubah expected return dan volatility kemudian amati perubahan allocation.

### C. Historical Data

Pada penelitian lanjutan, synthetic parameter dapat diganti dengan historical data yang valid. Data harus disertai sumber, periode, metode return calculation, volatility, correlation, dan covariance.

## 3.20 Kesimpulan Problem 5

Monte Carlo Simulation berhasil digunakan untuk menghasilkan dan mengevaluasi 10.000 kemungkinan portfolio.

Berdasarkan kriteria Maximum Sharpe Ratio, portfolio yang terpilih memiliki expected return sekitar **8.52%**, volatility sekitar **9.85%**, dan Sharpe Ratio sekitar **0.4590**.

Simulasi 100.000 kemungkinan return satu tahun menunjukkan distribusi hasil yang tidak hanya terdiri dari outcome positif. Hal ini memperlihatkan bahwa portfolio dengan expected return positif tetap mempunyai ketidakpastian dan risiko.

Hasil tersebut digunakan hanya untuk memahami konsep Monte Carlo Simulation dan portfolio optimization secara akademik, bukan sebagai rekomendasi investasi.

---

# 4. VALIDATION DAN CORRECTNESS CHECK

## 4.1 Problem 3

- [x] Probability distribution digunakan.
- [x] Durasi negatif dicegah.
- [x] 10.000 trial.
- [x] 100.000 trial.
- [x] 1.000.000 trial.
- [x] Mean.
- [x] Median.
- [x] Standard deviation.
- [x] Minimum.
- [x] Maximum.
- [x] P5.
- [x] P50.
- [x] P90.
- [x] P95.
- [x] Probability on-time.
- [x] Probability overrun.
- [x] P(On Time) + P(Overrun) ≈ 1.
- [x] Histogram.
- [x] Deadline reference.
- [x] Empirical CDF.
- [x] Perbandingan jumlah trial.

## 4.2 Problem 5

- [x] Multiple assets.
- [x] Expected return.
- [x] Volatility.
- [x] Correlation.
- [x] Covariance matrix.
- [x] 10.000 portfolio simulations.
- [x] Bobot non-negatif.
- [x] Total bobot = 1.
- [x] Portfolio expected return.
- [x] Covariance-based portfolio volatility.
- [x] Sharpe Ratio.
- [x] 100.000 future-return simulations.
- [x] Risk-return scatter.
- [x] Approximate efficient frontier.
- [x] Return distribution.
- [x] Allocation chart.
- [x] Mathematical optimization criteria.

---

# 5. ASPEK CORRECTNESS, EFFICIENCY, CLARITY, DAN CREATIVITY

## 5.1 Correctness

Formula yang digunakan mengikuti model Monte Carlo yang dijelaskan pada tugas. Probability calculation pada Problem 3 telah divalidasi, sedangkan portfolio risk pada Problem 5 dihitung menggunakan covariance matrix.

## 5.2 Efficiency

Untuk jumlah simulasi besar, implementasi menggunakan NumPy vectorization sehingga operasi dilakukan terhadap array secara langsung.

Hal ini lebih efisien dibandingkan menjalankan loop Python untuk setiap trial.

## 5.3 Clarity

Kode dibuat modular menggunakan beberapa function dan komentar. Struktur tersebut memudahkan proses pembacaan, pengujian, dan modifikasi.

## 5.4 Creativity

Beberapa fitur tambahan dikembangkan tanpa mengubah requirement utama:

- perbandingan 10K, 100K, dan 1M trial;
- P90/P95 schedule risk;
- empirical CDF;
- approximate efficient frontier;
- tiga kriteria pemilihan portfolio;
- simulasi future return 100.000 trial.

---

# 6. KESIMPULAN UMUM

Kedua eksperimen menunjukkan penerapan konsep utama Monte Carlo Simulation, yaitu merepresentasikan ketidakpastian menggunakan probability distribution, melakukan random sampling dalam jumlah besar, kemudian menganalisis distribusi hasil yang diperoleh.

Pada **Problem 3**, Monte Carlo digunakan untuk memodelkan ketidakpastian durasi proyek. Dengan 1.000.000 simulasi, rata-rata durasi sekitar **41.00 hari** dan probabilitas schedule overrun terhadap deadline 45 hari sebesar **13.33%**. P90 dan P95 memberikan informasi tambahan mengenai kemungkinan durasi pada bagian upper tail.

Pada **Problem 5**, Monte Carlo digunakan untuk mengeksplorasi 10.000 kombinasi allocation portfolio. Setiap portfolio dievaluasi berdasarkan expected return, covariance-based volatility, dan Sharpe Ratio. Portfolio kemudian dapat dibandingkan berdasarkan kriteria matematis seperti Maximum Sharpe, Minimum Volatility, dan Minimum Risk pada target return tertentu.

Secara keseluruhan, Monte Carlo Simulation memberikan cara untuk memahami sistem yang mengandung ketidakpastian secara lebih lengkap. Metode ini tidak hanya memberikan satu estimasi, tetapi menghasilkan distribusi kemungkinan yang dapat digunakan untuk menghitung probability, percentile, risk, dan berbagai ukuran statistik lainnya.

Dengan demikian, proyek ini menunjukkan bahwa Monte Carlo Simulation dapat diterapkan pada permasalahan yang berbeda, mulai dari manajemen proyek hingga analisis portfolio, dengan prinsip yang sama: **membangun model ketidakpastian, melakukan sampling berulang, dan menganalisis distribusi hasil.**
