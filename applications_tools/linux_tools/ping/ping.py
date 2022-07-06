import os
import subprocess
from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs, user_continue

def ping():
    command = "ping "
    print("""
\n ping \n
    1-ping infinite
    2-configurable ping
    0-exit""")
    users_input = users_inputs(0,2)
    
    ip_or_site_to_ping = str(input("Give me a Site or an ip to ping: "))
    
    if users_input == 1:
        command += ip_or_site_to_ping
    else:
        command += str(input("""
OPTIONS
       -4
           Use IPv4 only.

       -6
           Use IPv6 only.

       -a
           Audible ping.

       -A
           Adaptive ping. Interpacket interval adapts to round-trip time, so that effectively not more than
           one (or more, if preload is set) unanswered probe is present in the network. Minimal interval is
           200msec unless super-user. On networks with low RTT this mode is essentially equivalent to flood
           mode.

       -b
           Allow pinging a broadcast address.

       -B
           Do not allow ping to change source address of probes. The address is bound to one selected when
           ping starts.

       -c count
           Stop after sending count ECHO_REQUEST packets. With deadline option, ping waits for count
           ECHO_REPLY packets, until the timeout expires.

       -d
           Set the SO_DEBUG option on the socket being used. Essentially, this socket option is not used by
           Linux kernel.

       -D
           Print timestamp (unix time + microseconds as in gettimeofday) before each line.

       -f
           Flood ping. For every ECHO_REQUEST sent a period “.” is printed, while for every ECHO_REPLY
           received a backspace is printed. This provides a rapid display of how many packets are being
           dropped. If interval is not given, it sets interval to zero and outputs packets as fast as they
           come back or one hundred times per second, whichever is more. Only the super-user may use this
           option with zero interval.

       -F flow label
           IPv6 only. Allocate and set 20 bit flow label (in hex) on echo request packets. If value is
           zero, kernel allocates random flow label.

       -h
           Show help.

       -i interval
           Wait interval seconds between sending each packet. Real number allowed with dot as a decimal
           separator (regardless locale setup). The default is to wait for one second between each packet
           normally, or not to wait in flood mode. Only super-user may set interval to values less than 2
           ms.

       -I interface
           interface is either an address, an interface name or a VRF name. If interface is an address, it
           sets source address to specified interface address. If interface is an interface name, it sets
           source interface to specified interface. If interface is a VRF name, each packet is routed using
           the corresponding routing table; in this case, the -I option can be repeated to specify a source
           address. NOTE: For IPv6, when doing ping to a link-local scope address, link specification (by
           the '%'-notation in destination, or by this option) can be used but it is no longer required.

       -l preload
           If preload is specified, ping sends that many packets not waiting for reply. Only the super-user
           may select preload more than 3.

       -L
           Suppress loopback of multicast packets. This flag only applies if the ping destination is a
           multicast address.

       -m mark
           use mark to tag the packets going out. This is useful for variety of reasons within the kernel
           such as using policy routing to select specific outbound processing.

       -M pmtudisc_opt
           Select Path MTU Discovery strategy.  pmtudisc_option may be either do (prohibit fragmentation,
           even local one), want (do PMTU discovery, fragment locally when packet size is large), or dont
           (do not set DF flag).

       -N nodeinfo_option
           IPv6 only. Send ICMPv6 Node Information Queries (RFC4620), instead of Echo Request. CAP_NET_RAW
           capability is required.

           help
               Show help for NI support.

           name
               Queries for Node Names.

           ipv6
               Queries for IPv6 Addresses. There are several IPv6 specific flags.

               ipv6-global
                   Request IPv6 global-scope addresses.

               ipv6-sitelocal
                   Request IPv6 site-local addresses.

               ipv6-linklocal
                   Request IPv6 link-local addresses.

               ipv6-all
                   Request IPv6 addresses on other interfaces.

           ipv4
               Queries for IPv4 Addresses. There is one IPv4 specific flag.

               ipv4-all
                   Request IPv4 addresses on other interfaces.

           subject-ipv6=ipv6addr
               IPv6 subject address.

           subject-ipv4=ipv4addr
               IPv4 subject address.

           subject-name=nodename
               Subject name. If it contains more than one dot, fully-qualified domain name is assumed.

           subject-fqdn=nodename
               Subject name. Fully-qualified domain name is always assumed.

       -n
           Numeric output only. No attempt will be made to lookup symbolic names for host addresses.

       -O
           Report outstanding ICMP ECHO reply before sending next packet. This is useful together with the
           timestamp -D to log output to a diagnostic file and search for missing answers.

       -p pattern
           You may specify up to 16 “pad” bytes to fill out the packet you send. This is useful for
           diagnosing data-dependent problems in a network. For example, -p ff will cause the sent packet
           to be filled with all ones.

       -q
           Quiet output. Nothing is displayed except the summary lines at startup time and when finished.

       -Q tos
           Set Quality of Service -related bits in ICMP datagrams.  tos can be decimal (ping only) or hex
           number.

           In RFC2474, these fields are interpreted as 8-bit Differentiated Services (DS), consisting of:
           bits 0-1 (2 lowest bits) of separate data, and bits 2-7 (highest 6 bits) of Differentiated
           Services Codepoint (DSCP). In RFC2481 and RFC3168, bits 0-1 are used for ECN.

           Historically (RFC1349, obsoleted by RFC2474), these were interpreted as: bit 0 (lowest bit) for
           reserved (currently being redefined as congestion control), 1-4 for Type of Service and bits 5-7
           (highest bits) for Precedence.

       -r
           Bypass the normal routing tables and send directly to a host on an attached interface. If the
           host is not on a directly-attached network, an error is returned. This option can be used to
           ping a local host through an interface that has no route through it provided the option -I is
           also used.

       -R
           ping only. Record route. Includes the RECORD_ROUTE option in the ECHO_REQUEST packet and
           displays the route buffer on returned packets. Note that the IP header is only large enough for
           nine such routes. Many hosts ignore or discard this option.

       -s packetsize
           Specifies the number of data bytes to be sent. The default is 56, which translates into 64 ICMP
           data bytes when combined with the 8 bytes of ICMP header data.

       -S sndbuf
           Set socket sndbuf. If not specified, it is selected to buffer not more than one packet.

       -t ttl
           ping only. Set the IP Time to Live.

       -T timestamp option
           Set special IP timestamp options.  timestamp option may be either tsonly (only timestamps),
           tsandaddr (timestamps and addresses) or tsprespec host1 [host2 [host3 [host4]]] (timestamp
           prespecified hops).

       -U
           Print full user-to-user latency (the old behaviour). Normally ping prints network round trip
           time, which can be different f.e. due to DNS failures.

       -v
           Verbose output. Do not suppress DUP replies when pinging multicast address.

       -V
           Show version and exit.

       -w deadline
           Specify a timeout, in seconds, before ping exits regardless of how many packets have been sent
           or received. In this case ping does not stop after count packet are sent, it waits either for
           deadline expire or until count probes are answered or for some error notification from network.

       -W timeout
           Time to wait for a response, in seconds. The option affects only timeout in absence of any
           responses, otherwise ping waits for two RTTs. Real number allowed with dot as a decimal
           separator (regardless locale setup). 0 means infinite timeout.
Give me your options: """)) + ip_or_site_to_ping
    
    os.system(command)
    
    nothing = input("press enter to exit: ")
    
    print("\n\n")