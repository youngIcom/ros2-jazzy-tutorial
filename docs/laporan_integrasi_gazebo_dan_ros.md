# LAPORAN PRAKTIKUM

## **Integrasi ROS2 & Gazebo: Spawn URDF, Bridge, Interoperability, dan Template**

---

## **HALAMAN JUDUL**

|                     |                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Judul Praktikum** | Integrasi ROS2 dan Gazebo: Spawn URDF, ROS2 Integration Via Bridge, ROS2 Interoperability, dan ROS2 Integration Template |
| **Mata Kuliah**     | [Nama Mata Kuliah — contoh: Robotika / Simulasi Robot]                                                                   |

---

## **DAFTAR ISI**

1. Pendahuluan
2. Dasar Teori
3. Alat dan Bahan
4. Prosedur Percobaan
   - 4.1 Percobaan 1: Spawn URDF ke dalam Gazebo
   - 4.2 Percobaan 2: ROS2 Integration Via Bridge
   - 4.3 Percobaan 3: ROS2 Interoperability
   - 4.4 Percobaan 4: ROS2 Integration Template
5. Hasil Percobaan
   - 5.1 Hasil Percobaan 1
   - 5.2 Hasil Percobaan 2
   - 5.3 Hasil Percobaan 3
   - 5.4 Hasil Percobaan 4
6. Analisis dan Pembahasan
7. Kesimpulan
8. Daftar Pustaka
9. Lampiran

---

## **1. PENDAHULUAN**

### 1.1 Latar Belakang

Perkembangan industri robotika modern membutuhkan sistem yang mampu melakukan simulasi secara akurat sebelum implementasi pada hardware nyata. Gazebo merupakan salah satu simulator 3D yang paling banyak digunakan dalam komunitas robotika, sedangkan ROS2 (Robot Operating System 2) menjadi framework de facto untuk pengembangan perangkat lunak robot. Integrasi antara ROS2 dan Gazebo memungkinkan pengembang untuk melakukan simulasi sensor, aktuator, dan algoritma kontrol dalam lingkungan virtual yang mendekati kondisi nyata.

Pada praktikum ini, dibahas beberapa aspek kunci dari integrasi ROS2 dan Gazebo, mulai dari proses _spawn_ model robot yang didefinisikan dalam format URDF (Unified Robot Description Format) ke dalam lingkungan simulasi Gazebo, hingga penggunaan _bridge_ untuk menghubungkan komunikasi antara ROS2 dan Gazebo. Selain itu, dibahas pula aspek _interoperability_ yang memungkinkan komponen-komponen dari versi ROS yang berbeda untuk berkomunikasi, serta penggunaan template integrasi sebagai kerangka kerja standar untuk mempercepat proses pengembangan.

### 1.2 Tujuan Praktikum

1. Memahami proses _spawn_ model URDF ke dalam simulasi Gazebo.
2. Mengimplementasikan komunikasi antara ROS2 dan Gazebo menggunakan _ros_gz_bridge_.
3. Memahami konsep dan implementasi _interoperability_ pada ROS2.
4. Menggunakan dan memodifikasi template integrasi ROS2-Gazebo sebagai dasar pengembangan proyek robotika.

### 1.3 Manfaat Praktikum

1. Memberikan pemahaman langsung mengenai arsitektur integrasi ROS2-Gazebo.
2. Menjadi bekal untuk pengembangan proyek simulasi robot yang lebih kompleks.
3. Membiasakan mahasiswa dengan _workflow_ pengembangan robotika berbasis ROS2.

---

## **2. DASAR TEORI**

### 2.1 Gazebo Simulator

Gazebo adalah simulator 3D open-source yang mampu mensimulasikan robot, sensor, dan lingkungan secara fisik akurat. Gazebo mendukung berbagai jenis sensor (LiDAR, kamera, IMU) serta engine fisika (ODE, Bullet, DART) yang memungkinkan simulasi dinamika robot secara realistis. Pada versi terbaru, Gazebo hadir dalam dua varian utama: **Gazebo Classic** (berbasis Qt5, sering digunakan dengan ROS Noetic) dan **Gazebo (Ignition/Garden/Fortress/Harmonic)** yang merupakan generasi baru berbasis arsitektur modular.

### 2.2 URDF (Unified Robot Description Format)

URDF adalah format XML yang digunakan untuk merepresentasikan model robot secara hierarkis. URDF mendefinisikan komponen robot melalui dua elemen utama:

