'''
--- Test Edildi---
Bu modul daxil edilən byte ardıcıllığına uyğun , numpy array 
və ya tərsinə daxil edilən numpy array-a uyğun byte ardıcıllığı qaytarır

'''
import numpy as np

''' Daxil edilən  bit sırasına görə bizə massiv qaytarır '''
def bytes_to_arr(_bytes):
    return np.array(list(_bytes) , dtype=np.uint8)

''' Daxil edilən massivi uyğun bit ardıcıllığına çevirir '''
def arr_to_bytes(_arr):
    return bytes(list(_arr))

''' Bayt massivinin uzunluğu tapılır və bunun 1024 bitə çatdırılması üçün nə qədər bitin çatmadığı hesablanır
 	Əgər tapılan ədəd 128-dən böyük olarsa, n-128 qədər təsadüfi bit generasiya edilir
 '''
def length_1024(_arr):
    size = np.array(list((_arr.size).to_bytes(16, byteorder='big')), dtype=np.uint8)
    random = np.random.randint(256, size=(128-(_arr.size+16)%128) , dtype=np.uint8)
    return np.concatenate((_arr,random,size))

''' Əgər tapılan ədəd 128-dən kiçik olarsa, n+1024-128 qədər təsadüfi bit generasiya edilir '''
def shorter(_arr):
    size = int.from_bytes(bytes(list(_arr[-16:])), "big")
    return _arr[:size]

'''Generasiya edilən təsadüfi bitlər və bayt massivinin uzunluğunun 128 bitlik hissəsi bayt massivinə əlavə edilir '''
def add_end(_arr):
    array = np.insert(bytes(list(_arr[-16:])), 128)
    return _arr[:array]