CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule']},
        ],
        'height': 200,
        'width': '140%',
        'extraPlugins': 'autogrow',
        'autoGrow_minHeight': 200,
        'autoGrow_maxHeight': 600,
        'autoGrow_bottomSpace': 50,
        'removePlugins': 'elementspath',
        'allowedContent': True,
        'extraAllowedContent': 'img[alt,border,width,height,align];a[!href];',
        'language': 'ru',
        'uiColor': '#9AB8F3',
    },
}