- **`<link>`**: Merepresentasikan segmen fisik robot (badan, roda, lengan, dsb.) beserta properti visual (_mesh_, warna, ukuran) dan properti kolisi (_collision_).
- **`<joint>`**: Merepresentasikan hubungan kinematik antara dua _link_ (revolute, prismatic, fixed, continuous, dsb.).

```
Contoh struktur sederhana:
<robot name="my_robot">
  <link name="base_link"> ... </link>
  <link name="wheel_link"> ... </link>
  <joint name="wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="wheel_link"/>
    <origin xyz="0.1 0 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>
</robot>
```

### 2.3 ROS2 (Robot Operating System 2)

ROS2 adalah evolusi dari ROS1 yang dibangun di atas middleware DDS (Data Distribution Service). Perbedaan utama antara ROS2 dan ROS1 meliputi:

| Aspek       | ROS1                     | ROS2                |
| ----------- | ------------------------ | ------------------- |
| Arsitektur  | Master-Slave (rosmaster) | Peer-to-peer (DDS)  |
| Real-time   | Terbatas                 | Mendukung real-time |
| Keamanan    | Tidak built-in           | Built-in (SROS2)    |
| Multi-robot | Sulit                    | Native support      |
| Discovery   | Centralized              | Distributed         |

### 2.4 ros_gz_bridge

`ros_gz_bridge` adalah paket yang menyediakan _bridge_ komunikasi antara ROS2 dan Gazebo (khususnya Gazebo Sim/Ignition). Bridge ini menerjemahkan pesan dari topik ROS2 ke topik Gazebo dan sebaliknya. Tipe-tipe pesan yang didukung meliputi:

- `std_msgs` (String, Float32, Bool, dll.)
- `geometry_msgs` (Twist, Pose, Wrench, dll.)
- `sensor_msgs` (Image, LaserScan, Imu, PointCloud2, dll.)
- `nav_msgs` (Odometry, dll.)
- `tf2_msgs` (TFMessage)

```
Contoh konfigurasi bridge:
ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```

Format umum: `<topic_ros>@<type_ros>@<type_gz>`

### 2.5 ROS2 Interoperability

_Interoperability_ pada ROS2 merujuk pada kemampuan komponen-komponen yang dibangun dengan versi atau konfigurasi berbeda untuk saling berkomunikasi. Hal ini mencakup:

- **DDS Interoperability**: ROS2 menggunakan DDS sebagai middleware. Berbagai implementasi DDS (Fast DDS, Cyclone DDS, Connext DDS) dapat saling berkomunikasi selama menggunakan pengaturan yang kompatibel.
- **ROS1-ROS2 Bridge**: Menggunakan `ros1_bridge` untuk komunikasi antara node ROS1 dan ROS2 secara bersamaan.
- **Cross-domain communication**: Komunikasi antara node ROS2 pada _domain_ DDS yang berbeda.

### 2.6 ROS2 Integration Template

Template integrasi merupakan kerangka kerja (_boilerplate_) yang menyediakan struktur paket ROS2 siap pakai untuk integrasi dengan Gazebo. Template ini biasanya mencakup:

- Struktur direktori paket ROS2 standar (`src/`, `launch/`, `config/`, `urdf/`, `worlds/`)
- File _launch_ yang mengatur urutan启动 Gazebo, spawn robot, dan bridge
- File konfigurasi parameter (YAML)
- Contoh URDF dengan plugin Gazebo yang sudah terkonfigurasi

---

## **3. ALAT DAN BAHAN**

### 3.1 Perangkat Keras (Hardware)

- Komputer/Laptop dengan spesifikasi:
  - Prosesor: Minimal Intel Core i5 atau setara
  - RAM: Minimal 8 GB (direkomendasikan 16 GB)
  - GPU: Mendukung OpenGL 3.3+ (untuk rendering Gazebo)
  - Storage: Minimal 20 GB ruang kosong

### 3.2 Perangkat Lunak (Software)

- Sistem Operasi: Ubuntu 24.04 LTS
- ROS2 Distribution: ROS2 Jazzy Jalisco
- Gazebo: Gazebo Fortress / Gazebo Harmonic
- Paket ROS2 tambahan:
  - `ros-jazzy-ros-gz`
  - `ros-jazzy-ros-gz-bridge`
  - `ros-jazzy-ros-gz-sim`
  - `ros-jazzy-xacro`
  - `ros-jazzy-joint-state-publisher`
  - `ros-jazzy-robot-state-publisher`
- Text Editor / IDE: VS Code / Neovim
- Terminal emulator: GNOME Terminal / Tilix

### 3.3 Bahan Percobaan

