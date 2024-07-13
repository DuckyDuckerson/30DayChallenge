import subprocess


def compile_c_code(c_code_path, shared_lib_path):
    # compile the c code
    compile_command = "gcc -shared -o " + shared_lib_path + " " + c_code_path
    subprocess.run(compile_command, shell=True)
