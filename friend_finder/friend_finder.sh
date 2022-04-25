# !/bin/zsh
read -p 'venmo api token: ' venmo_api_token
read -p 'username to test: ' venmo_username

docker build -t friend_finder_image ..
docker run \
    -e venmo_token=$venmo_api_token \
    --name friend_finder_container \
    friend_finder_image:latest \
    python friend_finder/friend_finder.py $venmo_username

# cleaning up
docker container rm friend_finder_container
docker image rm friend_finder_image:latest