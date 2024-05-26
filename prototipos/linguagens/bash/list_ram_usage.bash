list_ram_usage(){
    {   
        echo -e "\n_______________ RAM Usage _______________\n"
        printf "%-8s %-10s %-10s %-10s %s\n" "PID" "USER" "%" "MB" "COMMAND"
        ps -e -o pid,user,%mem,rss,command --sort=-%mem | sed 1d | awk '{ printf "%-8s %-10s %-10s %-10.2f %s\n", $1, $2, $3, $4/1024, $5 }'
    } | less -S
}

alias ram='list_ram_usage'
alias RAM='list_ram_usage'
