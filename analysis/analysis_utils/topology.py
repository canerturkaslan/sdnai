from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.node import RemoteController
from mininet.util import customClass

# execfile('sflow-rt/extras/sflow.py')

# Rate limit links to 10Mbps
link = customClass({'tc': TCLink}, 'tc,bw=10')


def myNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8', switch='OpenFlow13', link=link)

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='172.17.0.2',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, protocols='OpenFlow13')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, protocols='OpenFlow13')

    info('*** Add hosts\n')
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.2.2', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.2.3', defaultRoute=None)
    info('*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h7, s1)
    net.addLink(h6, s1)
    net.addLink(h5, s1)
    net.addLink(h4, s1)
    net.addLink(h3, s1)
    net.addLink(h2, s1)
    net.addLink(h8, s2)
    net.addLink(h9, s2)
    net.addLink(h10, s3)
    net.addLink(h11, s3)
    net.addLink(s2, s1)
    net.addLink(s3, s1)

    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()