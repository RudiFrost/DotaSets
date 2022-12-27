import sqlite3
import os





def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def uploadGifs(empId):
    gif_names = []
    dir_name = '/home/sirius/DotaGit/DotaSkin/static/gifs'
    test = os.listdir(dir_name)
    
    for gif in test:
        if gif.endswith('.gif'):
            gif_names.append(gif)


    try:
        for name in gif_names:
            sqliteConnection = sqlite3.connect('/home/sirius/DotaGit/DotaSkin/db/blogs.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            with open(f"/home/sirius/DotaGit/DotaSkin/static/gifs/{name}","rb") as f:
                image = f.read()
            binary = sqlite3.Binary(image)
            cursor.execute("INSERT INTO skins_gif VALUES ((?),(?))",(f"{name[:-4]}",binary ,))
            sqliteConnection.commit()

    except Exception as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

# uploadGifs(1)
# uploadGifs(2)

def uploadImage(empID):
    image_names = []
    dir_name = '/home/sirius/DotaGit/DotaSkin/static/gifs'
    test = os.listdir(dir_name)

    for img in test:
        if img.endswith('.png'):
            image_names.append(img)

    try:
        for name in image_names:
            sqliteConnection = sqlite3.connect('/home/sirius/DotaGit/DotaSkin/db/blogs.db')
            cursor = sqliteConnection.cursor()

            print("Connected to SQLite")

            with open(f"/home/sirius/DotaGit/DotaSkin/static/gifs/{name}", "rb") as f:
                image = f.read()

            binary = sqlite3.Binary(image)
            cursor.execute("INSERT INTO avatars_of_skins VALUES ((?),(?))", (f"{name[:-4]}", binary,))
            sqliteConnection.commit()

    except Exception as error:
        print("Failed to read blob data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

# uploadImage(1)
# uploadImage(2)

def upload_link(empID):
    links = []
    dir_name = '/home/sirius/DotaGit/DotaSkin/static/gifs'
    test = os.listdir(dir_name)

    for gif in test:
        if gif.endswith('.gif'):
            links.append(gif)

    try:
        for name in links:
            sqliteConnection = sqlite3.connect('/home/sirius/DotaGit/DotaSkin/db/blogs.db')
            cursor = sqliteConnection.cursor()

            print("Connected to SQLite")

            with open(f"/home/sirius/DotaGit/DotaSkin/static/gifs/{name}", "rb") as f:
                gif = f.read()

            binary = sqlite3.Binary(gif)
            cursor.execute("INSERT INTO link_for_image VALUES((?),(?))", (f"{name[:-4]}", binary,))
            sqliteConnection.commit()

    except Exception as error:
        print("Failed to read blob data from sqlite table.", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


upload_link(1)
upload_link(2)