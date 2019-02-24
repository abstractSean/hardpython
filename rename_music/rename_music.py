
import glob
import os
import re
import sys

from pprint import pprint as pp
from string import Template


def parse_input_format(input_format):
    pass


def parse_filename(filename, input_format):
    result_dict = dict()

    for tag, delimiter in input_format:
        #print(filename)
        if tag == '<track>' or tag == '<year>':
            result_dict[tag] = re.search(r'\d+', filename)[0]
            filename = str(filename[len(result_dict[tag]):]).strip()
        else:
            result_dict[tag] = filename.split(delimiter)[0]
            filename = filename.split(delimiter)[1:]
            filename = delimiter.join(filename)
    return result_dict


def main():
    test_input = '<album> - <track> <title> (<year>).mp3'
    test_output = 'Bob Dylan/<year> <album>/<track> <title>.mp3'

    print('Specify filename input format:')
    input_format = test_input #input()
    print('Specify output format:')
    output_format = test_output #input()

    tag_re = re.compile(r'(\<)(\w+)(\>)')
    delimiter_re = re.compile(r'(?:.*?>)((?:.|\s)*?)(?:(?:<.*?)|(?:\.mp3))')

    input_delimiters = [s for s in delimiter_re.findall(input_format)]
    input_tags = [tag[2] for tag in tag_re.finditer(input_format)]
    input_format = list(zip(input_tags, input_delimiters))

    current_filenames = glob.glob('*.mp3')
    parsed_filenames =[parse_filename(filename,input_format)
                       for filename in current_filenames]

    output_format = output_format.replace('<', '{').replace('>', '}')
    output = [output_format.format(**filename)
              for filename in parsed_filenames]

    print(output)

    directory = os.getcwd()


if __name__ == '__main__':
    main()
