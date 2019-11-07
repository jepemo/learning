#!/usr/bin/env bash

ROOT_UID=0
E_NOTROOT=87
E_NOTWHICH=89

# Parametros de entrada
FLAG_STORE_FILES=0
FLAG_STORE_CONNS=0
FLAG_SEL_USER=

usage()
{
	echo "Uso: $0 [-a] [-e] [-u nombre_usuario]"
}

preconditions()
{
# Se comprueba si el usuario  tiene permisos de ROOT
if [ "$EUID" -ne 0 ]; then 
	echo "Se necesitan permisos de root para ejecutar este script"
	exit $E_NOTROOT
fi

# Comprobamos si tenemos las utilizadades que necesitamos
which_ex=$(which ac)
if [ -z "$which_ex" ]; then
	echo "La aplicacion ac debe estar instalada."
	exit $E_NOTWHICH
fi
}

# Comprobaciones para ver si se puede ejecutar el script
preconditions

while getopts "aeu:" flag; do
	case "${flag}" in
		a) 
			FLAG_STORE_FILES=1
			;;
		e)
			FLAG_STORE_CONNS=1
			;;
		u)
			FLAG_SEL_USER=${OPTARG}
			# Falta comprobar si el usuario existe
			;;
		*)
			usage
			exit 0
			;;
	esac
done

# Creamos el directorio de los informes si no existen
mkdir -p /root/informes

real_users=$(cat /etc/passwd | grep home | awk -F: '{print $1}')
if [ -z $FLAG_SEL_USER ]; then
	FLAG_SEL_USER=$real_users
fi

#echo $FLAG_STORE_FILES
#echo $FLAG_STORE_CONNS
#echo $FLAG_SEL_USER

for user in "$FLAG_SEL_USER"
do
	echo -ne "$user\n"
done
