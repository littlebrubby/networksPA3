FROM ubuntu

RUN apt-get update
RUN apt-get -y install bash iproute2 net-tools tcpdump vim iputils-ping
RUN apt-get clean

RUN apt -y install curl
RUN apt -y install gnupg
RUN curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null
RUN apt install lsb-release
ENV FRRVER "frr-stable"
RUN echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list
RUN apt update && apt -y install frr frr-pythontools
COPY daemons etc/frr
CMD service frr restart
CMD vtysh -c 'configure terminal' -c 'router ospf' -c 'network 10.0.14.0/24 area 0.0.0.0' -c 'network 10.0.16.0/24 area 0.0.0.0' -c 'network 10.0.18.0/24 area 0.0.0.0' -c 'end'
CMD vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'exit' -c 'end'
CMD vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'exit' -c 'end'
CMD vtysh -c 'configure terminal' -c 'interface eth2' -c 'ip ospf cost 5' -c 'exit' -c 'end'

CMD ["bash"]
