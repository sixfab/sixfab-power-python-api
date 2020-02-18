    
    class CRC16:
    
        CRC16_CCITT = 0x1021    #X.25, V.41, HDLC FCS, Bluetooth, ...

        def CRC16(self):
            #default constructer

        # crc16 base function 
        def crc16(self, crcValue, newByte):

            for i in range(8):

                if ((((crcValue & 0x8000) >> 8) ^ (newByte & 0x80)) > 0)
                {
                    crcValue = (crcValue << 1) ^ CRC16_CCITT
                }
                else
                {
                    crcValue = crcValue << 1
                }

                newByte <<= 1
            
            return crcValue
            

        # calculate crc function.
        def exampleOfUseCRC16(self, Data, len):
            
            aux = 0
            crc = 0xFFFF  # Initialization of crc to 0xFFFF for CCITT

            while (aux < len):
                
                crc = crc16(crc, Data[aux])
                aux += 1

            return crc