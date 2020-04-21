import subprocess
import sys
from pathlib import Path

import owlready2


def convert():
    ease_ugly = Path(__file__).parent.parent / 'owl' / 'EASE-UGLY.owl'
    if not ease_ugly.exists():
        print('Generating rdf')
        command = 'swipl -f prolog/uglify_ease.pl -t uglify_ease'.split()
        proc = subprocess.run(command, cwd='data/ontologies/ease_ontology', capture_output=True)
        print(proc.stdout.decode('utf8'), end='')
        print(proc.stderr.decode('utf8'), end='', file=sys.stderr)

    print('Converting to owl')
    owlready2.onto_path.insert(0, str(ease_ugly.parent))
    ontology = owlready2.get_ontology('EASE-UGLY.owl').load()
    ontology.save()
    print('Converted')


if __name__ == '__main__':
    convert()