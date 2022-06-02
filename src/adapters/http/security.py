from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from decouple import config
from datetime import datetime, timezone
import jwt
from fastapi import HTTPException, Request, Depends
from src.adapters.shared.beani_repository_adapter import BeaniUserRepositoryAdapter
from src.core.shared.models import User, UserNotFoundException
from src.core.shared.ports import UserRepositoryPort


class JWTBearer(HTTPBearer):
    user_repo: UserRepositoryPort

    def __init__(self, user_repo: UserRepositoryPort, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.user_repo = user_repo

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not await self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            jwt_data = jwt.decode(credentials.credentials, key=config('SECRET_KEY'), options={"verify_signature": True}, algorithms=["HS256"])
            user_id = jwt_data['user_id']

            user: User = await self.user_repo.find_user_or_throw(user_id)

            return user.wallet
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    async def verify_jwt(self, jwtoken: str) -> bool:
        # @TODO: check has user_id and throw 401 if not
        # @TODO: check if user_id actually exists
        try:
            auth = jwtoken
            tok = auth.replace("Bearer ", "")
            data = jwt.decode(tok, key=config('SECRET_KEY'), options={"verify_signature": True}, algorithms=["HS256"])
            if data['exp'] < datetime.now(tz=timezone.utc).timestamp():
                return False
        except:
            return False
        return True


jwt_bearer = JWTBearer(BeaniUserRepositoryAdapter())

# def jwt_user_data(jwt=Depends(sec)):
#     if jwt['user_id'] is None:
#         raise HTTPException(status_code=403, detail="Invalid authorization code.")
#
#     return jwt['user_id']