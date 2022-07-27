decode = ['A','B','C','D','E','F','G','H','I','J','K','L',
          'M','N','O','P','Q','R','S','T','U','V','W','X',
          'Y','Z','a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z', '0','1','2','3','4','5','6','7',
          '8','9','+','/']

T = int(input())

for i in range(T):
    case = input()
    value = ''
    for c in case:
        decode_num = decode.index(c)
        bit_ver = str(bin(decode_num)[2:])
        print(bit_ver)
    
    
    
    # for c in case:
    # case_bytes = " "
    # case_result = case_bytes.decode('ascii')
    
    # print(f'#{i+1} {case_result}')

