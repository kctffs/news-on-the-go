import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://uoinxdgnoet:bSYLayxSz7Ox@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech:5432/mousy_stony_snarl_880290',
        conn_max_age=600,
        ssl_require=True  # Enforce SSL
    )
}
