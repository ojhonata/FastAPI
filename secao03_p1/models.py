from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavra = value.split()

        if len(palavra) < 3:
            raise ValueError('O titulo precisa ter mais de 3 palavras')
        
        if value.islower():
            raise ValueError('O titulo deve ser captalizado')
        return value
    
    @validator('aulas')
    def validar_aulas(cls, value:int):
        if value < 12:
            raise ValueError('Precisa ter de mais que 12 aulas')
        return value
    
    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('Precisa ter mais de 10 horas')
        return value


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=122, horas=58),
    Curso(id=2, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=58)
]