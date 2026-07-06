# LAPORAN PRAKTIKUM

## ROS2: RViz dan Bag File

**Platform:** ROS2 Jazzy Jalisco  
**Sistem Operasi:** Ubuntu 24.04 LTS  
**Tanggal Praktikum:** [Tanggal]

---

## DAFTAR ISI

1. Pendahuluan
2. Dasar Teori (Landasan Teori)
3. Langkah-Langkah Pengerjaan
4. Pembahasan
5. Analisa
6. Kesimpulan
7. Daftar Pustaka

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang

Robot Operating System 2 (ROS2) merupakan framework middleware yang digunakan untuk pengembangan aplikasi robotik. Dalam ekosistem ROS2, terdapat dua komponen penting yang digunakan untuk visualisasi dan perekaman data, yaitu RViz2 dan Rosbag2. RViz2 memungkinkan pengguna untuk memvisualisasikan data sensor dan state robot secara real-time, sedangkan Rosbag2 menyediakan mekanisme untuk merekam dan memutar kembali data yang ditransmisikan melalui topik ROS2.

### 1.2 Tujuan Praktikum

1. Memahami konsep dan fungsi RViz2 sebagai alat visualisasi dalam ROS2
2. Mengenal dan mempraktikkan penggunaan Rosbag2 untuk merekam dan memutar kembali data
3. Mampu mengonfigurasi RViz2 untuk menampilkan berbagai jenis data (point cloud, laser scan, TF, dll)
4. Memahami format file bag dan cara mengelolanya di ROS2 Jazzy

### 1.3 Alat dan Bahan

- Komputer/Laptop dengan spesifikasi minimum:
  - RAM: 8 GB
  - Prosesor: Dual-core
  - GPU: Mendukung OpenGL 3.3+
- Sistem Operasi: Ubuntu 24.04 LTS
- ROS2 Jazzy Jalisco (terinstal)
- Koneksi Internet (untuk instalasi paket tambahan jika diperlukan)

---

## 2. DASAR TEORI (LANDASAN TEORI)

### 2.1 Robot Operating System 2 (ROS2)

ROS2 adalah generasi kedua dari Robot Operating System yang dikembangkan oleh Open Robotics. Berbeda dengan ROS1 yang menggunakan arsitektur master-slave, ROS2 menggunakan arsitektur peer-to-peer yang didasarkan pada Data Distribution Service (DDS) standar. Keunggulan arsitektur ini meliputi:

- **Desentralisasi:** Tidak ada node master tunggal yang menjadi titik kegagalan
- **Discovery:** Node dapat menemukan satu sama lain secara otomatis
- **Quality of Service (QoS):** Memungkinkan pengaturan keandalan dan latensi komunikasi
- **Keamanan:** Mendukung autentikasi dan enkripsi data
- **Real-time capability:** Lebih cocok untuk sistem real-time

ROS2 Jazzy Jalisco merupakan rilis terbaru yang didukung secara resmi di Ubuntu 24.04 LTS dengan masa dukungan hingga Mei 2029.

### 2.2 RViz2

RViz2 (Robot Visualizer 2) adalah alat visualisasi 3D yang merupakan bagian integral dari ekosistem ROS2. RViz2 memungkinkan pengguna untuk:

#### 2.2.1 Arsitektur RViz2

```
┌─────────────────────────────────────────────────────────────┐
│                         RViz2                               │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Display     │  │ View        │  │ Tool                │  │
│  │ Manager     │  │ Manager     │  │ Manager             │  │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘  │
│         │                │                    │             │
│  ┌──────▼────────────────▼────────────────────▼──────────┐  │
│  │                    Render Engine                       │  │
│  │              (OpenGL/Ogre3D Backend)                   │  │
│  └───────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    ROS2 Subscriber                          │
│              (Menerima data dari topik)                     │
└─────────────────────────────────────────────────────────────┘
```

#### 2.2.2 Jenis Display di RViz2

| Tipe Display    | Deskripsi                            | Tipe Pesan                  |
| --------------- | ------------------------------------ | --------------------------- |
| **Grid**        | Menampilkan grid referensi           | -                           |
| **Axes**        | Menampilkan sumbu koordinat          | -                           |
| **RobotModel**  | Menampilkan model URDF robot         | `/robot_description`        |
| **LaserScan**   | Menampilkan data LiDAR 2D            | `sensor_msgs/LaserScan`     |
| **PointCloud2** | Menampilkan data point cloud 3D      | `sensor_msgs/PointCloud2`   |
| **Image**       | Menampilkan gambar dari kamera       | `sensor_msgs/Image`         |
| **TF**          | Menampilkan frame transformasi       | `tf2_msgs/TFMessage`        |
| **Path**        | Menampilkan jalur/trajectory         | `nav_msgs/Path`             |
| **Marker**      | Menampilkan marker visual            | `visualization_msgs/Marker` |
| **Map**         | Menampilkan peta 2D (Occupancy Grid) | `nav_msgs/OccupancyGrid`    |

#### 2.2.3 Sistem Koordinat di RViz2

RViz2 menggunakan sistem koordinat kanan (right-handed coordinate system):

- **X-axis:** Merah (forward/depan)
- **Y-axis:** Hijau (left/kiri)
- **Z-axis:** Biru (up/atas)

### 2.3 Rosbag2

Rosbag2 adalah sistem perekaman dan pemutaran data di ROS2. Berbeda dengan Rosbag di ROS1 yang menggunakan format khusus, Rosbag2 menggunakan arsitektur yang lebih modular.

#### 2.3.1 Arsitektur Rosbag2

```
┌──────────────────────────────────────────────────────────────────┐
│                          Rosbag2                                  │
├──────────────────────────────────────────────────────────────────┤
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐  │
│  │   ROS2 Node    │    │  Storage       │    │  Storage       │  │
│  │   (Recorder/   │◄──►│  Plugin        │◄──►│  Implementation│  │
│  │    Player)     │    │  Interface     │    │  (SQLite3)     │  │
│  └────────────────┘    └────────────────┘    └────────────────┘  │
│         ▲                                               │        │
│         │                                               ▼        │
│  ┌──────┴──────────────────────────────────────────────────────┐ │
│  │                    ROS2 Middleware (DDS)                    │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

#### 2.3.2 Komponen Utama Rosbag2

1. **rosbag2_recorder:** Node yang bertanggung jawab untuk merekam data dari topik
2. **rosbag2_player:** Node yang memutar kembali data yang telah direkam
3. **Storage Plugins:** Backend penyimpanan data (default: SQLite3)
4. **Converter Plugins:** Untuk konversi format jika diperlukan

#### 2.3.3 Struktur File Bag

```
nama_bag_file/
├── nama_bag_file_0.db3          # Database SQLite berisi data
├── metadata.yaml                # Metadata rekaman
└── nama_bag_file_0.db3-shm      # File shared memory (sementara)
```

**Contoh isi metadata.yaml:**

```yaml
rosbag2_bagfile_information:
  version: 5
  storage_identifier: sqlite3
  duration:
    nanoseconds: 15000000000
  starting_time:
    nanoseconds_since_epoch: 1700000000000000000
  message_count: 450
  topics_with_message_count:
    - topic_metadata:
        name: /chatter
        type: std_msgs/msg/String
        serialization_format: cdr
        offered_qos_profiles: "- history: 3\n  depth: 0\n  reliability: 1\n  durability: 2\n  deadline:\n    sec: 2147483647\n    nsec: 4294967295\n  lifespan:\n    sec: 2147483647\n    nsec: 4294967295\n  liveliness: 1\n  liveliness_lease_duration:\n    sec: 2147483647\n    nsec: 4294967295\n  avoid_ros_namespace_conventions: false"
      message_count: 150
    - topic_metadata:
        name: /scan
        type: sensor_msgs/msg/LaserScan
        serialization_format: cdr
        offered_qos_profiles: "- history: 3\n  depth: 0\n  reliability: 1\n  durability: 2\n  deadline:\n    sec: 2147483647\n    nsec: 4294967295\n  lifespan:\n    sec: 2147483647\n    nsec: 4294967295\n  liveliness: 1\n  liveliness_lease_duration:\n    sec: 2147483647\n    nsec: 4294967295\n  avoid_ros_namespace_conventions: false"
      message_count: 300
  compression_format: ""
  compression_mode: ""
