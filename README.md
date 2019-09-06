# Yandex.Cloud Serverless Functions : Python Barcode Generator

Small example which shows how to bundle Python 3.7 dependencies
and involve HTTP Integration to return custom content types.

To build deployment package:

    make all

To deploy it:

    yc serverless function create --name barcode
    yc serverless function version create \
        --function-name barcode           \
        --runtime python37                \
        --entrypoint main.barcode         \
        --memory 128M                     \
        --execution-timeout 1s            \
        --source-path dist.zip

[Test it](https://functions.yandexcloud.net/d4ebju6dj7mm3d6vj651)

Get your own invocation URL using:

    yc serverless function get --name barcode

**Don't forget to allow unauthorized function invocation**

Documentation: https://cloud.yandex.ru/docs/serverless-functions/
