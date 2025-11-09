from fastapi import Depends

from fast_api_template.core.infra.postgres import get_session

PGSession = Depends(get_session)
