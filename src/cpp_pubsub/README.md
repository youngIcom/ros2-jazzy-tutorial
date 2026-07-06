# 📡 Modul: Publisher & Subscriber (C++)

Selamat datang di modul pembelajaran **Publisher dan Subscriber** menggunakan bahasa **C++**. Package `cpp_pubsub` ini akan mendemonstrasikan bagaimana dua *node* (program) ROS 2 dapat berkomunikasi pesan satu arah secara efisien.

## 📖 Konsep Teori: Publisher & Subscriber di ROS 2 Jazzy

Di dalam arsitektur ROS 2 (terutama pada distribusi mutakhir seperti Jazzy Jalisco), mekanisme komunikasi paling fundamental terjadi melalui sistem bernama **Pub/Sub** yang beroperasi menggunakan protokol DDS (Data Distribution Service) di belakang layar.

1. **Topik (Topic)**: Ibarat sebuah "saluran radio". Ia memiliki nama yang unik, misalnya `/topic`.
2. **Publisher (Pengirim)**: *Node* yang bertugas menerbitkan (menyiarkan) pesan ke dalam Topik tersebut secara berulang. Publisher tidak peduli apakah ada yang mendengarkan pesannya atau tidak; tugasnya murni hanya mengirimkan data.
3. **Subscriber (Penerima)**: *Node* yang mendaftarkan dirinya (subscribe) ke suatu Topik untuk "mendengarkan" lalu lintas data di dalamnya. Setiap kali ada pesan baru masuk dari Publisher, fungsi khusus (*callback function*) pada Subscriber akan otomatis tereksekusi.

**Mengapa menggunakan C++ di ROS 2?**
Walaupun Node berbasis Python (`rclpy`) sangat ramah pemula, penulisan Node menggunakan C++ (`rclcpp`) memberikan **performa eksekusi yang jauh lebih cepat**, manajemen memori yang efisien, dan tingkat *latency* yang sangat rendah. Karena itulah, algoritma kontrol dan visi komputer tingkat produksi (_production-grade_) hampir selalu ditulis dalam C++.

## 🛠️ Struktur Package C++

Berbeda dengan Python, package C++ membutuhkan file konfigurasi kompilasi agar sistem operasi dapat mengubah kode sumber menjadi *executable* (program siap jalan):
- `src/publisher_lambda_function.cpp`: Kode sumber untuk node Publisher. Ia mengirimkan pesan teks string secara terus-menerus (dilengkapi fitur modern *C++11 lambda expressions*).
- `src/subscriber_lambda_function.cpp`: Kode sumber untuk node Subscriber yang akan menerima dan mencetak pesan tersebut di layar.
- `CMakeLists.txt`: Konfigurasi *build system* C++ (CMake) yang mengatur pendaftaran library `rclcpp` dan `std_msgs` serta mengubah file `.cpp` menjadi file *executable* yang dikenali ROS.
- `package.xml`: File meta-data yang mendeklarasikan dependensi sistem _package_ Anda.

## 💻 Cara Menjalankan & Membuktikan Komunikasi

Mari kita buktikan secara langsung bagaimana program ini berjalan dan saling bertukar data!

### 1. Build Package (Kompilasi)
Karena ini adalah C++, kita harus mengkompilasinya terlebih dahulu. Buka terminal di direktori *root workspace* Anda (`~/ros2_praktikum`) lalu jalankan:

```bash
colcon build --packages-select cpp_pubsub
source install/setup.bash
```

### 2. Jalankan Node Publisher (Terminal 1)
Buka terminal, jangan lupa lakukan *source*, dan jalankan program **talker**:
```bash
source install/setup.bash
ros2 run cpp_pubsub talker
```
**Hasil (Bukti 1):** Anda akan melihat node ini terus-menerus mencetak log seperti:
`[INFO] [minimal_publisher]: Publishing: 'Hello, world! 1'` 
*(angka akan bertambah setiap detiknya)*

### 3. Jalankan Node Subscriber (Terminal 2)
Biarkan Terminal 1 tetap aktif. Buka tab Terminal baru (Terminal 2), lakukan *source* lagi, dan jalankan program **listener**:
```bash
source install/setup.bash
ros2 run cpp_pubsub listener
```
**Hasil (Bukti 2):** Begitu Node ini dijalankan, ia akan langsung menangkap siaran pesan dari "Terminal 1" dan mencetaknya:
`[INFO] [minimal_subscriber]: I heard: 'Hello, world! 1'`

**🎉 Pembuktian Berhasil!** 
Anda baru saja menyaksikan secara langsung bagaimana dua program C++ yang berjalan sebagai *process* terpisah (di terminal berbeda) mampu saling mendengarkan dan berkirim pesan _real-time_ dalam satu Topik di framework ROS 2!