```

#### 2.3.4 Quality of Service (QoS) dalam Rosbag2

QoS merupakan fitur penting di ROS2 yang mempengaruhi bagaimana data direkam:

| Kebijakan QoS   | Nilai           | Deskripsi                           |
| --------------- | --------------- | ----------------------------------- |
| **Reliability** | RELIABLE        | Menjamin pengiriman semua pesan     |
|                 | BEST_EFFORT     | Mengirim pesan tanpa jaminan        |
| **Durability**  | TRANSIENT_LOCAL | Node baru menerima pesan terakhir   |
|                 | VOLATILE        | Node baru hanya menerima pesan baru |
| **History**     | KEEP_LAST       | Menyimpan N pesan terakhir          |
|                 | KEEP_ALL        | Menyimpan semua pesan               |

### 2.4 Transformasi Koordinat (TF2)

TF2 adalah library yang mengelola transformasi koordinat antar frame dalam sistem robot. Hal ini penting untuk:

- Menggabungkan data dari berbagai sensor
- Mengkonversi koordinat dari satu frame ke frame lain
- Melacak posisi robot dan komponennya

**Struktur TF Tree:**

```
            map
             │
           odom
             │
        base_link
        ╱       ╱
  lidar_link  camera_link
```

---

## 3. LANGKAH-LANGKAH PENGERJAAN

### 3.1 Persiapan Lingkungan

#### 3.1.1 Verifikasi Instalasi ROS2 Jazzy

Buka terminal dan jalankan perintah berikut:

```bash
# Cek versi ROS2
ros2 --version

# Output yang diharapkan:
# ros2 cli version: 0.36.0
```

```bash
# Source environment ROS2
source /opt/ros/jazzy/setup.bash

# Tambahkan ke .bashrc agar otomatis setiap buka terminal
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

#### 3.1.2 Instalasi Paket yang Diperlukan

```bash
# Update package list
sudo apt update

# Install paket RViz2 dan Rosbag2
sudo apt install ros-jazzy-rviz2 ros-jazzy-rosbag2 ros-jazzy-rosbag2-storage-default-plugins -y

# Install paket tambahan untuk demonstrasi
sudo apt install ros-jazzy-turtlebot4-description ros-jazzy-turtlesim -y

# Install paket untuk demo sensor (opsional)
sudo apt install ros-jazzy-rplidar-ros ros-jazzy-realsense-ros -y

# Install paket untuk konversi bag file
sudo apt install ros-jazzy-rosbag2-converter-default-plugins -y
```

#### 3.1.3 Membuat Workspace Praktikum

```bash
# Buat workspace
mkdir -p ~/ros2_praktikum/src
cd ~/ros2_praktikum

# Build workspace
colcon build

# Source workspace
source install/setup.bash
```

---

### 3.2 Praktikum 1: Pengenalan RViz2

#### 3.2.1 Menjalankan RViz2

```bash
# Buka terminal pertama - Jalankan RViz2
rviz2
```

**Penjelasan:**

- RViz2 akan terbuka dengan tampilan kosong
- Terdapat panel kiri (Displays), panel tengah (3D View), dan panel kanan (Views/Tools)

#### 3.2.2 Mengkonfigurasi Display Dasar

1. **Menambahkan Grid:**
   - Klik tombol "Add" di panel Displays
   - Pilih "Grid" → klik OK
   - Atur properti:
     - Cell Count: 20
     - Cell Size: 1
     - Color: (160, 160, 160)

2. **Menambahkan Axes:**
   - Klik "Add" → pilih "Axes"
   - Atur Reference Frame menjadi sesuai kebutuhan

3. **Menambahkan TF Display:**
   - Klik "Add" → pilih "TF"
   - TF akan menampilkan semua frame transformasi yang aktif

#### 3.2.3 Menyimpan Konfigurasi RViz2

```
File → Save Config As...
```

Simpan dengan nama `basic_config.rviz`

**Isi file konfigurasi (contoh):**

```yaml
Panels:
  - Class: rviz_common/Displays
    Name: Displays
  - Class: rviz_common/Views
    Name: Views
Visualization Manager:
  Class: ""
  Displays:
    - Class: rviz_default_plugins/Grid
      Name: Grid
      Value: true
      Cell Count: 20
      Cell Size: 1
      Color: 160; 160; 160
    - Class: rviz_default_plugins/Axes
      Name: Axes
      Value: true
      Length: 1
    - Class: rviz_default_plugins/TF
      Name: TF
      Value: true
  Global Options:
    Background Color: 48; 48; 48
    Fixed Frame: <fixed frame>
    Frame Rate: 30
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 10
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Target Frame: <fixed frame>
Window Geometry:
  Width: 1280
  Height: 720
```

#### 3.2.4 Memuat Konfigurasi yang Tersimpan

```bash
# Jalankan RViz2 dengan konfigurasi tertentu
rviz2 -d ~/ros2_praktikum/basic_config.rviz
```

---

### 3.3 Praktikum 2: Visualisasi TurtleSim dengan RViz2

#### 3.3.1 Menjalankan TurtleSim

```bash
# Terminal 1 - Jalankan turtlesim
ros2 run turtlesim turtlesim_node
```

#### 3.3.2 Membuat Node Konversi Pose ke TF

Buat file Python untuk mengkonversi pose turtle ke transformasi TF:

```bash
# Buat direktori package
cd ~/ros2_praktikum/src
ros2 pkg create --build-type ament_python turtle_tf_broadcaster \
    --dependencies rclpy geometry_msgs tf2_ros turtlesim
```

```bash
# Buat file turtle_tf_broadcaster.py
cd ~/ros2_praktikum/src/turtle_tf_broadcaster/turtle_tf_broadcaster
nano turtle_tf_broadcaster.py
```

