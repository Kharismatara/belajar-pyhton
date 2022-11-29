print('Hallo Dunia ')
print("Apa Kabar ")

print('Hallo jomblos')
#ini adalah komen 
a= 10
"""ada anak jomblo yang belajar nih """
print(a)

"""menggunak compliier """

"""variable """
#tempat menyimpan data 

#menaruh /assigment nilai 
a=10
x=5
panjang =10000

"""untuk memanggil 1 """
print(a)
print("nilai panjang= ", panjang)

#tipedata apa aja dipyton 
# a=10 a adalah variabel 
# typedata 
# 1. type inter dimana tidak ada koma 
data_int = 10000
print("data integer : ", data_int )
print(type(data_int))

#2. type data flat ada komannya 
data_float = 1.90
print("data float :  " ,data_float, type(data_float)) 


#3. type data flat ada komannya 
data_string= "nabi yusuf"
print("data string : ", data_string, type(data_string))

#4. type data booo adalah type data yang true or flase
data_bool= True
print("data boolehan : ", data_bool, type(data_bool))

#type data khusus 
data_Complex = complex(5,10)
print("data complex : ", data_Complex, type(data_Complex))


#type data ambil dari c karean pyton merupakan bahasa dasar dari c 
#dan ditypon itu tidak ada char, loang doubel maka kita bisa gunakan punya c
#dengan cara import 

from ctypes import c_double ,c_char

data_cdouble = c_double(1000000.0000000000)
print("data c_double  : ", data_cdouble, type(data_cdouble))