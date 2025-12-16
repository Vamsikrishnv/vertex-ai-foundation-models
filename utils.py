def authenticate():
    from google.auth import default
    credentials, project_id = default()
    return credentials, project_id
