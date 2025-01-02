def read_bmp(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(54)
        width = int.from_bytes(header[18:22], 'little')
        height = int.from_bytes(header[22:26], 'little')
        row_size = (width * 3 + 3) & ~3
        pixel_data = f.read()
        return header, width, height, row_size, pixel_data

def write_bmp(file_path, header, pixel_data):
    with open(file_path, 'wb') as f:
        f.write(header)
        f.write(pixel_data)

def to_grayscale(pixel_data, width, height, row_size):
    new_pixel_data = bytearray()
    for y in range(height):
        row_start = y * row_size
        for x in range(0, width * 3, 3):
            b, g, r = pixel_data[row_start + x:row_start + x + 3]
            gray = int(0.114 * b + 0.587 * g + 0.299 * r)
            new_pixel_data.extend([gray, gray, gray])
        new_pixel_data.extend([0] * (row_size - width * 3))
    return new_pixel_data

def detect_motion(prev_pixel_data, curr_pixel_data, width, height, row_size):
    diff_pixel_data = bytearray()
    motion_detected = False
    for y in range(height):
        row_start = y * row_size
        for x in range(0, width * 3, 3):
            prev_gray = prev_pixel_data[row_start + x]
            curr_gray = curr_pixel_data[row_start + x]
            diff = abs(curr_gray - prev_gray)
            if diff > 151:
                motion_detected = True
                diff_pixel_data.extend([255, 0, 0])
            else:
                diff_pixel_data.extend([curr_gray, curr_gray, curr_gray])
        diff_pixel_data.extend([0] * (row_size - width * 3))
    return diff_pixel_data, motion_detected

if __name__ == "__main__":
    input_file_1 = "./sample/sample1.bmp"
    input_file_2 = "./sample/sample2.bmp"
    grayscale_file_1 = "./grayscale_frame1.bmp"
    grayscale_file_2 = "./grayscale_frame2.bmp"
    motion_file = "./result.bmp"

    header, width, height, row_size, pixel_data_1 = read_bmp(input_file_1)
    grayscale_data_1 = to_grayscale(pixel_data_1, width, height, row_size)
    write_bmp(grayscale_file_1, header, grayscale_data_1)

    _, _, _, _, pixel_data_2 = read_bmp(input_file_2)
    grayscale_data_2 = to_grayscale(pixel_data_2, width, height, row_size)
    write_bmp(grayscale_file_2, header, grayscale_data_2)

    motion_data, motion_detected = detect_motion(grayscale_data_1, grayscale_data_2, width, height, row_size)
    print("Motion detected!" if motion_detected else "No motion detected.")
   
    write_bmp(motion_file, header, motion_data)
   
