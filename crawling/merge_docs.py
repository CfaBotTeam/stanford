import json

if __name__ == '__main__':
    with open('investopedia_cfa.json', 'r') as f_invest, \
         open('data_collected.json', 'r') as f_docs:
        invest_red = f_invest.read()
        json_invest = json.loads(invest_red)
        docs_red = f_docs.read()
        json_docs = json.loads(docs_red)
        all_docs = json_invest['docs'] + json_docs

    with open('all_data_collected.json', 'w') as f_docs:
        to_write = json.dumps(all_docs)
        f_docs.write(to_write)
