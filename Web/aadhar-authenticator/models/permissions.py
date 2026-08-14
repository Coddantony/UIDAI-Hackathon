from enum import Enum

class Permission(str, Enum):
    VERIFY_IDENTITY = "verify_identity"
    VIEW_AUDIT = "view_audit"
    MANAGE_KEYS = "manage_keys"
