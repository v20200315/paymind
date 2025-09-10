ROLE_USER = "user"
ROLE_OWNER = "owner"
ROLE_ADMIN = "admin"
ROLE_MEMBER = "member"

ROLE_CHOICES = [
    (ROLE_OWNER, "Owner"),
    (ROLE_ADMIN, "Admin"),
    (ROLE_MEMBER, "Member"),
    (ROLE_USER, "User"),
]

ORG_ROLE_CHOICES = [
    (ROLE_OWNER, "Owner"),
    (ROLE_ADMIN, "Admin"),
    (ROLE_MEMBER, "Member"),
]

ADMIN_ROLES = [ROLE_OWNER, ROLE_ADMIN]
