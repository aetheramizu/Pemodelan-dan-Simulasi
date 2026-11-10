# Naskah Teleprompter
## Sugarscape with Traders — fokus Session 20: Batch Runner

Target durasi: sekitar 20 menit, bergantung pada tempo bicara dan jeda visual.

Catatan pemakaian: teks setelah label **NARASI** adalah bagian yang dibacakan. Baris **VISUAL** hanya panduan untuk presenter dan tidak dibacakan. Setiap paragraf dibuat pendek agar mudah diikuti saat scrolling teleprompter.

---

## 1. Pembuka — 00:00–00:40

VISUAL: Tampilkan halaman pembuka dan peta sugar.

NARASI

Selamat pagi. Pada presentasi ini, saya akan membahas Agent-Based Modeling menggunakan Python dan Mesa, dengan fokus pada Session 20 dari course Agent-Based Models with Python, yaitu Batch Runner.

Kita akan menggunakan model Sugarscape with Traders. Di dalam model ini, setiap trader bergerak, mengumpulkan sumber daya, memenuhi kebutuhan hidup, dan melakukan pertukaran dengan trader lain.

Pertanyaan yang ingin kita jawab bukan hanya bagaimana model ini berjalan. Kita juga ingin tahu: ketika parameternya berubah, apakah hasil simulasinya ikut berubah? Dan seberapa jauh kita bisa mempercayai pola yang terlihat dari hasil tersebut?

Itulah alasan kita beralih dari satu simulasi ke eksperimen menggunakan Batch Runner.

---

## 2. Peta pembahasan — 00:40–01:25

VISUAL: Tampilkan lima bagian utama presentasi.

NARASI

Saya akan mulai dengan konsep dasar Agent-Based Modeling, lalu menjelaskan bagian-bagian penting dari model Sugarscape with Traders.

Setelah itu, kita masuk ke inti presentasi: bagaimana Session 20 mengatur eksperimen, menjalankan beberapa kombinasi parameter, dan mengolah hasilnya menjadi data serta jaringan perdagangan.

Di bagian akhir, kita akan membandingkan empat hasil simulasi dan membahas apa yang bisa—dan belum bisa—disimpulkan dari data tersebut.

Jadi, sesi-sesi sebelumnya tetap menjadi fondasi, tetapi kita tidak akan membahasnya satu per satu. Kita akan mengambil konsep yang memang diperlukan untuk memahami eksperimen di Session 20.

---

## 3. Dasar ABM dan perjalanan course — 01:25–02:45

VISUAL: Tampilkan empat komponen ABM dan roadmap course.

NARASI

Agent-Based Modeling, atau ABM, adalah pendekatan untuk mempelajari sistem melalui perilaku individu dan interaksi di antara mereka.

Alih-alih menentukan hasil akhir sistem sejak awal, kita membuat lingkungan, menetapkan aturan bagi setiap agent, lalu menjalankan model dan mengamati pola yang muncul.

Dalam model ini, ada empat komponen yang perlu kita kenali. Pertama, environment, yaitu ruang tempat agent berada. Di sini, lingkungannya berupa grid berukuran 50 kali 50.

Kedua, autonomous agents. Agent utamanya adalah trader, dan setiap trader bisa memiliki vision, metabolism, serta cadangan sumber daya yang berbeda.

Ketiga, behavioral rules, yaitu aturan yang menentukan bagaimana trader bergerak, mengonsumsi sumber daya, dan melakukan barter.

Terakhir, measurement. Kita perlu mencatat apa yang terjadi selama simulasi supaya analisisnya didasarkan pada data, bukan hanya pengamatan visual.

Roadmap di samping merangkum bagaimana course membangun komponen-komponen ini secara bertahap. Sesi awal memperkenalkan Mesa dan lingkungan. Sesi berikutnya menambahkan trader, gerakan, konsumsi, dan kematian. Setelah itu, course mengembangkan mekanisme perdagangan dan pengukuran.

