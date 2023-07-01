# TODO: sync the port with the .env variable
URL="http://localhost:5050"

# export IDENTITY=<username>
# export PASSWORD=<password>
plogin:
	@curl -X POST -d "identity=${IDENTITY}&password=${PASSWORD}" ${URL}/api/collections/users/auth-with-password

# export TOKEN=<token>
# export USERID=<userid>
padd:
	@curl -X POST -H 'Content-Type: application/json' \
	-H "Authorization: Bearer ${TOKEN}" \
	-d '{"title":"testing", "recipe":"hello world", "chef":"${USERID}"}' \
	${URL}/api/collections/recipes/records

# export USERID=<userid>
plist:
	curl -g "${URL}/api/collections/recipes/records/?filter=(chef='${USERID}')"

# export RECORDID=<recordid>
pview:
	@curl ${URL}/api/collections/recipes/records/${RECORDID}

# export TOKEN=<token>
# export RECORDID=<recordid>
pedit:
	@curl -X PATCH -H 'Content-Type: application/json' \
	-H "Authorization: Bearer ${TOKEN}" \
	-d '{"title":"testing2"}' \
	${URL}/api/collections/recipes/records/${RECORDID}

# export TOKEN=<token>
# export RECORDID=<recordid>
pdelete:
	@curl -X DELETE \
	-H "Authorization: Bearer ${TOKEN}" \
	${URL}/api/collections/recipes/records/${RECORDID}