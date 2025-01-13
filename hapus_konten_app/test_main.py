import unittest
import os
from main import main  # Pastikan import sesuai dengan lokasi fungsi main Anda

class TestMainApp(unittest.TestCase):
    
    def setUp(self):
        self.file_path = "data/list_konten.txt"

    def test_file_not_found(self):
        # Menghapus file jika ada
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Memanggil fungsi main dan menguji hasilnya
        main(self.file_path)

        # Memastikan file dibuat
        self.assertTrue(os.path.exists(self.file_path), "File baru tidak dibuat saat file tidak ditemukan.")

if __name__ == "__main__":
    unittest.main()
