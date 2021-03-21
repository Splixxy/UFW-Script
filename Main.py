import os
install = input("Would you like to install the required packages and software for this script? Yes (Y) or No (N):")
if (install == "Y" or install == "y"):
    distro = input("Please input the package manager of your linux system")
    os.system("%s install pip3 -y" % distro)
    os.system("pip3 install pyufw -y")
    os.system("%s install ufw -y" % distro)
    import pyufw as ufw

    def firewallEnable():
        fEnable = input("Would you like to enable the UFW Firewall? Yes (Y) or No (N)")
        if (fEnable == "Y" or fEnable =="y"):
            ufw.enable()
            print("UFW has been Enabled.")
            SSH = input("Would you like to allow or deny port 22 (SSH) to the firewall (Highly Recommended, Denying could revoke access), Allow (A) or Deny (D):")
            if SSH == "A" or SSH == "a":
                ufw.add("allow 22")
                print("Port 22 (SSH) has been added to the firewall.")
            else:
                ufw.delete("allow 22")
                print("Port 22 (SSH) has been deleted if it was in the firewall.")

    def addORdeleteRule():
        aORdQuestion = input("Would you like to add or Delete a rule from the firewall, Yes (Y) or No (N):")
            if (aORdQuestion == "Y" or aORdQuestion == "y"):
                aORd = input("what you like to do Add a rule or Delete a rule (A) or (D)")
                if (aORd == "A" or aORd == "a"):
                    aport = input("Enter the ports you would like to add from the firewall with a comma seperating them:")
                    ufw.add("allow aport")
                else:
                    numORrule = input("Would you like to delete by number or rule, Num (N) or Rule (R):")
                    if (numORrule == "R" or numORrule == "r"):
                        dport = input("Enter the ports you would like to delete from the firewall with a common seperating them:")
                        ufw.delete("allow dport")
                    else:
                        ufw.get_rules()
                        dport = input("Enter the ports you would like to delete from the firewall with a common seperating them:")
                        ufw.delete(dport)

    def webServices():
        ufw.add("allow 80")
        ufw.add("allo 443")
        fOpen = open("/etc/ufw/before.rules", "r")
        contents = fOpen.readlines()
        fOpen.close()
        contents.insert(10, "\n*nat")
        contents.insert(11, "\n:PREROUTING ACCEPT [0:0]")
        contents.insert(12, "\n-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080")
        contents.insert(13, "\nCOMMIT")
        fOpen = open("/etc/ufw/before.rules", "w")
        contents = "".join(contents)
        fOpen.write(contents)
        fOpen.close()
        print("Ports 80 & 443 have been added to the firewall.")
        print("Port 80 is now being redirected to port 8080.")

    def portForward():
        dport = input("Please input the listening port:")
        rPort = input("Please input the port you would like %s redirected to:" % dPort)
        fOpen = open("/etc/ufw/before.rules", "r")
        contents = fOpen.readlines()
        fOpen.close()
        contents.insert(10, "\n*nat")
        contents.insert(11, "\n:PREROUTING ACCEPT [0:0]")
        contents.insert(12, "\n-A PREROUTING -p tcp --dport %s -j REDIRECT --to-port %s" % (dPort,rPort))
        contents.insert(13, "\nCOMMIT")
        fOpen = open("/etc/ufw/before.rules", "w")
        contents = "".join(contents)
        fOpen.write(contents)
        fOpen.close()
        print("Port %s is now being redirected to %s." % (dPort,rPort))

    def MySQL():
        SQLports = input("would you like to open the ports for Classic protocol (C), X protocol (X), or Both (B)")
        if (SQLports == "C" or SQLports == "c"):
            ufw.add("allow 3306")
            print("Port 3306 has been added to the firewall.")
        elif (SQLports == "X" or SQLports == "x"):
            ufw.add("allow 33060")
            print("Port 33060 has been added to the firewall.")
        else:
            ufw.add("allow 3306,33060")
            print("Ports 3306 & 33060 have been added to the firewall.")

    def mailPorts():
        mailPorts = input("What Mail services would like to allow through the firewall SMTP (SMTP), IMAP (IMAP), IMAPS (IMAPS), POP3 (POP3), Some (SOME), or All (A):")
        if (mailPorts == "SMTP" or mailPorts == "smtp"):
            ufw.add("allow 25")
            print("Port 25 has been added to the firewall.")
        elif (mailPorts == "IMAP" or mailPorts == "imap"):
            ufw.add("allow 143")
            print("Port 143 has been added to the firewall.")
        elif (mailPorts == "IMAPS" or mailPorts == "imaps"):
            ufw.add("allow 993")
            print("Port 993 has been added to the firewall.")
        elif (mailPorts == "POP3" or mailPorts == "pop3"):
            ufw.add("allow 110")
            print("Port 110 has been added to the firewall.")
        elif (mailPorts == "SOME" or mailPorts == "some"):
            sPorts = input("Please enter the ports of the Services you would like added seperated with a comma:")
            ufw.add("allow %s" % sPorts)
            print("Ports %s have been added to the firewall." % sPorts)
        else:
            allPorts = "25,143,993,110"
            ufw.add("allow %s" % allPorts)
            Print("Ports %s have been added to the firewall." % allPorts)

    def allowORblock():
        allowORblock = input("Would you like to allow specific hosts in the firewall hosts, Yes (Y) or No (N):")
        if (allowORblock == "Y" or allowORblock == "y"):
            hosts = input("Please input the IP or MAC Address you would like to allow")
            ufw.add("allow from %s" % hosts)
            print("%s is now allowed through the firewall." % hosts)
        else:
            pingAllow = input("Would you like to allow port 7 (Ping/ICMP) requests, Yes (Y) or No (N):")
            if (pingAllow == "Y" or pingAllow == "y"):
                ufw.add("allow 7")
                print("Port 7 has been added to the firewall.")
            else:
                telnetAllow = input("Would you like to allow port 23 (Telnet) through the firewall, Yes (Y) or No (N):")
                if (telnetAllow == "Y" or telnetAllow == "y"):
                    ufw.add("allow 23")
                    print("Port 23 has been added to the firewall.")

    def UFWbackup():
        os.system("%s install gzip" % distro)
        os.system("gzip -kv /etc/ufw/")
        print("/etc/ufw/ has been backupped.")

    run = input("Would you like to run all (A) the functions or only 1 (1)")
    if (run == "A" or run == "a"):
        firewallEnable()
        addORdeleteRule()
        portForward()
        MySQL()
        mailPorts()
        allowORblock()
        webServices()
        print("All functions completed")
    elif (run == "1")
        funSelect = input("Please input what function you would like to run firewallEnable (FIREWALLENABLE), addORdeleteRule (ADDORDELETERULE), portForward (PORTFORWARD, MySQL (MYSQL), mailPorts (MAILPORTS), allowORblock (ALLOWORBLOCK), or webServices (WEBSERVICES):")
        if (funSelect == "FIREWALLENABLE" or funSelect == "firewallenable"):
            firewallEnable()
        elif (funSelect == "ADDORDELETERULE" or funSelect == "addordeleterule"):
            addORdeleteRule()
        elif (funSelect == "PORTFORWARD" or funSelect == "portforward"):
            portForward()
        elif (funSelect == "MYSQL" or funSelect == "mysql"):
            MySQL()
        elif (funSelect == "MAILPORTS" or funSelect == "mailports"):
            mailPorts()
        elif (funSelect == "ALLOWORBLOCK" or funSelect == "alloworblock"):
            allowORblock()
        elif (funSelect == "WEBSERVICES" or funSelect == "webservices"):
            webServices()
        else:
            print("No function was selected, program is now exiting.")
            exit()

else:
    print("Program is now exiting.")
    exit()
