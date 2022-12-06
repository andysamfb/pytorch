import os
import subprocess
import sys
import contextlib


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


try:

    subprocess.call('python ' + os.environ['SCRIPT_HELPERS_DIR'] + '\\setup_pytorch_env.py', shell=True)

except Exception as e:

    subprocess.run(['echo', 'setup pytorch env failed'])
    subprocess.run(['echo', e])
    sys.exit()


subprocess.run(['echo', 'Installing test dependencies'])

try:
    subprocess.run(['conda', 'install', '-n', 'test_env', 'pip', 'install', 'networkx'])

except Exception as e:

    subprocess.run(['echo', 'install networkx failed'])
    subprocess.run(['echo', e])
    sys.exit()


subprocess.run(['echo', 'Test functorch'])

try:

    with pushd('test'):
        subprocess.run(['conda', 'install', '-n', 'test_env', 'python', 'run_test.py', '--functorch', '--shard',
            os.environ['SHARD_NUMBER'], os.environ['NUM_TEST_SHARDS'], '--verbose'])

except Exception as e:

    subprocess.run(['echo', 'run_test functorch shard failed'])
    subprocess.run(['echo', e])
    sys.exit()