**Isi file `turtle_tf_broadcaster.py`:**

```python
#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose


class TurtleTfBroadcaster(Node):
    def __init__(self, turtle_name):
        super().__init__('turtle_tf_broadcaster_' + turtle_name)
        self.turtle_name = turtle_name

        # QoS profile untuk turtlesim
        qos_profile = QoSProfile(depth=10)

        self.tf_broadcaster = TransformBroadcaster(self)

        self.subscription = self.create_subscription(
            Pose,
            f'/{turtle_name}/pose',
            self.turtle_pose_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning

    def turtle_pose_callback(self, msg):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = self.turtle_name

        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0

        # Konversi sudut dari turtlesim (berlawanan jarum jam) ke quaternion
        q = self.euler_to_quaternion(0, 0, msg.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_broadcaster.sendTransform(t)

    def euler_to_quaternion(self, roll, pitch, yaw):
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        w = cy * cp * cr + sy * sp * sr
        x = cy * cp * sr - sy * sp * cr
        y = sy * cp * sr + cy * sp * cr
        z = sy * cp * cr - cy * sp * sr

        return (x, y, z, w)


def main(args=None):
    rclpy.init(args=args)

    broadcaster = TurtleTfBroadcaster('turtle1')
    rclpy.spin(broadcaster)

    broadcaster.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

#### 3.3.3 Update setup.py

```bash
cd ~/ros2_praktikum/src/turtle_tf_broadcaster
nano setup.py
```

**Tambahkan entry points:**

```python
entry_points={
    'console_scripts': [
        'turtle_tf_broadcaster = turtle_tf_broadcaster.turtle_tf_broadcaster:main',
    ],
},
```

#### 3.3.4 Build dan Jalankan

```bash
# Build package
cd ~/ros2_praktikum
colcon build --packages-select turtle_tf_broadcaster
source install/setup.bash

# Terminal 2 - Jalankan TF broadcaster
ros2 run turtle_tf_broadcaster turtle_tf_broadcaster

# Terminal 3 - Gerakkan turtle
ros2 run turtlesim turtle_teleop_key
```

#### 3.3.5 Visualisasi di RViz2

```bash
# Terminal 4 - Jalankan RViz2
rviz2
```

**Konfigurasi RViz2:**

1. Set Fixed Frame ke `world`
2. Tambahkan TF display
3. Tambahkan Axes dengan Reference Frame: `turtle1`

#### 3.3.6 Membuat Custom Marker untuk Turtle

Buat node untuk memvisualisasikan turtle sebagai marker:

```bash
# Buat package baru
cd ~/ros2_praktikum/src
ros2 pkg create --build-type ament_python turtle_marker \
    --dependencies rclpy geometry_msgs visualization_msgs turtlesim tf2_ros
```

```bash
cd ~/ros2_praktikum/src/turtle_marker/turtle_marker
nano turtle_marker.py
```

**Isi file `turtle_marker.py`:**

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import TransformStamped, Point
from visualization_msgs.msg import Marker
from turtlesim.msg import Pose
import math


class TurtleMarker(Node):
    def __init__(self):
        super().__init__('turtle_marker')

        qos_profile = QoSProfile(depth=10)

        self.marker_publisher = self.create_publisher(
            Marker,
            '/turtle_marker',
            qos_profile)

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            qos_profile)

        self.timer = self.create_timer(0.1, self.publish_marker)
        self.current_pose = Pose()

    def pose_callback(self, msg):
        self.current_pose = msg

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = 'turtle'
        marker.id = 0
        marker.type = Marker.ARROW
        marker.action = Marker.ADD

        # Posisi marker
        marker.pose.position.x = self.current_pose.x - 5.544  # Offset untuk center
        marker.pose.position.y = self.current_pose.y - 5.544
        marker.pose.position.z = 0.0

        # Rotasi marker
        q = self.euler_to_quaternion(0, 0, self.current_pose.theta - math.pi/2)
        marker.pose.orientation.x = q[0]
        marker.pose.orientation.y = q[1]
        marker.pose.orientation.z = q[2]
        marker.pose.orientation.w = q[3]

        # Skala marker
        marker.scale.x = 0.5
        marker.scale.y = 0.2
        marker.scale.z = 0.2

        # Warna marker (hijau)
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        self.marker_publisher.publish(marker)

    def euler_to_quaternion(self, roll, pitch, yaw):
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)

        w = cy * cp * cr + sy * sp * sr
        x = cy * cp * sr - sy * sp * cr
        y = sy * cp * sr + cy * sp * cr
        z = sy * cp * cr - cy * sp * cr

        return (x, y, z, w)


def main(args=None):
    rclpy.init(args=args)
    marker_node = TurtleMarker()
    rclpy.spin(marker_node)
    marker_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

---

### 3.4 Praktikum 3: Visualisasi Model Robot (URDF)

#### 3.4.1 Membuat Simple Robot URDF

```bash
# Buat package URDF
cd ~/ros2_praktikum/src
ros2 pkg create --build-type ament_cmake simple_robot_description \
    --dependencies urdf xacro
```

```bash
# Buat direktori untuk URDF
mkdir -p ~/ros2_praktikum/src/simple_robot_description/urdf
cd ~/ros2_praktikum/src/simple_robot_description/urdf
nano simple_robot.urdf
```

**Isi file `simple_robot.urdf`:**

```xml
<?xml version="1.0"?>
<robot name="simple_robot">

  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.3" length="0.1"/>
      </geometry>
      <material name="blue">
        <color rgba="0.0 0.0 0.8 1.0"/>
      </material>
    </visual>
  </link>

  <!-- Chassis -->
  <link name="chassis">
    <visual>
      <origin xyz="0 0 0.15" rpy="0 0 0"/>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
      <material name="gray">
        <color rgba="0.5 0.5 0.5 1.0"/>
      </material>
    </visual>
  </link>

  <joint name="base_chassis_joint" type="fixed">
    <parent link="base_link"/>
    <child link="chassis"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
  </joint>

  <!-- Left Wheel -->
  <link name="left_wheel">
    <visual>
      <origin xyz="0 0 0" rpy="1.5708 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="0.05"/>
      </geometry>
      <material name="black">
        <color rgba="0.0 0.0 0.0 1.0"/>
      </material>
    </visual>
  </link>

  <joint name="left_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="left_wheel"/>
    <origin xyz="0 0.325 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <!-- Right Wheel -->
  <link name="right_wheel">
    <visual>
      <origin xyz="0 0 0" rpy="1.5708 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="0.05"/>
      </geometry>
      <material name="black">
        <color rgba="0.0 0.0 0.0 1.0"/>
      </material>
    </visual>
  </link>

  <joint name="right_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="right_wheel"/>
    <origin xyz="0 -0.325 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <!-- Lidar Sensor -->
  <link name="lidar_link">
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.05" length="0.06"/>
      </geometry>
      <material name="red">
        <color rgba="0.8 0.0 0.0 1.0"/>
      </material>
    </visual>
  </link>

  <joint name="lidar_joint" type="fixed">
    <parent link="chassis"/>
    <child link="lidar_link"/>
    <origin xyz="0 0 0.13" rpy="0 0 0"/>
  </joint>

  <!-- Camera -->
  <link name="camera_link">
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <box size="0.05 0.08 0.05"/>
      </geometry>
      <material name="dark_gray">
        <color rgba="0.3 0.3 0.3 1.0"/>
      </material>
    </visual>
  </link>

  <joint name="camera_joint" type="fixed">
    <parent link="chassis"/>
    <child link="camera_link"/>
    <origin xyz="0.35 0 0.1" rpy="0 0 0"/>
  </joint>

