# !/bin/zsh
heroku container:login

heroku container:push worker -a venmoscription-v2
heroku container:release worker -a venmoscription-v2

heroku container:push web -a venmoscription-v2
heroku container:release web -a venmoscription-v2