- File URDF robot sederhana (disediakan atau dibuat sendiri)
- File world Gazebo (disediakan)
- File konfigurasi bridge (YAML)
- Template integrasi ROS2-Gazebo

---

## **4. PROSEDUR PERCOBAAN**

### 4.1 Percobaan 1: Spawn URDF ke dalam Gazebo

**Tujuan**: Memuat model robot dari file URDF ke dalam lingkungan simulasi Gazebo.

**Langkah-langkah**:

1. Buka terminal dan _source_ environment ROS2:

   ```bash
   source /opt/ros/jazzy/setup.bash
   ```

2. Pastikan semua paket yang dibutuhkan terinstal:

   ```bash
   sudo apt install ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge
   ```

3. Buat workspace dan paket ROS2 baru (jika belum ada):

   ```bash
   mkdir -p ~/ros2_praktikum/src
   cd ~/ros2_praktikum/src
   ros2 pkg create --build-type ament_cmake my_robot_description \
     --dependencies urdf xacro
   ```

4. Siapkan file URDF robot pada direktori `urdf/` di dalam paket.

5. Jalankan Gazebo Sim:

   ```bash
   gz sim -v 4 empty.sdf
   ```

6. Spawn URDF ke dalam Gazebo menggunakan service call:

   ```bash
   ros2 run ros_gz_sim create -urdf -param robot_description \
     -x 0 -y 0 -z 0.5 -topic /robot_description
   ```

   _Atau melalui launch file yang mengintegrasikan kedua langkah di atas._

7. Amati model robot yang muncul di dalam Gazebo.

8. **(Opsional)** Verifikasi model dengan `joint_state_publisher`:
   ```bash
   ros2 run joint_state_publisher_gui joint_state_publisher_gui
   ```

---

### 4.2 Percobaan 2: ROS2 Integration Via Bridge

**Tujuan**: Menghubungkan komunikasi antara ROS2 dan Gazebo menggunakan `ros_gz_bridge`.

**Langkah-langkah**:

1. Pastikan Gazebo berjalan dan robot `my_robot.urdf` sudah berhasil di-_spawn_ (dari Percobaan 1).
   Pastikan juga simulasi dalam keadaan berjalan (_Play_), tidak di-_Pause_.

2. Buat folder konfigurasi dan buat file `bridge.yaml` di dalamnya:

   ```bash
   mkdir -p ~/ros2_praktikum/src/my_robot_description/config
   nano ~/ros2_praktikum/src/my_robot_description/config/bridge.yaml
   ```

3. Isi file `bridge.yaml` dengan pemetaan topik berikut (terutama pemetaan topik `/scan` ke `/lidar` Gazebo):

   ```yaml
   # config/bridge.yaml
   - ros_topic_name: "/cmd_vel"
     gz_topic_name: "/cmd_vel"
     ros_type_name: "geometry_msgs/msg/Twist"
     gz_type_name: "gz.msgs.Twist"
     direction: ROS_TO_GZ

   - ros_topic_name: "/odom"
     gz_topic_name: "/odom"
     ros_type_name: "nav_msgs/msg/Odometry"
     gz_type_name: "gz.msgs.Odometry"
     direction: GZ_TO_ROS

   - ros_topic_name: "/scan"
     gz_topic_name: "/lidar"
     ros_type_name: "sensor_msgs/msg/LaserScan"
     gz_type_name: "gz.msgs.LaserScan"
     direction: GZ_TO_ROS
   ```

4. Jalankan node bridge menggunakan file konfigurasi YAML tersebut di terminal baru:

   ```bash
   ros2 run ros_gz_bridge parameter_bridge \
     --ros-args -p config_file:=$HOME/ros2_praktikum/src/my_robot_description/config/bridge.yaml
   ```

5. Verifikasi pengiriman perintah gerak dari terminal ROS2 ke Gazebo:

   ```bash
   ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
     "{linear: {x: 0.5}, angular: {z: 0.3}}"
   ```

6. Amati pergerakan robot secara fisik di GUI Gazebo.

7. Verifikasi data odometri dan sensor LiDAR yang diterima oleh ROS2 dari Gazebo:

   ```bash
   ros2 topic echo /odom
   ros2 topic echo /scan
   ```

8. Daftarkan dan periksa seluruh topik yang aktif dari kedua belah pihak:
   ```bash
   ros2 topic list
   gz topic -l
   ```

---

### 4.3 Percobaan 3: ROS2 Interoperability

**Tujuan**: Menguji kemampuan interoperabilitas antara komponen ROS2 yang berbeda.

**Langkah-langkah**:

1. **Cek implementasi DDS utama yang aktif**:

   ```bash
   ros2 doctor --report | grep -i rmw
   ```

   _(Pesan ini seharusnya menunjukkan `middleware name : rmw_fastrtps_cpp`)_

2. **Instalasi DDS alternatif** (menambahkan Cyclone DDS ke dalam sistem):

   ```bash
   sudo apt install ros-jazzy-rmw-cyclonedds-cpp
   ```

3. Jalankan publisher pada **Terminal 1** (dengan Fast DDS bawaan):

   ```bash
   export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
   source /opt/ros/jazzy/setup.bash
   ros2 topic pub /test_interop std_msgs/msg/String "{data: 'Hello dari Fast DDS'}" -r 1
   ```

   _(Pesan akan terus-menerus disiarkan dengan interval 1 detik)_

4. Jalankan subscriber pada **Terminal 2** (menggunakan Cyclone DDS yang baru diinstal):

   ```bash
   export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
   source /opt/ros/jazzy/setup.bash
   ros2 topic echo /test_interop
   ```

   _(Perhatikan apakah Terminal 2 berhasil menerima pesan dari Terminal 1 meskipun mesin komunikasinya berbeda. Ini membuktikan interoperabilitas antar-vendor DDS pada ROS 2)._

5. **Uji isolasi jaringan (ROS Domain ID)**:
   ROS2 memisahkan jaringan komunikasi menggunakan ID unik. Mari kita buktikan.

   Pada **Terminal 3** (Gunakan Domain 42):

   ```bash
   export ROS_DOMAIN_ID=42
   source /opt/ros/jazzy/setup.bash
   ros2 topic echo /test_interop
   ```

6. Catat hasilnya dan analisis mengapa pesan di Terminal 3 tidak muncul (terisolasi), sedangkan di Terminal 2 tetap muncul.

---

### 4.4 Percobaan 4: ROS2 Integration Template

**Tujuan**: Menggunakan template integrasi ROS2-Gazebo sebagai kerangka kerja untuk proyek robotika.

**Langkah-langkah**:

1. Clone template resmi integrasi ROS 2 - Gazebo (dikelola langsung oleh tim OSRF):

   ```bash
   cd ~/ros2_praktikum/src
   git clone https://github.com/gazebosim/ros_gz_project_template.git
   ```

2. Pelajari struktur direktori template tingkat lanjut ini. Template resmi ini membagi arsitekturnya menjadi beberapa _package_ yang modular:

   ```
   ros_gz_project_template/
   ├── ros_gz_example_application/   # Berisi algoritma logika/kontrol (Python/C++)
   ├── ros_gz_example_bringup/       # Berisi launch files dan konfigurasi bridge (YAML)
   ├── ros_gz_example_description/   # Berisi model URDF/SDF, mesh, dan parameter robot
   └── ros_gz_example_gazebo/        # Berisi dunia (worlds) dan plugin spesifik Gazebo
   ```

3. Build _workspace_ khusus untuk paket-paket dari template tersebut:

   ```bash
   cd ~/ros2_praktikum
   # Menginstal dependensi otomatis menggunakan rosdep (jika belum)
   rosdep install --from-paths src -y --ignore-src

   # Set environment variable agar template di-build untuk versi Harmonic (Jazzy)
   export GZ_VERSION=harmonic

   # Build template (hanya mem-build direktori template)
   colcon build --packages-up-to ros_gz_example_bringup
   source install/setup.bash
   ```

4. Jalankan _launch file_ utama yang sudah terintegrasi (sekaligus membuka Gazebo, men-spawn robot diff-drive bawaan template, dan mengaktifkan Bridge):

   ```bash
   ros2 launch ros_gz_example_bringup diff_drive.launch.py
   ```

5. Verifikasi pengoperasian template dengan mengirim perintah gerak. Buka terminal baru:

   ```bash
   source ~/ros2_praktikum/install/setup.bash
   ros2 topic pub /diff_drive/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.5}}"
   ```

   _(Amati robot bergerak berputar di dalam Gazebo)_

6. **Modifikasi template (Tugas Tambahan)** — lakukan salah satu:
   - **a.** Masuk ke `ros_gz_example_description` dan ubah warna atau bentuk geometri robot.
   - **b.** Masuk ke `ros_gz_example_gazebo/worlds` dan tambahkan halangan (obstacle) baru ke dalam peta simulasi.

7. Rebuild dengan `colcon build` dan jalankan ulang untuk mengamati modifikasi yang Anda buat.

8. Catat seluruh topik ROS 2 dan topik Gazebo yang dijembatani secara otomatis oleh template ini:
   ```bash
   ros2 topic list
   gz topic -l
   ```