Pada Session 20, komponen-komponen tersebut sudah terintegrasi. Fokusnya beralih dari membangun model ke menguji bagaimana model berperilaku pada konfigurasi yang berbeda.

---

## 4. Arsitektur model — 02:45–04:00

VISUAL: Tampilkan diagram SugarscapeG1mt, lalu cuplikan kode inisialisasi.

NARASI

Model utama di sini adalah `SugarscapeG1mt`. Ada tiga bagian yang membantu kita memahami bagaimana model bekerja: scheduler, grid, dan DataCollector.

Scheduler mengatur urutan aktivasi agent. Pada implementasi ini, `RandomActivationByType` mengacak urutan aktivasi sesuai mekanisme scheduler yang digunakan.

Grid berukuran 50 kali 50 dan menggunakan `MultiGrid` dengan `torus=False`. Artinya, batas peta tidak tersambung ke sisi seberangnya. Grid juga memungkinkan lebih dari satu jenis agent berada pada sel yang sama, sesuai aturan model.

Bagian ketiga adalah `DataCollector`, yang akan kita bahas lebih lanjut. Komponen ini merekam jumlah trader, volume perdagangan, harga, serta catatan jaringan perdagangan pada level agent.

Di dalam environment terdapat Sugar, Spice, dan Trader. Sugar dan Spice tumbuh kembali, masing-masing sampai batas maksimum sel. Peta Spice dibuat dengan membalik peta Sugar secara horizontal, sehingga dua sumber daya memiliki distribusi spasial yang berbeda.

Perbedaan lokasi sumber daya ini penting. Trader mungkin memiliki gula yang cukup tetapi kekurangan rempah, atau sebaliknya. Karena itu, pertukaran dapat memberi manfaat bagi kedua pihak.

Setiap trader juga memiliki atribut seperti vision, metabolism untuk gula dan rempah, serta endowment atau cadangan awal. Banyak atribut ini diinisialisasi secara acak. Artinya, hasil satu run bisa dipengaruhi oleh pengacakan awal dan urutan kejadian selama simulasi.

---

## 5. Gerak, konsumsi, dan kematian — 04:00–05:15

VISUAL: Tampilkan cuplikan `move()`, `eat()`, dan `maybe_die()`.

NARASI

Sekarang kita lihat apa yang dilakukan trader pada setiap step. Ada tiga proses utama: bergerak, mengonsumsi sumber daya, lalu memeriksa apakah ia masih bisa bertahan hidup.

Pertama, `move()`. Trader mencari sel yang berada dalam jangkauan `vision`. Pencarian menggunakan jarak Manhattan, sehingga jangkauan ditentukan berdasarkan pergerakan horizontal dan vertikal, bukan diagonal.

Sel yang tidak memenuhi aturan model dikeluarkan dari kandidat. Untuk setiap sel yang tersisa, trader mengevaluasi potensi kesejahteraannya berdasarkan sumber daya yang tersedia dan kebutuhannya. Ia memilih kandidat terbaik. Jika ada nilai yang sama, aturan pemecah seri menentukan pilihan berikutnya.

Kedua, `eat()`. Setelah bergerak, trader mengambil sumber daya di sel tempatnya berada. Cadangan gula dan rempah bertambah dari hasil panen, kemudian berkurang sesuai nilai metabolism masing-masing.

Sumber daya yang dipanen di sel tersebut menjadi nol, lalu tumbuh kembali secara bertahap. Jadi, trader tidak bisa terus-menerus mengambil jumlah yang sama dari satu sel pada setiap step.

Ketiga, `maybe_die()`. Jika cadangan gula atau rempah tidak lagi mencukupi, trader dikeluarkan dari grid dan scheduler. Dalam model ini, trader yang mati tidak kembali ke populasi.

Aturan tersebut membantu menjelaskan mengapa `metabolism_max` menarik untuk diuji. Metabolism yang lebih tinggi berarti kebutuhan sumber daya dapat lebih besar, sementara sumber daya di lingkungan tumbuh dengan kecepatan yang dibatasi.