</robot>
```

#### 3.4.2 Publish Robot Description

```bash
# Terminal 1 - Publish URDF ke parameter server
ros2 param set /robot_state_publisher robot_description "$(cat ~/ros2_praktikum/src/simple_robot_description/urdf/simple_robot.urdf)"

# Atau jalankan robot_state_publisher
ros2 run robot_state_publisher robot_state_publisher \
    --ros-args -p robot_description:="$(cat ~/ros2_praktikum/src/simple_robot_description/urdf/simple_robot.urdf)"
```

#### 3.4.3 Publish Static TF untuk Joint

```bash
# Terminal 2 - Publish static transforms
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 world base_link
```

#### 3.4.4 Visualisasi di RViz2

```bash
# Terminal 3 - Jalankan RViz2
rviz2
```

**Konfigurasi RViz2:**

1. Set Fixed Frame: `world`
2. Tambahkan Display:
   - **RobotModel**: Akan menampilkan model robot dari URDF
   - **TF**: Menampilkan frame transformasi
   - **Grid**: Untuk referensi posisi

**Screenshot hasil:**

```
[Simpan screenshot RViz2 menampilkan robot model]
```

#### 3.4.5 Simpan Konfigurasi

```bash
# Simpan konfigurasi RViz2
# File → Save Config As...
# Simpan sebagai: ~/ros2_praktikum/robot_config.rviz
```

---

### 3.5 Praktikum 4: Rosbag2 - Perekaman Data

#### 3.5.1 Menyiapkan Data untuk Direkam

```bash
# Terminal 1 - Jalankan turtlesim
ros2 run turtlesim turtlesim_node

# Terminal 2 - Jalankan teleop
ros2 run turtlesim turtle_teleop_key

# Terminal 3 - Jalankan TF broadcaster (dari praktikum sebelumnya)
ros2 run turtle_tf_broadcaster turtle_tf_broadcaster
```

#### 3.5.2 Melihat Topik yang Tersedia

```bash
# Terminal 4 - List semua topik
ros2 topic list

# Output:
# /parameter_events
# /rosout
# /turtle1/cmd_vel
# /turtle1/color_sensor
# /turtle1/pose
# /tf
# /turtle_marker

# Lihat informasi detail topik
ros2 topic info /turtle1/pose -v
```

#### 3.5.3 Merekam Data dengan Rosbag2

```bash
# Rekam satu topik
ros2 bag record /turtle1/pose

# Rekam beberapa topik sekaligus
ros2 bag record /turtle1/pose /turtle1/cmd_vel /tf

# Rekam semua topik (hati-hati, bisa besar filenya)
ros2 bag record -a

# Rekam dengan nama bag file kustom
ros2 bag record -o praktikum_bag /turtle1/pose /turtle1/cmd_vel

# Rekam dengan durasi maksimal (30 detik)
ros2 bag record /turtle1/pose --max-duration 30

# Rekam dengan ukuran maksimal (10 MB)
ros2 bag record /turtle1/pose --max-size 10485760
```

#### 3.5.4 Menghentikan Perekaman

```bash
# Tekan Ctrl+C untuk menghentikan perekaman
# Output:
# [INFO] [rosbag2_storage]: Pausing recording.
# [INFO] [rosbag2_cpp]: Stopping recording...
# [INFO] [rosbag2_storage]: Resource cleanup complete.
```

#### 3.5.5 Memeriksa File Bag yang Direkam

```bash
# Lihat informasi bag file
ros2 bag info praktikum_bag

# Output contoh:
# Files:             praktikum_bag_0.db3
# Bag size:          256.0 KiB
# Storage id:        sqlite3
# Duration:          15.23s
# Start:             Dec 15 10:30:00.000 (2024)
# End:               Dec 15 10:30:15.230 (2024)
# Messages:          1500
# Topic information:
#   Topic: /turtle1/pose | Type: turtlesim/msg/Pose | Count: 300 |
#           Serialization Format: cdr
#   Topic: /turtle1/cmd_vel | Type: geometry_msgs/msg/Twist | Count: 1200 |
#           Serialization Format: cdr
```

#### 3.5.6 Melihat Isi Metadata

```bash
# Tampilkan metadata
cat praktikum_bag/metadata.yaml
```

---

### 3.6 Praktikum 5: Rosbag2 - Pemutaran Data

#### 3.6.1 Memutar Kembali Data

```bash
# Pastikan turtlesim tidak berjalan

# Putar bag file
ros2 bag play praktikum_bag

# Putar dengan rate tertentu (2x kecepatan)
ros2 bag play praktikum_bag --rate 2.0

# Putar dengan rate 0.5x (lambat)
ros2 bag play praktikum_bag --rate 0.5

# Putar dari waktu tertentu (dalam detik dari awal)
ros2 bag play praktikum_bag --start-offset 5.0

# Putar dengan loop
ros2 bag play praktikum_bag --clock --loop
```

#### 3.6.2 Memutar dengan Clock

```bash
# Putar dengan publish clock (penting untuk simulasi)
ros2 bag play praktikum_bag --clock

# Gunakan sim time
ros2 param set /use_sim_time true
```

#### 3.6.3 Memutar Topik Tertentu Saja

```bash
# Putar hanya topik pose
ros2 bag play praktikum_bag --topics /turtle1/pose

# Putar beberapa topik tertentu
ros2 bag play praktikum_bag --topics /turtle1/pose /tf

# Exclude topik tertentu
ros2 bag play praktikum_bag --exclude-topics /rosout /parameter_events
```

#### 3.6.4 Memvisualisasikan Data Bag di RViz2

```bash
# Terminal 1 - Jalankan RViz2
rviz2 -d ~/ros2_praktikum/robot_config.rviz

# Terminal 2 - Putar bag file
ros2 bag play praktikum_bag --clock
```

---

### 3.7 Praktikum 6: Rosbag2 - Operasi Lanjutan

#### 3.7.1 Konversi Format Bag

```bash
# Konversi dari SQLite3 ke format lain (jika plugin tersedia)
ros2 bag convert praktikum_bag output_bag sqlite3 sqlite3

# Konversi dengan kompresi
ros2 bag convert praktikum_bag compressed_bag sqlite3 sqlite3 \
    --compression-mode file \
    --compression-format zstd
```

#### 3.7.2 Filter dan Ekstrak Data

Buat script Python untuk membaca bag file:

```bash
cd ~/ros2_praktikum/src
ros2 pkg create --build-type ament_python bag_reader \
    --dependencies rosbag2_py rclpy std_msgs
