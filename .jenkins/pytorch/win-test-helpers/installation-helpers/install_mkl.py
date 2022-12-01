import os
import subprocess
import sys


tmp_win_dir = os.environ['TMP_DIR_WIN']

if os.environ['REBUILD'] == "":

    try:

        if os.environ['BUILD_ENVIRONMENT'] == "":

            subprocess.run(['curl', '--retry', '3', '-k',\
             'https://s3.amazonaws.com/ossci-windows/mkl_2020.2.254.7z',\
             '--output', tmp_win_dir + '\\mkl.7z'])

        else:

            subprocess.run(['aws', 's3', 'cp', 's3://ossci-windows/mkl_2020.2.254.7z',\
             tmp_win_dir + '\\mkl.7z', '--quiet'])

        subprocess.run(['7z', 'x', '-aoa', tmp_win_dir + '\\mkl.7z',\
         '-o' + tmp_win_dir + '\\mkl'])

    except Exception as e:

        subprocess.run(['echo', 'install mkl failed'])
        subprocess.run(['echo', e])
        sys.exit()


os.environ['CMAKE_INCLUDE_PATH'] = tmp_win_dir + '\\mkl\\include'
os.environ['LIB'] = tmp_win_dir + '\\mkl\\lib'
subprocess.run([os.environ['LIB']])
