from fastapi import FastAPI
from typing import Optional, Any, List, Dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Query
from fastapi import Header
from fastapi import Depends
from fastapi import status
from fastapi import Path
from models import Curso
from models import cursos
from time import sleep

app = FastAPI(title='API de Cursos da Geek University',
              description='API para estudos')

async def fake_db():
    try:
        print('Conexão com o Banco de Dados...')
        sleep(1)
    finally:
        print('Fechando a conexão com o Banco de Dados...')
        sleep(1)
    


@app.get('/cursos',
         summary='Retorna todos os cursos',
         description='Retorna uma lista de cursos ou uma lista vazia.',
         response_model=List[Curso],
         response_description='Cursos encontrados com sucesso')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{id_curso}')
async def get_curso(id_curso: int = Path(default=None, title="ID do Curso", description="Deve ser entre 1 e 2", gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[id_curso]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)   
    return curso

@app.put('/cursos/{id_curso}')
async def put_curso(id_curso: int, curso: Curso, db: Any = Depends(fake_db)):
    if id_curso in cursos:
        cursos[id_curso] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!')

@app.delete('/cursos/{id_curso}')
async def delete_curso(id_curso: int, db: Any = Depends(fake_db)):
    try:
        del cursos[id_curso]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        #raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.get('/calculadora')
async def somar(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=2), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma = a + b
    if c:
        soma += c

    print(f'x-geek: {x_geek}')
    return {'Resultado': soma}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)