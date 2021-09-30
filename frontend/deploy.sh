#!/user/bin/env sh

set -e

npm run build

cd dist

git init
git add -A 
git commit -m 'RealEstate'
git push -f https://github.com/tustica/RealEstate.git master:gh-pages

cd -