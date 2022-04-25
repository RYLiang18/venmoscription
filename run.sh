# !/bin/zsh
read -p 'venmo api token: ' venmo_api_token

docker build -t giich_venmoscription_image .
docker run \
    -e venmo_token=$venmo_api_token \
    --name giich_venmoscription_container \
    giich_venmoscription_image:latest

# cleaning up
docker container rm giich_venmoscription_container
docker image rm giich_venmoscription_image:latest