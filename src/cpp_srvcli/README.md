# 🛎️ Modul: Client & Server (C++ Services)

Selamat datang di modul pembelajaran **Services** pada ROS 2 menggunakan bahasa **C++**. Melalui package `cpp_srvcli` (singkatan dari C++ Service & Client) ini, Anda akan mempelajari cara program saling meminta tolong dan mengembalikan hasil (Request-Response).

## 📖 Konsep Teori: Apa itu Services?

Jika modul sebelumnya (*Publisher/Subscriber*) ibarat **siaran stasiun radio** di mana data disiarkan terus-menerus satu arah, maka **Services** (Servis) ibarat interaksi di **restoran**.

1. **Client (Pelanggan)**: Node yang meminta sesuatu (disebut **Request**). Misalnya pelanggan yang memesan makanan ke pelayan.
2. **Server (Dapur/Pelayan)**: Node yang menerima pesanan (Request), memprosesnya secara logika, lalu mengembalikan hasil akhirnya (disebut **Response**) kembali ke Client.

**Kapan harus menggunakan Services dan bukan Pub/Sub?**
- Gunakan **Pub/Sub** untuk data yang mengalir tiada henti dan terus berubah (contoh: data posisi robot, data gambar kamera).
- Gunakan **Services** untuk **perintah satu kali** (*one-off command*) yang membutuhkan kepastian atau jawaban bahwa tugas telah selesai dieksekusi (contoh: "Tolong simpan peta ini", "Tolong nyalakan sensor laser", atau "Tolong hitung 5 + 3").

Pada modul ini, kita menggunakan contoh *Service* matematika sederhana: **Penjumlahan Dua Angka**.
- Client mengirimkan dua angka acak ke Server.
- Server menerimanya, menjumlahkan kedua angka tersebut, lalu mengirimkan hasil hitungannya kembali.

## 🛠️ Struktur Package C++

- `src/add_two_ints_server.cpp`: Kode untuk *Server*. Ia membuka "layanan" bernama `add_two_ints` dan berdiam diri (*standby*) menunggu pelanggan (Client) datang membawa 2 angka.
- `src/add_two_ints_client.cpp`: Kode untuk *Client*. Ia mendatangi server, memberikan 2 angka dari terminal, menahan proses (*blocking*) hingga server selesai menghitung, lalu mencetak hasilnya ke layar.
- Secara teknis, package ini menggunakan antarmuka tipe pesan bawaan ROS 2, yaitu `example_interfaces/srv/AddTwoInts` untuk mendefinisikan bentuk tipe datanya.

## 💻 Cara Menjalankan & Pembuktian (Langkah-demi-Langkah)

Mari kita hidupkan Server-nya dan suruh Client meminta perhitungan matematika!

### Langkah 1: Kompilasi (Build) Program
Setiap kali kode C++ baru dibuat, kita harus mengkompilasinya. Buka terminal utama (di dalam folder root `~/ros2_praktikum`) dan jalankan:
```bash
colcon build --packages-select cpp_srvcli
source install/setup.bash
```

### Langkah 2: Hidupkan Node Server (Terminal 1)
Buka tab terminal baru, lakukan *source environment*, dan nyalakan Server.
```bash
source install/setup.bash
ros2 run cpp_srvcli server
```
**Ekspektasi di Terminal 1:**
Anda akan melihat tulisan `[INFO] [rclcpp]: Ready to add two ints.`. Ini berarti server sudah *online* dan siap menerima _request_ kapan saja!

### Langkah 3: Minta Perhitungan dari Node Client (Terminal 2)
Biarkan Terminal 1 (Server) tetap aktif. Buka Terminal baru lagi (Terminal 2), lakukan *source*, lalu jalankan Client. 
Perhatikan, saat menjalankan perintah `client`, Anda harus **memberikan 2 angka** yang ingin dijumlahkan di belakangnya (misalnya Anda ingin menghitung `4` ditambah `7`):
```bash
source install/setup.bash
ros2 run cpp_srvcli client 4 7
```

### 🎉 Hasil Pembuktian:

**1. Cek di Terminal 2 (Client):**
Sesaat setelah tombol Enter ditekan, Client akan segera memberikan output:
`[INFO] [rclcpp]: Result of add_two_ints: 11`
*(Keren! Client berhasil menerima hasil perhitungan dari Server).*

**2. Cek di Terminal 1 (Server):**
Jika Anda kembali melihat ke layar Terminal 1 (Server), Server akan mencatat log aktivitas bahwa ia baru saja sibuk melayani sebuah permintaan:
`[INFO] [rclcpp]: Incoming request`
`a: 4 b: 7`

**Kesimpulan:** 
Anda telah berhasil membuktikan arsitektur komunikasi **dua arah sinkron** (Request & Response) antar program di ROS 2 Jazzy! Client menugaskan Server, Server mengerjakannya, dan hasilnya dikembalikan dengan akurat.
