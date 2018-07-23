from parsimonious.grammar import Grammar

with open('tests/999-fullfile/2_5355206820858168112.hfss') as stub:
    text = stub.read()

with open('hfss_grammar') as grammar_file:
    grammar = Grammar(grammar_file.read())

print (grammar.parse(text))

