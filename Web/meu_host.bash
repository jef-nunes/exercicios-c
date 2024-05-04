# Visualizar status do host
hosting() {
    echo -e "\n_______________ Local Host Status _______________\n"
    echo "Name:" $(hostname)
    echo -e "\nIPs:\n"
    local out_ipaddr=$(ip addr | grep -Po 'inet \K[\d.]+')
    echo -e "${cor15}${out_ipaddr}${rescor}"
    echo -e "\nPortas abertas:\n"
    netstat -tuln | grep LISTEN | awk '{print $4}'
}
alias myhost='hosting'
alias myHost='hosting'
alias meuhost='hosting'
alias meuHost='hosting'
alias meuip='hosting'
alias meuIP='hosting'
alias myip='hosting'
alias myIP='hosting'
alias sobrehost='hosting'
alias sobreHost='hosting'
alias abouthost='hosting'
alias aboutHost='hosting'
