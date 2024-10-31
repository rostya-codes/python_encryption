import pyAesCrypt
import os


def encryption(file, password):
    """File encryption function"""
    # Set size of buffer
    buffer_size = 512*1024

    # Call encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    # To see result print the name of encrypted file
    print('[Файл \'' + str(os.path.splitext(file)[0]) + '\' зашифрован]')

    # Remove source file
    os.remove(file)

def walking_by_dirs(dir, password):
    """Scanning directories function"""
    # Cycle all subdirectories in chosen directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # If file found, encrypting it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # If directory found, repeat searching files cycle
        else:
            walking_by_dirs(path, password)


password = input('Enter password to encryption: ')
walking_by_dirs('/home/rostya/projects/other/python_encryption/files', password)
# os.remove(str(sys.argv[0]))
