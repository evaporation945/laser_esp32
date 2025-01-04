try:
    with open(r'C:\Users\zaizai\Desktop\code\esp32_test\laser_esp32\laser_esp32\test\1.ild', 'rb') as file:
        binary_data = file.read()
        print(hex(binary_data[0])[2:].zfill(2)+"first")
        hex_lines = []
        #以十六进制形式输出二进制数据，每行输出32个字节
        # for i in range(0, len(binary_data), 4):
        #     line = binary_data[i:i+4]
        #     hex_line = ' '.join(f'{byte:02x}' for byte in line)
        #     hex_lines.append(line)
        #print(hex_line)
        #print(str(hex_line))
        with open('output.txt', 'w') as OUT_file:
            count = 0
            for i in binary_data:
                count = count + 1
                if count == 4:
                #print(i)
                    OUT_file.write(hex(i)[2:].zfill(2)+' ')
                    OUT_file.write('\n')
                    count = 0
                else:                    
                    OUT_file.write(hex(i)[2:].zfill(2)+' ')              
except FileNotFoundError:
    print("文件未找到")