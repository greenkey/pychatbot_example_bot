CERTNAME=$1

openssl req -new -x509 -keyout $CERTNAME.pem -out $CERTNAME.pem -days 365 -nodes

