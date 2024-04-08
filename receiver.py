import time

def read_binary_message(file_path):
    with open(file_path, "r") as file:
        binary_message = file.read().strip()
    return binary_message

def decode_message(binary_message):
    chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    message = ''.join(chr(int(chunk, 2)) for chunk in chunks if chunk and set(chunk) <= {'0', '1'})
    
    return message

if __name__ == "__main__":
    file_path = "covert_channel.txt"
    eof_binary = ''.join(format(ord(c), '08b') for c in "EOF")
    message_received = False
    binary_message = ""

    while not message_received:
        binary_message = read_binary_message(file_path)
        
        eof_index = binary_message.find(eof_binary)
        if eof_index != -1: 
            message_received = True
            message = decode_message(binary_message[:eof_index])
            print(f"Received message: {message}")
        else:
            time.sleep(0.5)
