import sys, paramiko, time, os
from scapy.all import *

def installations():
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
#SFTP connection node 0
	t = paramiko.Transport((node_address, port0))
	t.connect(username=username, password=passpharse,pkey=mykey)
	sftp = paramiko.SFTPClient.from_transport(t)

#SFTP connection node 1
	t1 = paramiko.Transport((node1_address, port1))
	t1.connect(username=username, password=passpharse,pkey=mykey)
	sftp1 = paramiko.SFTPClient.from_transport(t1)

#SFTP connection node 2
	t2 = paramiko.Transport((node_address, port2))
	t2.connect(username=username, password=passpharse,pkey=mykey)
	sftp2 = paramiko.SFTPClient.from_transport(t2)

#SFTP connection node 3
	t3 = paramiko.Transport((node1_address, port3))
	t3.connect(username=username, password=passpharse,pkey=mykey)
	sftp3 = paramiko.SFTPClient.from_transport(t3)

#SFTP connection node 4
	t4 = paramiko.Transport((node4_address, port4))
	t4.connect(username=username, password=passpharse,pkey=mykey)
	sftp4 = paramiko.SFTPClient.from_transport(t4)

#SFTP connection node 5
	t5 = paramiko.Transport((node_address, port5))
	t5.connect(username=username, password=passpharse,pkey=mykey)
	sftp5 = paramiko.SFTPClient.from_transport(t5)

#SFTP connection node 6
	t6 = paramiko.Transport((node6_address, port6))
	t6.connect(username=username, password=passpharse,pkey=mykey)
	sftp6 = paramiko.SFTPClient.from_transport(t6)

#SFTP connection node 7
	t7 = paramiko.Transport((node7_address, port7))
	t7.connect(username=username, password=passpharse,pkey=mykey)
	sftp7 = paramiko.SFTPClient.from_transport(t7)

#SFTP connection node 8
	t8 = paramiko.Transport((node4_address, port8))
	t8.connect(username=username, password=passpharse,pkey=mykey)
	sftp8 = paramiko.SFTPClient.from_transport(t8)

#SFTP connection node 9
	t9 = paramiko.Transport((node_address, port9))
	t9.connect(username=username, password=passpharse,pkey=mykey)
	sftp9 = paramiko.SFTPClient.from_transport(t9)

#SFTP connection node 10
	t10 = paramiko.Transport((node6_address, port10))
	t10.connect(username=username, password=passpharse,pkey=mykey)
	sftp10 = paramiko.SFTPClient.from_transport(t10)

#SFTP connection node 11
	t11 = paramiko.Transport((node7_address, port11))
	t11.connect(username=username, password=passpharse,pkey=mykey)
	sftp11 = paramiko.SFTPClient.from_transport(t11)

	print ("-------Connections SFTP created for 12 nodes------")

#command executing on node 0
	#stdin, stdout, stderr = client.exec_command("sudo apt-get update -y")
	#stdout.read()
	#stdin, stdout, stderr = client.exec_command("sudo apt-get install -y tshark")



#command t-shark installing executing on node 1
	#stdin, stdout, stderr = client1.exec_command("sudo apt-get update -y")
	#stdout.read()
	#tdin, stdout, stderr = client1.exec_command("sudo apt-get install -y tshark")
	#stdout.read()
	
#command t-shark installing executing on node 2
#	stdin, stdout, stderr = client2.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client2.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 3
#	stdin, stdout, stderr = client3.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client3.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 4
#	stdin, stdout, stderr = client4.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client4.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 5
#	stdin, stdout, stderr = client5.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client5.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 6
#	stdin, stdout, stderr = client6.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client6.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 7
#	stdin, stdout, stderr = client7.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client7.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 8
#	stdin, stdout, stderr = client8.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client8.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 9
#	stdin, stdout, stderr = client9.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client9.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 10
#	stdin, stdout, stderr = client10.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client10.exec_command("sudo apt-get install -y tshark")
#	stdout.read()

