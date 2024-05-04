#!/usr/bin/perl

# Inicializando um servidor Deno JS
use strict;
use warnings;
use Time::HiRes qw(sleep);

system("clear");

# Verificar dentre as portas selecionadas
# se alguma esta disponivel
my @ports = (54321, 54320, 54322, 5454, 5353);
my $available_port;

for my $port (@ports) {
    my $output = `netstat -tln | grep ":$port\\b"`;
    unless ($output) {
        $available_port = $port;
        print "\n Porta $port está disponível. Estabelecendo conexão...\n";
        last; 
    }
}

if ($available_port) {
    sleep(1.5);
    system("deno run --allow-net --allow-read server.ts $available_port");
} else {
    print "Nenhuma porta disponível encontrada.\n";
}