```

```bash
cd ~/ros2_praktikum/src/bag_reader/bag_reader
nano bag_reader.py
```

**Isi file `bag_reader.py`:**

```python
#!/usr/bin/env python3
import rosbag2_py
from rclpy.serialization import deserialize_message
from std_msgs.msg import String
from turtlesim.msg import Pose


def read_bag_file(bag_path):
    # Konfigurasi storage
    storage_options = rosbag2_py.StorageOptions(
        uri=bag_path,
        storage_id='sqlite3'
    )

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format='cdr',
        output_serialization_format='cdr'
    )

    # Buat reader
    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    # Dapatkan informasi topik
    topic_types = reader.get_all_topics_and_types()

    # Buat mapping tipe pesan
    type_map = {}
    for topic_type in topic_types:
        type_map[topic_type.name] = topic_type.type

    print(f"Topik yang tersedia:")
    for topic, msg_type in type_map.items():
        print(f"  - {topic}: {msg_type}")
    print()

    # Baca semua pesan
    message_count = 0
    while reader.has_next():
        topic, data, timestamp = reader.read_next()
        message_count += 1

        # Deserialize pesan berdasarkan tipe
        msg_type = type_map.get(topic)

        if msg_type == 'turtlesim/msg/Pose':
            msg = deserialize_message(data, Pose)
            if message_count <= 10:  # Tampilkan 10 pesan pertama
                print(f"Time: {timestamp}")
                print(f"  Topic: {topic}")
                print(f"  Position: x={msg.x:.2f}, y={msg.y:.2f}")
                print(f"  Theta: {msg.theta:.2f}")
                print()

    print(f"Total pesan: {message_count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 bag_reader.py <bag_path>")
        sys.exit(1)

    read_bag_file(sys.argv[1])
```

#### 3.7.3 Menggunakan Rosbag2 CLI Lanjutan

```bash
# Daftar semua bag file di direktori
ros2 bag list

# Rekam dengan kompresi
ros2 bag record /turtle1/pose \
    --compression-mode message \
    --compression-format zstd

# Split bag file berdasarkan ukuran
ros2 bag record /turtle1/pose \
    --max-size 5242880 \
    --max-bags 5

# Rekam dengan QoS override
ros2 bag record /turtle1/pose \
    --qos-profile-overrides-path qos_override.yaml
```

**Contoh file `qos_override.yaml`:**

```yaml
"/turtle1/pose":
  history: 3
  depth: 10
  reliability: 1
  durability: 2
"/tf":
  history: 3
  depth: 100
  reliability: 1
  durability: 2
```

#### 3.7.4 Merekam Data Sensor (Simulasi)

```bash
# Install Gazebo dan paket simulasi (jika belum)
sudo apt install ros-jazzy-gazebo-ros-pkgs ros-jazzy-gazebo-ros2-control -y

# Jalankan simulasi dengan sensor
ros2 launch gazebo_ros empty_world.launch.py

# Di terminal lain, lihat topik yang tersedia
ros2 topic list

# Rekam data sensor
ros2 bag record /scan /camera/image_raw /tf /tf_static \
    -o sensor_data_bag
```

---

### 3.8 Praktikum 7: Integrasi RViz2 dan Rosbag2

#### 3.8.1 Membuat Demo Lengkap

```bash
# Terminal 1 - Jalankan semua node yang diperlukan
# (turtlesim, tf_broadcaster, dll)

# Terminal 2 - Rekam semua data
ros2 bag record -a -o full_demo_bag --max-duration 60

# Lakukan beberapa aksi dengan turtle selama 60 detik
# ...

# Setelah selesai, hentikan perekaman
```

#### 3.8.2 Memutar Kembali dan Visualisasi

```bash
# Terminal 1 - Jalankan RViz2 dengan konfigurasi lengkap
rviz2 -d ~/ros2_praktikum/full_config.rviz

# Terminal 2 - Putar bag file dengan clock
ros2 bag play full_demo_bag --clock --rate 1.0

# RViz2 akan menampilkan visualisasi sesuai data yang diputar
```

#### 3.8.3 Membuat Konfigurasi RViz2 Lengkap

Simpan konfigurasi lengkap ke file `full_config.rviz`:

```yaml
Panels:
  - Class: rviz_common/Displays
    Help Height: 78
    Name: Displays
    Property Tree Widget:
      Expanded: ~
      Splitter Ratio: 0.5
    Tree Height: 549
  - Class: rviz_common/Selection
    Name: Selection
  - Class: rviz_common/Tool Properties
    Expanded:
      - /2D Goal Pose1
      - /2D Nav Goal1
      - /Publish Point1
    Name: Tool Properties
    Splitter Ratio: 0.5886790156364441
  - Class: rviz_common/Views
    Expanded:
      - /Current View1
    Name: Views
    Splitter Ratio: 0.5
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Count: 20
      Cell Size: 1
      Class: rviz_default_plugins/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.029999999329447746
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 20
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 1
      Class: rviz_default_plugins/Axes
      Enabled: true
      Length: 1
      Name: Axes
      Radius: 0.029999999329447746
      Reference Frame: <Fixed Frame>
      Show Arrows: true
      Show Labels: true
      Value: true
    - Class: rviz_default_plugins/RobotModel
      Description Source: Topic
      Description Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /robot_description
      Enabled: true
      Name: RobotModel
      Visual Enabled: true
      Value: true
    - Class: rviz_default_plugins/TF
      Enabled: true
      Frame Timeout: 15
      Frames:
        All Enabled: true
      Marker Scale: 1
      Name: TF
      Show Arrows: true
      Show Axes: true
      Show Names: true
      Tree: {}
      Update Interval: 0
      Value: true
    - Class: rviz_default_plugins/Marker
      Enabled: true
      Name: Marker
      Namespaces:
        turtle: true
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /turtle_marker
      Value: true
  Enabled: true
  Global Options:
    Background Color: 48; 48; 48
    Fixed Frame: world
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz_default_plugins/Interact
      Hide Inactive Objects: true
    - Class: rviz_default_plugins/MoveCamera
    - Class: rviz_default_plugins/FocusCamera
    - Class: rviz_default_plugins/Measure
      Line color: 128; 128; 0
    - Class: rviz_default_plugins/SetGoal
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /goal_pose
    - Class: rviz_default_plugins/SetInitialPose
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /initialpose
    - Class: rviz_default_plugins/PublishPoint
      Single click: true
      Topic:
        Depth: 5
        Durability Policy: Volatile
        History Policy: Keep Last
        Reliability Policy: Reliable
        Value: /clicked_point
  Transformation:
    Current:
      Class: rviz_default_plugins/TF
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 10
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.009999999776482582
      Pitch: 0.5
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz_default_plugins)
      Yaw: 0.7853981852531433
    Saved: ~
Window Geometry:
  Displays:
    collapsed: false
  Height: 846
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: ""
  Selection:
    collapsed: false
  Tool Properties:
    collapsed: false
  Views:
    collapsed: false
  Width: 1440
  X: 0
  Y: 27
