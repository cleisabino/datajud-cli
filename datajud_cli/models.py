from pydantic import BaseModel, field_validator
from typing import Optional, Union

class Classe(BaseModel):
    codigo: Optional[int] = None
    nome: Optional[str] = None

class Tribunal(BaseModel):
    codigo: Optional[str] = None
    nome: Optional[str] = None

    @field_validator('*', mode='before')
    @classmethod
    def aceita_string(cls, v):
        return v

class ComplementoTabelado(BaseModel):
    codigo: Optional[int] = None
    valor: Optional[int | str] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None

class Movimento(BaseModel):
    codigo: Optional[int] = None
    nome: Optional[str] = None
    dataHora: Optional[str] = None
    complementosTabelados: Optional[list[ComplementoTabelado]] = None

class Processo(BaseModel):
    numeroProcesso: Optional[str] = None
    classe: Optional[Classe] = None
    tribunal: Optional[Union[Tribunal, str]] = None
    dataAjuizamento: Optional[str] = None
    ultimaAtualizacao: Optional[str] = None
    movimentos: Optional[list[Movimento]] = None