#command t-shark installing executing on node 11
#	stdin, stdout, stderr = client11.exec_command("sudo apt-get update -y")
#	stdout.read()
#	stdin, stdout, stderr = client11.exec_command("sudo apt-get install -y tshark")
#	stdout.read()



	print("\n ----------- installed tshark on 12 nodes (skipped) -----------")




	#tshark start node 0
	stdin, stdout, stderr = client.exec_command("sudo tshark -i eth2 -w /tmp/node0.pcap -a duration:15")
	
	print ("----Tshark on node 0 (eth2) started for 15 secs-----")

	
	#tshark start node 1
	stdin, stdout, stderr = client1.exec_command("sudo tshark -i eth2 -w /tmp/node1.pcap -a duration:15")
	
	print ("----Tshark on node 1 (eth2) started for 15 secs-----")

	#tshark start node 2
	stdin, stdout, stderr = client2.exec_command("sudo tshark -i eth2 -w /tmp/node2.pcap -a duration:15")
	
	print ("----Tshark on node 2 (eth2) started for 15 secs-----")

	#tshark start node 3
	stdin, stdout, stderr = client3.exec_command("sudo tshark -i eth1 -w /tmp/node3.pcap -a duration:15")
	
	print ("----Tshark on node 3 (eth1) started for 15 secs-----")

	#tshark start node 4
	stdin, stdout, stderr = client4.exec_command("sudo tshark -i eth1 -w /tmp/node4.pcap -a duration:15")
	
	print ("----Tshark on node 4 (eth1) started for 15 secs-----")
	
	#tshark start node 5
	stdin, stdout, stderr = client5.exec_command("sudo tshark -i eth2 -w /tmp/node5.pcap -a duration:15")
	
	print ("----Tshark on node 5 (eth2) started for 15 secs-----")

	#tshark start node 6
	stdin, stdout, stderr = client6.exec_command("sudo tshark -i eth2 -w /tmp/node6.pcap -a duration:15")
	
	print ("----Tshark on node 6 (eth2) started for 15 secs-----")

	#tshark start node 7
	stdin, stdout, stderr = client7.exec_command("sudo tshark -i eth1 -w /tmp/node7.pcap -a duration:15")
	
	print ("----Tshark on node 7 (eth1) started for 15 secs-----")

	#TRAFFIC GENERATING on node 2 to node 3
	#stdin, stdout, stderr = client2.exec_command("ping -c 10 -s 3000 10.10.3.2")
	stdin, stdout, stderr = client11.exec_command("iperf -s -u &")
	stdin, stdout, stderr = client8.exec_command("iperf -u -c 10.10.9.2 &")
	stdout.read()
	print ("-------Traffic generating on Node 8 and node 11 completed--------")
	
	i=0
	for i in range (0,15,1):

		time.sleep(1)
		print (str(15-i) + " seconds until downloading pcaps")
	
	stdin, stdout, stderr = client1.exec_command("sudo chmod 777 /tmp/node1.pcap")
	stdin, stdout, stderr = client.exec_command("sudo chmod 777 /tmp/node0.pcap")
	stdin, stdout, stderr = client2.exec_command("sudo chmod 777 /tmp/node2.pcap")
	stdin, stdout, stderr = client3.exec_command("sudo chmod 777 /tmp/node3.pcap")
	stdin, stdout, stderr = client4.exec_command("sudo chmod 777 /tmp/node4.pcap")
	stdin, stdout, stderr = client5.exec_command("sudo chmod 777 /tmp/node5.pcap")
	stdin, stdout, stderr = client6.exec_command("sudo chmod 777 /tmp/node6.pcap")
	stdin, stdout, stderr = client7.exec_command("sudo chmod 777 /tmp/node7.pcap")

	stdout.read()
	print ("---------Chmod of pcaps changed----------")
	#kill process
	stdin, stdout, stderr = client8.exec_command("pkill iperf")
	stdin, stdout, stderr = client11.exec_command("pkill iperf")
	stdout.read()
	print ("---------Process (Iperf) killed----------")
	sftp1.get("/tmp/node1.pcap","node1.pcap",callback=None)
	print ("\n ---------pcap node 1 downloaded--------------")
	
	sftp.get("/tmp/node0.pcap","node0.pcap",callback=None)
	print ("\n ---------pcap node 0 downloaded--------------")

	sftp2.get("/tmp/node2.pcap","node2.pcap",callback=None)
	print ("\n ---------pcap node 2 downloaded--------------")

	sftp3.get("/tmp/node3.pcap","node3.pcap",callback=None)
	print ("\n ---------pcap node 3 downloaded--------------")

	sftp4.get("/tmp/node4.pcap","node4.pcap",callback=None)
	print ("\n ---------pcap node 4 downloaded--------------")

	sftp5.get("/tmp/node5.pcap","node5.pcap",callback=None)
	print ("\n ---------pcap node 5 downloaded--------------")

	sftp6.get("/tmp/node6.pcap","node6.pcap",callback=None)
	print ("\n ---------pcap node 6 downloaded--------------")

	sftp7.get("/tmp/node7.pcap","node7.pcap",callback=None)
	print ("\n ---------pcap node 7 downloaded--------------")

	#closing connections
	client.close()
	t.close()

	client1.close()
	t1.close()

	client2.close()
	t2.close()

	client3.close()
	t3.close()

	client4.close()
	t4.close()

	client5.close()
	t5.close()

	client6.close()
	t6.close()

	client7.close()
	t7.close()

	client8.close()
	t8.close()

	client9.close()
	t9.close()

	client10.close()
	t10.close()

	client11.close()
	t11.close()