---

## **5. KESIMPULAN**

Praktikum integrasi ROS 2 dengan Gazebo ini secara keseluruhan berjalan dengan baik dan memberikan banyak pelajaran yang berharga. Tidak semua langkah berjalan mulus di percobaan pertama — ada kendala teknis seperti model robot yang ditolak Gazebo karena tidak memiliki parameter fisika — namun justru dari sinilah pemahaman yang lebih dalam terbentuk.

Dari serangkaian percobaan yang telah dilakukan, berikut adalah poin-poin utama yang dapat disimpulkan:

1. **Spawn URDF ke Gazebo**: Untuk mensimulasikan robot di Gazebo, sebuah model URDF tidak cukup hanya memiliki bagian visual saja. Gazebo sebagai simulator fisika mengharuskan setiap _link_ memiliki blok `<inertial>` (massa dan momen inersia) serta `<collision>` (batas tabrakan). Tanpa keduanya, Gazebo akan menolak model tersebut karena dianggap tidak memiliki massa fisik yang valid.

2. **ROS 2 Integration Via Bridge**: Komunikasi dua arah antara ROS 2 dan Gazebo berhasil dibangun menggunakan `ros_gz_bridge`. Dengan mendefinisikan pemetaan topik dalam satu file konfigurasi YAML, perintah gerak dari topik `/cmd_vel` dapat diteruskan ke simulator, sementara data sensor (`/scan`) dan odometri (`/odom`) dapat mengalir kembali ke ROS 2. Pendekatan YAML ini jauh lebih efisien daripada menjalankan _bridge_ satu per satu secara manual di terminal yang berbeda.

3. **ROS 2 Interoperability**: Salah satu keunggulan mendasar ROS 2 yang terbukti dalam praktikum ini adalah kemampuannya untuk menjalankan komunikasi antar-_node_ meskipun keduanya menggunakan implementasi DDS yang berbeda (Fast DDS dan Cyclone DDS). Di sisi lain, pengujian isolasi jaringan menggunakan `ROS_DOMAIN_ID` membuktikan bahwa _node_ yang berada pada _domain_ yang berbeda tidak dapat saling berkomunikasi, yang merupakan mekanisme penting untuk memisahkan beberapa sistem ROS di dalam satu jaringan yang sama.

4. **ROS 2 Integration Template**: Penggunaan template resmi `ros_gz_project_template` dari OSRF menunjukkan cara yang lebih profesional dan terstruktur dalam membangun proyek robotika. Dengan memisahkan kode ke dalam beberapa _package_ modular (deskripsi, bringup, aplikasi, dan Gazebo), template ini mempercepat proses pengembangan karena seluruh komponen — mulai dari _launch file_, konfigurasi _bridge_, model robot, hingga _world_ simulasi — sudah tersedia dan saling terintegrasi secara otomatis.

Secara keseluruhan, praktikum ini memberikan fondasi yang kuat untuk memahami ekosistem pengembangan robot modern. Kemampuan untuk mensimulasikan, menghubungkan, dan menguji sistem robot secara virtual sebelum diimplementasikan pada perangkat keras nyata adalah kompetensi yang sangat krusial dalam dunia robotika saat ini.

---

## **8. DAFTAR PUSTAKA**

```
[1]  Open Robotics, "ROS 2 Documentation: Jazzy,"
     https://docs.ros.org/en/jazzy/, diakses [tanggal akses].

[2]  Gazebo Project, "Gazebo Sim Documentation,"
     https://gazebosim.org/docs, diakses [tanggal akses].

[3]  Open Robotics, "ros_gz_bridge — ROS 2 Package Documentation,"
     https://docs.ros.org/en/jazzy/p/ros_gz_bridge/, diakses [tanggal akses].

[4]  Open Robotics, "URDF — ROS 2 Tutorial,"
     https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html,
     diakses [tanggal akses].

[5]  OMG, "DDS (Data Distribution Service) Specification,"
     https://www.omg.org/spec/DDS/, diakses [tanggal akses].

[6]  Macenski, S., et al., "The Marathon 2: A Navigation System,"
     IEEE RAM, 2023.

[7]  [Tambahkan referensi lain yang relevan — buku, jurnal, dll.]
```

---

> **Catatan**: Format laporan ini mengikuti standar penulisan laporan praktikum di bidang teknik/informatika. Sesuaikan bagian-bagian tertentu (nama dosen, asisten, format referensi) dengan ketentuan yang berlaku di laboratorium/tempat praktikum Anda.