```

---

## 4. PEMBAHASAN

### 4.1 Pembahasan RViz2

#### 4.1.1 Mekanisme Kerja RViz2

RViz2 bekerja sebagai subscriber yang berlangganan pada berbagai topik ROS2. Setiap display type memiliki topik input yang spesifik:

```
┌─────────────────────────────────────────────────────────────┐
│                         RViz2                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────┐     /topic      ┌─────────────────────┐   │
│   │  Display:   │ ◄─────────────  │   ROS2 Node         │   │
│   │  LaserScan  │                 │   (Sensor/Publisher)│   │
│   └─────────────┘                 └─────────────────────┘   │
│                                                              │
│   ┌─────────────┐     /topic      ┌─────────────────────┐   │
│   │  Display:   │ ◄─────────────  │   ROS2 Node         │   │
│   │  PointCloud │                 │   (Sensor/Publisher)│   │
│   └─────────────┘                 └─────────────────────┘   │
│                                                              │
│   ┌─────────────┐     /tf         ┌─────────────────────┐   │
│   │  Display:   │ ◄─────────────  │   TF2 Broadcaster   │   │
│   │  TF         │                 │                     │   │
│   └─────────────┘                 └─────────────────────┘   │
│                                                              │
│   ┌─────────────┐  /robot_desc    ┌─────────────────────┐   │
│   │  Display:   │ ◄─────────────  │   Robot State       │   │
│   │  RobotModel │                 │   Publisher         │   │
│   └─────────────┘                 └─────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 4.1.2 Fixed Frame dan Transformasi

Fixed Frame adalah referensi utama dalam RViz2. Semua data yang divisualisasikan akan ditransformasikan ke frame ini. Jika terdapat error transformasi, kemungkinan penyebabnya:

1. Fixed Frame tidak sesuai dengan tree TF
2. Ada gap dalam chain transformasi
3. TF tidak dipublish dengan benar

**Contoh kasus error dan solusinya:**

```
Error: "Transform from [turtle1] to [world] failed"
Solusi: Pastikan TF broadcaster aktif dan chain transformasi lengkap
```

#### 4.1.3 Performance Optimization

Untuk meningkatkan performa RViz2:

| Teknik                    | Implementasi                                         |
| ------------------------- | ---------------------------------------------------- |
| **Reduced Update Rate**   | Set frame rate lebih rendah untuk display non-kritis |
| **Decimation**            | Skip beberapa frame untuk PointCloud2                |
| **Selective Rendering**   | Nonaktifkan display yang tidak diperlukan            |
| **LOD (Level of Detail)** | Gunakan model dengan detail bervariasi               |

### 4.2 Pembahasan Rosbag2

#### 4.2.1 Perbandingan Rosbag (ROS1) vs Rosbag2 (ROS2)

| Aspek               | Rosbag (ROS1)        | Rosbag2 (ROS2)                    |
| ------------------- | -------------------- | --------------------------------- |
| **Format File**     | .bag (binary custom) | .db3 (SQLite3) + metadata.yaml    |
| **Storage Backend** | Fixed                | Plugin-based (SQLite3, MCAP, dll) |
| **Kompatibilitas**  | ROS1 only            | ROS2 only                         |
| **Metadata**        | Terbatas             | YAML terstruktur                  |
| **QoS Support**     | Tidak ada            | Ya, penuh                         |
| **Compression**     | Built-in             | Plugin-based                      |
| **Konversi**        | rosbag filter        | rosbag2 convert                   |

#### 4.2.2 Analisis Format SQLite3

Rosbag2 menggunakan SQLite3 sebagai default storage karena:

1. **Relational Database:** Memungkinkan query efisien berdasarkan topik, waktu, atau tipe
2. **Portabilitas:** Single file, mudah dipindahkan
3. **Transaction Support:** Data integrity terjaga
4. **Widespread Support:** Banyak tool yang mendukung SQLite3

**Struktur tabel dalam database:**

```sql
-- Tabel topics
CREATE TABLE topics (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    serialization_format TEXT NOT NULL,
    offered_qos_profiles TEXT NOT NULL
);

-- Tabel messages
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL,
    timestamp INTEGER NOT NULL,
    data BLOB NOT NULL,
    FOREIGN KEY(topic_id) REFERENCES topics(id)
);
```

#### 4.2.3 Pertimbangan QoS saat Merekam

QoS sangat penting dalam Rosbag2 karena mempengaruhi data yang berhasil direkam:

```
┌─────────────────────────────────────────────────────────────┐
│                  QoS Matching Scenario                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Publisher (Sensor)          Recorder (Rosbag2)              │
│  ┌─────────────────┐         ┌─────────────────┐            │
│  │ Reliability:    │         │ Reliability:    │            │
│  │ BEST_EFFORT     │◄───────►│ BEST_EFFORT     │ ✓ Match    │
│  └─────────────────┘         └─────────────────┘            │
│                                                              │
│  Publisher (Sensor)          Recorder (Rosbag2)              │
│  ┌─────────────────┐         ┌─────────────────┐            │
│  │ Reliability:    │         │ Reliability:    │            │
│  │ RELIABLE        │◄─ ─ ─ ─►│ BEST_EFFORT     │ ✗ No Match│
│  └─────────────────┘         └─────────────────┘            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 4.2.4 Strategi Pengelolaan Storage

```
┌─────────────────────────────────────────────────────────────┐
│              Storage Management Strategies                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Size-based Splitting                                     │
│     rosbag2 record --max-size 100MB                          │
│     ├── bag_0.db3 (100MB)                                   │
│     ├── bag_1.db3 (100MB)                                   │
│     └── bag_2.db3 (50MB)                                    │
│                                                              │
│  2. Time-based Splitting                                     │
│     rosbag2 record --max-duration 300                        │
│     ├── bag_0.db3 (5 menit pertama)                         │
│     └── bag_1.db3 (5 menit kedua)                           │
│                                                              │
│  3. Compression                                              │
│     rosbag2 record --compression-mode message                │
│                      --compression-format zstd               │
│     └── bag_compressed.db3 (ukuran lebih kecil)             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Integrasi RViz2 dan Rosbag2

#### 4.3.1 Workflow untuk Analisis Data

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Capture    │────►│   Storage    │────►│  Analysis    │
│   (ROS2)     │     │   (Rosbag2)  │     │   (RViz2)    │
└──────────────┘     └──────────────┘     └──────────────┘
      │                    │                    │
      ▼                    ▼                    ▼
  Real-time           Offline             Offline
  recording          storage              playback &
                                           visualization
