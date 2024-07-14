# User Service

## Install:
```
poetry install
```

## Endpoints:

### UserProfileViewSet
This class represents a set of views for handling user profiles. It supports standard CRUD operations (Create, Read, Update, Delete).

- `GET /profiles/` : Retrieve a list of all user profiles.
- `POST /profiles/` : Create a new user profile.
- `GET /profiles/{id}/` : Retrieve details of a specific user profile by ID.
- `PUT /profiles/{id}/` : Update a user profile by ID.
- `PATCH /profiles/{id}/` : Partially update a user profile by ID.
- `DELETE /profiles/{id}/` : Delete a user profile by ID.
- `GET /profiles/search/?{query}` : Search for user profiles by name or email.

### UserLoginApiView
This class is used for authenticating users and obtaining an access token.

- `POST /login/` : Authenticate a user and obtain an access token.

### UserProfileFeedViewSet
This class represents a set of views for handling profile feed items. It supports operations for creating, reading, and updating.

- `GET /feed/` : Retrieve a list of all profile feed items.
- `POST /feed/` : Create a new item in the profile feed.
- `GET /feed/{id}/` : Retrieve details of a specific profile feed item by ID.
- `PUT /feed/{id}/` : Update a profile feed item by ID.
- `PATCH /feed/{id}/` : Partially update a profile feed item by ID.
- `DELETE /feed/{id}/` : Delete a profile feed item by ID.