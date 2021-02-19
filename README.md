## deploy
```` $ docker build -t getdata-crypto:latest . ````

## run-getdata-crypto

Para cuestiones de desarrollo y prueba se monta un volumen apuntando a una carpeta donde descarga csv

````
docker run -it --rm \
	 --mount type=bind,source=$(pwd)/data,target=/data \
	-e API_KEY="key" \
	-e APIAPI_SECRET_KEY="secret_key" \
	--name getdata-crypto \
	getdata-crypto:latest
````