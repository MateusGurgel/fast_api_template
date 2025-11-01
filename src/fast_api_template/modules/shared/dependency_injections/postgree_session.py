from fastapi import Depends

from fast_api_template.core.infra.database import get_session

PGSession = Depends(get_session)
