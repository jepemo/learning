#!/usr/bin/env bash
# -------------------------------------------------
# Herramiento que muestra y almacena información de uso de los usuarios.
#
# - Almacena en el directorio "/root/informes" informacion historica de las generaciones.
# - El formato de los ficheros es: usuario-anyo-mes-dia-hora
# - En cada fichero puede almacenar dos tipos de informacion:
#   - Ficheros modificador por el usuario en ficho dia/hora (prefijo FICHERO_MODIFICADO)
#   - Tiempo de duracion de la conexion en la hora (prefijo TIEMPO_SESSION_USUARIO)
# - La herramienta tiene que ejecutarse con permisos de root, además tiene que estar instalada la herramienta ac.
# - Los parametros de entrada son:
#   -a: Extrae informacion ficheros modificados
#   -e: Extrae informacion conexiones
#   -u <NombreUsuario>: Realiza la tarea para un usuario concreto
# - Si no se marca ninguna opción por defecto NO realiza ninguna de las operaciones.
# -------------------------------------------------

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
			# TODO: Comprobar si el usuario existe, sino salir
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
	sudo find /home/mgr/tmp/ -mtime -1 -exec ls -ltr --time-style=full-iso {} + > $PATH_MODIFIED_FILES
fi

for user in $FLAG_SEL_USER
do
	echo -ne "=> Procesando usuario: $user\n"
	if [ ! -z $FLAG_STORE_FILES ]; then
		echo "==> Extrayendo informacion ficheros modificados"
		
		tmp_user_file=/tmp/${user}_tmp

		grep "$user" $PATH_MODIFIED_FILES \
			| awk '{print $6 " " $7 " " $9}' \
			| awk -F: '{print $1 " " $3}' \
			| awk '{print $1 " " $2 " " $4}' > $tmp_user_file

		days=$(cat $tmp_user_file | awk '{print $1}' | sort | uniq)
		hours=$(cat $tmp_user_file | awk '{print $2}' | sort | uniq)

		# Mostramos la salida por pantalla
		echo "===> Ficheros modificados por $user"
		cat $tmp_user_file

		for day in $days
		do
			for hour in $hours
			do
				file=${PATH_INFORMES}/${user}-${day}-${hour}

				ptt="$day_$hour"
				grep $ptt $tmp_user_file \
					| awk '{print "FICHERO_MODIFICADO:" $3}' >> $file
			done
		done

		rm -f $tmp_user_file
	fi
	
	if [ ! -z $FLAG_STORE_CONNS ]; then
		echo "==> Extrayendo informacion sessiones"
		tmp_user_file1=/tmp/${user}_tmp1
		tmp_user_file2=/tmp/${user}_tmp2
		tmp_user_file3=/tmp/${user}_tmp3
		
		# Extraemos las diferentes fechas
		ac -day $user | head -n -1 | awk '{print "date -d\""$1FS$2FS$3"\" +%Y-%m-%d"}' | bash > $tmp_user_file1
		ac -day $user | head -n -1 | awk '{print $5}' > $tmp_user_file2
		
		paste $tmp_user_file1 $tmp_user_file2 > $tmp_user_file3
		
		# Mostramos la salida por pantalla
		echo "===> Conexiones del usuario"
		cat $tmp_user_file3
		
		fechas=$(cat $tmp_user_file3 | sort | uniq | awk '{print $1}')
		for fecha in $fechas
		do
			file=${PATH_INFORMES}/${user}-${fecha}-00
			grep $fecha $tmp_user_file3 | awk '{print "TIEMPO_SESSION_USUARIO:"$2}' >> $file
		done
		
		rm -f $tmp_user_file1
		rm -f $tmp_user_file2
		rm -f $tmp_user_file3
	fi
done

rm -f $PATH_MODIFIED_FILES

# Compactacion de los ficheros, para evitar duplicados
echo "==> Compactando ficheros generados"
FILES=${PATH_INFORMES}/*
for filepath in $FILES
do
	#filepath=${PATH_INFORMES}/$filename
	tmp_file=/tmp/informe_out_tmp
	
	# Reordenamos y quitamos duplicados
	cat $filepath | sort | uniq > $tmp_file
	
	# sustituimos el fichero de entrada por la salida limpia
	cat $tmp_file > $filepath
	
	# Borramos el fichero temporal
	rm -f $tmp_file
done 

echo "=> Ficheros historicos actualizados en $PATH_INFORMES"
