# 📦 Modul: Custom Interfaces (Pesan Khusus)

Package `custom_action_interfaces` ini sedikit unik: **tidak mengandung kode logika (Python/C++)**. Package ini hanya berisi definisi tipe data mentah yang kita buat sendiri.

## 📖 Konsep Dasar: Apa itu Interfaces?

ROS 2 memiliki banyak tipe pesan standar (contoh: teks, gambar, suhu, atau kecepatan). Namun saat Anda membuat sistem sendiri, Anda mungkin butuh data yang lebih spesifik, di sinilah **Custom Interfaces** berperan.

Di ROS 2, ada 3 format data:
1. **`.msg`**: Format data untuk Publisher/Subscriber.
2. **`.srv`**: Format Request dan Response untuk Client/Server.
3. **`.action`**: Format Goal, Result, dan Feedback untuk Actions.

Pada modul ini, kita membuat file `Fibonacci.action`. Dengan mendefinisikannya di sini, node Python (dari package lain) bisa menggunakan format Action ini secara universal.

## 🛠️ Struktur Package
- `action/Fibonacci.action`: File inti yang mendefinisikan format.
  - **Goal**: Urutan deret ke-berapa yang diminta (integer).
  - **Result**: Daftar deret hasil akhir (array integer).
  - **Feedback**: Daftar deret sementara saat sedang diproses (array integer).
- Konfigurasi spesial di `CMakeLists.txt` dan `package.xml` yang memberitahu compiler (`rosidl_default_generators`) untuk mengubah file text `.action` menjadi bahasa C++ dan Python secara otomatis saat di-build.

## 💻 Cara Build

**PENTING:** Setiap ada perubahan sekecil apa pun pada file `.action`, package ini **wajib** di-build ulang sebelum node lain dijalankan, agar sistem mendeteksi tipe data terbaru.

```bash
colcon build --packages-select custom_action_interfaces
source install/setup.bash
```