---

## 6. Mekanisme perdagangan — 05:15–06:30

VISUAL: Tampilkan `trade()` dan kalkulator transaksi.

NARASI

Selain mencari makan, trader juga dapat melakukan pertukaran. Mekanismenya menggunakan konsep ekonomi bernama Marginal Rate of Substitution, atau MRS.

Secara sederhana, MRS menggambarkan bagaimana seorang trader menilai pertukaran antara gula dan rempah berdasarkan cadangan dan kebutuhan metaboliknya.

Ketika dua trader bertemu, model membandingkan MRS mereka. Jika nilainya terlalu mirip, tidak ada alasan yang cukup untuk melanjutkan pertukaran. Jika berbeda, harga perdagangan ditentukan menggunakan geometric mean dari kedua nilai MRS.

Namun, harga saja tidak membuat transaksi otomatis berhasil. Kesejahteraan kedua trader dihitung menggunakan fungsi Cobb-Douglas. Transaksi hanya diterima jika kesejahteraan kedua pihak meningkat dan kondisi MRS setelah pertukaran tetap memenuhi aturan model.

Jika transaksi berhasil, proses dapat berulang sampai tidak ada lagi pertukaran yang memenuhi syarat. Karena itu, satu pertemuan bisa menghasilkan beberapa transaksi, bukan selalu satu transaksi saja.

Kalkulator di layar membantu memperlihatkan hubungan antara cadangan sumber daya, MRS, harga, dan jumlah transaksi. Kalkulator ini mengikuti logika perhitungan yang ditampilkan pada materi, sehingga kita bisa melihat bagaimana perubahan kondisi awal memengaruhi keputusan pertukaran.

---

## 7. Apa yang direkam DataCollector? — 06:30–07:15

VISUAL: Tampilkan model reporters dan agent reporter.

NARASI

Sebelum menjalankan eksperimen batch, kita perlu memahami data apa yang dikumpulkan.

`DataCollector` merekam informasi pada dua level. Pada level model, ada tiga reporter utama: jumlah Trader yang masih hidup, Trade Volume pada step tersebut, dan Price yang dihitung dari harga transaksi.

Pada level agent, reporter `Trade Network` mencatat daftar ID mitra dagang setiap trader.

Perbedaannya berpengaruh besar pada ukuran data. Reporter level model umumnya menghasilkan satu catatan untuk setiap step model. Reporter level agent menghasilkan catatan untuk setiap agent yang direkam pada setiap step.

Ketika empat run dijalankan sampai seribu step, pencatatan per agent inilah yang membuat ukuran dataset menjadi sangat besar. Kita akan melihat angka sebenarnya pada bagian Batch Runner.

---

## 8. Satu run sebagai titik pembanding — 07:15–08:25

VISUAL: Tampilkan replay seed 42 dan grafik populasi, volume, serta harga.

NARASI

Sebelum membandingkan beberapa konfigurasi, kita lihat dulu satu simulasi dengan seed 42 sebagai titik pembanding. Run ini dimulai dengan 200 trader.

Jumlah trader berkurang selama simulasi, lalu berhenti berubah sejak step 312 pada angka 64. Setelah itu, tidak ada trader lain yang mati sampai akhir run pada step 1.000.

Trade Volume pada step pertama mencapai 781 transaksi. Pada bagian akhir simulasi, rata-rata Trade Volume dari step 800 sampai 999 adalah 8,3 transaksi per step.

Rata-rata harga sepanjang run adalah 1,1068. Jika kita membandingkan simpangan baku harga pada 100 step pertama dengan 200 step terakhir, nilainya berubah dari 0,206 menjadi 0,2209.

Jadi, dalam run ini, variasi harga pada akhir simulasi tidak lebih kecil daripada variasi di awal. Harga tetap bergerak.

