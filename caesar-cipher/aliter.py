
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift=shift  % 25


def caesar(text,shift):#hello   # 2
    #cipher_text=''
    d_text=''
    for i in text:
      
      if i in alphabet:
        
        if direction=='encode':
          if alphabet.index(i) + shift > 25:
              d_text=d_text + alphabet[shift-(alphabet.index('z')-alphabet.index(i))-1]
          else:
              d_text= d_text + alphabet[alphabet.index(i) + shift]
              
        if direction=='decode':
          if alphabet.index(i)-shift < 0:
              d_text = d_text + alphabet[alphabet.index('z') +alphabet.index(i) -shift+1]
          else:
              d_text = d_text + alphabet[alphabet.index(i) -shift]
      else:
        d_text+=i
    print(d_text)
    #print(cipher_text)

caesar(text,shift)


# example output
'''
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
eureka i got it
Type the shift number:
4
iyvioe m ksx mx

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
iyvioe m ksx mx
Type the shift number:
4
eureka i got it
'''
