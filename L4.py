import os
import sys

# 1. Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din
# directorul dat ca parametru.

def extensions_sorted(directory: str):
    if os.path.exists(directory):
        files = [x for x in os.listdir(directory) if os.path.isfile(directory + '\\' + x)]
        return sorted({os.path.splitext(x)[-1] for x in files})

# print(extensions_sorted("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\dir2"))


# 2. Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

def file_paths(directory: str, file: str):
    paths = list()
    try:
        with open(file, "w") as f:
            files = [x for x in os.listdir(directory) if os.path.isfile(directory + '\\' + x)]
            f.writelines([directory + '\\' + x + '\n' for x in files if x.startswith('A')])
    except FileNotFoundError:
        print('Error: file not found')


# file_paths("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\dir2",
#            "C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\paths.txt")


# 3. Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată
# descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie.
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.

def file_or_directory(my_path: str):
    if os.path.isfile(my_path):
        try:
            with open(my_path, 'r') as f:
                file_content = f.read()
                return file_content[-20:]
        except FileNotFoundError:
            print('Error: file not found')
    elif os.path.isdir(my_path):
        files = [x for x in os.listdir(my_path) if os.path.isfile(my_path + '\\' + x)]
        extensions = list()
        for ext in [os.path.splitext(x)[-1] for x in files]:
            extensions.append(ext)
        return [(ext, extensions.count(ext)) for ext in extensions_sorted(my_path)]
    return 'Path is neither file or directory'

# print(file_or_directory("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\paths.txt"))
# print(file_or_directory("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\dir2"))


# 4. Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat
# ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

def arg_extensions_sorted():
    directory = sys.argv[1]
    directory.replace('\\', '\\\\')
    return extensions_sorted(directory)

# print(arg_extensions_sorted())


# 5. Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza
# o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar
# in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă
# target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.

def files_containing(target: str, to_search: str):
    if os.path.isfile(target):
        try:
            with open(target, 'r') as f:
                return [target] if to_search in f.read() else []
        except FileNotFoundError:
            print('Error: file not found')
    elif os.path.isdir(target):
        paths = list()
        for path in [target + '\\' + x for x in os.listdir(target)]:
            paths += files_containing(path, to_search)
        return paths
    else:
        raise ValueError('Target path is neither file or directory')

# print(files_containing("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir", ".txt"))


# 6. Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că
# primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută
# în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.

def exception_handler(ex: Exception):
    print('Error of type', type(ex).__name__, 'occured')

def files_containing_with_handle(target: str, to_search: str, handle):
        if os.path.isfile(target):
            try:
                with open(target, 'r') as f:
                    return [target] if to_search in f.read() else []
            except Exception as ex:
                handle(ex)
        elif os.path.isdir(target):
                paths = list()
                for path in [target + '\\' + x for x in os.listdir(target)]:
                    paths += files_containing(path, to_search)
                return paths
        else:
            raise ValueError('Target path is neither file or directory')

print(files_containing_with_handle("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir", ".txt",
                       exception_handler))
print(files_containing_with_handle("C:\\Users\\alinh\\Documents\\Facultate\\Semestrul V\\Python\\lab\\Python\\L4\\dir\\path.txt", ".txt",
                       exception_handler))


# 7. Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer
# si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.

def file_attributes(file: str):
    d = dict()
    if os.path.isfile(file):
        d['full_path'] = os.path.abspath(file)
        d['file_size'] = os.path.getsize(file)
        d['file_extension'] = os.path.splitext(file)[-1]
        d['can_read'] = os.access(file, os.R_OK)
        d['can_write'] = os.access(file, os.W_OK)
    return d

# print(file_attributes("dir\\paths.txt"))


# 8. Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea
# către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate
# în rădăcina directorului dir_path.

def file_absolute_paths(dir_path: str):
    ls = list()
    if os.path.isdir(dir_path):
        ls = [os.path.join(os.path.abspath(dir_path), x) for x in os.listdir(dir_path)
              if os.path.isfile(os.path.join(dir_path, x))]
    return ls

# print(file_absolute_paths("dir\\dir2"))
