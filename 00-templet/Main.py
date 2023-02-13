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
data_string= "10 "
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



#canting yaitu merubah data 
print("=====INTEGER=====")
data_float1= float(data_int)
data_str1 =str(data_int)
data_bool1 = bool(data_int)
print(data_float1)
print(data_str1)
print(data_bool1) # jika 0 false 

print("=====Float=====")
data_int2= float(data_float)
data_str2 =str(data_float)
data_bool2 = bool(data_float)
print(data_int)
print(data_str2)
print(data_bool2) # jika 0 false 

print("=====BOOLEHAN =====")
data_int3= float(data_bool)
data_float3 =str(data_bool)
data_str3 = float(data_bool)
print(data_int3)
print(data_float3)
print(data_str3) 

#print("===== STRING =====")
# data_int4= float(data_string) # harus angka "10"
# data_bool4 =bool(data_string) # jika nilai string maka false ""
# data_float4 = float(data_string)
# print(data_int4)
# print(data_float4)
# print(data_bool4) 

#eps input user 
# data = input("masukan data: ")
# print("data : ", data, "type= ", type(data))


# data_int = int(input("masukan angka 1-5 : ",))
# print("data_int : ", data_int, "type= ", type(data_int))
 

#data_float90 = float(input("masukan angka : "))
# print("data_float : ", data_float90, "type : ", type(data_float90))


#biner = bool(int(input("masukan bolehan : ")))
#print("biner : ", biner," type : ", type(biner))

# aritmatika pada pthyon 

a = 19
b = 5

# artimatika tambah 
hasil = a + b 
print( a, '+', b, '=', hasil)
# artimatika bagi
hasil = a / b 
print( a, '/', b, '=', hasil)
# artimatika kurang
hasil = a - b 
print( a, '-', b, '=', hasil)
# artimatika kali
hasil = a * b 
print( a, '*', b, '=', hasil)
# artimatika ekponen/pangkat
hasil = a ** b 
print( a, '**', b, '=', hasil)
# artimatika modulus 
hasil = a % b 
print( a, '%', b, '=', hasil)
# artimatika floor devisiin pembulatan ke bawah 
hasil = a // b 
print( a, '//', b, '=', hasil)

#priotias aritmatika 
#1. tanda kurung ()
#2. tanda eksponen/pangkat **
#3 perkalian ( % / // %)
#4. penjumlahan (+ - )

x = 10
y = 9
z = 2

hasil = x ** y * z + x % z / z - y // z
print(x,'**', y,'*', z , '+',x,'%',z,'/',z,'-',y,'//',z,'=' ,hasil)