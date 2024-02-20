import hashlib      
import bcrypt
import os


def script_colors(color_type, text):
    
    if os.name == 'nt':
        return text
    else:
        color_end = '\033[0m'

        if color_type.lower() == "r" or color_type.lower() == "red":
            red = '\033[91m'
            text = red + text + color_end
        elif color_type.lower() == "lgray":
            gray = '\033[2m'
            text = gray + text + color_end
        elif color_type.lower() == "gray":
            gray = '\033[90m'
            text = gray + text + color_end
        elif color_type.lower() == "strike":
            strike = '\033[9m'
            text = strike + text + color_end
        elif color_type.lower() == "underline":
            underline = '\033[4m'
            text = underline + text + color_end
        elif color_type.lower() == "b" or color_type.lower() == "blue":
            blue = '\033[94m'
            text = blue + text + color_end
        elif color_type.lower() == "g" or color_type.lower() == "green":
            green = '\033[92m'
            text = green + text + color_end
        elif color_type.lower() == "y" or color_type.lower() == "yellow":
            yellow = '\033[93m'
            text = yellow + text + color_end
        elif color_type.lower() == "c" or color_type.lower() == "cyan":
            cyan = '\033[96m'
            text = cyan + text + color_end
        elif color_type.lower() == "cf" or color_type.lower() == "cafe":
            cafe = '\033[52m'
            text = cafe + text + color_end
        else:
            return text
        return  text

def banner_welcome():
    banner = '''
    
        ██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗ ███████╗███╗   ██╗
        ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝ ██╔════╝████╗  ██║
        ███████║███████║███████╗███████║██║  ███╗█████╗  ██╔██╗ ██║
        ██╔══██║██╔══██║╚════██║██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
        ██║  ██║██║  ██║███████║██║  ██║╚██████╔╝███████╗██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝

                                                                        version: 1.0
                                                         Autor: Juan Francisco Illan
                                                                @JohnCyberResistance
                                                                     
    '''
    return script_colors('lgray',banner)


def main():
    print(banner_welcome())
      
    clave = str(input("Introduce la contraseña: ")).encode('utf-8')
    print("==========================================")
    print("")

    hashmd5 = hashlib.md5(clave).hexdigest()
    #'42d8aa7cde9c78c4757862d84620c335'
    #len(hashmd5) #32

    hashsha1 = hashlib.sha1(clave).hexdigest()
    #'5d70c3d101efd9cc0a69f4df2ddf33b21e641f6a'
    #len(hashsha1) #40

    hashsha224 = hashlib.sha224(clave).hexdigest() 
    #'b05843cf74926ed0dfb6af2b2c6494eeb947203bac2ce5ff1d26f617'
    #len(hashsha224) #56

    hashsha256 = hashlib.sha256(clave).hexdigest() 
    #'23b5ed29a1e8409f70644e44faebae79ae687318efd719d9af29f8496b016a81'
    #len(hashsha256) #64

    hashsha384 = hashlib.sha384(clave).hexdigest() 
    #'2b998455bbe8636fc17547414259c1b3a643e4d01f9da1d08c37ce89dfaa66b77faf532337c336e200ffd9f517a23f19'
    #len(hashsha384) #96

    hashsha512 = hashlib.sha512(clave).hexdigest()
    #'8f225ddd400f8a0d6b36b85c6ccecc0436cea6a8e32f203fc5cef7932ffe5a0788eef1a1faf4acb307c5f831292574d6d05d3cad23f2468577b41c4c31ffc37a'
    #len(hashsha512) #128

    # Hash a password for the first time, with a randomly-generated salt
    hashbcrypt = bcrypt.hashpw(clave, bcrypt.gensalt()).hex()

    print("hashmd5:("+str(len(hashmd5))+")" + hashmd5)    
    print("hashsha1:("+str(len(hashsha1))+")" + hashsha1)    
    print("hashsha224:("+str(len(hashsha224))+")" + hashsha224)
    print("hashsha384:("+str(len(hashsha384))+")" + hashsha384)
    print("hashsha512:("+str(len(hashsha512))+")" + hashsha512)
    print("hashbcrypt:("+str(len(hashbcrypt))+")" + hashbcrypt)


if __name__ == '__main__':
    main()
    