from __future__ import with_statement
from __future__ import absolute_import
from subprocess import check_output
import re
import sys
from io import open



def submitJob_local(index, commandExecutable):
    """
    This routine is to submit job locally
    One needs to do a little edit based on your own case.

    Step 1: to prepare the job script which is required by your supercomputer
    Step 2: to submit the job with the command like qsub, bsub, llsubmit, .etc.
    Step 3: to get the jobID from the screen message
    :return: job ID
    """

    RUN_FILENAME = 'myrun'
    JOB_NAME = 'USPEX-{}'.format(index)

    # Step 1
    myrun_content = u''
    myrun_content += u'#!/bin/bash\n'
    myrun_content += u'#PBS -l nodes=1:ppn=4\n'
    myrun_content += u'#PBS -l walltime=4:00:00\n'
    myrun_content += u'#PBS -l mem=1gb\n'
    myrun_content += u'#PBS -N "name"\n'
    myrun_content += u'\n'
    myrun_content += u'#Nuestro directorio de scratch\n'
    myrun_content += u'scrt=/gscratch/quaqugaj/$PBS_JOBID\n'
    myrun_content += u'echo $scrt\n'
    myrun_content += u'#Creamos el directorio\n'
    myrun_content += u'mkdir $scrt\n'
    myrun_content += u'#Copiamos los archivos al directorio scratch\n'
    myrun_content += u'#Usaremos cp -r $scrt para copiar tambien subdirectorios.\n'
    myrun_content += u'#cp $PBS_O_WORKDIR/* $scrt\n'
    myrun_content += u'cp $PBS_O_WORKDIR/* $scrt\n'
    myrun_content += u'\n'
    myrun_content += u'#Nos movemos de directorio\n'
    myrun_content += u'cd $scrt\n'
    myrun_content += u'\n'
    myrun_content += u'#Ejecutamos el programa\n'
    myrun_content += u'./siesta2gulp.sh\n'
    myrun_content += u'/software/bin/gulp < input_gulp.in > output_gulp.out\n'
    myrun_content += u'./gulp2siesta.sh\n'
    myrun_content += u'/software/siesta-4.0/siesta_mpi < input.fdf > output\n'
    myrun_content += u'\n'
    myrun_content += u'#Movemos los archivos finales\n'
    myrun_content += u'\n'
    myrun_content += u'outdir=$PBS_JOBID\n'
    myrun_content += u'mkdir $PBS_O_WORKDIR/$outdir\n'
    myrun_content += u'mv -f $scrt/* $PBS_O_WORKDIR/$outdir\n'
    myrun_content += u'cp $PBS_O_WORKDIR/$outdir/output $PBS_O_WORKDIR\n'
    myrun_content += u'cp $PBS_O_WORKDIR/$outdir/siesta.STRUCT_OUT $PBS_O_WORKDIR\n'
    myrun_content += u'\n'
    myrun_content += u'#Borramos el directorio\n'
    myrun_content += u'rmdir $scrt \n'
    myrun_content += u'cd $PBS_O_WORKDIR\n'
    myrun_content += u'\n'
    # myrun_content += 'cd ${PBS_O_WORKDIR}\n' check this, must have /cephfs suffix with SBATCH in my case
    myrun_content.format(JOB_NAME, commandExecutable)


    with open(RUN_FILENAME, 'w') as fp:
        fp.write(myrun_content)

    # Step 2
    # It will output some message on the screen like '2350873.nano.cfn.bnl.local'
    output = check_output('qsub {}'.format(RUN_FILENAME), shell=True, universal_newlines=True)
    print(output, flush=True)
    print(output.split('.')[0], flush=True)


    # Step 3
    # Here we parse job ID from the output of previous command
    jobNumber = int(output.split('.')[0])
    print(str(jobNumber))
    return jobNumber


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='index', type=int)
    parser.add_argument('-c', dest='commandExecutable', type=str)
    args = parser.parse_args()

    jobNumber = submitJob_local(index=args.index, commandExecutable=args.commandExecutable)
    print('<CALLRESULT>')
    print(int(jobNumber))
