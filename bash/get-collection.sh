#!/bin/bash

COLLECTION="doodles-official"
set -x

curl --request GET \
     --url https://api.opensea.io/api/v1/collection/$COLLECTION/stats \
     --header 'Accept: application/json'