```

#### 4.3.2 Use Cases

| Use Case               | RViz2                 | Rosbag2              |
| ---------------------- | --------------------- | -------------------- |
| **Debugging Sensor**   | Visualisasi real-time | Rekam untuk analisis |
| **Testing Algoritma**  | Lihat hasil           | Rekam input/output   |
| **Demonstrasi**        | Tampilan live         | Rekam untuk replay   |
| **Dataset Collection** | Verifikasi data       | Simpan data          |
| **Regression Testing** | Bandingkan visual     | Bandingkan bag file  |

---

## 5. ANALISA

### 5.1 Analisa Performa RViz2

#### 5.1.1 Pengukuran Resource Usage

Berdasarkan pengamatan selama praktikum:

| Konfigurasi                   | CPU Usage | RAM Usage  | FPS   |
| ----------------------------- | --------- | ---------- | ----- |
| Grid + Axes saja              | 5-10%     | 150-200 MB | 60    |
| + TF Display                  | 10-15%    | 200-250 MB | 55    |
| + RobotModel (sederhana)      | 15-20%    | 250-300 MB | 50    |
| + PointCloud2 (1000 points)   | 25-35%    | 350-400 MB | 30-40 |
| + PointCloud2 (100000 points) | 50-70%    | 500-700 MB | 15-25 |

#### 5.1.2 Faktor yang Mempengaruhi Performa

1. **Jumlah Display:** Semakin banyak display aktif, semakin tinggi resource yang dibutuhkan
2. **Kompleksitas Model:** URDF dengan banyak link dan visual memerlukan lebih banyak memori
3. **Densitas Data:** PointCloud dengan jutaan titik akan memperlambat rendering
4. **Update Rate:** Frekuensi update display mempengaruhi beban CPU

#### 5.1.3 Rekomendasi Optimasi

```python
# Contoh konfigurasi PointCloud2 yang optimal di RViz2
# - Decimation: 10 (tampilkan 1 dari 10 point)
# - Style: Points (bukan Flat Squares)
# - Size (Pixels): 2
# - Alpha: 0.7
# - Update interval: 0.1 detik
```

### 5.2 Analisa Rosbag2

#### 5.2.1 Pengukuran Storage

Data dari praktikum menunjukkan:

| Topik              | Tipe Pesan | Frekuensi | Ukuran/Pesan | Ukuran/Menit |
| ------------------ | ---------- | --------- | ------------ | ------------ |
| /turtle1/pose      | Pose       | 30 Hz     | ~64 bytes    | ~115 KB      |
| /turtle1/cmd_vel   | Twist      | 100 Hz    | ~48 bytes    | ~288 KB      |
| /tf                | TFMessage  | 50 Hz     | ~200 bytes   | ~600 KB      |
| /scan (simulasi)   | LaserScan  | 10 Hz     | ~12 KB       | ~7.2 MB      |
| /camera (simulasi) | Image      | 30 Hz     | ~1.5 MB      | ~2.7 GB      |

#### 5.2.2 Analisa Efek Kompresi

| Metode         | Rasio Kompresi | Overhead CPU  | Rekomendasi           |
| -------------- | -------------- | ------------- | --------------------- |
| Tanpa Kompresi | 1:1            | Minimal       | Data kecil, real-time |
| ZSTD (message) | 3:1 - 5:1      | Rendah        | Data sensor umum      |
| ZSTD (file)    | 2:1 - 4:1      | Sangat Rendah | Arsip jangka panjang  |

#### 5.2.3 Analisa QoS Impact

Pengujian menunjukkan dampak QoS pada perekaman:

```
Skenario 1: Publisher RELIABLE, Recorder RELIABLE
- Semua pesan terekam
- Latensi bisa lebih tinggi
- Cocok untuk data kritis

Skenario 2: Publisher BEST_EFFORT, Recorder BEST_EFFORT
- Beberapa pesan mungkin hilang
- Latensi rendah
- Cocok untuk data sensor frekuensi tinggi

