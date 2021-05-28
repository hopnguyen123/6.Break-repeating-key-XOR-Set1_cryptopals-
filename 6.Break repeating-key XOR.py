#   XONG
#   ------------------    Base64 -> List -> String     ----------------------------------
from base64 import b64decode,b64encode
data = open("data06.txt")
Data = data.read().split('\n')              #Data có kiểu List, len(Data) = 64 tương ứng 64 dòng


List_cipher=[]                              #Chuyen base64 -> chuoi string
for i in Data:
    i=b64decode(i).decode()
    List_cipher.append(i)

String_cipher=''.join(List_cipher)          #Chuyển List -> String


#   --------------      Tìm KEYSIZE     ------------------------------
def Convert_String_to_bit(input):           #Chuyển string -> bit (type = string)
    x1=""
    for i in input:
        x2=bin(ord(i))[2:]
        them_=8-len(x2)
        x2=them_*"0"+x2
        x1+=x2
    return x1
def Distance_Hamminng(input1,input2):       #Khoảng cách giữa 2 chuỗi
    dem=0
    input1=Convert_String_to_bit(input1)
    input2=Convert_String_to_bit(input2)
    for i1,i2 in zip(input1,input2):
        if i1 != i2:
            dem+=1
    return dem

def Find_KEY_SIZE():                        #Tìm KEY_SIZE
    key_sizes = []
    for KEYSIZE in range(2, 41):
        avr_of_1keysize = []
        len_ = len(String_cipher)
        last_ = int(len_ / KEYSIZE) - 1
        for i in range(0, last_):
            str_truoc = String_cipher[KEYSIZE * i:KEYSIZE * (i + 1)]
            str_sau = String_cipher[KEYSIZE * (i + 1):KEYSIZE * (i + 2)]
            KHOANGCACH = Distance_Hamminng(str_truoc, str_sau)
            tb = KHOANGCACH / KEYSIZE
            avr_of_1keysize.append(tb)
        tong = sum(avr_of_1keysize)
        len_ = len(avr_of_1keysize)
        key_sizes.append((tong / len_, KEYSIZE))
    key_sizes.sort(key=lambda a: a[0])
    len_key = key_sizes[0][1]
    return len_key


#   -------------       CẮT CHUỖI -> HOÁN VỊ CHUỖI      -----------------------
len_key=Find_KEY_SIZE()

index_cut=[]
chieudai=len(String_cipher)
for i in range(0,chieudai,len_key):
    index_cut.append(i)

List_after_cut=[]
for i in index_cut:
    if i != 2871:
        x=String_cipher[i:i+len_key]
        List_after_cut.append(x)

list1=[]
for i in range(len_key):
    x=""
    for j in range(len(List_after_cut)):
        x+=List_after_cut[j][i]
    list1.append(x)


#   -----------------       TÌM REPEAT KEY XOR      -------------------------
def DemKiTu(s):
    dem=0
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' '):
            dem+=1
    return dem

def str_xor_chr(s,c):
    s1=""
    for i in s:
        s2=chr(ord(i)^ord(c))
        s1+=s2
    return s1

list_KEY=[]
for i in range(len(list1)):
    list_256=[]
    for so in range(256):  # Xét từng kí tự 0 -> 255 (bảng ascii)
        CHR=chr(so)
        chuoi_sau_xor=str_xor_chr(list1[i],CHR)
        list_256.append(chuoi_sau_xor)

    max = 0
    index = 0
    for i in range(len(list_256)):
        soluong = DemKiTu(list_256[i])
        if soluong > max:
            max = soluong
            index = i
    list_KEY.append(index)

for i in list_KEY:
    print(chr(i),end='')