Angka-angka ini menarik, tetapi semuanya berasal dari satu run. Karena inisialisasi dan beberapa keputusan model melibatkan pengacakan, kita belum bisa menganggap 64 trader sebagai hasil yang pasti terjadi setiap kali model dijalankan.

Pertanyaan berikutnya adalah: bagaimana hasilnya jika kita mengubah parameter tertentu? Itulah yang diuji menggunakan Batch Runner.

---

## 9. Alur kerja Batch Runner — 08:25–09:40

VISUAL: Ikuti lima tahap alur eksperimen dari kiri ke kanan.

NARASI

Session 20 mengubah cara kita menggunakan model. Kita tidak hanya menjalankan satu simulasi, tetapi merancang eksperimen yang membandingkan beberapa konfigurasi.

Alurnya bisa dibaca dalam lima tahap. Pertama, pilih parameter yang ingin diuji. Kedua, tentukan kombinasi nilainya. Ketiga, jalankan setiap kombinasi melalui `batch_run()`. Keempat, kumpulkan hasilnya dalam satu struktur data agar mudah diolah. Terakhir, bandingkan hasil dan analisis pola yang muncul.

Ada satu detail penting: Batch Runner membuat instance model baru untuk setiap kombinasi parameter. Jadi, nilai yang ingin kita variasikan harus dapat diberikan ketika model dibuat, biasanya melalui argumen pada `__init__`.

Jika suatu nilai ditulis langsung di dalam kode dan tidak dijadikan parameter, Batch Runner tidak dapat mengubahnya hanya dengan mengisi dictionary parameter. Model perlu dirancang sejak awal agar eksperimen yang diinginkan bisa dilakukan dengan mudah.

Dengan pendekatan ini, kita dapat membandingkan hasil beberapa konfigurasi secara terstruktur, bukan hanya mengandalkan satu contoh simulasi.

---

## 10. Parameter dan pemanggilan batch_run — 09:40–11:25

VISUAL: Tampilkan kode `params` dan pemanggilan `batch_run()`; sorot tiap parameter saat disebut.

NARASI

Pada notebook Session 20, eksperimen menggunakan dua parameter utama: `vision_min` dan `metabolism_max`.

Ukuran grid tetap 50 kali 50, sehingga lingkungan yang dibandingkan memiliki ukuran yang sama. Dengan 200 trader awal, jumlah sel dan populasi awal juga tetap sama pada semua konfigurasi.

Parameter `vision_min` menggunakan `range(1, 3)`, yang menghasilkan dua nilai: 1 dan 2. `vision_max` tetap menggunakan nilai default 5. Jadi, kelompok pertama memiliki rentang vision 1 sampai 5, sedangkan kelompok kedua 2 sampai 5. Yang sedang kita uji adalah batas bawah vision, bukan mengganti seluruh rentang penglihatan.

Parameter kedua adalah `metabolism_max`, dengan nilai 3 dan 5. Karena batas bawah metabolism tetap 1 dan nilai dihasilkan melalui konversi integer dari rentang yang digunakan kode, kelompok pertama memiliki metabolism 1 sampai 3, sedangkan kelompok kedua 1 sampai 5.

Dua nilai `vision_min` dikombinasikan dengan dua nilai `metabolism_max`. Hasilnya adalah empat konfigurasi: 1 dan 3, 1 dan 5, 2 dan 3, serta 2 dan 5.

Pada pemanggilan `batch_run()`, `iterations=1` berarti setiap konfigurasi dijalankan satu kali. `number_processes=1` berarti eksekusinya menggunakan satu proses. `data_collection_period=1` berarti pengumpulan data dilakukan setiap step, dan `display_progress=True` menampilkan progres proses.

Notebook tidak menetapkan `max_steps` pada pemanggilan ini. Dalam konfigurasi model yang digunakan, simulasi berjalan sampai model mencapai kondisi berhentinya pada step 1.000.

Perlu diingat, satu iterasi per kombinasi cukup untuk melihat perbedaan awal, tetapi belum cukup untuk mengukur variasi hasil akibat seed secara statistik. Batas ini akan penting ketika kita menafsirkan hasil nanti.

