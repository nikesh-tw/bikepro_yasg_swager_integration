# import mimetypes
# from base64 import b64decode, b64encode

# def encode_b64(value):
#     value.file.seek(0)
#     mime_type,encoding = mimetypes.guess_type(value.name)
#     if not mime_type:
#         mime_type = 'image/png'
#     data = value.file.read()
#     image_data = bytes('data:'+mime_type + ';base64,' encoding = 'UTF-8' ) + b64encode(data) 
#     return image_data # or str(image_data, 'utf-8')
