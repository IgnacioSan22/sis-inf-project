from app import db, login
from app.models import User, Poster


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def read_blob(id, filename):
    # select photo column of a specific poster
    photo = Poster.getImagen(id)

    # write blob data into a file
    write_file(photo, filename)