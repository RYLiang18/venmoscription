#!/bin/zsh

venmoscription_dir="/home/giich/programming_projects/venmoscription"
venmo_token_loc="/home/giich/programming_projects/venmoscription/secrets/venmo_api_token.txt"

# echo "$venmo_token"

docker build -t venmoscription "$venmoscription_dir"
docker run -e venmo_token=$(cat "$venmo_token_loc" ) venmoscription