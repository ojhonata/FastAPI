from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 122,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 58
    }
}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{id_curso}')
async def get_curso(id_curso: int):
    try:
        curso = cursos[id_curso]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!')




if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)