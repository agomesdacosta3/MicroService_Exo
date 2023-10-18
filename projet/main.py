from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi.staticfiles import StaticFiles  # Importez la fonctionnalité des fichiers statiques

app = FastAPI()
engine = create_engine('postgresql://postgres:postgres@db/northwind')
Session = sessionmaker(bind=engine)
templates = Jinja2Templates(directory="templates")

# Utilisez la fonction app.mount() pour servir les fichiers statiques depuis le répertoire "styles"
app.mount("/styles", StaticFiles(directory="styles"), name="styles")

@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/add_customer')
async def add_customer(request: Request):
    return templates.TemplateResponse("add_customer.html", {"request": request})

@app.get('/get_customer')
async def get_customer(request: Request):
    return templates.TemplateResponse("get_customer.html", {"request": request})

@app.get('/search_customer')
async def search_customer(request: Request, contact_name: str):
    session = Session()
    result = session.execute(text('SELECT customer_id, company_name, contact_name FROM customers WHERE contact_name = :contact_name'), {"contact_name": contact_name})
    customer = result.fetchone()

    if customer:
        return customer._asdict()  # Convert to a dictionary for JSON
    else:
        return {"error": "Customer not found"}  # Renvoyer un objet JSON en cas de client non trouvé

@app.get('/get_all_customer')
async def get_all_customer(request: Request):
    session = Session()
    result = session.execute(text('SELECT customer_id, company_name, contact_name FROM customers LIMIT 10'))
    customers = [dict(customerid=row[0], companyname=row[1], contactname=row[2]) for row in result]
    return templates.TemplateResponse("get_all_customer.html", {"request": request, "customers": customers})
