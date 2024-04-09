#this class will return a fortune
import hug
import subprocess

@hug.get()
def generate(): 
    cmd = "/usr/games/fortune"
    result = subprocess.run([cmd], stdout=subprocess.PIPE)
    return { "fortune":result.stdout }


if __name__=="__main__":
    generate()
