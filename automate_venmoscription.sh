#!/bin/zsh

venmoscription_dir="/home/giich/programming_projects/venmoscription"
venmo_token_loc="/home/giich/programming_projects/venmoscription/secrets/venmo_api_token.txt"
# log_location="/home/giich/programming_projects/venmoscription/logs"

# echo "$venmo_token"

docker build -t venmoscription "$venmoscription_dir"
# docker run -v "$log_location":/app/logs:Z -e venmo_token=$(cat "$venmo_token_loc" ) venmoscription
docker run -e venmo_token=$(cat "$venmo_token_loc" ) venmoscription

exit 0