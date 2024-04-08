import time

def encode_message(message):
    return ''.join(format(ord(c), '08b') for c in message) + ' ' + ''.join(format(ord(c), '08b') for c in "EOF")

def send_message(file_path, message):
    binary_message = encode_message(message)
    with open(file_path, "w") as file:
        for bit in binary_message:
            file.write(bit)
            file.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    message = input("Enter your message: ")
    file_path = "covert_channel.txt"
    send_message(file_path, message)
    print("Message sent.")
