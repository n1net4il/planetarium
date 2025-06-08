import argparse
import requests

from bs4 import BeautifulSoup

if  __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data-dir', type = str, required = True)
    parser.add_argument('--problem-no', type = int, required = True)

    args = parser.parse_args()

    response = requests.get(f'https://www.acmicpc.net/problem/{args.problem_no}', headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ko-KR, ko; q=0.9, en-US; q=0.8, en; q=0.7',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    })
    soup = BeautifulSoup(response.text, 'html.parser')

    for element in soup.find_all('pre', class_ = 'sampledata'):
        _, type_, index = element.get('id').split('-')
        if type_ == 'input':
            with open(f'{args.data_dir}/{index}.in', 'w') as f:
                f.write(element.text)
        elif type_ == 'output':
            with open(f'{args.data_dir}/{index}.out', 'w') as f:
                f.write(element.text)
