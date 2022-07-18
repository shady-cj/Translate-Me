#! /bin/bash
sam build
sam local invoke -e payload.json
