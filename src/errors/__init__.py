class Error(Exception):
    """Base class for other exceptions"""
    pass


"""
########### DATABASE ERRORS ###########
"""


class Neo4jUriError(Error):
    """Raised when the neo4j uri is not defined"""
    pass


class Neo4jAuthError(Error):
    """Raised when neo4j username and/or password are not defined"""
    pass
