{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww19280\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', \
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', \
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', \
'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
't', 'u', 'v', 'w', 'x', 'y', 'z']\
\
decision = input("Do you want to encode or decode the message?\\n").lower()\
shift = int(input( "Enter the shift number: \\n"))\
message = input("Enter the message: \\n")\
\
def ceaser (message,shift,decision):\
  text = ""\
  for letter in message:\
    position = alphabet.index(letter)\
    if decision == "encode":\
      newposition = position + shift\
      text += alphabet[newposition]\
      print(f"\\n The encoded message is \\n \{text\}")\
    else:\
      revposition = alphabet.index(letter)\
      reverse = revposition - shift\
      text += alphabet[reverse]\
      print(f"\\n The decoded message is \{text\} \\n")\
    \
ceaser(message,shift,decision)   \
repeat = input ("\\n Do you want to run the program again?").lower()\
\
if repeat == "yes":\
    import main\
else:\
    print("Terminating")}