#!/bin/bash
rm -rf ./nordigen/
curl https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.21/swagger-codegen-cli-3.0.21.jar -o ./swagger-codegen-cli.jar
java -jar swagger-codegen-cli.jar generate -i https://ob.nordigen.com/api/swagger.json -l python -o ./nordigen/ -DpackageName=nordigen
rm ./swagger-codegen-cli.jar
