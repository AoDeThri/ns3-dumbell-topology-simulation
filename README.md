# ns3-dumbell-topology-simulation

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Analyze and compare TCP Reno, TCP Westwood, and TCP Fack performance using NS3 simulator

### Topology

       H1 ---+      +--- H4
             |      |
       H2 ---R1 -- R2--- H5
             |      |
       H3 ---+      +--- H6

A Dumbbell topology with two routers R1 and R2 connected by a (10 Mbps, 50 ms) wired link.

Each of the routers is connected to 3 hosts
i.e., H1, H2 and H3 are connected to R1,
and H4, H5 and H6 are connected to R2.
All the hosts are attached to the routers with (100 Mbps, 20ms) links.

Both the routers use drop-tail queues with a equal queue size set according to bandwidth-delay product.

Senders (i.e. H1, H2 and H3) are attached with TCP Reno, TCP Westwood, and TCP Fack agents respectively.

Packet size is 1.2KB.

### Simulation

For all the simulations:
- An error model with error rate of 0.000001 was installed on the each link between host and router.
- Congestion window, throughput, goodput and congestion loss are traced using NS3 only, with no other utility except for gnuplot for plotting traces.
- Congestion window, throughput and goodput are measured using TraceCallbacks and congestion loss is measured using FlowMonitor.
- Following dumbbell topology is used:
Implementation detail:
		 _					_
		|	H1------+	  +------H4	 |
		|		 |	  |		 |
Senders	|	H2------R1------R2-----H5	 |	Receivers
		|		 |	  |		 |
		|_	H3------+	  +------H6	_|
	Representation in code:
	H1(n0), H2(n1), H3(n2), H4(n3), H5(n4), H6(n5), R1(n6), R2(n7) :: n stands for node
	Dumbbell topology is used with 
	H1, H2, H3 on left side of dumbbell,
	H4, H5, H6 on right side of dumbbell,
	and routers R1 and R2 form the bridge of dumbbell.
	H1 is attached with TCP Reno agent.
	H2 is attached with TCP Westwood agent.
	H3 is attached with TCP Tahoe agent.
	Links:
	H1R1/H2R1/H3R1/H4R2/H5R2/H6R2: P2P with 100Mbps and 20ms.
	R1R2: (dumbbell bridge) P2P with 10Mbps and 50ms.
	packet size: 1.2KB.
	Number of packets decided by Bandwidth delay product:
	i.e. #packets = Bandwidth*Delay(in bits)
	Therefore, max #packets (HiRj) = 100Mbps*20ms = 2000000
	and max #packets (R1R2) = 10Mbps*50ms = 500000