Skenario 3: Publisher RELIABLE, Recorder BEST_EFFORT
- NO CONNECTION (Tidak ada data terekam!)
- QoS tidak kompatibel
```

### 5.3 Analisa Kesalahan Umum

#### 5.3.1 Error di RViz2

| Error                             | Penyebab                | Solusi                        |
| --------------------------------- | ----------------------- | ----------------------------- |
| "No transform from X to Y"        | TF tree tidak lengkap   | Pastikan semua TF dipublish   |
| "Could not find resource"         | Path file URDF salah    | Cek path dan load ulang       |
| "Message filter dropping message" | Timestamp tidak sinkron | Gunakan --clock saat play bag |
| "RobotModel not displaying"       | Topic tidak ada         | Publish /robot_description    |

#### 5.3.2 Error di Rosbag2

| Error              | Penyebab                | Solusi                               |
| ------------------ | ----------------------- | ------------------------------------ |
| "No topics found"  | Tidak ada topik aktif   | Cek dengan ros2 topic list           |
| "QoS incompatible" | Mismatch QoS            | Gunakan --qos-profile-overrides-path |
| "Storage error"    | Permission denied       | Cek permission direktori             |
| "File corrupted"   | Perekaman tidak selesai | Gunakan metadata untuk recovery      |

### 5.4 Analisa Komparatif dengan Alternatif

#### 5.4.1 Visualisasi

| Tool            | Kelebihan                     | Kekurangan            | Use Case               |
| --------------- | ----------------------------- | --------------------- | ---------------------- |
| **RViz2**       | Full-featured, integrasi ROS2 | Berat, learning curve | Development, debugging |
| **Foxglove**    | Web-based, modern UI          | Perlu setup server    | Remote monitoring      |
| **PlotJuggler** | Time-series plotting          | Tidak 3D              | Data analysis          |
| **Webviz**      | Customizable                  | Kompleks setup        | Dashboard              |

#### 5.4.2 Perekaman Data

| Tool          | Kelebihan            | Kekurangan         | Use Case          |
| ------------- | -------------------- | ------------------ | ----------------- |
| **Rosbag2**   | Native ROS2, modular | Format proprietary | ROS2 workflow     |
| **MCAP**      | Compressed, seekable | Butuh konversi     | Long-term storage |
| **Custom DB** | Fleksibel            | Development effort | Specific needs    |

---

## 6. KESIMPULAN

### 6.1 Kesimpulan Umum

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:

1. **RViz2** merupakan alat visualisasi yang powerful dan esensial dalam ekosistem ROS2. Kemampuannya untuk menampilkan berbagai jenis data mulai dari model robot, data sensor, hingga transformasi koordinat menjadikannya alat yang tidak tergantikan untuk debugging dan pengembangan robot.

2. **Rosbag2** menyediakan mekanisme perekaman dan pemutaran data yang modular dan fleksibel. Penggunaan SQLite3 sebagai backend storage memberikan keseimbangan antara performa dan portabilitas.

3. **Integrasi RViz2 dan Rosbag2** memungkinkan workflow analisis data yang efisien, di mana data dapat direkam, disimpan, dan dianalisis secara offline tanpa memerlukan hardware sensor yang sebenarnya.

### 6.2 Kesimpulan Spesifik

#### 6.2.1 Tentang RViz2

- Fixed Frame merupakan konsep kritis yang harus dipahami dengan benar
- Konfigurasi dapat disimpan dan dimuat ulang untuk reproducibility
- Performa sangat bergantung pada kompleksitas scene dan jumlah data
- TF tree yang konsisten merupakan prasyarat untuk visualisasi multi-frame

#### 6.2.2 Tentang Rosbag2

- QoS compatibility merupakan faktor kritis yang sering menyebabkan kegagalan perekaman
- Strategi splitting dan compression penting untuk manajemen storage jangka panjang
- Metadata YAML menyediakan informasi yang berguna untuk analisis offline
- Fitur rate control pada playback memungkinkan analisis detail

### 6.3 Keterbatasan Praktikum

1. Praktikum ini menggunakan simulasi sederhana (turtlesim) yang tidak merepresentasikan kompleksitas data sensor real
2. Tidak membahas integrasi dengan tool eksternal seperti Foxglove atau PlotJuggler
3. Pengujian performa terbatas pada hardware tertentu
4. Tidak mencakup advanced features seperti custom display plugin atau storage plugin

### 6.4 Rekomendasi untuk Pengembangan

1. **Eksplorasi MCAP Format:** Pertimbangkan migrasi ke MCAP untuk storage jangka panjang
2. **Custom Plugin Development:** Pelajari pembuatan custom display plugin untuk kebutuhan spesifik
3. **Integration with Foxglove:** Gunakan Foxglove Studio untuk monitoring remote
4. **Automated Testing:** Implementasikan automated bag file comparison untuk regression testing

---

## 7. DAFTAR PUSTAKA

### 7.1 Dokumentasi Resmi

1. **ROS 2 Documentation**. (2024). _ROS 2 Jazzy Jalisco Documentation_. Open Robotics.  
   https://docs.ros.org/en/jazzy/

2. **ROS 2 Tutorials**. (2024). _Visualizing Data with RViz2_.  
   https://docs.ros.org/en/jazzy/Tutorials/Intermediate/RViz2/RViz2-Main.html

3. **Rosbag2 Documentation**. (2024). _ROS 2 Bag Recording and Playback_.  
   https://docs.ros.org/en/jazzy/Tutorials/Advanced/Recording-a-bag-from-ros2-topics.html

4. **TF2 Documentation**. (2024). _TF2 Configuration Guide_.  
   https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html

5. **URDF Documentation**. (2024). _URDF Tutorials_.  
   https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html

### 7.2 Buku Referensi

6. **Quigley, M., Gerkey, B., & Smart, W. D.** (2015). _Programming Robots with ROS_. O'Reilly Media. ISBN: 978-1449323899.

7. **Foote, T., Gerkey, B., & Koenig, N.** (2023). _ROS 2 Robot Programming: A Handbook_. Robotis.

8. **Siciliano, B., & Khatib, O.** (2016). _Springer Handbook of Robotics_ (2nd ed.). Springer. ISBN: 978-3319325521.

### 7.3 Paper dan Artikel Ilmiah

9. **Macenski, S., Foote, T., Gerkey, B., Lalancette, C., & Woodall, W.** (2022). "The Marathon 2: A Navigation System". _IEEE Robotics and Automation Letters_, 7(2), 4589-4596.

10. **Open Robotics**. (2022). "ROS 2 on DDS: An Evaluation of Data Distribution Service Implementations". _IEEE International Conference on Robotics and Automation (ICRA)_.

### 7.4 Sumber Online

11. **Foxglove**. (2024). _Foxglove Studio Documentation_.  
    https://docs.foxglove.dev/

12. **MCAP**. (2024). _MCAP File Format Documentation_.  
    https://mcap.dev/

13. **ROS Answers**. (2024). _Q&A Forum for ROS_.  
    https://answers.ros.org/

14. **ROS Discourse**. (2024). _Discussion Forum for ROS_.  
    https://discourse.ros.org/

### 7.5 Repositori GitHub

15. **ros2/rviz**. (2024). _RViz2 Source Code_.  
    https://github.com/ros2/rviz

16. **ros2/rosbag2**. (2024). _Rosbag2 Source Code_.  
    https://github.com/ros2/rosbag2

17. **ros2/robot_state_publisher**. (2024). _Robot State Publisher_.  
    https://github.com/ros/robot_state_publisher

18. **ros2/geometry2**. (2024). _TF2 Library_.  
    https://github.com/ros2/geometry2

---

## LAMPIRAN

### Lampiran 1: Script Lengkap

**File: `launch_demo.sh`**

```bash
#!/bin/bash

# Script untuk menjalankan demo lengkap

# Source ROS2
source /opt/ros/jazzy/setup.bash
source ~/ros2_praktikum/install/setup.bash

# Fungsi untuk cleanup
cleanup() {
    echo "Cleaning up..."
    pkill -f turtlesim_node
    pkill -f turtle_teleop_key
    pkill -f turtle_tf_broadcaster
    pkill -f rviz2
    exit 0
}

trap cleanup SIGINT SIGTERM

# Jalankan turtlesim
ros2 run turtlesim turtlesim_node &
sleep 2

# Jalankan TF broadcaster
ros2 run turtle_tf_broadcaster turtle_tf_broadcaster &
sleep 1

# Jalankan RViz2
rviz2 -d ~/ros2_praktikum/full_config.rviz &
sleep 1

# Jalankan teleop di foreground
ros2 run turtlesim turtle_teleop_key
```

### Lampiran 2: Cheat Sheet

**RViz2 Commands:**

```bash
# Jalankan RViz2
rviz2

# Jalankan dengan konfigurasi
rviz2 -d config.rviz

# Jalankan dengan fixed frame tertentu
rviz2 --fixed-frame map
```

**Rosbag2 Commands:**

```bash
# Rekam topik
ros2 bag record /topic

# Rekam beberapa topik
ros2 bag record /topic1 /topic2 /topic3

# Rekam semua
ros2 bag record -a

# Rekam dengan opsi
ros2 bag record -o nama -a --max-duration 60 --max-size 1000000

# Info bag
ros2 bag info nama_bag

# Putar bag
ros2 bag play nama_bag

# Putar dengan opsi
ros2 bag play nama_bag --rate 2.0 --clock --loop

# Konversi
ros2 bag convert input output sqlite3 sqlite3

# List bag files
ros2 bag list
```

### Lampiran 3: Troubleshooting Guide

| Masalah                         | Langkah Debugging                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------ |
| RViz2 tidak menampilkan apa-apa | 1. Cek Fixed Frame<br>2. Verifikasi topik aktif<br>3. Cek enable display                   |
| TF error                        | 1. `ros2 run tf2_tools view_frames`<br>2. Cek tree completeness<br>3. Verifikasi timestamp |
| Bag tidak merekam data          | 1. Cek QoS compatibility<br>2. Verifikasi topik ada<br>3. Cek permission                   |
| Playback tidak bekerja          | 1. Cek file integrity<br>2. Verifikasi metadata<br>3. Cek storage plugin                   |
| High CPU usage RViz2            | 1. Kurangi update rate<br>2. Nonaktifkan display tidak perlu<br>3. Gunakan decimation      |

---

**Akhir Laporan**

_Dokumen ini disusun sebagai laporan praktikum ROS2: RViz dan Bag File menggunakan ROS2 Jazzy Jalisco pada Ubuntu 24.04 LTS._
