#!/usr/bin/env bash

ROOT_UID=0
E_NOTROOT=87
E_NOTWHICH=89
PATH_MODIFIED_FILES=/tmp/modified_files_tmp
PATH_INFORMES=/root/informes

# Parametros de entrada
FLAG_STORE_FILES=
FLAG_STORE_CONNS=
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
mkdir -p $PATH_INFORMES

real_users=$(cat /etc/passwd | grep home | awk -F: '{print $1}')
if [ -z $FLAG_SEL_USER ]; then
	FLAG_SEL_USER=$real_users
fi

#echo $FLAG_STORE_FILES
#echo $FLAG_STORE_CONNS
#echo $FLAG_SEL_USER

touch $PATH_MODIFIED_FILES

# Almacenamos en un fichero el listado de los ficheros de todos los usuarios
if [ ! -z $FLAG_STORE_FILES ]; then
	#current_secs=$(date +%s)
	#day_ago_secs=`expr $current_secs - 86400`
	#echo $day_ago_secs
	#sudo find /home/mgr/tmp/ -exec stat --format '%Y %n' "{}" \; \
	#	| awk -v secs="$day_ago_secs" '{ if($1 > secs) { print $2; } }' > $PATH_MODIFIED_FILES
	sudo find /home/mgr/tmp/ -mtime -1 -exec ls -ltr --time-style=full-iso {} + > $PATH_MODIFIED_FILES
fi

for user in $FLAG_SEL_USER
do
	#echo -ne "$user\n"
	if [ ! -z $FLAG_STORE_FILES ]; then
		tmp_user_file=/tmp/${user}_tmp
		echo $tmp_user_file

		#cat $PATH_MODIFIED_FILES

		grep "$user" $PATH_MODIFIED_FILES \
			| awk '{print $6 " " $7 " " $9}' \
			| awk -F: '{print $1 " " $3}' \
			| awk '{print $1 " " $2 " " $4}' > $tmp_user_file

		days=$(cat $tmp_user_file | awk '{print $1}' | sort | uniq)
		hours=$(cat $tmp_user_file | awk '{print $2}' | sort | uniq)

		echo "Ficheros modificados por $user"
		cat $tmp_user_file

		for day in $days
		do
			for hour in $hours
			do
				file=${PATH_INFORMES}/${user}-${day}-${hour}
				#echo $file

				ptt="$day_$hour"
				grep $ptt $tmp_user_file \
					| awk '{print "FICHERO_MODIFICADO:" $3}' >> $file
			done
		done

		#echo $days
		#echo $hours

		rm -f $tmp_user_file
	fi
done

rm -f $PATH_MODIFIED_FILES