---

## 11. Mengapa dataset mencapai 442.905 baris? — 11:25–13:05

VISUAL: Tampilkan ukuran DataFrame, lalu tunjukkan perbedaan reporter model dan agent.

NARASI

Setelah hasil batch diubah menjadi DataFrame, ukurannya mencapai 442.905 baris dan 12 kolom.

Angka ini tampak besar jika kita hanya membayangkan empat run dengan seribu step. Jika yang dicatat hanya metrik level model, jumlah barisnya akan berada di sekitar empat ribu, karena setiap run menyumbang catatan untuk setiap step, termasuk step awal yang direkam.

Yang membuat dataset jauh lebih besar adalah `agent_reporters`, terutama reporter `Trade Network`. Setiap trader yang tercatat dapat menyumbang satu baris pada setiap step saat ia masih ada dalam simulasi. Dengan populasi rata-rata sekitar 110 trader, empat run dan sekitar 1.001 titik pencatatan menghasilkan jumlah baris pada kisaran ratusan ribu.

Jadi, 442.905 baris bukan dengan sendirinya tanda bahwa ada kesalahan. Itu merupakan konsekuensi dari pilihan kita untuk merekam data setiap agent, setiap step.

Namun, pencatatan terperinci juga punya biaya. Jika jumlah iterasi diperbesar, penggunaan memori bisa meningkat tajam. Untuk eksperimen yang lebih besar, kita perlu mempertimbangkan apakah semua data level agent benar-benar dibutuhkan, atau cukup menyimpan metrik level model.

Notebook juga memfilter hasil dengan `metabolism_max == 3`. Setelah penyaringan ini, tersisa 306.267 baris. Jumlah tersebut menunjukkan bahwa dua run dengan metabolism maksimum 3 menyumbang bagian besar dari dataset, sejalan dengan jumlah trader yang lebih banyak bertahan pada kedua konfigurasi itu.

Hasil batch dikumpulkan menjadi satu tabel dan diberi penanda `RunId`. Penanda ini penting karena memungkinkan kita mengelompokkan data berdasarkan konfigurasi, lalu membandingkan trajektori setiap run tanpa mencampur semua hasilnya.

---

## 12. Dari transaksi menjadi jaringan — 13:05–15:35

VISUAL: Tampilkan kode NetworkX, metrik graf, histogram derajat, dan catatan tentang penggabungan RunId.

NARASI

Selain melihat populasi dan harga, notebook juga mengubah catatan perdagangan menjadi jaringan menggunakan NetworkX.

Caranya adalah membuat graf, lalu menambahkan hubungan antara `AgentID` dan setiap mitra dagang yang tercatat pada reporter `Trade Network`. Dengan begitu, trader direpresentasikan sebagai simpul, sedangkan hubungan perdagangan menjadi sisi di antara simpul-simpul tersebut.

Dari graf yang dibangun pada Cell 31, notebook melaporkan tiga metrik utama. Node connectivity bernilai 14. Average clustering adalah 0,6826, sedangkan global efficiency bernilai 0,8045.

Histogram derajat menunjukkan bahwa derajat simpul berada pada rentang 14 hingga 171, dengan banyak nilai terkumpul di kisaran 90 sampai 120. Angka-angka ini menggambarkan struktur graf yang terbentuk dari data yang diproses notebook.

Tetapi ada satu hal yang perlu diperhatikan sebelum menarik kesimpulan. Graf pada Cell 31 dibangun dari `results_df` yang menggabungkan seluruh `RunId`. Pada saat yang sama, `agent_id` dimulai kembali dari nol pada setiap run.

Akibatnya, ID yang sama dari dua run berbeda dapat diperlakukan sebagai simpul yang sama. Hubungan dari beberapa simulasi pun bisa tergabung dalam satu graf. Karena itu, metrik 14, 0,6826, dan 0,8045 harus dibaca sebagai metrik graf agregat lintas-run, bukan gambaran satu pasar dari satu simulasi.

