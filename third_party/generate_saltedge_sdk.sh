#!/bin/bash
java -jar swagger-codegen-cli.jar generate -i https://docs.saltedge.com/assets/swagger-aisp-v5-services.json -l python -o saltedge
