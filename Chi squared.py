NatFreq = {"a":8.167,"b":1.492,"c":2.782,"d":4.253,"e":12.702,"f":2.228,"g":2.015,"h":6.094,
   "i":6.966,"j":0.153,"k":0.772,"l":4.025,"m":2.406,"n":6.749,"o":7.507,"p":1.929,
   "q":0.095,"r":5.987,"s":6.327,"t":9.056,"u":2.758,"v":0.978,"w":2.360,"x":0.150,
   "y":1.974,"z":0.074}

Cphrtxt = "This is a rather long string. This is actually not even encrypted."
TestFreq = {}
for i in range (97,123):
  TestFreq[chr(i)] = 0


def getFreq(Cphrtxt):
  TotLet = 0
  for i in range (len(Cphrtxt)):
    letter = (Cphrtxt[i].lower())
    if (ord(letter) >= 97) and (ord(letter) <= 122):
      TestFreq[letter] += 1
      TotLet += 1
  for i in range (97,123):
    TestFreq[chr(i)] = ((TestFreq[chr(i)])/TotLet)*100
  return TotLet

def Method():
  cont =0
  while cont == 0:
    try:
      Type = int(input("What encryption method do you think is being used?\n1 - Caesar Shift\n2 - Substitution\n3 - Unsure \n"))
      cont = 1
    except:
      print("Please enter a valid option. Enter 3 if you are unsure")
  return Type

def DecodeShift():
  MinChiVal = [Chi(TestFreq),0]
  for shift in range (1,25):
    S_TestFreq = {}
    for char in TestFreq:
      S_TestFreq[char] = TestFreq[chr((ord(char)-97+shift)%26+97)]
    ChiVal = Chi(S_TestFreq)
    if ChiVal < MinChiVal[0]:
      MinChiVal = [ChiVal, shift]
  plntxt = ''
  for i in range(len(Cphrtxt)):
    if (ord(Cphrtxt[i].lower()) < 97) or (ord(Cphrtxt[i].lower()) > 122):
      plntxt += Cphrtxt[i]
    else:
      if Cphrtxt[i].lower() != Cphrtxt[i]:
       plntxt += chr(((ord(Cphrtxt[i].lower())-MinChiVal[1]-97)%26)+97).upper()
      else:
       plntxt += chr(((ord(Cphrtxt[i])-MinChiVal[1]-97)%26)+97)
  return plntxt,MinChiVal[1]

def DecodeSub():
  return
  
def Chi(Test):
  Total = 0
  for char in NatFreq:
    Total += ((NatFreq[char] - Test[char])**2)/NatFreq[char]
  return Total
    

Method()
getFreq(Cphrtxt)
print('Likley Plaintext: '+ DecodeShift()[0] +'\nkey: shift '+ str(DecodeShift()[1]))