Sebagai pembanding, graf dari satu run pada Cell 21 menghasilkan node connectivity 0, average clustering 0,3969, dan global efficiency 0,4461, dengan catatan bahwa tidak semua trader terhubung.

Perbedaan antara kedua hasil ini bukan bukti bahwa satu pasar tiba-tiba menjadi jauh lebih kuat. Cara graf dibangun juga berbeda. Ini contoh penting bahwa sebelum menafsirkan metrik jaringan, kita perlu memeriksa bagaimana data disusun dan simpul diidentifikasi.

Ada juga pertimbangan komputasi. Notebook menggunakan `iterrows()` untuk memproses baris demi baris. Cara ini cukup untuk data yang tersedia, tetapi bisa menjadi lambat ketika jumlah run dan baris meningkat.

---

## 13. Hasil empat kombinasi — 15:35–16:55

VISUAL: Tampilkan tabel empat run, kemudian grafik populasi dan harga.

NARASI

Sekarang kita bandingkan hasil dari empat kombinasi parameter.

Pada `vision_min` 1 dan `metabolism_max` 3, ada 145 trader pada akhir simulasi, harga rata-ratanya 0,9612, dan total Trade Volume mencapai 29.589.

Ketika `vision_min` tetap 1 tetapi `metabolism_max` naik menjadi 5, jumlah trader akhir turun menjadi 64. Harga rata-ratanya 1,1070 dan total Trade Volume 12.795.

Pada kombinasi `vision_min` 2 dan `metabolism_max` 3, ada 155 trader yang bertahan, harga rata-rata 0,9762, dan total Trade Volume 26.079.

Terakhir, pada `vision_min` 2 dan `metabolism_max` 5, jumlah trader akhir adalah 71, harga rata-rata 1,1288, dan total Trade Volume 11.628.

Dari grafik populasi, terlihat bahwa dua run dengan `metabolism_max` 3 mempertahankan populasi lebih besar daripada dua run dengan nilai 5. Sementara itu, perubahan `vision_min` dari 1 ke 2 menghasilkan selisih yang lebih kecil dalam dua pasangan ini.

Harga rata-rata juga berbeda di antara kombinasi, tetapi nilainya masih berada di sekitar satu. Grafik menunjukkan bahwa harga tetap bervariasi sepanjang simulasi, jadi kita tidak boleh menyamakan harga rata-rata yang mendekati satu dengan harga yang selalu tetap.

---

## 14. Membaca hasil dengan hati-hati — 16:55–18:55

VISUAL: Tampilkan empat temuan, lalu bagian tentang batas interpretasi.

NARASI

Ada empat hal yang menonjol dari hasil ini.

Pertama, pada dua pasangan yang dibandingkan, nilai `metabolism_max` yang lebih tinggi berkaitan dengan jumlah trader akhir yang lebih rendah. Saat batas maksimum metabolism berubah dari 3 menjadi 5, jumlah trader akhir turun dari 145 menjadi 64 ketika `vision_min` bernilai 1, dan dari 155 menjadi 71 ketika `vision_min` bernilai 2.

Kedua, perubahan `vision_min` dari 1 menjadi 2 memberikan perbedaan yang lebih kecil. Jumlah trader akhir naik dari 145 menjadi 155 pada kelompok metabolism 3, dan dari 64 menjadi 71 pada kelompok metabolism 5.

Ketiga, volume perdagangan cenderung lebih tinggi pada dua konfigurasi dengan `metabolism_max` 3. Totalnya berada di kisaran 26 ribu sampai hampir 30 ribu transaksi, dibandingkan sekitar 11 ribu sampai hampir 13 ribu pada konfigurasi dengan nilai 5. Salah satu penjelasan yang masuk akal adalah lebih banyak trader yang bertahan, sehingga peluang terjadinya perdagangan juga lebih besar.

