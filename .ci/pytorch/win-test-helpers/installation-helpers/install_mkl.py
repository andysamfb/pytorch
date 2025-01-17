import os
import subprocess
import sys
import pathlib


tmp_win_dir = os.environ['TMP_DIR_WIN']

if 'REBUILD' not in os.environ:

    try:

        if 'BUILD_ENVIRONMENT' not in os.environ:

            subprocess.run('curl --retry 3 -k https://s3.amazonaws.com/ossci-windows/mkl_2020.2.254.7z ' +
                    '--output ' + tmp_win_dir + '\\mkl.7z', shell=True, check=True)

        else:

            subprocess.run('aws s3 cp s3://ossci-windows/mkl_2020.2.254.7z ' +
                tmp_win_dir + '\\mkl.7z --quiet', shell=True, check=True)

        subprocess.run('7z x -aoa ' + tmp_win_dir + '\\mkl.7z -o' + tmp_win_dir + '\\mkl', shell=True, check=True)

    except Exception as e:

        subprocess.run('echo install mkl failed', shell=True)
        subprocess.run('echo ' + str(e), shell=True)
        sys.exit()

os.system(str(pathlib.Path(__file__).parent.resolve()) + '\\mkl_vars.bat')
