import json

if __name__ == '__main__':
    all_data = []
    with open('investopedia_cfa.json', 'r') as f_invest, \
         open('data_collected.json', 'r') as f_docs:
        invest_red = f_invest.read()
        json_invest = json.loads(invest_red)
        docs_red = f_docs.read()
        json_docs = json.loads(docs_red)
        all_docs = json_invest['docs'] + json_docs

    with open('all_data_collected.txt', 'w') as f_docs:
        for doc in all_docs:
            to_write = json.dumps(doc)
            f_docs.write(to_write + '\n')
