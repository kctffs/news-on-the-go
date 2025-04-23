import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_WEDxlNU3Hy1S@ep-proud-grass-a2f34ebo.eu-central-1.aws.neon.tech/date_outer_pod_313966',
        conn_max_age=600,
        ssl_require=True  # Enforce SSL
    )
}
