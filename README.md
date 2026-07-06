# 🤖 Belajar ROS 2: Praktikum & Tutorial Terpadu (Jazzy)

Selamat datang di repositori ROS 2(Robot Operating System 2)! Repositori ini berisi kumpulan paket (_packages_), kode sumber (Python & C++), dan dokumentasi mengenai konsep dasar hingga menengah dalam ekosistem ROS 2 Jazzy.

---

## 📋 Daftar Isi & Modul Pembelajaran

Repositori ini telah menstrukturkan pembelajaran ke dalam beberapa modul _package_. Klik tautan pada masing-masing modul untuk membaca panduan detail teori dan cara menggunakannya:

### 1. Fundamental Komunikasi

- 📡 **[Publisher & Subscriber (Python)](./src/py_pubsub/)**: Belajar _streaming_ data terus-menerus.
- 📡 **[Publisher & Subscriber (C++)](./src/cpp_pubsub/)**: Implementasi berkinerja tinggi menggunakan C++ modern.
- 🛎️ **[Client & Server (Python)](./src/py_srvcli/)**: Konsep Request-Response (_blocking_) menggunakan Python.
- 🛎️ **[Client & Server (C++)](./src/cpp_srvcli/)**: Membangun kalkulator _Service_ di C++.
- 🏃‍♂️ **[Actions (Python)](./src/action_tutorials_py/)**: Menyuruh robot mengerjakan tugas panjang disertai _Feedback_.
- 🏃‍♂️ **[Actions (C++)](./src/custom_action_cpp/)**: Membangun _Action Server_ dalam C++ tanpa menyebabkan _hang_ sistem.

### 2. Konsep Tingkat Menengah

- 📦 **[Custom Interfaces](./src/custom_action_interfaces/)**: Memahami cara membuat format tipe data (_Message/Service/Action_) buatan sendiri.
- 📦 **[Struktur Package Dasar](./src/my_package/)**: Membedah anatomi file dan struktur wajib sebuah _package_ di ekosistem ROS 2.
- 🐢 **[Transform / TF2](./src/turtle_tf_broadcaster/)**: Matematika rotasi dan translasi koordinat orientasi secara _real-time_.

### 3. Dunia Fisik & Simulasi

- 🤖 **[URDF & Integrasi Gazebo](./src/my_robot_description/)**: Mendesain tubuh fisik robot, mengatur _Differential Drive_, memasang sensor LiDAR virtual, dan menjembatani komunikasi data menuju Gazebo Simulator.
- 💡 **[Dokumentasi Laporan Tambahan](./docs/)**: Menyimpan laporan akademis komprehensif mengenai simulasi Gazebo, visualisasi RViz2, dan rekaman data dengan _Rosbag_.

---

## 📖 Glosarium (Kamus ROS 2)

Bagi pemula, istilah-istilah di bawah ini wajib dipahami:

- **ROS 2**: Bukan sistem operasi sungguhan (seperti Windows/Linux), melainkan semacam _middleware_ (kumpulan library canggih) untuk mempermudah pembuatan aplikasi robotika.
- **Workspace**: Direktori folder utama (contoh: `ros2_praktikum`) tempat di mana seluruh proyek dan _source code_ Anda dibangun.
- **Colcon**: _Build tool_ (alat kompilasi) resmi ROS 2. Digunakan untuk merakit kode mentah di Workspace menjadi aplikasi yang bisa dieksekusi (`colcon build`).
- **Package**: Wadah organisasi terkecil. ROS 2 tidak bisa menjalankan sebuah _script_ jika ia tidak dibungkus di dalam sebuah _Package_ yang resmi.
- **Node**: Sebuah program/proses mandiri tunggal (misal: satu file python). Contoh: "Node pengontrol roda", "Node pembaca suhu".
- **Topic**: Saluran komunikasi mirip siaran radio. _Publisher_ memancarkan data secara konstan tanpa peduli siapa _Subscriber_ yang mendengarkannya.
- **Service**: Sistem komunikasi dua arah sinkron. Anda meminta sesuatu (_Request_), dan Anda harus diam menunggu sampai mendapat jawaban (_Response_).
- **Action**: Komunikasi untuk target komputasi berdurasi panjang. Anda tidak akan disuruh menunggu pasif, karena sistem akan mencetak laporan _Feedback_ selama ia bekerja, dan mengabari _Result_ di akhir.
- **TF2 (Transform)**: Library sakti pelacak koordinat. Digunakan untuk menanyakan matematis spasial, misalnya "Berapa meter persis jarak antara ujung capit robot terhadap roda utamanya sekarang?".
- **URDF (Unified Robot Description Format)**: File teks XML yang mendeskripsikan secara dimensi, massa, warna, dan sendi engsel dari fisik sebuah robot.

---

## 🛠️ Prasyarat Sistem

Sebelum mulai bereksperimen, pastikan komputer Anda telah dikonfigurasi:

- **Sistem Operasi**: Ubuntu 24.04 LTS (Noble Numbat).
- **Distribusi ROS 2**: [Jazzy Jalisco](https://docs.ros.org/en/jazzy/Installation.html).
- **Dependensi Tambahan** (Install melalui Terminal):
  - `colcon` (alat untuk _build_).
  - `ros-jazzy-gazebo-ros-pkgs` (untuk interaksi simulasi Gazebo).
  - `ros-jazzy-rosbag2` (untuk rekam-putar data robot).

---

## 🚀 Cara Instalasi & Setup Lingkungan

Ikuti langkah-langkah ini untuk menyalin _workspace_ ini ke komputer Anda:

1. **Kloning (Download) Repositori:**

   ```bash
   git clone <URL_GITHUB_ANDA_DISINI>
   cd ros2_praktikum
   ```

2. **Install Dependensi Eksternal (`rosdep`):**
   Jalankan dari _root_ direktori untuk memastikan seluruh _library_ bawaan terpenuhi:

   ```bash
   sudo rosdep init
   rosdep update
   rosdep install -i --from-path src --rosdistro jazzy -y
   ```

3. **Build Workspace Anda:**
   Rakitan (_compile_) seluruh package menggunakan `colcon`:

   ```bash
   colcon build --symlink-install
   ```

4. **Aktifkan (Source) Lingkungan:**
   Langkah **wajib** yang harus dilakukan setiap kali Anda membuka terminal baru, agar sistem mengenali program yang baru saja di-_build_:
   ```bash
   source install/setup.bash
   ```
