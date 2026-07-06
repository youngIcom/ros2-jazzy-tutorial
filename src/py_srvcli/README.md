# 🛎️ Modul: Client & Server (Python Services)

Selamat datang di modul pembelajaran **Services** menggunakan bahasa **Python**. Melalui package `py_srvcli` (singkatan dari Python Service & Client) ini, Anda akan mempraktikkan konsep arsitektur tanya-jawab (Request-Response) pada ROS 2 Jazzy menggunakan pustaka inti `rclpy`.

## 📖 Konsep Teori: Karakteristik Service di Python

Berbeda dengan pola komunikasi Pub/Sub yang menyiarkan data tanpa henti ke segala arah, **Service** dirancang khusus untuk "Panggilan Tugas Sekali Waktu" yang membutuhkan penyelesaian jelas secara sinkron.

Prosesnya sangat mirip dengan Anda (sebagai **Client**) menelepon layanan restoran (sebagai **Server**):
1. **Client** memanggil dan mengirimkan parameter (disebut **Request**). Selama pekerjaan belum selesai, Client akan tertahan (*blocking* / menunda baris kode selanjutnya).
2. **Server** menerima perintah, memprosesnya secara logika, lalu mengembalikan nilai akhirnya (disebut **Response**) ke Client.
3. Setelah Client menerima Response tersebut, proses interaksi selesai, dan Client bisa lanjut bekerja.

**Kenapa menggunakan Python?**
Meski C++ lebih gegas dari sisi performa kalkulasi rumit, penulisan ROS 2 Node menggunakan **Python (`rclpy`)** jauh lebih unggul dalam kecepatan *prototyping*. Kode Python jauh lebih ringkas, intuitif dibaca oleh pemula, dan sangat cocok untuk proses integrasi logika _Machine Learning_ atau GUI.

## 🛠️ Struktur Package Python

Pada folder ini, struktur program bergantung sepenuhnya pada file Python:
- `py_srvcli/service_member_function.py`: Ini adalah Node Server. Ia akan membuka "layanan" bernama `add_two_ints` lalu diam (standby) menunggu *Client* mengirimkan permohonan kalkulasi matematika.
- `py_srvcli/client_member_function.py`: Ini adalah Node Client. Ia diprogram untuk mengambil 2 angka acak yang diketik user di terminal (Request), lalu menyerahkannya ke Server.
- Program ini mengimpor format pesan *Service* standar dari ROS 2 yaitu `example_interfaces/srv/AddTwoInts`. Interface ini secara baku mendefinisikan variabel `a` dan `b` sebagai Request, dan variabel `sum` (hasil penjumlahan) sebagai Response.

## 💻 Cara Menjalankan & Pembuktian (Langkah-demi-Langkah)

Mari kita nyalakan Server-nya dan perintahkan Client untuk meminta perhitungan penjumlahan dasar!

### Langkah 1: Kompilasi (Build) Program
Walaupun kode Python tidak benar-benar di-compile seperti C++, sistem ROS 2 tetap mewajibkan proses *build* agar file `setup.py` dapat mendaftarkan Node Anda secara resmi ke dalam jeroan Linux OS. Buka terminal utama (root `~/ros2_praktikum`) dan jalankan:
```bash
colcon build --packages-select py_srvcli
source install/setup.bash
```

### Langkah 2: Hidupkan Node Server (Terminal 1)
Buka tab terminal baru, lakukan *source environment*, lalu nyalakan Server.
```bash
source install/setup.bash
ros2 run py_srvcli service
```
**Ekspektasi di Terminal 1:**
Node akan berdiam diri dan mencetak log `[INFO] [minimal_service]: Ready to add two ints.`. Selamat, Server (Kalkulator) Anda kini berstatus _online_!

### Langkah 3: Kirim Tugas lewat Node Client (Terminal 2)
Biarkan Terminal 1 (Server) tetap aktif. Buka Terminal baru (Terminal 2), jalankan instruksi *source*, lalu panggil perintah Client. 
Pastikan Anda menyematkan **2 buah angka** di akhir perintah (sebagai contoh, masukkan angka `15` dan `22`):
```bash
source install/setup.bash
ros2 run py_srvcli client 15 22
```

### 🎉 Hasil Pembuktian Visual:

**1. Cek di Terminal 2 (Client):**
Hanya sepersekian detik setelah di-enter, Client akan segera mencetak hasil penjumlahan dari Server:
`[INFO] [minimal_client]: Result of add_two_ints: for 15 + 22 = 37`
*(Sukses! Client berhasil memaksa Server bekerja dan menarik jawabannya).*

**2. Cek di Terminal 1 (Server):**
Apabila Anda menengok kembali ke layar Terminal 1 (Server), Server diam-diam mencatat riwayat bahwa ia baru saja selesai dipekerjakan:
`[INFO] [minimal_service]: Incoming request`
`a: 15 b: 22`

**Kesimpulan Penuh:** 
Anda telah mendemonstrasikan secara nyata bagaimana dua entitas program terpisah dapat berkomunikasi lewat **Request-Response tersinkronisasi** menggunakan ekosistem Python (`rclpy`) pada sistem operasi mutakhir ROS 2 Jazzy!
