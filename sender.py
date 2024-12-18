import socket

def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0:pick]
    while pick<len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor,tmp) + divident[pick]
        else:
            tmp = xor('0'*pick,tmp) + divident[pick]

        pick += 1 


    if tmp[0] == '1':
        tmp = xor(divisor,tmp)
    else:
        tmp = xor('0'*pick,tmp)

    checkword = tmp
    return checkword

def encodeData(data,key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data,key)
    codeword = data + remainder
    return codeword

s = socket.socket()

port = 54321

s.connect(('127.0.0.1',port))

while True:
    input_string = input("Enter data you want to send -->")
    if input_string == "exit":
        break
    data = (''.join(format(ord(x),'b') for x in input_string))
    print("Entered data in binary format --> "+data)
    key = "1001"

    ans = encodeData(data,key)
    print("Encoded data to be sent to receiver in binary format --> ",ans)
    s.sendto(ans.encode(),('127.0.0.1',54321))
    print("Received feedback from server :",s.recv(1024).decode())

s.close()