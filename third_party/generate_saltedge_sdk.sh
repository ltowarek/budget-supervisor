#!/bin/bash
rm -rf ./saltedge/
curl https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.21/swagger-codegen-cli-3.0.21.jar -o ./swagger-codegen-cli.jar
java -jar swagger-codegen-cli.jar generate -i https://docs.saltedge.com/assets/swagger-aisp-v5-services.json -l python -o ./saltedge/
rm ./swagger-codegen-cli.jar
