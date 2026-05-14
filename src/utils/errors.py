"""Custom exceptions for More-D-Admin"""

class MoreDAdminException(Exception):
    """Base exception for More-D-Admin"""
    pass

class AdminPrivilegesError(MoreDAdminException):
    """Raised when admin privileges are required but not available"""
    pass

class ServiceError(MoreDAdminException):
    """Raised when a service operation fails"""
    pass

class FileOperationError(MoreDAdminException):
    """Raised when a file operation fails"""
    pass

class RegistryError(MoreDAdminException):
    """Raised when a registry operation fails"""
    pass

class ProcessError(MoreDAdminException):
    """Raised when a process operation fails"""
    pass

class ApplicationError(MoreDAdminException):
    """Raised when an application operation fails"""
    pass

class SystemError(MoreDAdminException):
    """Raised when a system operation fails"""
    pass
