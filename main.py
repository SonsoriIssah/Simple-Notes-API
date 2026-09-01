from fastapi import FastAPI,Depends,HTTPException
from database import get_db,engine
from models import Note,Base
from contextlib import asynccontextmanager
from sqlalchemy import select
from pydantic import BaseModel

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app= FastAPI(lifespan=lifespan)

class NoteDetails(BaseModel):
    title:str
    content:str

@app.get('/notes')
async def get_notes(db=Depends(get_db)):
    result= await db.execute(select(Note))
    all_notes = result.scalars().all()
    return all_notes

@app.get('/notes/{id}')
async def get_note(id:int,db=Depends(get_db)):
    result= await db.execute(select(Note).where(Note.id==id))
    single_note = result.scalars().first()
    if not single_note:
        raise HTTPException(status_code=404,detail='Note not found')
    return single_note

@app.post('/notes')
async def create_notes(note:NoteDetails,db=Depends(get_db)):
    db_note = Note(**note.model_dump())
    db.add(db_note)
    await db.commit()
    await db.refresh(db_note)
    return db_note

@app.delete('/notes/{id}')
async def delete_note(id:int,db=Depends(get_db)):
    result= await db.execute(select(Note).where(Note.id==id))
    single_note = result.scalars().first()
    if not single_note:
        raise HTTPException(status_code=404,detail='Note not found')
    await db.delete(single_note)
    await db.commit()
    return {"detail": "Note deleted successfully"}



