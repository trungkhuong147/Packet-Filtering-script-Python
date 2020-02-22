import sys, paramiko, time, os
from scapy.all import *

def remove():
	node_address = 'pc1.uky.emulab.net'
	node1_address = 'pc3.uky.emulab.net'
	node4_address = 'pc5.uky.emulab.net'
	node6_address = 'pc2.uky.emulab.net'
	node7_address = 'pc4.uky.emulab.net'
	username = 'tk7311'
	port0 = 25610
	port1 = 25610
	port2 = 25611
	port3 = 25611
	port4 = 25610
	port5 = 25612
	port6 = 25611
	port7 = 25611
	port8 = 25611
	port9 = 25613
	port10 = 25610
	port11 = 25610
	passpharse = '123456'
	mykey = paramiko.RSAKey.from_private_key_file('/home/student/.ssh/id_geni_ssh_rsa',password=passpharse)

	
#SSH connection node 0
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.WarningPolicy)
	client.connect(node_address, port=port0, username=username, pkey=mykey)

#SSH connection node 1
	client1 = paramiko.SSHClient()
	client1.set_missing_host_key_policy(paramiko.WarningPolicy)
	client1.connect(node1_address, port=port1, username=username, pkey=mykey)

#SSH connection node 2
	client2 = paramiko.SSHClient()
	client2.set_missing_host_key_policy(paramiko.WarningPolicy)
	client2.connect(node_address, port=port2, username=username, pkey=mykey)

#SSH connection node 3
	client3 = paramiko.SSHClient()
	client3.set_missing_host_key_policy(paramiko.WarningPolicy)
	client3.connect(node1_address, port=port3, username=username, pkey=mykey)

#SSH connection node 4
	client4 = paramiko.SSHClient()
	client4.set_missing_host_key_policy(paramiko.WarningPolicy)
	client4.connect(node4_address, port=port4, username=username, pkey=mykey)

#SSH connection node 5
	client5 = paramiko.SSHClient()
	client5.set_missing_host_key_policy(paramiko.WarningPolicy)
	client5.connect(node_address, port=port5, username=username, pkey=mykey)

#SSH connection node 6
	client6 = paramiko.SSHClient()
	client6.set_missing_host_key_policy(paramiko.WarningPolicy)
	client6.connect(node6_address, port=port6, username=username, pkey=mykey)

#SSH connection node 7
	client7 = paramiko.SSHClient()
	client7.set_missing_host_key_policy(paramiko.WarningPolicy)
	client7.connect(node7_address, port=port7, username=username, pkey=mykey)

#SSH connection node 8
	client8 = paramiko.SSHClient()
	client8.set_missing_host_key_policy(paramiko.WarningPolicy)
	client8.connect(node4_address, port=port8, username=username, pkey=mykey)

#SSH connection node 9
	client9 = paramiko.SSHClient()
	client9.set_missing_host_key_policy(paramiko.WarningPolicy)
	client9.connect(node_address, port=port9, username=username, pkey=mykey)


#SSH connection node 10
	client10 = paramiko.SSHClient()
	client10.set_missing_host_key_policy(paramiko.WarningPolicy)
	client10.connect(node6_address, port=port10, username=username, pkey=mykey)


#SSH connection node 11
	client11 = paramiko.SSHClient()
	client11.set_missing_host_key_policy(paramiko.WarningPolicy)
	client11.connect(node7_address, port=port11, username=username, pkey=mykey)

	print ("-------Connections SSH created for 12 nodes------")

	#File removing
	stdin, stdout, stderr = client.exec_command("sudo rm /tmp/node0.pcap")
	print ("----Removed node 0 pcap file completed-----")

	stdin, stdout, stderr = client1.exec_command("sudo rm /tmp/node1.pcap")
	print ("----Removed node 1 pcap file completed-----")

	stdin, stdout, stderr = client2.exec_command("sudo rm /tmp/node2.pcap")
	print ("----Removed node 2 pcap file completed-----")

	stdin, stdout, stderr = client3.exec_command("sudo rm /tmp/node3.pcap")
	print ("----Removed node 3 pcap file completed-----")

	stdin, stdout, stderr = client4.exec_command("sudo rm /tmp/node4.pcap")
	print ("----Removed node 4 pcap file completed-----")
	
	stdin, stdout, stderr = client5.exec_command("sudo rm /tmp/node5.pcap")
	print ("----Removed node 5 pcap file completed-----")

	stdin, stdout, stderr = client6.exec_command("sudo rm /tmp/node6.pcap")
	print ("----Removed node 6 pcap file completed-----")

	stdin, stdout, stderr = client7.exec_command("sudo rm /tmp/node7.pcap")
	print ("----Removed node 7 pcap file completed-----")

	stdin, stdout, stderr = client8.exec_command("sudo rm /tmp/node8.pcap")
	print ("----Removed node 8 pcap file completed-----")

	stdin, stdout, stderr = client9.exec_command("sudo rm /tmp/node9.pcap")
	print ("----Removed node 9 pcap file completed-----")

	stdin, stdout, stderr = client10.exec_command("sudo rm /tmp/node10.pcap")
	print ("----Removed node 10 pcap file completed-----")

	stdin, stdout, stderr = client11.exec_command("sudo rm /tmp/node11.pcap")
	print ("----Removed node 11 pcap file completed-----")
	stdout.read()
	
	#closing connections
	client.close()

	client1.close()

	client2.close()

	client3.close()

	client4.close()

	client5.close()

	client6.close()

	client7.close()

	client8.close()

	client9.close()

	client10.close()

	client11.close()




#MAIN--------------------
print ("---Starting removing pcaps on nodes-----")
remove()
