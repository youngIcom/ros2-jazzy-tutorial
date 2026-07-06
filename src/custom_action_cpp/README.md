# 🏃‍♂️ Modul: Actions C++ Custom (Tugas Jangka Panjang)

Selamat datang di modul pembelajaran **Custom Actions** menggunakan bahasa **C++**. Melalui package `custom_action_cpp` ini, Anda akan mempelajari konsep arsitektur paling canggih di ROS 2 untuk menyuruh robot/sistem melakukan proses komputasi berdurasi panjang tanpa membuat sistem mengalami kemacetan (*freeze* / *blocking*).

## 📖 Konsep Teori: Mengapa Kita Butuh "Action"?

Pada modul *Service* sebelumnya, saat Client meminta Server menghitung sesuatu, Client harus **menunggu secara pasif** (tertahan) sampai Server selesai menghitung. Konsep ini sangat bagus untuk perintah singkat. Namun, bayangkan jika tugasnya memakan waktu lama? Misalnya "Tolong jalankan robot sejauh 100 meter ke depan". Tentu kita tidak ingin komputer robot *hang* atau tidak bisa merespons perintah lain selama beberapa menit perjalanan. 

Di sinilah **Action** menjadi solusi utama dalam sistem robotika!

Dalam kerangka kerja Action:
1. **Goal (Target Tujuan)**: Client meminta sebuah target (contoh: "Tolong hitung deret Fibonacci ke-10"). Setelah perintah dikirim, Client **tidak terkunci**, ia bebas melakukan tugas atau logika lain.
2. **Feedback (Laporan Sementara)**: Selama Server sibuk berhitung (berjalan), ia akan secara konstan melaporkan _progresnya_ ke Client (*real-time*) (contoh: "Aku baru dapat angka 1", "Sekarang aku di angka 3", "Lanjut angka 5...").
3. **Result (Hasil Akhir)**: Ketika tugas sudah 100% tuntas, barulah Server mengirimkan satu nilai kesimpulan final.

**Ketergantungan Package (Penting):**
Package `custom_action_cpp` ini tidak mendefinisikan bentuk datanya sendiri. Ia sangat bergantung pada "cetak biru" yang telah kita buat di package `custom_action_interfaces`. Karena itulah ia disebut *custom action*.

## 🛠️ Struktur Package C++

- `src/fibonacci_action_server.cpp`: Kode Server C++ yang membuka jasa `fibonacci`. Ketika diminta, program ini akan menghitung satu per satu angka Fibonacci dengan sengaja memberikan jeda waktu (sekitar 1 detik) per angkanya agar kita bisa melihat *Feedback*-nya secara kasat mata.
- `src/fibonacci_action_client.cpp`: Kode Client C++ yang akan datang untuk memesan kalkulasi, lalu mencetak setiap *Feedback* yang masuk perlahan-lahan sembari menunggu hasil akhir.

## 💻 Cara Menjalankan & Pembuktian (Langkah-demi-Langkah)

Mari kita saksikan kecanggihan "Feedback" pada sistem Action!

### Langkah 1: Kompilasi (Build) Program
Pastikan Anda selalu me-*build* package setelah ada perubahan kode. Buka terminal di folder root workspace (`~/ros2_praktikum`) dan jalankan:
```bash
colcon build --packages-select custom_action_cpp
source install/setup.bash
```

### Langkah 2: Hidupkan Action Server (Terminal 1)
Buka tab terminal baru, lakukan *source*, lalu nyalakan Server-nya.
```bash
source install/setup.bash
ros2 run custom_action_cpp fibonacci_action_server
```
*(Ekspektasi: Server akan diam berjaga-jaga tanpa output apa-apa).*

### Langkah 3: Beri Perintah lewat Action Client (Terminal 2)
Biarkan Terminal 1 tetap hidup. Buka Terminal baru (Terminal 2), lakukan *source*, lalu jalankan Client. Pada modul ini, target urutan Fibonacci (contoh ke-10) sudah disematkan *hardcoded* di dalam kodenya.
```bash
source install/setup.bash
ros2 run custom_action_cpp fibonacci_action_client
```

### 🎉 Hasil Pembuktian (Ajaibnya Laporan *Feedback*!):

**1. Pantau Terminal 2 (Client):**
Jangan berkedip! Begitu dienter, Anda akan melihat Client menerima rentetan deret angka **secara bertahap** (berkat mekanisme Feedback) dengan jeda 1 detik per baris:
```text
[INFO] [fibonacci_action_client]: Feedback received: 0 1 1 
[INFO] [fibonacci_action_client]: Feedback received: 0 1 1 2 
[INFO] [fibonacci_action_client]: Feedback received: 0 1 1 2 3 
[INFO] [fibonacci_action_client]: Feedback received: 0 1 1 2 3 5
... (terus bertambah panjang)
```
Hingga pada akhirnya, saat kalkulasi selesai 100%, sistem akan melaporkan **Result**:
`[INFO] [fibonacci_action_client]: Result received: 0 1 1 2 3 5 8 13 21 34 55`

**2. Pantau Terminal 1 (Server):**
Jika Anda melirik kembali ke Terminal Server, Anda akan melihat log yang menunjukkan ia telah menerima tujuan baru (*Accepted new goal*), memprosesnya, dan menyatakan misi berhasil diselesaikan (*Goal succeeded*).

**Kesimpulan Utama:** 
Anda telah membuktikan dengan sukses bagaimana arsitektur **Action** ROS 2 Jazzy sanggup menangani **tugas berdurasi panjang** dengan mulus! Komputer Client sama sekali tidak terkunci secara statis, melainkan tetap mendapatkan pelaporan _real-time_ (Feedback) hingga tugasnya paripurna (Result).
