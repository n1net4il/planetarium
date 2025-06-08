import argparse
import difflib
import glob
import math
import os
import subprocess

from rich.console import Console

if  __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data-dir', required = True)
    parser.add_argument('--executable', required = True)

    args = parser.parse_args()
    console = Console()

    for in_path in glob.glob(os.path.join(args.data_dir, '*.in')):
        out_path = in_path[:-3] + '.out'

        in_file = open(in_path, 'r')
        out_file = open(out_path, 'r')

        console.print('\n[yellow]Input: [/yellow][cyan]{}[/cyan]'.format(in_path), end = '\n');

        expected_lines = out_file.read().strip().splitlines()
        actual_lines = subprocess.check_output([args.executable], stdin = in_file, text = True).strip().splitlines()            

        max_lines = max(len(expected_lines), len(actual_lines))
        align = max(max(map(len, actual_lines)), 10) + 3

        success = True

        console.print('\n[yellow]Output: [/yellow]', end = '\n\n');
        console.print('{} \t{}{}'.format(' ' * (int(math.log10(max_lines)) + 1), 'actual'.ljust(align, ' '), 'expected'), style = 'yellow', end = '\n')
        for i in range(max_lines):
            console.print('{}:\t'.format(str(i + 1).rjust(int(math.log10(max_lines)) + 1, ' ')), style = 'yellow', end = '')
            if i >= len(expected_lines):
                console.print('[red]{}[/red]'.format(actual_lines[i].ljust(align, ' ')), end = '')
                console.print('[green]<blank>[/green]', end = '\n')
                success = False
            elif i >= len(actual_lines):
                console.print('[red]<blank>[/red]' + ' ' * (align - 7), style = 'red', end = '')
                console.print('[green]{}[/green]'.format(expected_lines[i]), end = '\n')
                success = False
            else:
                if expected_lines[i] != actual_lines[i]:
                    console.print('[red]{}[/red]'.format(actual_lines[i].ljust(align, ' ')), end = '')
                    console.print('[green]{}[/green]'.format(expected_lines[i]), end = '\n')
                    success = False
                else:
                    console.print('[green]{}[/green]'.format(actual_lines[i].ljust(align, ' ')), end = '')
                    console.print('[green]{}[/green]'.format(expected_lines[i]), end = '\n')

        console.print('\nResult: ', style = 'yellow', end = '')
        if success:
            console.print('Correct', style = 'green')
        else:
            console.print('Wrong Answer', style = 'red')


        in_file.close()
        out_file.close()