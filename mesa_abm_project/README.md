# Mesa ABM Project — Sugarscape with Traders

Presentasi interaktif (Bahasa Indonesia) dan naskah video untuk tugas mata kuliah **Pemodelan dan Simulasi**.

Materi: course Complexity Explorer *Agent-Based Models with Python: An Introduction to Mesa* (Santa Fe Institute), dengan fokus **Session 20 — Batch Runner**. Model yang dibahas adalah Sugarscape with Traders (G1MT): grid 50×50, dua kutub sumber daya (gula dan rempah), trader heterogen yang bergerak, makan, dan bertukar.

## Isi

| File | Keterangan |
|---|---|
| `index.html` | Presentasi 15 bagian, satu file, tanpa CDN dan tanpa internet |
| `video-script-final.md` | Naskah narasi ±20 menit: timestamp, narasi, dan visual cue per bagian |
| `sugarscape_g1mt.py` | Model akhir Session 20 (satu run, 1.000 step, seed tetap) |
| `export_results.py` | Menjalankan model + `mesa.batch_run`, lalu menyuntikkan hasil rekaman ke `index.html` |
| `sugar-map.txt` | Peta landscape 50×50 |
| `assets/` | Grafik hasil eksekusi notebook (PNG) yang dipakai di presentasi |
| `mesa-abm-course.md` | Catatan course, sumber istilah dan urutan sesi |
| `Mesa-ABM-Tutorial/` | Notebook resmi course, dipakai sebagai referensi kode per sesi |
| `D121241001_Mohamad Alief Nauval Mohi_Mesa ABM Video.pdf` | Dokumen pendukung tugas video |
| `requirements.txt` | Dependensi Python |

## Membuka presentasi

Klik dua kali `index.html`, atau drag ke browser. Tidak perlu server dan tidak perlu koneksi internet.

Presentasi berupa halaman scroll vertikal, bukan slide deck. Diagram, grafik, dan panel kode dirender dengan JavaScript dari data yang tertanam di file itu sendiri.

## Menjalankan model

Model hanya diuji di **Mesa 1.2.1**; `requirements.txt` membatasi `mesa>=1.2.1,<2.0.0`.

- Mesa 2.4.0 gagal dengan `KeyError` di `step()`, karena `DataCollector` versi itu memakai `model._steps`, bukan `schedule.steps`.
- Mesa 3.x tidak kompatibel karena `mesa.time` dan `mesa.space` sudah diubah.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python sugarscape_g1mt.py    # satu run, 1.000 step, seed 42
python export_results.py     # opsional: hitung ulang DATA di index.html (±4 menit)
```

Output yang diharapkan dari `sugarscape_g1mt.py` pada seed 42: populasi 200 → 64 trader (stabil sejak step 312), rata-rata harga 1,1068.

## Sumber angka

Semua angka di presentasi dan naskah berasal dari eksekusi Python, bukan karangan:

- **Single run** (seed 42): `sugarscape_g1mt.py` → 200 → 64 trader, volume step 1 = 781, rata-rata volume akhir 8,3, harga rata-rata 1,1068.
- **Batch 4 kombinasi** (`vision_min` ∈ {1,2} × `metabolism_max` ∈ {3,5}):

  | vision_min | metabolism_max | Trader | Harga rata-rata | Total volume |
  |---|---|---|---|---|
  | 1 | 3 | 145 | 0,9612 | 29.589 |
  | 1 | 5 | 64 | 1,1070 | 12.795 |
  | 2 | 3 | 155 | 0,9762 | 26.079 |
  | 2 | 5 | 71 | 1,1288 | 11.628 |

- **Metrik jaringan batch**: node connectivity 14, average clustering 0,6826, global efficiency 0,8045.

Grafik dan posisi trader di `index.html` adalah rekaman output Python (`DATA` blob), bukan simulasi ulang di JavaScript. Kalkulator trade di bagian mekanisme tukar adalah terjemahan rumus MRS/Cobb-Douglas untuk ilustrasi, bukan menjalankan model.

## Catatan metodologis

- **Graf batch bersifat agregat lintas-run.** Kode notebook (Cell 31) membangun graf dari `results_df` gabungan semua `RunId`, sementara `agent_id` dimulai ulang dari 0 pada setiap model. Akibatnya metrik 14 / 0,6826 / 0,8045 menggambarkan graf gabungan, bukan pasar satu run. Pembanding satu run (Cell 21): connectivity 0, clustering 0,3969, efficiency 0,4461.
- **Satu iterasi per kombinasi parameter.** Cukup untuk menunjukkan percabangan rezim, belum cukup untuk interval kepercayaan atau uji signifikansi. Replikasi Monte Carlo (30–50 seed per sel) adalah pekerjaan lanjutan.
- **Klaim variansi harga mengecil tidak terbukti pada seed 42**: simpangan baku 0,206 di 100 step pertama vs 0,2209 di 200 step terakhir.
- **Perubahan dari kode course** hanya yang diperlukan agar berjalan di luar Google Colab: path landscape lokal, `geometric_mean` yang aman untuk daftar kosong, `coord_iter()` sesuai Mesa 1.2.1, dan parameter `seed` agar run dapat diulang. Logika agent tidak diubah.
- Notebook sesi 3–19 tidak dijalankan ulang; di presentasi fungsinya sebagai tahap belajar, bukan hasil pengukuran.
