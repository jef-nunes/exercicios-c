# Cor do texto suportadas apenas de 8bits
cor1='\033[0;30m' # Black
cor2='\033[0;31m' # Red
cor3='\033[0;32m' # Green
cor4='\033[0;33m' # Yellow
cor5='\033[0;34m' # Blue
cor6='\033[0;35m' # Purple
cor7='\033[0;36m' # Aqua
cor8='\033[0;37m' # Light Grey
cor9='\033[1;30m' # Dark Grey
cor10='\033[1;31m' # Bright Red
cor11='\033[1;32m' # Bright Green
cor12='\033[1;33m' # Brigth Yellow
cor13='\033[1;34m' # Bright Blue
cor14='\033[1;35m' # Bright Purple
cor15='\033[1;36m' # Bright Aqua
cor16='\033[1;37m' # White
corBg1="\033[0;40m" # Black
rescor='\033[0m' # Reset

xPS1_DEFAULT="$PS1"
bashIcon="\$"
xPS1_STYLE_1="\n\[$cor3\]«\[$rescor\]\[$cor11\]User\[$rescor\]\[$cor3\]»\[$rescor\] \[$cor7\]\w/ \[$rescor\]\[$corBg1\]\[$cor15\]$bashIcon\[$rescor\] "
PS1="${xPS1_STYLE_1}"
# Alias
# Padrao
alias prefixReset='export PS1="$DEFAULT_PS1"'
# Estilo 1
alias prefixStyle1='export PS1="xPS1_STYLE_1"'


