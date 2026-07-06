# 🐢 Modul: Transform & TF2

Package ini dibuat untuk memahami salah satu pustaka (*library*) paling penting dalam navigasi robotika: **TF2 (Transform Library)**.

## 📖 Konsep Dasar: Apa itu TF?

**TF (Transform)** digunakan untuk melacak koordinat setiap bagian robot dan lingkungannya dalam bentuk _tree_ (pohon hubungan kekerabatan). 
Bayangkan sebuah robot: sensor LiDAR ada di atas, roda ada di bawah. Jika sensor LiDAR mendeteksi dinding di jarak 1 meter dari perspektif `lidar_link`, sistem harus menerjemahkan jarak tersebut relatif terhadap pusat robot (`base_link`) agar robot tahu dengan pasti jarak dinding dari badannya.

Fungsi utama TF2:
- Melacak perubahan posisi dan rotasi antar komponen (seperti tangan robot terhadap bahu).
- Melakukan konversi matematika antar koordinat secara otomatis _real-time_.

## 🛠️ Struktur Package
- `turtle_tf_broadcaster.py`: Node Python ini membaca *pose* (posisi X, Y, dan rotasi Theta) dari robot simulasi Turtlesim, lalu menerbitkannya (broadcast) sebagai data TF agar sistem lain tahu di mana posisi Turtlesim tersebut di dunia (world frame).

## 💻 Cara Menjalankan

1. Lakukan build dan source:
   ```bash
   colcon build --packages-select turtle_tf_broadcaster
   source install/setup.bash
   ```

2. Buka node Turtlesim (biasanya menggunakan `ros2 run turtlesim turtlesim_node`).

3. Di Terminal lain, jalankan node Broadcaster ini:
   ```bash
   ros2 run turtle_tf_broadcaster broadcaster
   ```
   *Node ini akan berjalan dan siap mem-broadcast pergerakan turtle.*
