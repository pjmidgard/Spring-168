from time import time
Times_change_info=0
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_unpack(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
                    Times_of_compression1=0
                    
                    
                    Times1=0
                    
                    
                    INFO4=""
                        
                   
                    
                    count3=0
                    count4=-1
                   
                    Times1=0
                    Times3=0
                    Times_of_compression=0
                    
              

                    Times=0
                    
                    
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    Save_name=len(nameas)

                    Times_of_compression=0
                    
                    countraz=0
                    Times=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                    c=2
                    R=0
                    
                    
                    count4=-1
                 
                    INFO3=""
                    INFO2=""

                    ssTimes_change_info=0
                    
                    

                    block=2
                    

                    count_time_of_copression=0
                    countraz=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                                        
                    
                    c=2
                    
                    
                       
                    INFO3=""

                    ssTimes_change_info=0
                        
                    

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        
                    
                        
                        s=str(data)
                        
            
                  
                        long_file1=len(data)
                        long_file5=len(data)
                        
            
                  
                    
                        if long_file1==0:
                            
                            raise SystemExit

                        Times_Finish=0
                        Times_Plus=0
                        
            
                   
                        while Times_Finish<10:
                       
                            
                            

                
           
                    
                            Times_change_info=Times_change_info+1
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_file=len(INFO)
                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1

      
                                    
                                    
                                    INFO=INFO+INFO2

                                    if countraz==1:
                                        INFO2=INFO
                            
                                    n = int(INFO2, 2)
                                
                                    binary_to_data=len(INFO2)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    jl=binascii.unhexlify(binary_to_data % n)
                                    size_of_file_count=len(jl)
                                    
                                    data=jl
                                    Times_Plus=Times_Plus+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        long_file5=len(data)

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_file=len(INFO)

                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1


                                    
                                    INFO2=INFO
                                 

                                    long_file3=len(INFO2)
                                long_file2=len(INFO2)
                                
                                
                                
                                Long_file=int(INFO2[0:32],2)
                                Times_compress=int(INFO2[32:80],2)
                                
                                Times_F=0
                                #print(Long_file)

                                
                                while Times_F!=1:
                                    if Times3==0:
                                            Start_file=INFO2[80:]
                                            size_data3=INFO2[80:]
                                            
          
                                            
                                            while size_data3[0:1]!="1":
                                                if size_data3[0:1]=="0":
                                                    Start_file=Start_file[1:]
                                                    size_data3=size_data3[1:]
                                                    
                                                    
                                             
                                            Start_file=Start_file[1:]
                                            INFO2=Start_file
                                         
                                            	
                                        #print(INFO2)
                                    	  
                                    

                                    block3=0
                                    INFO3=""
                                    INFO5=""
                                    INFO8=""
                                    
                                    #INFO4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(INFO2))
                                    F=0
                                    B=0
                                    count4=-1
                                 
                                    long_file2=len(INFO2)
                                    #print(INFO2)
                                    

                              
                                     								                          
                                                             
                                    
                                  
 
                                        
                                    

                                    
                                  
                                    
                                    #Reverse
                                    INFO3=INFO2
                                    long_file3=len(INFO2)
                                        
                                    block3=0
                                    long_3=len(INFO3)
                                 
                                    INFO4=""
                                    INFO_3=""
                                    
                                    while block3<long_3:
                                    	INFO_3=INFO3[block3:block3+1]
                                    	
                                    	if INFO_3=="0":
                                    		INFO4+="1"
                                    	elif INFO_3=="1":
                                    		INFO4+="0"
                                    	block3+=1
                                    	
                                    INFO2=INFO4
                                    INFO3=""
                                    long_file2=len(INFO2) 
                                    print(long_file2)
                                    #Huffman
                                    if INFO2[long_file2-2:long_file2]=="00":
                                    	INFO3=INFO2[:long_file2-2]+"10"
                                    elif INFO2[long_file2-2:long_file2]=="10":
                                    	INFO3=INFO2[:long_file2-2]+"01"
                                    elif INFO2[long_file2-2:long_file2]=="01":
                                    	INFO3=INFO2[:long_file2-2]+"11"
                                    elif INFO2[long_file2-2:long_file2]=="11":
                                    	INFO3=INFO2[:long_file2-2]+"00"      
                                    
                                    long_5=len(INFO2)
                                    Mod=int(INFO2[long_5-1:],2)
                                    Minus=int(INFO2[:long_5-1],2)
                                 
                                    Minus=(Minus*2)+Mod
                                    
                                  
                                    INFO2=bin(Minus)[2:]
                                  
                                    
                                              
                                    #print(len(INFO2))
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    
                                    Times3+=1  
                                    #print(Times3)
                                    if Times3==Times_compress:
                                       #print(INFO3)
    
                                       
                                       
                                       Times3=0
                                       #print(Times3)
                                       Times=1
                                       Times_F=1
                                       	                                                                                            
											                                                                                            
											                                                                                            
                                    
                                    
                                    #print(Times)
                                if Times==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO3)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(INFO3, 2)
                                        binary_to_data=len(INFO3)
                                        binary_to_data=Long_file*2
                                        binary_to_data=str(binary_to_data)
                                        binary_to_data="%0"+binary_to_data+"x"
                                        jl=binascii.unhexlify(binary_to_data % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        Times1=1
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                        if Times1==1:
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)                                  

                           
    
            
    def cryptograpy_compression(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        
                        R=0
                       
                        
                        count3=0
                        count4=-1
                       
                        Times1=0
                        Times3=0
                        Times_of_compression=0
                        
              

                        Times=0
                        
                        
                        nameas=name
                        
                        Save_name=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        Times_change_info=2
                        Times_change_info1=0
                        s=""
                        INFO_5=""
                        
                        
                        
                        c=2
                        
                        
                       
                        INFO3=""
                        INFO_5=""
                        ssTimes_change_info=0
                        
                        

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()

                        
                            s=str(data)
                            long_file1=len(data)
                            #print(long_file1)
                            
                            

                          
                            long_file5=len(data)
                            
                            if long_file1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if long_file1==0:
                            	raise SystemExit
                            
                            Times_Finish=0
                            
                            Times_Plus=0
                            while Times_Finish<10:
                          
                                
                                
                                
                                Times_change_info=Times_change_info+1
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        INFO=bin(int(binascii.hexlify(data),16))[2:]
                                        long_file=len(INFO)
                                        
                                        long_file1=len(data) 
                                        xc=(long_file1*8)-long_file
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                INFO="0"+INFO
                                                z=z+1
                                        INFO2=INFO
                                        long_file3=len(INFO2)
                                      
                                    long_file2=len(INFO2)  
                                    INFO3=""
                                    
                                    Minus=int(INFO2,2)
                                    N1=Minus%8
                                    Minus=Minus//8
                                  
                                  
                               
                                    C="0"+str(str(long_file2-(long_file2-3)))+"b"
                                    INFO_2=format(Minus,C)
                                    
                                    Cr="0"+str(2)+"b"
                                    #print(len(INFO_2))
                                    Mod=bin(N1)[2:]
                                   
                                    #print(len(Mod))
                                    INFO6=""#
                                    INFO6=INFO_2+Mod
                                    while len(INFO6)!=len(INFO2):
                                    	INFO6="0"+INFO6
                             
                                  
                                
                                    INFO2=INFO6

                                
                                    #print(len(INFO6))
                                    
                                    
                                    long_file2=len(INFO6)
                                   
                                    #Huffman
                                    if INFO2[long_file2-2:long_file2]=="10":
                                    	INFO3=INFO2[:long_file2-2]+"00"
                                    elif INFO2[long_file2-2:long_file2]=="01":
                                    	INFO3=INFO2[:long_file2-2]+"10"
                                    elif INFO2[long_file2-2:long_file2]=="11":
                                    	INFO3=INFO2[:long_file2-2]+"01"
                                    elif INFO2[long_file2-2:long_file2]=="00":
                                    	INFO3=INFO2[:long_file2-2]+"11"                                     
                                    #print(len(INFO3))
                                    
                                    #Reverse
                                    block3=Times3
                                    long_3=len(INFO3)
                                 
                                    INFO4=""
                                    INFO_3=""
                                    
                                    while block3<long_3:
                                    	INFO_3=INFO3[block3:block3+1]
                                    	
                                    	if INFO_3=="0":
                                    		INFO4+="1"
                                    	elif INFO_3=="1":
                                    		INFO4+="0"
                                    	block3+=1
                                    
                                    INFO4=INFO3[:Times3]+INFO4[Times3:]
                                    INFO2=INFO4
                                    INFO3=INFO4
                                    #print(INFO2)
                                       
                                    
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    #print(Times3)
                                    
                                    Times3+=1  
                                    if Times3==long_file1*2:
                                        #print(Bias2)
                                        
                                   

                                        
                                     
     #print(Bias2)
                                        Times=1
                                    #print(Times)
                                    if Times==1:
                                       Start_file=INFO3
                                       size_data3=INFO3
                                       while size_data3[0:1]!="1":
                                                if size_data3[0:1]=="0":
                                                    Start_file=Start_file[1:]
                                                    size_data3=size_data3[1:]
                                       B1=format(long_file1,'032b')
                                       INFO3="1"+Start_file
                                       long_file=len(INFO3)
                                       add_bits118=""
                                       count_bits=8-long_file%8
                                       z=0
                                       if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                       INFO3=add_bits118+INFO3
                                       INFO3=B1+INFO3
                                     
                                      
                                       n = int(INFO3, 2)
                                       binary_to_data=len(INFO3)
                                       binary_to_data=(binary_to_data/8)*2
                                       binary_to_data=str(binary_to_data)
                                       binary_to_data="%0"+binary_to_data+"x"
                                       jl=binascii.unhexlify(binary_to_data % n)
                                       Times1=1 
                                       if Times1==1:
                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO2)
                                        #os.system("pause")
                                        
                                        
                                            
               

                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                       
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)        
                                                                                  														    
                                         



   



            
                     

d=compression()

xw1=d.cryptograpy_unpack()
print(xw1)

xw=d.cryptograpy_compression()
print(xw)
