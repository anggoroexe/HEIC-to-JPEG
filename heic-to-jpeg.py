import os
from PIL import Image
import pyheif

def konversi_heic_ke_jpg(input_path, output_path):
    heif_file = pyheif.read(input_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(output_path, "JPEG")

def konversi_semua_heic_dalam_folder(folder):
    folder_konversi = os.path.join(folder, 'convert')
    if not os.path.exists(folder_konversi):
        os.makedirs(folder_konversi)

    for nama_file in os.listdir(folder):
        if nama_file.lower().endswith('.heic'):
            input_path = os.path.join(folder, nama_file)
            nama_file_output = os.path.splitext(nama_file)[0] + '.jpg'
            output_path = os.path.join(folder_konversi, nama_file_output)
            konversi_heic_ke_jpg(input_path, output_path)
            print(f'Converted {nama_file} to {nama_file_output}')

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
konversi_semua_heic_dalam_folder(folder_saat_ini)
