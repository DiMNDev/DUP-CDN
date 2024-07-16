# Load each image in a directory, resize, and save thumbnail in new directory
import os
import shutil

load_directory_path = "DUP_Thumbs/"
save_directory_path = "Chunks/"

def getFilesInDirectory(directory):
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory,f))]
        files.sort()
        return files
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def chunkFileNames(chunk_size, files):
    count = 0
    chunks = []
    chunk = []
    for index, file in enumerate(files):
        chunk.append(file)
        if (index + 1) % chunk_size == 0 or index == len(files) - 1:
            chunks.append(chunk)
            # print(f"chunk {count} added with {len(chunk)} chunks")
            chunk = []
            count += 1
    return chunks

def loadAndCopyIntoChunks(chunks, load_directory, save_directory):
    count = 0
    for chunk in chunks:
        for file in chunk:
            sourceFile = os.path.join(load_directory, file)
            destination_directory = os.path.join(save_directory, f"Chunk_{count}/")
            if os.path.exists(destination_directory):
                if os.path.exists(sourceFile):
                    shutil.copy(sourceFile, destination_directory)
                    print(f"Copied {file} to {destination_directory}")
                else:
                    print("Done did messed up my dude!")
            else:
                os.makedirs(destination_directory)
                if os.path.exists(sourceFile):
                    shutil.copy(sourceFile, destination_directory)
                    print(f"Copied {file} to {destination_directory}")
                else:
                    print("Done did messed up my dude!")
        count += 1

files = getFilesInDirectory(load_directory_path)
chunks = chunkFileNames(20, files)
loadAndCopyIntoChunks(chunks, load_directory_path, save_directory_path)

