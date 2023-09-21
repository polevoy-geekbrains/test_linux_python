"""
Задание 1.
Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
и разархивирования с путями (x).
*Задание 2. *
- Установить пакет для расчёта crc32 > sudo apt install libarchive-zip-perl
- Доработать проект, добавив тест команды расчёта хеша (h).
Проверить, что хеш совпадает с рассчитанным командой crc32.
"""
import subprocess
from sem import checkout

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"
folderext2 = "/home/user/folder2"


def test_step8():
    #test8
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "2 files")


def test_step9():
    # test9
    assert checkout(f"cd {folderout}; 7z x arx2.7z -o{folderext2} -y", "Everything is Ok"), "test9 FAIL"


def test_step10():
    # test10
    res = subprocess.run("crc32 /home/user/out/arx2.7z", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    assert checkout(f"cd {folderout}; 7z h arx2.7z", f"{(res.stdout).rstrip().upper()}"), "test10 FAIL"
    