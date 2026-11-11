# Pemodelan dan Simulasi

Repository ini berisi kumpulan tugas dan proyek mata kuliah **Pemodelan dan Simulasi**.

**Mohamad Alief Nauval Mohi** — D121241001

## Isi Repository

| Folder | Topik | Keterangan |
|---|---|---|
| [`mesa_abm_project/`](mesa_abm_project) | Agent-Based Modeling | Sugarscape with Traders memakai Python + Mesa, dengan fokus Session 20 (Batch Runner). Berisi presentasi interaktif, naskah video, model yang bisa dijalankan, dan hasil eksperimen parameter sweep. |
| [`monte_carlo_project/`](monte_carlo_project) | Simulasi Monte Carlo | Analisis risiko dan optimasi portofolio saham melalui simulasi Monte Carlo, lengkap dengan laporan, kode Python, dan visualisasi. |

## Menjalankan

Setiap folder punya `README.md` dan `requirements.txt` sendiri.

```bash
cd mesa_abm_project        # atau monte_carlo_project
pip install -r requirements.txt
```

- `mesa_abm_project` hanya kompatibel dengan **Mesa 1.2.1** (`mesa>=1.2.1,<2.0.0`). Presentasinya bisa dibuka langsung dengan klik `index.html` tanpa server.
- `monte_carlo_project` bisa dijalankan di Google Colab, Jupyter Notebook, atau Python lokal.

## Catatan

Seluruh kode dan angka di repository ini dihasilkan dari eksekusi sendiri, bukan salinan hasil orang lain. Data yang dipakai bersifat sintetis atau berasal dari materi course, dan hanya digunakan untuk keperluan akademik. Batasan metodologis tiap proyek dijelaskan di README masing-masing folder.
