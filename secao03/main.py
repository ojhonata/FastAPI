from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import status
from models import Curso

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


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id    
    return curso

@app.put('/cursos/{id_curso}')
async def put_curso(id_curso: int, curso: Curso):
    if id_curso in cursos:
        cursos[id_curso] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!')

@app.delete('/cursos/{id_curso}')
async def delete_curso(id_curso: int):
    try:
        del cursos[id_curso]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        #raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')






if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)