def scappy(nodename):
	n0p=0
	ssend=0
	dsend=0
	n3datartemp=0
	n3datar=0
	n2datastemp=0
	n2datas=0
	timetemp1=0
	timetemp2=0
	time=0
	firstpacket=0
	node=''
	UDPp=0
	i=0
	print ("------------SCAPPY PROCESS------------")

	if (nodename == 0 ):
		node='node0.pcap'
	elif (nodename == 1 ):
		node='node1.pcap'
	elif (nodename == 2 ):
		node='node2.pcap'
	elif (nodename == 3 ):
		node='node3.pcap'
	elif (nodename == 4 ):
		node='node4.pcap'
	elif (nodename == 5 ):
		node='node5.pcap'
	elif (nodename == 6 ):
		node='node6.pcap'
	elif (nodename == 7 ):
		node='node7.pcap'
	
	# rdpcap comes from scapy and loads in our pcap file
	packets = rdpcap(node)
	pkts = rdpcap(node)
	filtered = (pkt for pkt in pkts if UDP in pkt)
	wrpcap(node+"_filtered.pcap", filtered)
	
	
	
	#print (packets.sessions())
	print ("------------" + str (node) +" result------------")
	# Let's iterate through every packet
	for packet in packets:
	
		#if packet.haslayer(UDP) and packet.haslayer(IP) and packet.haslayer(Raw): 
		#	if packet.getlayer(Raw).load == sys.argv[2]: 
		#	start = packet.time 
		#if packet.getlayer(Raw).load == sys.argv[3]: 
		#	end = packet.time 
		#	print (end - start)*1000 

		n0p = n0p+1

		
		if ( packet.haslayer(UDP) ) :
			if (firstpacket == 0):
				firstpacket=1
				print ("First UDP packet started at " + datetime.fromtimestamp(int(packet.time)).strftime('%H:%M:%S'))
				timetemp1=datetime.fromtimestamp(int(packet.time)).strftime('%S')
			UDPp=UDPp+1
			

		if ( packet.haslayer(UDP) and packet[IP].src == "10.10.11.2" ) :
			#print (packet.payload)
			ssend = ssend+1
			n2datastemp = int(packet.sprintf("%IP.len%"))
			n2datas = n2datastemp + n2datas
		

		if ( packet.haslayer(UDP) and packet[IP].dst == "10.10.9.2" ) :
			dsend+=1
			n3datartemp = int(packet.sprintf("%IP.len%"))
			n3datar= n3datar + n3datartemp

		
	
	#ffiltered pcap for time
	i=0
	for pkt in pkts :
		i=i+1
		if (i == UDPp):
			print ("Last UDP packet stopped at " + datetime.fromtimestamp(int(pkt.time)).strftime('%H:%M:%S'))
			timetemp2=datetime.fromtimestamp(float(pkt.time)).strftime('%S')

	
	
	time = int(timetemp2) - int(timetemp1)
	
	#print ("The time it takes to finish the transmission is: "+ str(time) + "(seconds)")
	
	#print (datetime.fromtimestamp(time).strftime('%H:%M:%S'))

	print ("Total number of packet travel through " + str (node) + " is " + str (n0p) +" packets")
	print ("Total number of packet sent by NODE 8 (10.10.11.2) is " + str (ssend) +" packets")
	print ("Total number of data sent by NODE 8 (10.10.11.2) is " + str (n2datas) +" bytes")
	print ("")
	print ("Total number of packet sent by NODE 11 (10.10.9.2) is " + str (dsend) +" packets")
	print ("Total number of data received by NODE 11 (10.10.9.2) is " + str (n3datar) +" bytes")
	if (ssend != 0)	:
		print ("Data rate of UDP traffics is " + str (n2datas/ssend) + " bytes/s")
	elif (ssend == 0) :
		print ("Data rate of UDP traffics is 0 bytes/s")
	
	print ("Good throughput of node 8 = " + str (n2datas) + "/ (transmision time in secs) " + " (bytes/s)")
	print ("---------------------------------------------")
	

#MAIN--------------------
print ("---Starting demo-----")
installations()

scappy(0)
scappy(1)
scappy(2)
scappy(3)
scappy(4)
scappy(5)
scappy(6)
scappy(7)
