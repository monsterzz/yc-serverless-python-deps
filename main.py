from io import BytesIO
from barcode import generate
from barcode.writer import SVGWriter


def barcode(event, context):
    buf = BytesIO()
    generate('EAN13', '5901234123457', writer=SVGWriter(), output=buf)
    result = buf.getvalue().decode('utf-8')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/svg+xml',
        },
        'body': result,
        'isBase64Encoded': False,
    }
