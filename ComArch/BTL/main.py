import struct
import random

def create_random_int_file(file_path):
    # Sinh số nguyên ngẫu nhiên từ 0 đến 2^31 - 1
    random_int = random.randint(0, 2**31 - 1)
    
    # Ghi số nguyên vào file bin
    with open(file_path, 'wb') as bin_file:
        # Sử dụng struct để đóng gói số nguyên thành dữ liệu bin
        bin_data = struct.pack('i', random_int)
        bin_file.write(bin_data)

# Tạo 30 file
for i in range(30): 
    file_name = f'random_int_{i+1}.bin'
    create_random_int_file(file_name)

print('30 files đã được tạo thành công.')
