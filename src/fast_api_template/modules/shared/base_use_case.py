from abc import ABC, abstractmethod
from typing import Union, Awaitable, TypeVar, Generic

from fast_api_template.modules.shared.base_dto import BaseDTO

InputDTO = TypeVar("InputDTO", bound=BaseDTO)
OutputDTO = TypeVar("OutputDTO", bound=BaseDTO)


class BaseUseCase(ABC, Generic[InputDTO, OutputDTO]):

    @abstractmethod
    def handle(self, dto: InputDTO) -> Union[OutputDTO, Awaitable[OutputDTO]]: ...