Keempat, harga tidak menjadi konstan. Pada run seed 42, simpangan baku harga di 200 step terakhir adalah 0,2209, sedikit lebih tinggi daripada 0,206 pada 100 step pertama. Jadi, dari data ini kita tidak melihat penyusutan variasi harga pada bagian akhir run tersebut.

Tetapi kesimpulan ini perlu dibatasi. Setiap kombinasi parameter hanya dijalankan satu kali. Kita bisa menyebut bahwa pola yang sama terlihat pada dua pasangan run yang tersedia, tetapi belum bisa memastikan bahwa perbedaan itu akan selalu muncul untuk semua seed.

Kita juga belum bisa mengukur interval kepercayaan atau menguji signifikansi statistik dari satu iterasi per kombinasi. Langkah lanjutan yang lebih kuat adalah menjalankan replikasi dengan banyak seed untuk setiap konfigurasi, misalnya 30 sampai 50 iterasi, lalu membandingkan distribusi hasilnya.

Jadi, hasil sekarang berguna sebagai eksplorasi awal dan menunjukkan pola yang layak diteliti lebih lanjut. Namun, hasil ini belum menjadi bukti statistik umum tentang pengaruh parameter terhadap semua kemungkinan simulasi.

---

## 15. Kesimpulan — 18:55–20:00

VISUAL: Tampilkan dua panel kesimpulan.

NARASI

Ada tiga hal utama yang bisa kita bawa dari model ini.

Pertama, pola pada tingkat sistem dapat muncul dari aturan lokal. Model tidak menetapkan secara langsung berapa trader yang akan bertahan atau berapa harga yang akan terbentuk. Hasil itu muncul dari interaksi trader dengan lingkungan dan satu sama lain.

Kedua, lingkungan dan kebutuhan setiap agent ikut membentuk perilaku ekonomi. Karena gula dan rempah tersebar secara berbeda, trader memiliki alasan untuk bergerak dan melakukan pertukaran. Perbedaan metabolism juga berkaitan dengan seberapa banyak trader yang bertahan dalam empat run yang kita bandingkan.

Ketiga, Session 20 menunjukkan mengapa Batch Runner penting. Satu run memberi kita satu contoh hasil. Eksperimen dengan beberapa konfigurasi membantu kita membandingkan hasil secara terstruktur. Semakin kuat pertanyaan yang ingin dijawab, semakin penting pula desain eksperimen dan jumlah replikasi yang memadai.

Dari hasil yang tersedia, metabolism tampak berkaitan kuat dengan jumlah trader yang bertahan dan volume perdagangan. Namun, karena setiap konfigurasi baru dijalankan satu kali, pola ini masih perlu diuji melalui replikasi lebih banyak.

Dengan demikian, Batch Runner bukan sekadar cara menjalankan banyak simulasi. Ia membantu mengubah model menjadi alat eksperimen yang hasilnya dapat dibandingkan, diperiksa, dan ditafsirkan secara hati-hati.

Terima kasih. Saya siap menerima pertanyaan.

---

## Catatan presenter — tidak dibacakan kecuali ditanya

- Model lokal menggunakan Mesa 1.2.1. Dependensi dan kendala kompatibilitas hanya dijelaskan jika ditanyakan.
- Hasil single run seed 42 berasal dari eksekusi lokal `sugarscape_g1mt.py`; empat hasil batch berasal dari `export_results.py` dengan seed tetap. Notebook asli tidak menetapkan seed, sehingga hasilnya dapat berbeda jika dijalankan ulang tanpa seed.
- Pada graf Cell 31, semua `RunId` digabung dan `agent_id` dimulai ulang pada setiap run. Karena itu, metrik graf tersebut adalah metrik agregat lintas-run, bukan satu pasar tunggal.
- Trade Volume menghitung pasangan mitra yang berhasil bertransaksi pada step tersebut. Satu pertemuan yang menghasilkan beberapa transaksi dapat menambah volume lebih dari satu.
