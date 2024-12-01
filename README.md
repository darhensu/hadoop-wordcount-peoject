# Hadoop WordCount Project

## Deskripsi
Proyek ini menggunakan Hadoop Streaming untuk melakukan penghitungan kata (word count) pada file teks `pembukaan_uud1945.txt`. Proyek ini mengimplementasikan dua skrip Python (`mapper.py` dan `reducer.py`) untuk memproses data secara terdistribusi menggunakan Hadoop.

## Persyaratan
- **Hadoop 3.2.3** atau lebih baru yang berjalan dalam *standalone mode*.
- **Python** (versi yang kompatibel dengan Hadoop Streaming, biasanya Python 2.x atau 3.x).
- **Windows** sebagai sistem operasi (dengan pengaturan lingkungan yang sesuai).

## Instalasi
1. **Instal Hadoop**: Pastikan Anda telah menginstal Hadoop pada mesin Anda.
2. **Konfigurasi Hadoop**: Edit file konfigurasi seperti `core-site.xml` dan `mapred-site.xml` untuk menjalankan Hadoop dalam *standalone mode*. 
3. **Persiapkan File Input**: Pastikan file `pembukaan_uud1945.txt` tersedia di direktori yang tepat.
4. **Persiapkan Mapper dan Reducer**:
   - `mapper.py`: Skrip ini akan memetakan kata-kata dari input file dan memberikan output pasangan kata dan jumlah kemunculannya.
   - `reducer.py`: Skrip ini akan menerima hasil mapper dan menggabungkan hasilnya untuk menghitung total kemunculan setiap kata.


## Cara Menjalankan

### 1. Menjalankan Hadoop Streaming Job
Setelah Anda mengonfigurasi Hadoop dan mempersiapkan file input (`pembukaan_uud1945.txt`), Anda dapat menjalankan job Hadoop menggunakan perintah berikut:


hadoop jar "%HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.2.3.jar" \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -input file:///C:/Users/user/Desktop/hadoop_wordcount_project/input/pembukaan_uud1945.txt \
    -output output

atau jika ingin line:
hadoop jar "%HADOOP_HOME%\share\hadoop\tools\lib\hadoop-streaming-3.2.3.jar" -mapper "python mapper.py" -reducer "python reducer.py" -input file:///C:/Users/user/Desktop/hadoop_wordcount_project/input/pembukaan_uud1945.txt -output output

## Memeriksa Hasil Output

hadoop fs -ls output

hadoop fs -cat output/part-00000


hadoop fs -rm -r output # Membersihkan output

