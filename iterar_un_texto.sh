set -x
var='Un hombre
en una mañana de enero
ahorra dinero'
fun() {
echo "-$1-"
echo "*$2*"
echo ".$3."
}
fun $var
