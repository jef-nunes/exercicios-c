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
alias meuhost='hosting'
