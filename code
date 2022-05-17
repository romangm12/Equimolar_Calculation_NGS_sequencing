# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 06:54:15 2021

@author: roman
"""

##DNA1

print('The DNA1 length in pb for the first fragment')

DNA1L = int(input('DNA1 can only acquire values >0 :'))

while DNA1L<0 or DNA1L>1000000:
    print("Error -> into a valid number for the DNA1 Lenght")
    
    DNA1L = int(input('DNA1 can only acquire values >0 :'))

print('The DNA1 mass(ng) for the first fragment')

DNA1m = float(input('DNA1 mass can only acquire values(ng)>0 :'))

while DNA1m<0 or DNA1m>1000000:
    print("Error -> into a valid number for the DNA1L Lenght")
    
    DNA1m = float(input('DNA1Lcan only acquire values >0 :'))

Moles_DNA1=(DNA1m/((DNA1L*617.96)+36.04))

fMoles_DNA1= (Moles_DNA1*10**-15)

print(fMoles_DNA1,'fMoles')

##DNA2

print('The DNA2 length in pb for the second fragment')

DNA2L = int(input('DNA2 Lenght can only acquire values >0: '))

while DNA2L<0 or DNA2L>1000000:
    print("Error -> into a valid number for the DNA2 Lenght")
    
    DNA2L = int(input('DNA2 Lenght can only acquire values>0: '))

print('The DNA2 mass(ng) for the second fragment')

DNA2m = float(input('DNA2 mass can only acquire values(ng)>0: '))

while DNA2m<0 or DNA2m>1000000:
    print("Error -> into a valid number for the DNA2m mass")
    
    DNA2m = float(input('DNA2m can only acquire values(ng)>0: '))

Moles_DNA2=(DNA2m/((DNA2L*617.96)+36.04))

fMoles_DNA2= (Moles_DNA2*10**-15)

print(fMoles_DNA2,'fMoles')

##Volumen_DNA1
print('How much volume has DNA1')

DNA1v = float(input('DNA1 volume(ul) can only acquire values(ul)>0: '))

while DNA1v<0 or DNA1v>1000000:
    print("Error -> into a valid number for the DNA1v volumen")
    
    DNA1v = float(input('volumen can only acquire values(ul)>0: '))

##Volumen_DNA2
print('How much volume has DNA2')

DNA2v = float(input('DNA2 volume(ul) can only acquire values >0: '))

while DNA2v<0 or DNA2v>1000000:
    print("Error -> into a valid number for the DNA2v volumen")
    DNA2v = float(input('volumen can only acquire values (ul)>0: '))

Total_fMoles_DNA1=(DNA1v*fMoles_DNA1)
Total_fMoles_DNA2=(DNA2v*fMoles_DNA2)

if fMoles_DNA1 >= fMoles_DNA2:
    PVolDNA1=((fMoles_DNA2*DNA1v)/Total_fMoles_DNA1)
    print('Put',(PVolDNA1),'of DNA1 in the total volumen in DNA2')
    if PVolDNA1 <= 0.5:
        print('I recommend making a 1/6 dilution of the DNA1')
        
        print('For prepare 10ul, put 1.7ul DNA1 and 8.4ul de H2O nucleasea free')
        
        print('Put',(PVolDNA1*6),'ul of dilution DNA1 in DNA2')
        
    if PVolDNA1 >= 0.5 and PVolDNA1 >= 1:
        print('I recommend making a 1/2 dilution of the DNA1')
        
        print('For prepare 5ul, put 2.5 ul DNA1 and 2.5 ul de H2O nucleasea free')
        
        print('Put',(PVolDNA1*2),'ul of dilution DNA1 in DNA2')

if fMoles_DNA2 >= fMoles_DNA1:
    PVolDNA2=((fMoles_DNA1*DNA2v)/Total_fMoles_DNA2)
    print('Put',(PVolDNA2),'of DNA2 in the total volumen in DNA1')
    if PVolDNA2 <= 0.5:
        print('I recommend making a 1/6 dilution of the DNA2')
        
        print('For prepare 5ul, put 1.7ul  DNA2 and 8.4ul de H2O nucleasea free')
        
        print('Put',(PVolDNA2*6),'ul of dilution DNA2 in DNA1')
        
    if PVolDNA2 >= 0.5 and PVolDNA2 >= 1:
        print('I recommend making a 1/2 dilution of the DNA2')
        
        print('For prepare 5ul, put 2.5 ul DNA2 and 2.5 ul de H2O nucleasea free')
        
        print('Put',(PVolDNA2*2),'ul of dilution DNA2 in DNA1')

k=input("press close to exit")
