# 🚀 Modul: ROS 2 Actions (Python)

Selamat datang di modul pembelajaran **ROS 2 Actions**. Package `action_tutorials_py` ini adalah implementasi _Action Server_ dan _Action Client_ menggunakan bahasa pemrograman Python.

## 📖 Konsep Dasar: Apa itu Action?

Dalam ROS 2, terdapat tiga cara utama komunikasi antar _node_:
1. **Topics (Publisher/Subscriber)**: Streaming data satu arah (terus-menerus tanpa henti).
2. **Services (Client/Server)**: Pemanggilan fungsi sinkron (request-response singkat).
3. **Actions**: Digunakan untuk **proses jangka panjang** (long-running tasks) yang membutuhkan proses bertahap.

**Kapan menggunakan Action?**
Gunakan action saat Anda menyuruh robot melakukan tugas yang butuh waktu lama (misalnya: "Navigasi ke ruangan B" atau "Hitung deret Fibonacci hingga angka ke-10"). Selama proses berjalan, Action dapat memberikan **Feedback** secara _real-time_ sebelum memberikan hasil akhir (**Result**).

## 🛠️ Struktur Package
- `fibonacci_action_server.py`: Node yang memproses permintaan (menghitung deret Fibonacci secara bertahap).
- `fibonacci_action_client.py`: Node yang mengirimkan permintaan target dan menerima feedback.

## 💻 Cara Menjalankan

1. Pastikan Anda telah melakukan *build* workspace dan mengaktifkan environment:
   ```bash
   colcon build --packages-select action_tutorials_py
   source install/setup.bash
   ```

2. Buka **Terminal 1**, jalankan Action Server:
   ```bash
   ros2 run action_tutorials_py fibonacci_action_server
   ```
   *Terminal ini akan diam (standby) menunggu request masuk.*

3. Buka **Terminal 2**, jalankan Action Client (pastikan di-source juga):
   ```bash
   source install/setup.bash
   ros2 run action_tutorials_py fibonacci_action_client
   ```

**Output yang Diharapkan:**
Client akan meminta target Fibonacci (misal: urutan ke-10). Server akan menghitung perlahan-lahan dan mengirimkan _feedback_ progres ke client. Setelah selesai, server mengirimkan _result_ (hasil akhir).
