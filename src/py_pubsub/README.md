# 📡 Modul: Publisher & Subscriber (Python)

Package ini mengajarkan konsep paling fundamental dalam ROS 2: **Pub/Sub** (Publisher & Subscriber) menggunakan bahasa Python.

## 📖 Konsep Dasar: Apa itu Publisher & Subscriber?

Konsep Pub/Sub adalah arsitektur komunikasi data satu arah secara kontinu (streaming).
- **Publisher**: Node pengirim data. Ia menulis pesan ke dalam suatu saluran komunikasi yang disebut "Topik" (Topic).
- **Subscriber**: Node penerima data. Ia membaca/mendengarkan pesan yang masuk ke "Topik" tersebut.

Karakteristik Topic di ROS 2:
- **Many-to-Many**: Satu topik bisa memiliki banyak publisher dan banyak subscriber secara bersamaan.
- Sangat cocok untuk data sensor yang dikirim berulang, seperti data kecepatan roda, suhu, atau _odometry_.

## 🛠️ Struktur Package
- `publisher_member_function.py`: Node yang secara konstan mempublikasikan data (pesan teks) ke topik tertentu.
- `launch/`: Direktori yang berisi file _Launch_ untuk menjalankan banyak node sekaligus hanya dengan satu perintah (mendukung format XML, YAML, dan Python).

## 💻 Cara Menjalankan

1. Pastikan telah di-build dan di-source:
   ```bash
   colcon build --packages-select py_pubsub
   source install/setup.bash
   ```

2. **Menjalankan Node Secara Manual (Terpisah):**
   - Terminal 1 (Publisher): `ros2 run py_pubsub talker`
   - Terminal 2 (Subscriber): `ros2 run py_pubsub listener`

3. **Menjalankan Node dengan Launch File:**
   Anda dapat menjalankan keduanya sekaligus dalam satu terminal menggunakan _Launch file_:
   ```bash
   ros2 launch py_pubsub python_example.launch.py
   ```
   *Sistem akan otomatis menjalankan node publisher dan subscriber secara bersamaan.*
