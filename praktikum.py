# The main dictionary to store student data.
# The key is the Student ID (NIM), and the value is another dictionary 
# containing the student's name and scores.
data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    """
    Calculates the final score based on the given weights.
    Tugas (Assignment): 30%, UTS (Midterm): 35%, UAS (Final): 35%
    """
    nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
    return round(nilai_akhir, 2)

def tampilkan_data():
    """
    Displays the entire student grade list.
    """
    print("\n--- Daftar Nilai Mahasiswa ---")
    # Header
    print("| No. | Nama             | NIM        | Tugas | UTS | UAS | Akhir |")
    print("|-----|------------------|------------|-------|-----|-----|-------|")

    if not data_mahasiswa:
        print("| **TIDAK ADA DATA** |")
    else:
        no = 1
        for nim, data in data_mahasiswa.items():
            # Calculate final grade for display
            nilai_akhir = hitung_nilai_akhir(
                data['tugas'], data['uts'], data['uas']
            )
            print(
                f"| {no:<3} | {data['nama'][:16]:<16} | {nim:<10} | "
                f"{data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | "
                f"{nilai_akhir:<5} |"
            )
            no += 1
    
    print("--------------------------------------------------")

def tambah_data():
    """
    Adds new student data.
    """
    print("\n--- Tambah Data Baru ---")
    while True:
        nim = input("Masukkan NIM (Nomor Induk Mahasiswa): ").strip()
        if nim in data_mahasiswa:
            print(f"**Error:** NIM '{nim}' sudah terdaftar. Gunakan NIM lain.")
        elif nim:
            break
        else:
            print("**Error:** NIM tidak boleh kosong.")
    
    nama = input("Masukkan Nama Mahasiswa: ").strip() or "N/A"
    
    # Input scores with basic validation
    try:
        tugas = int(input("Masukkan Nilai Tugas (0-100): "))
        uts = int(input("Masukkan Nilai UTS (0-100): "))
        uas = int(input("Masukkan Nilai UAS (0-100): "))
        
        if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
             print("**Peringatan:** Nilai harus antara 0 dan 100. Data ditambahkan, tapi perhatikan nilai yang diinput.")
    except ValueError:
        print("**Error:** Nilai harus berupa angka. Data dibatalkan.")
        return

    # Store the data
    data_mahasiswa[nim] = {
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas
    }
    print(f"\n✅ Data mahasiswa dengan NIM {nim} berhasil ditambahkan.")

def ubah_data():
    """
    Modifies existing student data based on NIM.
    """
    print("\n--- Ubah Data Mahasiswa ---")
    nim_cari = input("Masukkan NIM mahasiswa yang ingin diubah: ").strip()

    if nim_cari in data_mahasiswa:
        data = data_mahasiswa[nim_cari]
        print(f"Data saat ini untuk NIM {nim_cari}:")
        print(f"Nama: {data['nama']}, Tugas: {data['tugas']}, UTS: {data['uts']}, UAS: {data['uas']}")
        
        print("\n--- Masukkan Nilai Baru (Kosongkan jika tidak ingin diubah) ---")
        
        # New Name
        new_nama = input(f"Nama baru (Saat ini: {data['nama']}): ").strip()
        if new_nama:
            data['nama'] = new_nama
            
        # New Scores
        try:
            new_tugas_str = input(f"Nilai Tugas baru (Saat ini: {data['tugas']}): ").strip()
            if new_tugas_str:
                data['tugas'] = int(new_tugas_str)
                
            new_uts_str = input(f"Nilai UTS baru (Saat ini: {data['uts']}): ").strip()
            if new_uts_str:
                data['uts'] = int(new_uts_str)
                
            new_uas_str = input(f"Nilai UAS baru (Saat ini: {data['uas']}): ").strip()
            if new_uas_str:
                data['uas'] = int(new_uas_str)
                
            print(f"\n✅ Data mahasiswa dengan NIM {nim_cari} berhasil diubah.")
        except ValueError:
            print("\n**Error:** Input nilai harus berupa angka. Perubahan dibatalkan.")
    else:
        print(f"\n❌ Data mahasiswa dengan NIM {nim_cari} tidak ditemukan.")

def hapus_data():
    """
    Deletes student data based on NIM.
    """
    print("\n--- Hapus Data Mahasiswa ---")
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dihapus: ").strip()

    if nim_cari in data_mahasiswa:
        del data_mahasiswa[nim_cari]
        print(f"\n✅ Data mahasiswa dengan NIM {nim_cari} berhasil dihapus.")
    else:
        print(f"\n❌ Data mahasiswa dengan NIM {nim_cari} tidak ditemukan.")

def cari_data():
    """
    Searches for and displays student data based on NIM.
    """
    print("\n--- Cari Data Mahasiswa ---")
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_mahasiswa:
        data = data_mahasiswa[nim_cari]
        nilai_akhir = hitung_nilai_akhir(data['tugas'], data['uts'], data['uas'])
        
        print("\n--- Data Ditemukan ---")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS: {data['uts']}")
        print(f"Nilai UAS: {data['uas']}")
        print(f"Nilai Akhir: {nilai_akhir}")
        print("-----------------------")
    else:
        print(f"\n❌ Data mahasiswa dengan NIM {nim_cari} tidak ditemukan.")

def tampilkan_menu():
    """
    Displays the main menu.
    """
    print("\n==============================")
    print(" PROGRAM MANAJEMEN NILAI MAHASISWA")
    print("==============================")
    print("1. Lihat Nilai")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Keluar Program")
    print("------------------------------")

# Main program loop
if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            ubah_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("\n👋 Program selesai. Sampai jumpa!")
            break
        else:
            print("\n⚠️ Pilihan tidak valid. Silakan masukkan angka antara 1 dan 6.")
