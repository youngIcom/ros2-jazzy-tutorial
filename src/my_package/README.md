# 📦 Modul: Struktur Dasar Package (Python)

Selamat datang di direktori `my_package`. Ini adalah sebuah _package_ Python dasar berbentuk kerangka awal (*boilerplate*). Direktori ini mendemonstrasikan fondasi paling awal dari setiap program aplikasi ROS 2.

## 📖 Konsep Teori: Apa itu "Package" di ROS 2?

Di dalam ekosistem ROS 2, **Package (Paket)** adalah unit terkecil dan paling utama untuk mengorganisasi, membangun (*build*), serta mendistribusikan program robotika Anda. 
Sistem ROS **tidak akan mengenali** skrip Python tunggal jika ia diletakkan sembarangan. Setiap baris kode program (`.py` maupun `.cpp`) **wajib** hidup di dalam wadah yang disebut _Package_.

**Tujuan Pembuatan Package:**
1. **Modularitas (Kerapian):** Memecah arsitektur sistem robot yang masif menjadi modul-modul kecil. (Contoh: satu _package_ khusus pengolahan kamera, satu _package_ khusus kontrol roda penggerak).
2. **Manajemen Dependensi:** Menyediakan file konfigurasi yang mencatat library eksternal apa saja yang dibutuhkan agar program bisa jalan (seperti Numpy, OpenCV, atau library ROS lain).
3. **Standarisasi Eksekusi:** Memungkinkan _build tool_ (`colcon`) untuk memaketkan program Anda sedemikian rupa agar bisa dieksekusi dengan rapi melalui perintah global `ros2 run` dari direktori mana pun.

## 🛠️ Anatomi (Struktur File) Standar Python Package

Kerangka kerja package ini secara ajaib dibuat (*generated*) menggunakan perintah standar bawaan ROS 2:
```bash
ros2 pkg create --build-type ament_python my_package
```

Ketika perintah di atas dieksekusi, ia akan menghasilkan file krusial berikut:

1. **`package.xml`**:
   Ini adalah "KTP" dari _package_ Anda. File berbasis XML ini memuat _metadata_ (nama pembuat, email, lisensi) dan pendaftaran dependensi. Contohnya, jika program Python Anda butuh `rclpy`, Anda harus menuliskannya di sini (`<depend>rclpy</depend>`). File ini yang akan dibaca oleh alat instalasi otomatis (`rosdep`).

2. **`setup.py`**:
   Ini adalah tulang punggung instalasi Python. Di file inilah Anda **mendaftarkan program (Node) Anda**. Pada bagian konfigurasi `entry_points`, kita mendefinisikan jembatan agar perintah terminal `ros2 run` terhubung ke fungsi `main()` di dalam kode Python Anda.

3. **`setup.cfg`**:
   File pembantu untuk memberitahu _colcon_ persis di direktori instalasi mana sistem harus menaruh file *executable* Anda agar terdeteksi oleh radar ROS 2.

4. **`my_package/` (Sub-Direktori)**:
   Di dalam folder yang bernama sama persis dengan package-nya inilah, tempat semua *source code* logika Python (`.py`) Anda akan bersarang. Keberadaan `__init__.py` di dalamnya menjadi validasi bagi OS Linux bahwa direktori tersebut adalah Modul Python yang sah.

## 💻 Panduan Eksperimen: Membuat Node Pertama Anda

Jika suatu saat Anda ingin mengisi kerangka kosong ini menjadi program utuh, inilah _workflow_-nya:

1. **Buat Logika Program**: Buat file Python (misal `node_pertamaku.py`) di dalam folder `src/my_package/my_package/`. 
2. **Tulis Kode**: Gunakan library `rclpy` untuk membuat sebuah Node.
3. **Daftarkan di setup.py**: Buka `setup.py`, gulir ke bagian `entry_points` -> `console_scripts`, lalu tambahkan format ini:
   `'jalankan_program = my_package.node_pertamaku:main'`
4. **Kompilasi / Build**:
   ```bash
   colcon build --packages-select my_package
   source install/setup.bash
   ```
5. **Eksekusi**:
   Voila! Node buatan Anda kini sudah diakui ROS 2 dan bisa langsung dipanggil dengan:
   ```bash
   ros2 run my_package jalankan_program
   ```
