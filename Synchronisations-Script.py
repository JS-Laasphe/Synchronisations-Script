# Das Programm vergleicht die Änderungszeiten der beiden Dateien.
# Wenn die Änderungszeit der Quelldatei neuer oder gleich der Änderungszeit der Zieldatei ist,
# wird die Zieldatei gelöscht und die Quelldatei an ihren Speicherort kopiert.

import os
import time

try:
    source_file = "//NAS/Volume 3/Testumgebung/Testdatei.kdbx"
    target_file = "C:/Python/Testumgebung/Testdatei.kdbx"

    source_info = os.stat(source_file)
    target_info = os.stat(target_file)

    if source_info.st_mtime >= target_info.st_mtime:
        os.remove(target_file)

        f_src = open(source_file, 'rb')
        f_tar = open(target_file, 'wb')

        f_tar.write(f_src.read())

        f_src.close()
        f_tar.close()

        print("Neue Version gefunden und ersetzt.")

    else:
        print("Es ist bereits die aktuellste Version vorhanden.")

except Exception as error:
    print(error)

finally:
    time.sleep(3)
