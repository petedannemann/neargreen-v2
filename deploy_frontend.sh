#!/usr/bin/env sh

# abort on errors
set -e

NODE_ENV="production"

# build
yarn run build

# navigate into the build output directory
cd dist

git init
git add -A
git commit -m 'deploy'

# deploy to https://petedannemann.github.io/petedannemann/neargreen-v2
git push -f https://github.com/petedannemann/neargreen-v2.git master:gh-pages

cd -