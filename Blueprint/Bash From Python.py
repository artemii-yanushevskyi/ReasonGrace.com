bashCommand = "ls -al" # allows to run only one command at a time; & and && are unavailable 
# for scripts insert "./testbash.sh", better "sh test.sh" or "bash test.sh"
import subprocess 
# Directory /home/fabulous == ~
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd="/home/fabulous/site/mysite/Blueprint") 
output, error = process.communicate()
print("Output:\n{}\n\nError:\n{}\n\n".format(output, error))
binoutput = map(hex,output)
print("Output:\n{}\n\nError:\n{}\n\n".format(" ".join(char for char in binoutput), error) )
