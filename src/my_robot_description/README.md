# 🤖 Modul: URDF & Simulasi Gazebo

Package ini difokuskan pada pemodelan fisik robot dan bagaimana membawa robot tersebut ke dalam dunia simulasi **Gazebo**.

## 📖 Konsep Dasar: URDF & Gazebo

1. **URDF (Unified Robot Description Format)**:
   Ini adalah format file berbasis XML standar ROS untuk mendefinisikan struktur fisik robot. Di sini Anda mendefinisikan bentuk, massa, inersia, warna, hingga sendi (*joint*) yang menghubungkan komponen satu dan komponen lain (misal: roda dengan body utama).

2. **Gazebo Simulator**:
   Gazebo adalah simulator fisika 3D yang sangat kuat. Melalui package bawaan ROS, kita bisa "melahirkan" (spawn) file URDF kita ke dunia Gazebo. Gazebo akan memberikan efek gravitasi, mencegah benturan tembus, dan memungkinkan robot digerakkan secara virtual seolah-olah di dunia nyata menggunakan plugin (seperti *differential drive plugin* atau sensor LiDAR).

## 🛠️ Struktur Package
- `urdf/my_robot.urdf`: File utama yang mendeskripsikan kerangka fisik robot dan mengimpor plugin simulasi.
- `config/bridge.yaml`: File konfigurasi yang bertugas "menjembatani" topik dari Gazebo Harmonic agar bisa dibaca atau ditulis oleh ROS 2 Jazzy.

## 💻 Cara Penggunaan dan Integrasi

*(Untuk instruksi detail integrasi, pelajari selengkapnya di laporan [Laporan Integrasi Gazebo](../../docs/laporan_integrasi_gazebo_dan_ros.md))*

1. Build paket ini:
   ```bash
   colcon build --packages-select my_robot_description
   source install/setup.bash
   ```

2. *Workflow* penggunaannya biasanya melibatkan _launch file_ yang akan:
   - Membuka lingkungan dunia Gazebo (`ros_gz_sim`).
   - Menerjemahkan node `robot_state_publisher` agar ROS tahu bentuk robot.
   - Melakukan eksekusi *Spawning* model URDF ke Gazebo (`ros_gz_sim create`).
   - Membuka jembatan (`ros_gz_bridge`) menggunakan `bridge.yaml`.
